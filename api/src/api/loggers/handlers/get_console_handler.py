import sys
import logging
from logging import StreamHandler


def get_console_handler():
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [req_id=%(request_id)s] '
        '[file=%(filename)s:%(lineno)d] [func=%(funcName)s] '
        '[message=%(message)s]'
    )

    handler = StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    return handler
