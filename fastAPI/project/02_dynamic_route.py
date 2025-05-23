from fastapi import FastAPI

app = FastAPI()

inventory = {
    "item1": {"name": "Laptop", "price": 1200, "quantity": 5},
    "item2": {"name": "Smartphone", "price": 800, "quantity": 10},
    "item3": {"name": "Tablet", "price": 600, "quantity": 7},
}

@app.get("/get-item/{item_id}")
def get_item(item_id: str):
    """
    Get item details by item ID.
    """
    item = inventory[item_id]
    if item:
        return {"item_id": item_id, "details": item}
    else:
        return {"error": "Item not found"}
