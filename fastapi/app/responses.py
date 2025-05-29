from pydantic import BaseModel
from typing import Optional
from .models import Item

class ItemResponse(BaseModel):
    item_id: str
    details: Item

class ItemResponseWithTest(ItemResponse):
    test: Optional[int] = None

class UpdatedItemResponse(BaseModel):
    item_id: str
    updated: Item

class DeleteItemResponse(BaseModel):
    message: str
    item_id: str
