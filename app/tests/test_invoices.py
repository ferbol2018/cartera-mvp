import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app


client = TestClient(app)

def test_create_invoice():
    # Primero creamos un cliente
    client_response = client.post("/clients/", params={"name": "Cliente Test", "email": "cliente@test.com"})
    client_id = client_response.json()["id"]

    # Creamos una factura para ese cliente
    response = client.post("/invoices/", params={"client_id": client_id, "amount": 1000})
    assert response.status_code == 200
    data = response.json()
    assert data["client_id"] == client_id
    assert data["amount"] == 1000

def test_list_invoices():
    response = client.get("/invoices/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)