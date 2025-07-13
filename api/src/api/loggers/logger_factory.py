import logging
from api.middleware.request_id_middleware import request_id_var
from api.loggers.handlers.get_file_handler import get_file_handler
from api.loggers.handlers.get_console_handler import get_console_handler


class RequestIDFilter(logging.Filter):
    def filter(self, record):
        # Attach request_id to log record from context var
        record.request_id = request_id_var.get() or "unknown"
        return True


class LoggerFactory:
    def __init__(
        self,
        name: str = "api-logger",
        enable_console: bool = True,
        enable_file: bool = True,
        filename: str = "logfile.log",
        when: str = "midnight",
        log_level: str = "INFO"
    ):
        self.name = name
        self.enable_console = enable_console
        self.enable_file = enable_file
        self.filename = filename
        self.when = when
        self.log_level = log_level.upper()

    def get_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.name)
        logger.setLevel(self.log_level)

        # Avoid adding handlers multiple times
        if not logger.handlers:
            if self.enable_console:
                logger.addHandler(get_console_handler())
            if self.enable_file:
                logger.addHandler(get_file_handler(filename=self.filename, when=self.when))

            logger.addFilter(RequestIDFilter())
            logger.propagate = False

        return logger
