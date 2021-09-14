from fastapi import responses
from fastapi.testclient import TestClient
import random
from app.main import app

client = TestClient(app)


def test_get_metrics():
    response = client.get("/metrics/")
    assert response.status_code == 200


