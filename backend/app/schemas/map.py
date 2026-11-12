from pydantic import BaseModel, ConfigDict


class MapResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    kingdom_id: int
    width: int
    height: int