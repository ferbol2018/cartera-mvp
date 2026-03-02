from fastapi import APIRouter
from app.models.invoice import InvoiceCreate, InvoiceRead

router = APIRouter()

fake_invoices_db = []

@router.post("/", response_model=InvoiceRead)
def create_invoice(invoice: InvoiceCreate):
    new_invoice = {"id": len(fake_invoices_db) + 1, **invoice.dict()}
    fake_invoices_db.append(new_invoice)
    return new_invoice

@router.get("/", response_model=list[InvoiceRead])
def list_invoices():
    return fake_invoices_db