from fastapi import responses
from fastapi.testclient import TestClient
import random
from app.main import app

client = TestClient(app)


def test_get_metric_types():
    response = client.get("/metric_types/")
    assert response.status_code == 200

def test_get_metric_by_id_pass():
    response = client.get(f"/metric_types/{4}/")
    assert response.status_code == 200

def test_get_metric_type_id_fail():
    response = client.get(f"/metric_types/{random.randrange(100, 10**3)}/")
    assert response.status_code == 404


def test_post_metric_type():
    data = {"type_name":f"test{random.randrange(0,10**3)}"}
    response = client.post("/metric_types/", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 200

def test_post_metric_types_fail_missing_parameter():
    data = {}
    response = client.post("/metric_types/", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 422
