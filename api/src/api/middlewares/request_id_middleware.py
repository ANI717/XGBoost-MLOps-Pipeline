import uuid
import contextvars
from urllib.parse import urlencode, parse_qs
from starlette.datastructures import Headers


request_id_var = contextvars.ContextVar("request_id", default=None)


class RequestIDMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            # Pass through non-HTTP events (like websockets)
            await self.app(scope, receive, send)
            return

        # Parse the query string
        raw_query = scope.get("query_string", b"").decode("utf-8")
        query_params = parse_qs(raw_query)

        # Check for 'req_id', generate if missing
        if "req_id" not in query_params:
            req_id = str(uuid.uuid4())
            query_params["req_id"] = [req_id]
            # Reconstruct query string with req_id
            scope["query_string"] = urlencode(query_params, doseq=True).encode("utf-8")
        else:
            req_id = query_params["req_id"][0]
        
        # Set req_id into context var
        request_id_var.set(req_id)

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                headers = Headers(raw=message.get("headers", []))
                new_headers = list(headers.raw)
                new_headers.append((b"request-id", req_id.encode("utf-8")))
                message["headers"] = new_headers
            await send(message)

        await self.app(scope, receive, send_wrapper)
