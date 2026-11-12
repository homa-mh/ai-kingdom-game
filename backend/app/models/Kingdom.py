from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Kingdom(Base):
    __tablename__ = "kingdoms"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    day: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    food: Mapped[int] = mapped_column(
        Integer,
        default=100,
        nullable=False,
    )

    wood: Mapped[int] = mapped_column(
        Integer,
        default=50,
        nullable=False,
    )

    gold: Mapped[int] = mapped_column(
        Integer,
        default=100,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
