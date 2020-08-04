# project/app/main.py

import logging
from fastapi import FastAPI
from app.db import init_db
from app.api import ping

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    """
    Start up handler
    """
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Shutdown handler
    """
    log.info("Shutting down...")
