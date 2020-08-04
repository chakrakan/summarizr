# project/tests/test_ping.py

from app import main

def test_ping(test_app):
    # Given
    # test_app

    # When
    resp = test_app.get("/ping")

    # Then
    assert resp.status_code == 200
    assert resp.json() == {"environment": "dev", "ping": "pong!", "testing": True}
