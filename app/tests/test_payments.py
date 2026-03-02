import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app


client = TestClient(app)

def test_create_payment():
    # Primero creamos un cliente
    client_response = client.post("/clients/", params={"name": "Cliente Pago", "email": "pago@test.com"})
    client_id = client_response.json()["id"]

    # Creamos una factura
    invoice_response = client.post("/invoices/", params={"client_id": client_id, "amount": 500})
    invoice_id = invoice_response.json()["id"]

    # Creamos un pago para esa factura
    response = client.post("/payments/", params={"invoice_id": invoice_id, "amount": 500})
    assert response.status_code == 200
    data = response.json()
    assert data["invoice_id"] == invoice_id
    assert data["amount"] == 500

def test_list_payments():
    response = client.get("/payments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)