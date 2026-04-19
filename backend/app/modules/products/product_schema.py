from typing import Optional, Field
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    price: float = Field(gt=0)
    description: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    price: Optional[float] = Field(default=None, gt=0)
    description: Optional[str] = Field(default=None, min_length=1, max_length=255)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None