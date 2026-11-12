
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.kingdom import KingdomCreate, KingdomResponse
from app.services.kingdom_service import create_kingdom, get_all_kingdoms, get_kingdom

router = APIRouter(
    prefix="/kingdoms",
    tags=["Kingdoms"],
)


@router.post("/", response_model=KingdomResponse, status_code=201)
def create_new_kingdom(
    kingdom_data: KingdomCreate,
    db: Session = Depends(get_db),
):
    return create_kingdom(db, kingdom_data)

@router.get("/", response_model=list[KingdomResponse])
def read_all_kingdoms(
    db: Session = Depends(get_db),
):
    return get_all_kingdoms(db)

@router.get("/{kingdom_id}", response_model=KingdomResponse)
def read_kingdom(
    kingdom_id: int,
    db: Session = Depends(get_db),
):
    kingdom = get_kingdom(db, kingdom_id)

    if kingdom is None:
        raise HTTPException(
            status_code=404,
            detail="Kingdom not found",
        )

    return kingdom

