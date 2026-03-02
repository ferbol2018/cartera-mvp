from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(
    prefix="/kpis",
    tags=["kpis"]
)

@router.get("/total_revenue")
def total_revenue(db: Session = Depends(get_db)):
    result = db.query(models.Payment).all()
    total = sum([p.amount for p in result])
    return {"total_revenue": total}

@router.get("/pending_invoices")
def pending_invoices(db: Session = Depends(get_db)):
    result = db.query(models.Invoice).filter(models.Invoice.status == "pending").count()
    return {"pending_invoices": result}

@router.get("/monthly_flow")
def monthly_flow(db: Session = Depends(get_db)):
    # Agrupar pagos por mes
    from collections import defaultdict
    import datetime

    result = db.query(models.Payment).all()
    flow = defaultdict(float)
    for p in result:
        month = p.date.strftime("%Y-%m")
        flow[month] += p.amount

    return {"monthly_flow": dict(flow)}