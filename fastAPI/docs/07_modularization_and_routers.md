# 🧩 07 - Modularization and Routers in FastAPI

As your FastAPI application grows, keeping all endpoints in a single `main.py` file becomes hard to manage.

FastAPI provides **`APIRouter`** to help split your app into multiple logical files or modules — making it cleaner, maintainable, and scalable.

---

## 🧱 Why Modularize?

### ✅ Benefits

- Separation of concerns
- Easier to read, test, and maintain
- Scalable project structure
- Reusable route modules across projects or apps

---

## 📦 Example Project Structure

```plaintext
your_project/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── items.py
```

---

## 🔧 Step-by-Step Modularization

### 1️⃣ Create a Router Module: `items.py`

```python
# app/routes/items.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@router.post("/items/")
def create_item(name: str):
    return {"message": f"Created item '{name}'"}
```

---

### 2️⃣ Connect It in `main.py`

```python
# app/main.py

from fastapi import FastAPI
from app.routes import items

app = FastAPI()

app.include_router(items.router)
```

* `include_router()` mounts the router inside your main app
* All routes in `items.py` are now accessible from the base URL

---

### 3️⃣ Optional: Use Tags or Prefixes

You can **group routes** or **prefix them**:

```python
# app/main.py

app.include_router(items.router, prefix="/api/items", tags=["Items"])
```

* This changes `/items/1` to `/api/items/1`
* `tags=["Items"]` improves Swagger UI grouping

---

## 🔄 Multiple Routers Example

You can have separate files for:

* `users.py`
* `orders.py`
* `admin.py`

Each with its own router, all included in `main.py`.

```python
from app.routes import items, users, orders

app.include_router(items.router)
app.include_router(users.router)
app.include_router(orders.router)
```

---

## ✅ Summary

| Feature            | Description                               |
| ------------------ | ----------------------------------------- |
| `APIRouter()`      | Defines a router in any module            |
| `include_router()` | Adds that router to your main FastAPI app |
| `prefix="/..."`    | Adds a route prefix (e.g., `/api/items`)  |
| `tags=["..."]`     | Categorizes routes in Swagger UI          |

---

## 🧠 Final Tip

Modularization is **not just for large apps** — it’s a best practice for any project beyond a few endpoints. You’ll thank yourself later when it’s time to refactor, test, or expand.

Start modular, stay modular. 🎯

