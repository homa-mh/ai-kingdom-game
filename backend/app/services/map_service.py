from sqlalchemy.orm import Session

from app.models.kingdom import Kingdom
from app.models.map import GameMap


def get_kingdom_map(db: Session, kingdom_id: int) -> GameMap | None:
    kingdom = db.get(Kingdom, kingdom_id)

    if kingdom is None:
        return None

    return kingdom.game_map