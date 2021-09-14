from fastapi import responses
from fastapi.testclient import TestClient
import random
from app.main import app

client = TestClient(app)


def test_get_user():
    response = client.get("/users/")
    assert response.status_code == 200

def test_get_user_id_pass():
    response = client.get(f"/users/{1}/")
    assert response.status_code == 200

def test_get_user_id_fail():
    response = client.get(f"/users/{random.randrange(100, 10**3)}/")
    assert response.status_code == 404


def test_post_user():
    data = {"email":f"test{random.randrange(0,10**3)}@test.com", "password":"test_password"}
    response = client.post("/users/", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 200

def test_post_user_fail_missing_parameter():
    data = {"password":"test_password"}
    response = client.post("/users/", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 400
    assert response.reason == "Bad Request"
