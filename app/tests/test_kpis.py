import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_total_revenue_empty_db(client):
    response = client.get("/kpis/total_revenue")
    assert response.status_code == 200
    data = response.json()
    assert data["total_revenue"] == 0

def test_pending_invoices_empty_db(client):
    response = client.get("/kpis/pending_invoices")
    assert response.status_code == 200
    data = response.json()
    assert data["pending_invoices"] == 0

def test_monthly_flow_empty_db(client):
    response = client.get("/kpis/monthly_flow")
    assert response.status_code == 200
    data = response.json()
    assert data["monthly_flow"] == {}

def test_total_revenue_with_data(client, sample_data):
    response = client.get("/kpis/total_revenue")
    assert response.status_code == 200
    data = response.json()
    assert data["total_revenue"] == 500  # único pago registrado

def test_pending_invoices_with_data(client, sample_data):
    response = client.get("/kpis/pending_invoices")
    assert response.status_code == 200
    data = response.json()
    assert data["pending_invoices"] == 1  # una factura pendiente

def test_monthly_flow_with_data(client, sample_data):
    response = client.get("/kpis/monthly_flow")
    assert response.status_code == 200
    data = response.json()
    assert any(val == 500 for val in data["monthly_flow"].values())