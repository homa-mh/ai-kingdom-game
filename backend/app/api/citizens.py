from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.citizen import CitizenCreate, CitizenResponse
from app.services.citizen_service import (
    create_citizen,
    get_kingdom_citizens,
)

router = APIRouter(prefix="/kingdoms/{kingdom_id}/citizens", tags=["Citizens"])


@router.post("/", response_model=CitizenResponse, status_code=201)
def create_new_citizen(
    kingdom_id: int,
    citizen_data: CitizenCreate,
    db: Session = Depends(get_db),
):
    citizen = create_citizen(db, kingdom_id, citizen_data)

    if citizen is None:
        raise HTTPException(status_code=404, detail="Kingdom not found")

    return citizen

@router.get("/", response_model=list[CitizenResponse])
def read_kingdom_citizens(
    kingdom_id: int,
    db: Session = Depends(get_db),
):
    citizens = get_kingdom_citizens(db, kingdom_id)

    if citizens is None:
        raise HTTPException(status_code=404, detail="Kingdom not found")

    return citizens