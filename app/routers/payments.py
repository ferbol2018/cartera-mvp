from fastapi import APIRouter
from app.models.payment import PaymentCreate, PaymentRead

router = APIRouter()

fake_payments_db = []

@router.post("/", response_model=PaymentRead)
def create_payment(payment: PaymentCreate):
    new_payment = {"id": len(fake_payments_db) + 1, **payment.dict()}
    fake_payments_db.append(new_payment)
    return new_payment

@router.get("/", response_model=list[PaymentRead])
def list_payments():
    return fake_payments_db