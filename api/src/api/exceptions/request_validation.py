from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
import logging


def register_request_validation_exception_handler(
    app: FastAPI,
    logger: logging.Logger,
    status_code: int = status.HTTP_400_BAD_REQUEST,
    message: str = "Bad Request: Input keys do not match expected schema"
):
    """
    Registers a custom handler for FastAPI's RequestValidationError.

    Args:
        app (FastAPI): The FastAPI application instance.
        logger (logging.Logger): The logger to record validation errors.
        status_code (int): The HTTP status code to return (default: 400).
        message (str): A custom error message for the response body.
    """

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"{status_code} - {message} - {exc}")
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder({
                "message": message,
                "errors": exc.errors()
            })
        )
