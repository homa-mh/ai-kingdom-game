from pydantic import BaseModel, ConfigDict, Field


class CitizenCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)


class CitizenResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    kingdom_id: int
    name: str
    hunger: int
    energy: int
    health: int
    happiness: int