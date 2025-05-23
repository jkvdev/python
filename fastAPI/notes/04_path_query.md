# 📦 04 — FastAPI Dynamic Routes with Pydantic Models and Query Filters

This FastAPI project provides a simple inventory API for retrieving item details by ID, name, or both. It uses Python type hints and Pydantic models to ensure clean, readable, and well-documented code.

---

## 🔧 Features

* ✅ Get item details by **ID**
* ✅ Search item by **name**
* ✅ Combine ID with optional name filtering
* ✅ Well-documented endpoints with OpenAPI auto-doc support (`/docs`)
* ✅ Strong input validation and clean error handling

---

## 🧠 Concepts Explained (Beginner Friendly)

### 🔹 1. `FastAPI` & Decorators

Each endpoint uses the `@app.get()` decorator to define a route. For example:

```python
@app.get("/get-item/{item_id}")
```

This tells FastAPI to run a function when someone accesses `/get-item/item1` (or any item ID).

---

### 🔹 2. `Path` and `Query` Parameters

* `Path(...)` is used for required values in the URL.
* `Query(...)` is used for optional values like filters.

Example:

```python
item_id: str = Path(..., description="The ID of the item")
test: Optional[int] = Query(None, description="Optional test parameter")
```

The `...` means the `item_id` is **required**. `None` means the query parameter is optional.

---

### 🔹 3. `Pydantic` Models

We use `BaseModel` to define what an item looks like.

```python
class Item(BaseModel):
    name: str
    price: float
    quantity: int
```

This ensures consistency in data — no surprises or messy types. Responses follow the `ItemResponse` model:

```python
class ItemResponse(BaseModel):
    item_id: str
    details: Item
    test: Optional[int] = None
```

This keeps the API clean and predictable for users and developers.

---

### 🔹 4. Response Models & OpenAPI Docs

Each endpoint uses a `response_model=ItemResponse`, which automatically:

* Validates and formats the output
* Generates clean Swagger docs at `/docs`
* Makes testing and frontend integration much easier

```python
@app.get("/get-by-name", response_model=ItemResponse)
```

`summary` and `response_description` are also used to power the built-in interactive API docs:

```python
summary="Get item details by name",
response_description="The item details matching the given name"
```

---

### 🔹 5. Error Handling

Using `HTTPException` ensures meaningful error messages:

```python
raise HTTPException(status_code=404, detail="Item not found")
```

FastAPI automatically sends back a proper JSON error like:

```json
{
  "detail": "Item not found"
}
```

---

### 🔹 6. Type Hints & Return Types

Each function has a clear return type:

```python
def get_item_by_name(...) -> ItemResponse:
```

This helps FastAPI validate your code and improves editor autocompletion.

---

## 🚀 Available Endpoints

| Method | Path                                                | Description                                  |
| ------ | --------------------------------------------------- | -------------------------------------------- |
| GET    | `/get-item/{item_id}`                               | Get item by ID                               |
| GET    | `/get-by-name?name=Laptop`                          | Get item by name (query param)               |
| GET    | `/get-item-combined/{item_id}?name=Laptop&test=123` | Get item by ID and optionally filter by name |

---

## ✅ Example Usage

### ➤ Get item by ID:

```bash
GET /get-item/item1
```

### ➤ Get item by name:

```bash
GET /get-by-name?name=Tablet
```

### ➤ Combined:

```bash
GET /get-item-combined/item2?name=Smartphone&test=99
```

---

## 🧪 Try it Out

Once the app is running, visit:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc (alternative docs): `http://localhost:8000/redoc`

---

