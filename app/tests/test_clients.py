import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app


client = TestClient(app)

def test_create_client():
    response = client.post("/clients/", params={"name": "Fernando", "email": "fernando@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Fernando"
    assert data["email"] == "fernando@example.com"

def test_list_clients():
    response = client.get("/clients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)