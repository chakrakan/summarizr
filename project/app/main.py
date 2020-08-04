# project/app/main.py

import logging
from fastapi import FastAPI
from app.db import init_db
from app.api import ping, summaries

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """
    Create the FastAPI application, add the routes using the router for ping, summaries
    :return: fastAPI app
    """
    application = FastAPI()
    application.include_router(ping.router)
    # the tags is for the OpenAPI schema for grouping operations
    application.include_router(summaries.router, prefix="/summaries", tags=["summaries"])

    return application


# instantiate
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
