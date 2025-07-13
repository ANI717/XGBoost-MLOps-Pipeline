from fastapi import FastAPI

from api.config import settings, logger
from api.events import startup, shutdown
from api.middleware.process_time_middleware import ProcessTimeMiddleware
from api.middleware.request_id_middleware import RequestIDMiddleware
from api.middleware.request_response_logger_middleware import RequestResponseLoggerMiddleware
from api.routers import home
from api.routers import health
from api.routers import metadata
from api.routers import xgboost
from api.exceptions.register import register_all_exception_handlers


app = FastAPI(
    title="XGBoost Model Serving API",
    version="1.0.0",
    description="A robust API for serving predictions using an XGBoost model.",
    contact={
        "name": "Animesh Bala Ani",
        "email": "animesh.ani@live.com",
    },
    root_path=settings.ROOT_PATH,
)


startup.include_event(app, logger)
shutdown.include_event(app, logger)

app.add_middleware(ProcessTimeMiddleware)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(RequestResponseLoggerMiddleware,
                   logger=logger,
                   excluded_paths=settings.EXCLUDED_PATHS)

app.include_router(home.router)
app.include_router(health.router)
app.include_router(metadata.router)
app.include_router(xgboost.router)

register_all_exception_handlers(app, logger)
