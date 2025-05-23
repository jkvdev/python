# 📍 03 — FastAPI Dynamic Routes with Pydantic Models

This section shows how to create dynamic API routes using FastAPI, utilize Pydantic models for data validation, and handle errors gracefully.

---

## 🧠 Key Concepts

### ➕ Using Pydantic Models for Data Validation

We define an `Item` model to represent our inventory items:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    quantity: int
````

**Benefits of using Pydantic models:**

* Validates incoming and outgoing data types automatically.
* Provides clear structure and type hints, making the code safer and easier to maintain.
* Enables FastAPI to generate interactive API documentation.
* Handles serialization to JSON format for API responses.

---

### 🌐 Inventory Storage

We store our items in a Python dictionary with IDs as keys and `Item` instances as values:

```python
inventory = {
    "item1": Item(name="Laptop", price=1200, quantity=5),
    "item2": Item(name="Smartphone", price=800, quantity=10),
    "item3": Item(name="Tablet", price=600, quantity=7),
}
```

* Using Python native data structures allows efficient runtime data handling.
* JSON is used mainly for communication between client and server, while Python objects are easier to manipulate within the app.

---

### 🌐 Dynamic Route: `/get-item/{item_id}`

```python
@app.get("/get-item/{item_id}", response_model=dict)
def get_item(item_id: str):
    """
    Retrieve item details by ID.
    """
    item = inventory.get(item_id)
    if item:
        return {"item_id": item_id, "details": item}
    raise HTTPException(status_code=404, detail="Item not found")
```

* The endpoint returns item details dynamically based on the `item_id` provided.
* Returns a 404 error if the item does not exist.

---

### 📌 What is `response_model=dict`?

* It declares the expected response type (a Python dictionary here).
* Helps FastAPI validate and document the API response.
* Ensures consistent data structure is returned to clients.

---

## 🧪 How to Run

Inside the project directory, run:

```bash
uvicorn 02_dynamic_route:app --reload
```

Access endpoints:

* [http://127.0.0.1:8000/get-item/item1](http://127.0.0.1:8000/get-item/item1) — returns Laptop details
* [http://127.0.0.1:8000/get-item/nonexistent](http://127.0.0.1:8000/get-item/nonexistent) — returns 404 error
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) — interactive API docs

