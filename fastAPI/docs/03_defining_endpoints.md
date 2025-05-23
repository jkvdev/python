# 📘 03 - Defining Endpoints in FastAPI

## 🌐 What is an Endpoint?

In FastAPI, an **endpoint** is a function that handles a specific HTTP request (GET, POST, etc.) made to a particular **URL path**.

Each endpoint is defined using a Python function decorated with `@app.get()`, `@app.post()`, etc., and is automatically documented via FastAPI's built-in Swagger UI.

---

## 🛠 How to Define an Endpoint

### 🔹 Basic Structure

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, world!"}
````

### ✅ What Happens

* `@app.get("/hello")`: Registers a `GET` route at `/hello`.
* `say_hello`: The function that gets executed when that route is hit.
* Return values are automatically converted to JSON.

---

## 🔀 Common HTTP Methods

| Method | Decorator       | Use Case                |
| ------ | --------------- | ----------------------- |
| GET    | `@app.get()`    | Retrieve data           |
| POST   | `@app.post()`   | Create new resource     |
| PUT    | `@app.put()`    | Replace/update resource |
| DELETE | `@app.delete()` | Remove resource         |

---

## 🧠 Example: Multiple Endpoints

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory API"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}
```

### 🔍 Explanation

* `/`: Basic GET request (homepage).
* `/items/{item_id}`: Path parameter (dynamic route).
* `/items/` with `POST`: Accepts query parameters (or body with Pydantic, which you’ll explore later).

---

## 🗂 Organizing Endpoints (Optional Preview)

As your app grows, you can split endpoints into **routers** or modules using `APIRouter` and include them in your main app with `include_router()` — covered in a future note.

---

## 🧪 Try It!

Run your app and open:

* Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

FastAPI generates this documentation for **every defined endpoint** automatically.

---

## ✅ Summary

* FastAPI endpoints are Python functions decorated with HTTP method decorators.
* Each decorator defines **which URL** and **what kind of request** the function handles.
* You can return any data (dicts, models, etc.), and FastAPI will convert it to JSON.
* The docs are **auto-generated** from these declarations, including descriptions, parameters, and return types.
