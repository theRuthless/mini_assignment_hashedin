from fastapi import responses
from fastapi.testclient import TestClient
import random
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "ok!"}
