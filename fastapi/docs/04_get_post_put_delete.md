# 🔁 04 - HTTP Methods: GET, POST, PUT, DELETE

## 🌐 What Are HTTP Methods?

HTTP methods define the **action** to be performed for a given resource. FastAPI supports all major methods and maps them cleanly to Python functions using decorators.

---

## 📌 1. `GET` – Retrieve Data

### 🔹 Use Case:
Used to fetch data without modifying it.

### ✅ Example:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

* `@app.get(...)`: Registers a `GET` route
* No body is sent; only parameters (like `item_id`)

---

## ➕ 2. `POST` – Create Data

### 🔹 Use Case:

Used to send data to the server to create a resource.

### ✅ Example:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"message": f"Item '{item.name}' created.", "item": item}
```

* Data is passed in the **request body** and validated by `Item` model
* `POST` is used when **submitting new resources**

---

## 🔁 3. `PUT` – Update Data (Replace or Modify)

### 🔹 Use Case:

Used to **update** an existing resource — either fully or partially.

### ✅ Example:

```python
class UpdateItem(BaseModel):
    name: str
    price: float

@app.put("/items/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    return {"message": f"Item {item_id} updated.", "item": item}
```

* Like `POST`, the body is validated using a model
* Often used for **partial or full updates**

> 💡 Tip: Use `exclude_unset=True` in `.model_dump()` if supporting partial updates.

---

## ❌ 4. `DELETE` – Remove Data

### 🔹 Use Case:

Used to delete a specific resource by ID.

### ✅ Example:

```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted."}
```

* No body is sent, just a path parameter
* Typically returns a confirmation message

---

## 📋 Summary Table

| Method   | Decorator       | Purpose              | Has Body? |
| -------- | --------------- | -------------------- | --------- |
| `GET`    | `@app.get()`    | Read/Retrieve data   | ❌         |
| `POST`   | `@app.post()`   | Create new resource  | ✅         |
| `PUT`    | `@app.put()`    | Update existing data | ✅         |
| `DELETE` | `@app.delete()` | Delete resource      | ❌         |

---

## ✅ Summary

FastAPI makes it easy to define RESTful APIs using Python decorators:

* Use the **appropriate method** for each kind of operation
* Use **Pydantic models** to validate input for `POST` and `PUT`
* FastAPI automatically adds these to your API docs, including schemas

Mastering these methods is essential for building full CRUD applications.

