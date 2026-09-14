from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    """Short view category inside answer about question"""
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: Optional[int] = None


class QuestionResponse(BaseModel):
    id: int
    text: str
    category: Optional[CategoryBase] = None

    class Config:
        orm_mode = True
        from_attributes = True


class MessageResponse(BaseModel):
    message: str