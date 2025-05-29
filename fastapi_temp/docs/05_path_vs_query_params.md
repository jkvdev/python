# 🔍 05 - Path Parameters vs Query Parameters

FastAPI allows us to **capture data from the URL** in two ways:

- **Path Parameters**: Required parts of the URL path
- **Query Parameters**: Optional or named values after `?`

Understanding the difference is essential for designing clean, intuitive APIs.

---

## 📌 1. Path Parameters

Path parameters are **embedded in the URL** and are typically used to **identify a specific resource**.

### ✅ Example:

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

* The `item_id` in `{item_id}` is part of the URL structure.
* If you visit `/items/123`, you'll get `{"item_id": 123}`

> ❗ Path parameters are **always required** — the route won’t match if they're missing.

---

## ❓ 2. Query Parameters

Query parameters appear **after the `?`** in a URL. They are used for:

* Filtering
* Searching
* Optional flags (e.g., pagination)

### ✅ Example:

```python
@app.get("/search/")
def search_items(name: str = "", limit: int = 10):
    return {"query": name, "limit": limit}
```

* This matches `/search/?name=apple&limit=5`
* They are **optional by default** unless you omit the default value

---

## 🔁 Mixed Parameters (Path + Query)

You can use both together:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, details: bool = False):
    return {"item_id": item_id, "show_details": details}
```

Call it like:

```
GET /items/42?details=true
```

---

## ⚠️ Parameter Order Matters

In Python and FastAPI:

* **Path parameters must come first** in your function definition
* **Query parameters must come after**
* If you mix them in the wrong order, you’ll get a syntax error unless you use a `*` to explicitly separate keyword-only arguments

### ❌ Incorrect:

```python
# This will raise an error!

@app.get("/items/{item_id}")
def read_item(details: bool = False, item_id: int): ...
```

### ✅ Correct:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, details: bool = False): ...
```

### ✅ Or use keyword-only separator:

```python
@app.get("/items/{item_id}")
def read_item(*, item_id: int, details: bool = False): ...
```

> 💡 The `*` tells Python that all parameters after it must be passed as **keyword arguments** (e.g., `details=true`).

---

## 🧠 Summary Table

| Feature           | Path Parameter      | Query Parameter          |
| ----------------- | ------------------- | ------------------------ |
| In URL path?      | ✅ Yes               | ❌ No (after `?`)         |
| Required?         | ✅ Always            | ❌ Optional by default    |
| Use case          | Identify resource   | Filter, search, optional |
| Declared as       | `/items/{id}`       | `limit: int = 10`        |
| Order in function | Before query params | After path params        |

---

## ✅ Summary

* Use **path parameters** to identify a specific resource (e.g., `/users/123`)
* Use **query parameters** for optional filters and configuration (e.g., `/search?name=apple`)
* FastAPI handles both cleanly, but you must **respect their order in function definitions**
* Use `*` if you want to force parameters to be passed as keywords only

Understanding this distinction helps you write clean, RESTful, and maintainable APIs.
