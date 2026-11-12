from sqlalchemy.orm import Session

from app.models.kingdom import Kingdom
from app.models.map import GameMap
from app.schemas.kingdom import KingdomCreate, KingdomUpdate


def create_kingdom(db: Session, kingdom_data: KingdomCreate) -> Kingdom:
    kingdom = Kingdom(name=kingdom_data.name)

    game_map = GameMap(
        width=20,
        height=20,
    )

    kingdom.game_map = game_map

    db.add(kingdom)
    db.commit()
    db.refresh(kingdom)

    return kingdom


def get_kingdom(
    db: Session,
    kingdom_id: int,
) -> Kingdom | None:
    return db.get(Kingdom, kingdom_id)

def get_all_kingdoms(db: Session) -> list[Kingdom]:
    return db.query(Kingdom).order_by(Kingdom.id).all()

def update_kingdom(
    db: Session,
    kingdom_id: int,
    kingdom_data: KingdomUpdate,
) -> Kingdom | None:
    kingdom = db.get(Kingdom, kingdom_id)

    if kingdom is None:
        return None

    update_data = kingdom_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(kingdom, field, value)

    db.commit()
    db.refresh(kingdom)

    return kingdom