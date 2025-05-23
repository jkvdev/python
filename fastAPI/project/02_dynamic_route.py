from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int

inventory = {
    "item1": Item(name="Laptop", price=1200, quantity=5),
    "item2": Item(name="Smartphone", price=800, quantity=10),
    "item3": Item(name="Tablet", price=600, quantity=7),
}

@app.get("/get-item/{item_id}", response_model=dict)
def get_item(item_id: str):
    """
    Get item details by item ID.
    """
    item = inventory.get(item_id)
    if item:
        return {"item_id": item_id, "details": item}
    raise HTTPException(status_code=404, detail="Item not found")

