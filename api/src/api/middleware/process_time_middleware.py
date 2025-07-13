import time
from starlette.datastructures import Headers


class ProcessTimeMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            # Pass through non-HTTP events (like websockets)
            await self.app(scope, receive, send)
            return

        start_time = time.time()
        
        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                process_time = time.time() - start_time
                headers = Headers(raw=message.get("headers", []))
                new_headers = list(headers.raw)
                new_headers.append((b"process-time", f"{process_time:.4f}".encode("utf-8")))
                message["headers"] = new_headers
            await send(message)

        await self.app(scope, receive, send_wrapper)
