from fastapi import FastAPI
from app.routers import clients, invoices, payments

app = FastAPI(title="Cartera MVP")

app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])