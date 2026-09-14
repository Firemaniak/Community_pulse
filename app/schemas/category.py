from pydantic import BaseModel, Field
from typing import Optional


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True