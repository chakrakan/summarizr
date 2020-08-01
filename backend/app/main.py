# backend/app/main.py

from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Depends function is a dependency that declares another dependency and relies on its value (get_settings)
    The value returned, Settings is then assigned to the settings param
    Instead of spinning up a task queue like Celery or RQ, or using threads, FastAPI delivers routes in async manner
    as long as we don't have any blocking i/o calls in the handler.
    :param settings: holds env and test values
    :return: resp object
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
