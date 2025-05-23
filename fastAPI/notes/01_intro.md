# 🚀 FastAPI Basics

This note summarizes the foundational concepts of FastAPI, a modern web framework for building APIs with Python 3.7+.

---

## 🧠 What Is FastAPI?

- **FastAPI** stands for **Fast** Application Programming Interface.
- It is a modern, fast (high-performance), web framework for building APIs using Python type hints.
- APIs are web services that allow applications to **retrieve and manipulate information** — frontend, mobile, or other backends can access them.

---

## ⚙️ Installation and Setup

Install FastAPI and a server like `uvicorn`:

```bash
pip install fastapi uvicorn
````

To run your FastAPI app:

```bash
uvicorn <filename-without-.py>:<app-variable-name> --reload
```

* `--reload`: Automatically reloads the server when code changes (useful for development).

---

## 🔍 Key Features

* **Automatic data validation**: Uses Python type hints to validate request parameters automatically.
* **Auto-generated documentation**: Interactive docs available via:

  * `http://127.0.0.1:8000/docs` (Swagger UI)
  * `http://127.0.0.1:8000/redoc` (ReDoc)
* **Great IDE support**: FastAPI's use of type hints enables powerful autocompletion and inline docs.

---

## 🧾 HTTP Methods and Routing

FastAPI supports the core HTTP verbs via decorators:

```python
@app.get("/")
@app.post("/")
@app.put("/")
@app.delete("/")
```

Each one defines a route handler. Example:

```python
@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

---

## 🧪 Data Types and Parameters

* Returns data as **JSON** (JavaScript Object Notation).
* Supports:

  * **Path Parameters** (`/items/{id}`)
  * **Query Parameters** (`/items?limit=10`)
* You can enforce constraints like `gt`, `lt`, `max_length`, etc.

Example with validation:

```python
from fastapi import Query

@app.get("/items/")
def read_items(limit: int = Query(..., gt=0, lt=100)):
    return {"limit": limit}
```

---

## 📦 Request Body and POST Methods

* `.post()` routes can accept a **request body**.
* Use **Pydantic models** for data validation:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

---

## ⚠️ Error Handling

* FastAPI supports **status codes** and **exception handling**.
* You can raise exceptions like this:

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {"item_id": item_id}
```

---

## ✅ Summary

| Feature         | Description                                |
| --------------- | ------------------------------------------ |
| Type Validation | Automatic using Python hints               |
| Auto Docs       | Swagger UI & ReDoc at `/docs` and `/redoc` |
| Request Methods | `.get()`, `.post()`, `.put()`, `.delete()` |
| Parameters      | Path & query parameters                    |
| JSON            | Default format for API input/output        |
| Request Body    | Use Pydantic models                        |
| Error Handling  | HTTPException + status codes               |

---

