# project/tests/test_summaries.py

import json
import pytest


def test_create_summary(test_app_with_db):
    resp = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))

    assert resp.status_code == 201
    assert resp.json()["url"] == "https://foo.bar"
