from fastapi import FastAPI, Path, HTTPException, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int

class ItemResponse(BaseModel):
    item_id: str
    details: Item
    test: Optional[int] = None

inventory = {
    "item1": Item(name="Laptop", price=1200, quantity=5),
    "item2": Item(name="Smartphone", price=800, quantity=10),
    "item3": Item(name="Tablet", price=600, quantity=7),
}

@app.get(
    "/get-item/{item_id}", 
    response_model=ItemResponse,
    summary="Get item details by ID",
    response_description="The item details with the given ID"
)
def get_item_by_details(
    item_id: str = Path(..., description="The ID of the item you'd like to view")
) -> ItemResponse:
    """
    Retrieve item details by item ID.

    - **item_id**: Unique identifier for the item.
    """
    item = inventory.get(item_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemResponse(item_id=item_id, details=item)

@app.get(
    "/get-by-name",
    response_model=ItemResponse,
    summary="Get item details by name",
    response_description="The item details matching the given name"
)
def get_item_by_name(
    name: Optional[str] = Query(None, description="Name of the item to search for"),
    test: Optional[int] = Query(None, description="Optional test integer parameter")
) -> ItemResponse:
    """
    Retrieve item details by item name.

    - **name**: Name of the item to search for (required).
    - **test**: Optional test parameter for demonstration.
    """
    if not name:
        raise HTTPException(status_code=400, detail="Query parameter 'name' is required")
    
    for item_id, item in inventory.items():
        if item.name.lower() == name.lower():
            return ItemResponse(item_id=item_id, details=item, test=test)
        
    raise HTTPException(status_code=404, detail="Item not found")

@app.get(
    "/get-item-combined/{item_id}",
    response_model=ItemResponse,
    summary="Get item details by ID and optionally filter by name",
    response_description="The item details if ID and optional name match"
)
def get_item_combined(
    item_id: str = Path(..., description="The ID of the item"),
    test: Optional[int] = Query(None, description="Optional test parameter"),
    name: Optional[str] = Query(None, description="Optional item name to filter by")
) -> ItemResponse:
    """
    Retrieve item details by ID and optionally filter by name.

    - **item_id**: Unique identifier for the item.
    - **test**: Optional test parameter for demonstration.
    - **name**: Optional item name to filter the result.
    """
    item = inventory.get(item_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if name and item.name.lower() != name.lower():
        raise HTTPException(status_code=404, detail="Item name does not match")
    
    return ItemResponse(item_id=item_id, details=item, test=test)
