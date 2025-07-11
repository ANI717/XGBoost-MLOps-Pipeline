import json
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from starlette.responses import JSONResponse

from api.loggers.logger_factory import LoggerFactory
from api.middlewares.request_id_middleware import request_id_var


logger = LoggerFactory(name="api-logger").get_logger()


class RequestResponseLoggerMiddleware:
    def __init__(self, app: ASGIApp, logger=logger):
        self.app = app
        self.logger = logger

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        # ---- Capture request body ----
        body_chunks = []

        async def buffered_receive():
            message = await receive()
            if message["type"] == "http.request":
                body_chunks.append(message.get("body", b""))
            return message

        request_body_bytes = b""
        while True:
            message = await buffered_receive()
            request_body_bytes += message.get("body", b"")
            if not message.get("more_body", False):
                break

        try:
            request_json = json.loads(request_body_bytes.decode("utf-8"))
        except Exception:
            request_json = "unparsable"


        # ---- Replay body for downstream ----
        async def receive_replay() -> Message:
            return {
                "type": "http.request",
                "body": request_body_bytes,
                "more_body": False,
            }


        # ---- Capture response body ----
        response_body = b""

        async def send_wrapper(message: Message):
            nonlocal response_body
            if message["type"] == "http.response.body":
                response_body += message.get("body", b"")

            # ---- Log request and response ----
            if message["type"] == "http.response.body" and not message.get("more_body", False):
                try:
                    response_json = json.loads(response_body.decode("utf-8"))
                except Exception:
                    response_json = "unparsable"

                try:
                    # Log the request and response
                    payload = {
                        "request_id": request_id_var.get(),
                        "request": request_json,
                        "response": response_json,
                    }

                    logger.info(payload)

                except Exception as e:
                    message = f"Failed to log request/response: {str(e)}"
                    logger.error(message)
                    error_response = JSONResponse(
                        status_code=500,
                        content={
                            "detail": message,
                        }
                    )
                    await error_response(scope, receive, send)

            await send(message)

        await self.app(scope, receive_replay, send_wrapper)
