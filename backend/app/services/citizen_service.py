from sqlalchemy.orm import Session

from app.models.citizen import Citizen
from app.models.kingdom import Kingdom
from app.schemas.citizen import CitizenCreate


def create_citizen(
    db: Session,
    kingdom_id: int,
    citizen_data: CitizenCreate,
) -> Citizen | None:
    kingdom = db.get(Kingdom, kingdom_id)

    if kingdom is None:
        return None

    citizen = Citizen(
        name=citizen_data.name,
        kingdom_id=kingdom_id,
    )

    db.add(citizen)
    db.commit()
    db.refresh(citizen)

    return citizen

def get_kingdom_citizens(
    db: Session,
    kingdom_id: int,
) -> list[Citizen] | None:
    kingdom = db.get(Kingdom, kingdom_id)

    if kingdom is None:
        return None

    return (
        db.query(Citizen)
        .filter(Citizen.kingdom_id == kingdom_id)
        .order_by(Citizen.id)
        .all()
    )