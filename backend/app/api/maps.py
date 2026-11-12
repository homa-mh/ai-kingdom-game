from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.map import MapResponse
from app.services.map_service import get_kingdom_map

router = APIRouter(
    prefix="/kingdoms/{kingdom_id}/map",
    tags=["Map"],
)


@router.get("/", response_model=MapResponse)
def read_kingdom_map(
    kingdom_id: int,
    db: Session = Depends(get_db),
):
    game_map = get_kingdom_map(db, kingdom_id)

    if game_map is None:
        raise HTTPException(
            status_code=404,
            detail="Kingdom or map not found",
        )

    return game_map