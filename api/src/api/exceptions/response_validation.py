from fastapi import Request, status, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
import logging


def register_response_validation_exception_handler(
    app: FastAPI,
    logger: logging.Logger,
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    message: str = "Internal Server Error: Response schema does not match"
):
    """
    Registers a custom handler for FastAPI's ResponseValidationError.

    Args:
        app (FastAPI): The FastAPI application instance.
        logger (logging.Logger): The logger to record validation errors.
        status_code (int): HTTP status code to return (default: 500).
        message (str): A custom error message for the response.
    """

    @app.exception_handler(ResponseValidationError)
    async def response_validation_exception_handler(
        request: Request, exc: ResponseValidationError
    ):
        logger.error(f"{status_code} - {message} - {exc}")
        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder({
                "message": message,
                "errors": exc.errors()
            })
        )
