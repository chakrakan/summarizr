# backend/app/config.py

import logging
import os
from dotenv import load_dotenv
from pydantic import BaseSettings
from functools import lru_cache

load_dotenv()
log = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    BaseSettings: from pydantic validates data so we have types str, bool respectively for environment and testing
    environment: defines the env (dev, stage, prod)
    testing: defines if we are in test mode or not
    """
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Use LRU cache to cache settings so get_settings is only called once
    :return:
    """
    log.info("Loading config settings from the environment...")
    return Settings()
