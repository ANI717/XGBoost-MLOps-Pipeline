import logging
from logging.handlers import TimedRotatingFileHandler


def get_file_handler(filename="logfile.log", when="midnight", backup_count=7):
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [req_id=%(request_id)s] '
        '[file=%(filename)s:%(lineno)d] [func=%(funcName)s] '
        '[message=%(message)s]'
    )

    handler = TimedRotatingFileHandler(
        filename=filename,
        when=when,
        backupCount=backup_count,
        encoding="utf-8"
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    return handler
