# project/tests/test_summaries.py

import json


def test_create_summary(test_app_with_db):
    resp = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))

    assert resp.status_code == 201
    assert resp.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app):
    resp = test_app.post("/summaries/", data=json.dumps({}))

    assert resp.status_code == 422
    assert resp.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_read_summary(test_app_with_db):
    resp = test_app_with_db.post("/summaries/", data=json.dumps({"url": "http://foo.bar"}))
    summary_id = resp.json()['id']
    resp = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert resp.status_code == 200

    resp_dict = resp.json()
    assert resp_dict['id'] == summary_id
    assert resp_dict['url'] == "https://foo.bar"
    assert resp_dict['summary']
    assert resp_dict['created_at']
