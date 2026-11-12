
from sqlalchemy.orm import Session

from app.models.kingdom import Kingdom
from app.schemas.kingdom import KingdomCreate


def create_kingdom(
    db: Session,
    kingdom_data: KingdomCreate,
) -> Kingdom:
    kingdom = Kingdom(
        name=kingdom_data.name,
    )

    db.add(kingdom)
    db.commit()
    db.refresh(kingdom)

    return kingdom


def get_kingdom(
    db: Session,
    kingdom_id: int,
) -> Kingdom | None:
    return db.get(Kingdom, kingdom_id)
