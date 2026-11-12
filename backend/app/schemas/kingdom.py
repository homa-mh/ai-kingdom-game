
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class KingdomCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )


class KingdomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    day: int
    food: int
    wood: int
    gold: int
    created_at: datetime
