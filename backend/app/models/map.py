
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.kingdom import Kingdom


class GameMap(Base):
    __tablename__ = "maps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    kingdom_id: Mapped[int] = mapped_column(
        ForeignKey("kingdoms.id"),
        unique=True,
        nullable=False,
    )

    width: Mapped[int] = mapped_column(
        Integer,
        default=20,
        nullable=False,
    )

    height: Mapped[int] = mapped_column(
        Integer,
        default=20,
        nullable=False,
    )

    kingdom: Mapped["Kingdom"] = relationship(
        back_populates="game_map",
    )
