# 📘 01 - FastAPI Overview

## 🚀 What is FastAPI?

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on **standard Python type hints**.

### 🔑 Key Features

- **Fast**: Very high performance (on par with Node.js and Go)
- **Pythonic**: Fully type-hint driven (based on Pydantic & Starlette)
- **Automatic docs**: Interactive documentation with Swagger and ReDoc
- **Validation**: Powerful input validation using Pydantic
- **Async support**: First-class support for async/await and concurrency

---

## ⚙️ When to Use FastAPI

- Building modern REST APIs
- Backend for frontend apps (React, Vue, etc.)
- Microservices or event-driven apps
- ML/AI model serving
- Prototyping APIs with rich docs

---

## 📈 Comparison

| Framework  | Auto Docs | Type Safety | Async Support | Performance |
|------------|-----------|-------------|----------------|-------------|
| Flask      | ❌        | ❌          | ⚠️ Limited     | 🟨 Moderate  |
| Django     | ⚠️ Partial| ❌          | ⚠️ Partial     | 🟨 Moderate  |
| FastAPI    | ✅        | ✅          | ✅             | ✅ Excellent |

---

## 🧪 Minimal Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
````

### 🔍 What happens here?

* `FastAPI()` creates the app instance.
* `@app.get("/")` declares a route for HTTP `GET` at `/`.
* The function defines the logic to run and returns a dictionary (converted to JSON).
* Interactive docs automatically available at `/docs`.

---

## 🎯 Summary

FastAPI is ideal for building APIs quickly and safely with minimal code. With type hints, data validation, and modern features like automatic docs and async support, it's a great choice for both learning and production use.

