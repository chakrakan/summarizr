# project/app/db.py

import os
import logging
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger(__name__)


def init_db(app: FastAPI) -> None:
    """
    We don't want to create schema each time the app is reloaded so port everything into an init function
    :param app: the FastAPI app
    """
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True
    )


async def generate_schema() -> None:
    """
    In order to generate schemas when needed, calls Tortoise.init to set up tortoise and generates the schema
    """
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={'models': ['models.tortoise']}
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
