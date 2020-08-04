# project/app/main.py

import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api import ping


def create_application() -> FastAPI:
    application = FastAPI()

    # set up tortoise ORM on startup and clean up on teardown
    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True
    )

    application.include_router(ping.router)

    return application


app = create_application()
