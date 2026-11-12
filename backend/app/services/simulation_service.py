from sqlalchemy.orm import Session

from app.models.kingdom import Kingdom


DAILY_FOOD_CONSUMPTION = 10


def advance_day(db: Session, kingdom_id: int) -> Kingdom | None:
    kingdom = db.get(Kingdom, kingdom_id)

    if kingdom is None:
        return None

    kingdom.day += 1

    kingdom.food = max(
        0,
        kingdom.food - DAILY_FOOD_CONSUMPTION,
    )

    db.commit()
    db.refresh(kingdom)

    return kingdom
