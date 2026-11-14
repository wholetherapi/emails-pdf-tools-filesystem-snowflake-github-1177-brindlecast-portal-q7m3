from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_session
from models import Remittance
from schemas import RemittanceOut

router = APIRouter()


@router.get("/remittances", response_model=list[RemittanceOut])
def list_remittances(session: Session = Depends(get_session)):
    return session.query(Remittance).order_by(Remittance.paid_on.desc()).all()


@router.get("/remittances/{remittance_id}", response_model=RemittanceOut)
def get_remittance(remittance_id: str, session: Session = Depends(get_session)):
    row = session.get(Remittance, remittance_id)
    if row is None:
        raise HTTPException(status_code=404, detail="remittance not found")
    return row
