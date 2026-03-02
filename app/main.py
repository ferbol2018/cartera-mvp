from fastapi import FastAPI
from app.routers import clients, invoices, payments, kpis
from app.db import Base, engine

# Crear tablas si no existen (solo útil en desarrollo)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar routers
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(kpis.router, prefix="/kpis", tags=["kpis"])
