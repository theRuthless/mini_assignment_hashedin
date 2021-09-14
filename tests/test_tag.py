from fastapi import responses
from fastapi.testclient import TestClient
import random
from app.main import app

client = TestClient(app)


def test_get_tags():
    response = client.get("/tags/")
    assert response.status_code == 200

def test_get_tag_id_pass():
    response = client.get(f"/tags/{1}/")
    assert response.status_code == 200

def test_get_tag_id_fail():
    response = client.get(f"/tags/{random.randrange(100, 10**3)}/")
    assert response.status_code == 404


def test_post_tag():
    data = {"display_name":f"test{random.randrange(0,10**3)}"}
    response = client.post("/tags/", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 200

def test_post_tag_fail_missing_parameter():
    data = {}
    response = client.post("/tags/", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 422
