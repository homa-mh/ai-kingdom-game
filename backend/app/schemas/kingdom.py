
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator


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


class KingdomUpdate(BaseModel):
    food: int | None = Field(default=None, ge=0)
    wood: int | None = Field(default=None, ge=0)
    gold: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def validate_update(self):
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")

        if any(getattr(self, field) is None for field in self.model_fields_set):
            raise ValueError("Fields cannot be null")

        return self