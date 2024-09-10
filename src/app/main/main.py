from fastapi import FastAPI
from faststream.asgi import AsgiFastStream

from src.app.presentation.api.v1.check_health import health_check_router


def get_fastapi_app() -> FastAPI:
    app = FastAPI()
    app.include_router(health_check_router)
    return app

def get_faststream_app() -> AsgiFastStream:
    app = AsgiFastStream()
    return app