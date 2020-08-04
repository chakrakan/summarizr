# project/tests/conftest.py

import os
import pytest
from starlette.testclient import TestClient
from app.main import create_application
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_URL"))


# Fixtures are reusable objects for tests, they have a scope which indicates how often the fixture is invoked
# function: once per test function (default)
# class: once per test class
# module (our case): once per test module
# session: once per test session
@pytest.fixture(scope="module")
def test_app():
    """
    We use imported Starlette TestClient which uses the requests library to make requests against the FastAPI app.
    To override dependencies, we use the dependecy_override attribute which is a dict of key/val pairs where the
    key: get_settings (is the dependency name)
    value: get_settings_override (what we'd like to override the dependency with)
    """
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        # testing
        yield test_client
    # tear down
