
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.kingdom import Kingdom


class Citizen(Base):
    __tablename__ = "citizens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    kingdom_id: Mapped[int] = mapped_column(
        ForeignKey("kingdoms.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    hunger: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    energy: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    health: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    happiness: Mapped[int] = mapped_column(Integer, default=100, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    kingdom: Mapped["Kingdom"] = relationship(
        back_populates="citizens",
    )
