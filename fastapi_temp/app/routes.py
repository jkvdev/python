from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import Optional
from .models import Item, UpdateItem
from .responses import ItemResponse, ItemResponseWithTest, UpdatedItemResponse, DeleteItemResponse
from .inventory import inventory


router = APIRouter()


@router.get("/get-item/{item_id}", response_model=ItemResponse)
def get_item(item_id: str = Path(...)):
    item = inventory.get(item_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemResponse(item_id=item_id, details=item)


@router.get("/get-by-name", response_model=ItemResponseWithTest)
def get_item_by_name(name: Optional[str] = Query(None), test: Optional[int] = Query(None)):
    if not name:
        raise HTTPException(status_code=400, detail="Query parameter 'name' is required")
    
    for item_id, item in inventory.items():
        if item.name.lower() == name.lower():
            return ItemResponseWithTest(item_id=item_id, details=item, test=test)
        
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/get-item-combined/{item_id}", response_model=ItemResponseWithTest)
def get_item_combined(item_id: str, test: Optional[int] = None, name: Optional[str] = None):
    item = inventory.get(item_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if name and item.name.lower() != name.lower():
        raise HTTPException(status_code=404, detail="Item name does not match")
    
    return ItemResponseWithTest(item_id=item_id, details=item, test=test)


@router.post("/create-item/{item_id}", response_model=ItemResponse)
def create_item(item_id: str, item: Item):
    
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    inventory[item_id] = item
    return ItemResponse(item_id=item_id, details=item)


@router.put("/update-item/{item_id}", response_model=UpdatedItemResponse)
def update_item(item_id: str, item: UpdateItem):
    existing = inventory.get(item_id)
    
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated = existing.model_copy(update=item.model_dump(exclude_unset=True))
    
    inventory[item_id] = updated
    return UpdatedItemResponse(item_id=item_id, updated=updated)


@router.delete("/delete-item/{item_id}", response_model=DeleteItemResponse, status_code=status.HTTP_200_OK)
def delete_item(item_id: str):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del inventory[item_id]
    return DeleteItemResponse(message="Item deleted successfully", item_id=item_id)
