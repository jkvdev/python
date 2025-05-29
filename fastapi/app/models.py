from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)
