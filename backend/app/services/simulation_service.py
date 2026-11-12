from sqlalchemy.orm import Session

from app.models.citizen import Citizen
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

    update_citizens_daily_needs(db, kingdom_id)

    db.commit()
    db.refresh(kingdom)

    return kingdom


def update_citizens_daily_needs(db: Session, kingdom_id: int) -> None:
    citizens = (
        db.query(Citizen)
        .filter(Citizen.kingdom_id == kingdom_id)
        .all()
    )

    for citizen in citizens:
        citizen.hunger = min(100, citizen.hunger + 20)