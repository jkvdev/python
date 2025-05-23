from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional, Dict
from pydantic import BaseModel


app = FastAPI()


# Data Models
class Item(BaseModel):
    name: str
    price: float
    quantity: int


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


# Response Models
class ItemResponse(BaseModel):
    item_id: str
    details: Item


class ItemResponseWithTest(ItemResponse):
    test: Optional[int] = None


class UpdatedItemResponse(BaseModel):
    item_id: str
    updated: Item


# Inventory Storage
inventory: Dict[str, Item] = {
    "item1": Item(name="Laptop", price=1200, quantity=5),
    "item2": Item(name="Smartphone", price=800, quantity=10),
    "item3": Item(name="Tablet", price=600, quantity=7),
}


@app.get(
    "/get-item/{item_id}",
    summary="Get item by ID",
    response_description="Item details for given ID",
    response_model=ItemResponse
)
def get_item(item_id: str = Path(..., description="The ID of the item you'd like to view")) -> ItemResponse:
    """
    Retrieve item details by item ID.
    """
    item = inventory.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(item_id=item_id, details=item)


@app.get(
    "/get-by-name",
    summary="Get item by name",
    response_description="Item details for matching name",
    response_model=ItemResponseWithTest
)
def get_item_by_name(
    name: Optional[str] = Query(None, description="Name of the item"),
    test: Optional[int] = Query(None, description="Optional test parameter")
) -> ItemResponseWithTest:
    """
    Retrieve item details by name (case insensitive).
    """
    if not name:
        raise HTTPException(status_code=400, detail="Query parameter 'name' is required")

    for item_id, item in inventory.items():
        if item.name.lower() == name.lower():
            return ItemResponseWithTest(item_id=item_id, details=item, test=test)
    raise HTTPException(status_code=404, detail="Item not found")


@app.get(
    "/get-item-combined/{item_id}",
    summary="Get item by ID with optional name filter",
    response_description="Item details if ID and optional name match",
    response_model=ItemResponseWithTest
)
def get_item_combined(
    item_id: str = Path(..., description="The ID of the item"),
    test: Optional[int] = Query(None, description="Optional test parameter"),
    name: Optional[str] = Query(None, description="Optional name to filter by")
) -> ItemResponseWithTest:
    """
    Retrieve item details by ID and optionally filter by name.
    """
    item = inventory.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if name and item.name.lower() != name.lower():
        raise HTTPException(status_code=404, detail="Item name does not match")

    return ItemResponseWithTest(item_id=item_id, details=item, test=test)


@app.post(
    "/create-item/{item_id}",
    summary="Create a new item",
    response_description="Item successfully created",
    response_model=ItemResponse
)
def create_item(item_id: str, item: Item) -> ItemResponse:
    """
    Add a new item to the inventory.
    """
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item_id] = item
    return ItemResponse(item_id=item_id, details=item)


@app.put(
    "/update-item/{item_id}",
    summary="Update an existing item",
    response_description="Updated item details",
    response_model=UpdatedItemResponse
)
def update_item(item_id: str, item: UpdateItem) -> UpdatedItemResponse:
    """
    Update an existing item with new values.
    """
    existing_item = inventory.get(item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_data = item.model_dump(exclude_unset=True)
    updated_item = existing_item.model_copy(update=updated_data)
    inventory[item_id] = updated_item

    return UpdatedItemResponse(item_id=item_id, updated=updated_item)
