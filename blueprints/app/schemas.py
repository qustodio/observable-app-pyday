from datetime import datetime

from pydantic import BaseModel


class BlueprintBase(BaseModel):
    name: str
    description: str | None = None


class BlueprintCreate(BlueprintBase):
    pass


class Blueprint(BlueprintBase):
    id: int
    created_at: datetime | None = None
    # owner_id: int

    class Config:
        orm_mode = True
