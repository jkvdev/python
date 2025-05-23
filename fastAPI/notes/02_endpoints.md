# 📍 02 — FastAPI Endpoints

This section demonstrates how to define basic endpoints using FastAPI and return JSON responses.

---

## 🧠 Key Concepts

### ➕ Creating the API Object
```python
from fastapi import FastAPI
app = FastAPI()
```

This creates the FastAPI application instance.

---

### 🌐 Defining Basic Routes

#### `/` (Root Endpoint)

```python
@app.get("/")
def read_root():
    return {"message": "Hello, world! I'm testing my FastAPI."}
```

This defines a GET endpoint at `/`. When accessed, it returns a simple JSON greeting.

#### `/about` Endpoint

```python
@app.get('/about')
def get_about():
    return {
        "description": "This is a test API for learning FastAPI. Welcome to the About Page!"
    }
```

Another basic endpoint providing static content as a JSON response.

---

## 🧪 How to Run

Make sure you're inside the `project/` directory and run:

```bash
uvicorn 01_endpoints:app --reload
```

Then visit:

* [http://127.0.0.1:8000](http://127.0.0.1:8000) → Root
* [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about) → About
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → Swagger UI

