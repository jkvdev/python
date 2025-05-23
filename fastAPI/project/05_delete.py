from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional, Dict
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

# Initialize inventory with Item instances for type consistency
inventory: Dict[str, Item] = {
    "item1": Item(name="Laptop", price=1200, quantity=5),
    "item2": Item(name="Smartphone", price=800, quantity=10),
    "item3": Item(name="Tablet", price=600, quantity=7),
}

@app.get("/get-item/{item_id}")
def get_item(item_id: str = Path(description="The ID of the item you'd like to view")):
    """
    Get item details by item ID.
    """
    item = inventory.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "details": item}

@app.get('/get-by-name')
def get_item_by_name(name: Optional[str] = Query(None, description="Name of the item to search for"), test: Optional[int] = None):
    """
    Get item details by item name.
    """
    if not name:
        raise HTTPException(status_code=400, detail="Name query parameter is required")
    for item_id, item in inventory.items():
        if item.name.lower() == name.lower():
            return {"item_id": item_id, "details": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/get-item-combined/{item_id}")
def get_item_combined(
    item_id: str = Path(..., description="The ID of the item"),
    test: Optional[int] = Query(None),
    name: Optional[str] = Query(None)
):
    """
    Get item by ID and optionally verify name matches.
    """
    item = inventory.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if name and item.name.lower() != name.lower():
        raise HTTPException(status_code=404, detail="Item name does not match")
    return {"item_id": item_id, "details": item}

@app.post("/create-item/{item_id}")
def create_item(item_id: str, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: str, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    stored_item_data = inventory[item_id].dict()
    update_data = item.dict(exclude_unset=True)
    updated_item = Item(**stored_item_data, **update_data)
    inventory[item_id] = updated_item
    return updated_item

@app.delete("/delete-item/")
def delete_item(item_id: str = Query(..., description="The ID of the item you'd like to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    del inventory[item_id]
    return {"message": "Item deleted successfully"}
