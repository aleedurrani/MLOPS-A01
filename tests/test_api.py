# File: tests/test_api.py
import pytest
from app.api import app
import json

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict(client):
    data = {"age": 30, "weekly_usage_hrs": 10.5, "avg_session_duration": 35.0}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in json.loads(response.data)