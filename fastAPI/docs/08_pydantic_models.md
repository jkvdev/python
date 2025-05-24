# 🧬 08 - Pydantic Models in FastAPI

## 🧠 What is Pydantic?

**Pydantic** is a data validation and parsing library used by FastAPI to define and enforce data structures using Python type hints.

FastAPI uses Pydantic under the hood to:

- Validate request bodies
- Serialize responses
- Generate OpenAPI docs
- Ensure type safety at runtime

---

## 📦 Basic `BaseModel` Usage

Define data models by subclassing `BaseModel`.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    quantity: int
```

This model can be used for input validation in routes:

```python
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

---

## 🧪 Validation Example

If a client sends invalid data:

```json
{
  "name": "Tablet",
  "price": "not_a_number",
  "quantity": 5
}
```

FastAPI automatically returns:

```json
{
  "detail": [
    {
      "loc": ["body", "price"],
      "msg": "value is not a valid float",
      "type": "type_error.float"
    }
  ]
}
```

---

## 🔤 Advanced Field Options with `Field`

You can add metadata and validation constraints using `Field`:

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0, description="Must be 0 or more")
```

* `...` means "required"
* `gt`, `ge` are validation rules (greater than, greater or equal)
* These also enhance the generated documentation!

---

## 🧩 Optional Fields and Defaults

Use `Optional` or default values for non-required fields:

```python
from typing import Optional

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
```

This is perfect for partial updates (`PUT` or `PATCH`).

---

## 🔁 `.model_dump()` and `.model_copy()`

### `model_dump()`

Returns a dictionary version of the model:

```python
item = Item(name="Tablet", price=600, quantity=3)
item_dict = item.model_dump()
```

You can also use:

```python
item.model_dump(exclude_unset=True)
```

To get only the fields that were actually set (useful for updates).

---

### `model_copy(update=...)`

Create a modified copy of a model:

```python
new_item = item.model_copy(update={"price": 700})
```

This avoids mutating the original object — a clean, immutable approach.

---

## 🔗 Nested Models

Pydantic models can contain other models:

```python
class Dimensions(BaseModel):
    width: float
    height: float

class Product(BaseModel):
    name: str
    dimensions: Dimensions
```

FastAPI will handle nested validation automatically.

---

## ✅ Summary

| Feature                  | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `BaseModel`              | Base class for creating Pydantic models         |
| `Field(...)`             | Adds validation and metadata to fields          |
| `Optional[...]`          | Allows fields to be missing (or default `None`) |
| `model_dump()`           | Converts model to a dictionary                  |
| `model_copy(update=...)` | Returns an updated, new model instance          |
| Nested models            | Pydantic handles validation recursively         |

---

## 🧠 Final Tip

Pydantic isn't just for FastAPI — it's a general-purpose validation tool. But FastAPI makes it shine by:

* Autogenerating docs
* Validating request and response bodies
* Providing runtime safety with minimal code

Mastering Pydantic means mastering FastAPI. 🔥

