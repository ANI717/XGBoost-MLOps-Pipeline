from typing import Union
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

from api.loggers.logger_factory import LoggerFactory 


load_dotenv()
load_dotenv(find_dotenv("../.env"))


class Settings(BaseSettings):
    ENV: str = "dev"
    ROOT_PATH: Union[str, None] = None
    LOG_LEVEL: str = "INFO"
    EXCLUDED_PATHS: set[str] = {"/docs", "/openapi.json", "/health"}


settings = Settings()
logger = LoggerFactory(log_level=settings.LOG_LEVEL).get_logger()
