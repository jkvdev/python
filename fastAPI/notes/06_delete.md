# ⚡FastAPI Inventory Management API

This is a simple inventory management API built with FastAPI. It lets you create, read, update, and delete items from an in-memory inventory.

---

## How to Run Locally

1. Make sure you have Python 3.7 or higher installed.

2. Install FastAPI and Uvicorn (the server):
   ```bash
   pip install fastapi uvicorn
    ```

3. Save the code in a file named `main.py` (or your preferred name).

4. Run the app using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and go to [http://localhost:8000](http://localhost:8000) to see the API docs or start testing endpoints.

---

## Code Overview

### Imports and Setup

```python
from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional, Dict
from pydantic import BaseModel

app = FastAPI()
```

* **FastAPI**: The web framework used to build the API.
* **Path, Query**: Help declare and validate parameters.
* **HTTPException**: Used to return error responses.
* **Optional, Dict**: Type hints.
* **BaseModel**: Used to define data models with validation.

---

### Data Models

```python
class Item(BaseModel):
    name: str
    price: float
    quantity: int

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
```

* **Item**: Represents a full item with all required fields.
* **UpdateItem**: Represents fields that can be updated (all optional).

---

### Inventory Data

```python
inventory: Dict[str, Item] = {
    "item1": Item(name="Laptop", price=1200, quantity=5),
    "item2": Item(name="Smartphone", price=800, quantity=10),
    "item3": Item(name="Tablet", price=600, quantity=7),
}
```

* Inventory is a simple dictionary with string IDs as keys and `Item` objects as values.

---

## API Endpoints

### 1. Get Item by ID

```python
@app.get("/get-item/{item_id}")
def get_item(item_id: str = Path(description="The ID of the item you'd like to view")):
    item = inventory.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "details": item}
```

* **Usage example:**

  Open in browser or send GET request to:

  ```
  http://localhost:8000/get-item/item1
  ```

* **Response:**

  ```json
  {
    "item_id": "item1",
    "details": {
      "name": "Laptop",
      "price": 1200,
      "quantity": 5
    }
  }
  ```

---

### 2. Get Item by Name

```python
@app.get('/get-by-name')
def get_item_by_name(name: Optional[str] = Query(None, description="Name of the item to search for"), test: Optional[int] = None):
    if not name:
        raise HTTPException(status_code=400, detail="Name query parameter is required")
    for item_id, item in inventory.items():
        if item.name.lower() == name.lower():
            return {"item_id": item_id, "details": item}
    raise HTTPException(status_code=404, detail="Item not found")
```

* **Usage example:**

  ```
  http://localhost:8000/get-by-name?name=Laptop
  ```

* **Response:**

  ```json
  {
    "item_id": "item1",
    "details": {
      "name": "Laptop",
      "price": 1200,
      "quantity": 5
    }
  }
  ```

---

### 3. Get Item by ID and Optional Name Check

```python
@app.get("/get-item-combined/{item_id}")
def get_item_combined(
    item_id: str = Path(..., description="The ID of the item"),
    test: Optional[int] = Query(None),
    name: Optional[str] = Query(None)
):
    item = inventory.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if name and item.name.lower() != name.lower():
        raise HTTPException(status_code=404, detail="Item name does not match")
    return {"item_id": item_id, "details": item}
```

* **Usage example:**

  ```
  http://localhost:8000/get-item-combined/item1?name=Laptop
  ```

---

### 4. Create New Item

```python
@app.post("/create-item/{item_id}")
def create_item(item_id: str, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item_id] = item
    return inventory[item_id]
```

* **Usage example:** Use a tool like Postman or Curl to send a POST request.

* **Example JSON body:**

  ```json
  {
    "name": "Monitor",
    "price": 300,
    "quantity": 15
  }
  ```

---

### 5. Update Existing Item

```python
@app.put("/update-item/{item_id}")
def update_item(item_id: str, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    stored_item_data = inventory[item_id].dict()
    update_data = item.dict(exclude_unset=True)
    updated_item = Item(**stored_item_data, **update_data)
    inventory[item_id] = updated_item
    return updated_item
```

* **Usage example:** Update one or more fields by sending a PUT request with only the fields to update.

* **Example JSON body:**

  ```json
  {
    "price": 1100
  }
  ```

* This updates the price only, keeping other fields unchanged.

---

### 6. Delete Item by ID

```python
@app.delete("/delete-item/")
def delete_item(item_id: str = Query(..., description="The ID of the item you'd like to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    del inventory[item_id]
    return {"message": "Item deleted successfully"}
```

* **Usage example:**

  ```
  http://localhost:8000/delete-item/?item_id=item1
  ```

* **Response:**

  ```json
  {
    "message": "Item deleted successfully"
  }
  ```

---

## Notes

* The inventory is stored in memory — meaning changes will reset when you restart the app.
* Use the built-in interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs) for easier testing and exploration.

---

