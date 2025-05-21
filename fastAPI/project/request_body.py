from fastapi import FastAPI, Path
from typing import Optional
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

inventory = {
    "item1": {"name": "Laptop", "price": 1200, "quantity": 5},
    "item2": {"name": "Smartphone", "price": 800, "quantity": 10},
    "item3": {"name": "Tablet", "price": 600, "quantity": 7},
}

# Variable path, no more need for default value
@app.get("/get-item/{item_id}")
def get_item(item_id: str = Path(description="The ID of the item you'd like to view")):
    """
    Get item details by item ID.
    """
    item = inventory[item_id]
    if item:
        return {"item_id": item_id, "details": item}
    else:
        return {"error": "Item not found"}
      
# Query parameter
@app.get('/get-by-name')
# Default value is used to make the parameter optional
def get_item(*, name: Optional[str] = None, test: int):
    """
    Get item details by item name.
    """
    for item_id, item in inventory.items():
        if item["name"].lower() == name.lower():
            return {"item_id": item_id, "details": item}
    return {"error": "Item not found"}
  
# http://localhost:8000/get-by-name?name=smartphone
# http://localhost:8000/get-by-name?test=1&name=smartphone

# to merge both path and query parameters
@app.get("/get-item/{item_id}")
def get_item(item_id: str, test: int, name: Optional[str] = None):
    """
    Get item details by item ID and name.
    """
    item = inventory[item_id]
    if item:
        return {"item_id": item_id, "details": item}
    else:
        return {"error": "Item not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: str, item: Item):
    if item_id in inventory:
        return {"error": "Item already exists"}
    inventory[item_id] = {"name": item.name, "price": item.price, "quantity": item.quantity}
    return inventory[item_id]
    
# @app.put("/update-item/{item_id}")
# def update_item(item_id: str, item: UpdateItem):
#     if item_id not in inventory:
#         return {"error": "Item not found"}
    
#     if item.name != None:
#         inventory[item_id].name = item.name
#     if item.price != None:
#         inventory[item_id].price = item.price
#     if item.quantity != None:
#         inventory[item_id].quantity = item.quantity
#     return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: str, item: UpdateItem):
    if item_id not in inventory:
        return {"error": "Item not found"}
    inventory[item_id].update(item)
    return inventory[item_id]
