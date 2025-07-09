from api.exceptions.request_validation import register_request_validation_exception_handler
from api.exceptions.response_validation import register_response_validation_exception_handler


def register_all_exception_handlers(app, logger):
    register_request_validation_exception_handler(app, logger)
    register_response_validation_exception_handler(app, logger)
