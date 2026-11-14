from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from db import get_session
from models import Invoice
from schemas import InvoiceOut

router = APIRouter()


@router.get("/invoices", response_model=list[InvoiceOut])
def list_invoices(session: Session = Depends(get_session)):
    return session.query(Invoice).order_by(Invoice.issued_on.desc()).limit(200).all()


@router.post("/invoices", status_code=201)
async def upload_invoice(file: UploadFile = File(...), session: Session = Depends(get_session)):
    payload = await file.read()
    invoice = Invoice(source_name=file.filename, payload=payload)
    session.add(invoice)
    session.commit()
    return {"id": invoice.id}
