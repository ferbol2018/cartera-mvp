import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_total_revenue_empty_db():
    response = client.get("/kpis/total_revenue")
    assert response.status_code == 200
    data = response.json()
    # En una DB vacía, el revenue debe ser 0
    assert data["total_revenue"] == 0

def test_pending_invoices_empty_db():
    response = client.get("/kpis/pending_invoices")
    assert response.status_code == 200
    data = response.json()
    # En una DB vacía, no hay facturas pendientes
    assert data["pending_invoices"] == 0

def test_monthly_flow_empty_db():
    response = client.get("/kpis/monthly_flow")
    assert response.status_code == 200
    data = response.json()
    # En una DB vacía, el flujo mensual debe estar vacío
    assert data["monthly_flow"] == {}

def test_total_revenue_with_data(client, sample_data):
    response = client.get("/kpis/total_revenue")
    assert response.status_code == 200
    data = response.json()
    # Debe sumar el único pago registrado (500)
    assert data["total_revenue"] == 500

def test_pending_invoices_with_data(client, sample_data):
    response = client.get("/kpis/pending_invoices")
    assert response.status_code == 200
    data = response.json()
    # Debe haber 1 factura pendiente
    assert data["pending_invoices"] == 1

def test_monthly_flow_with_data(client, sample_data):
    response = client.get("/kpis/monthly_flow")
    assert response.status_code == 200
    data = response.json()
    # Debe existir un flujo mensual con el pago de 500
    assert any(val == 500 for val in data["monthly_flow"].values())