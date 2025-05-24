# 🚨 09 - HTTPException and Status Codes in FastAPI

FastAPI makes it easy to handle errors using built-in tools like `HTTPException` and the `status` module. This allows your API to return consistent, informative responses when something goes wrong.

---

## ⚠️ What is `HTTPException`?

`HTTPException` is a built-in FastAPI exception class used to return **custom error responses** with a specific status code and message.

---

## 🔧 Basic Usage

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

### ✅ What happens?

* If the item isn’t found, the API returns:

```json
{
  "detail": "Item not found"
}
```

* With status code: `404 Not Found`

---

## 🎯 Why Use `HTTPException`?

* It integrates cleanly with FastAPI’s docs
* You don’t have to manually format JSON errors
* You can customize the message and status code

---

## 📦 Using `status` for Readable Codes

Instead of writing raw integers (e.g. `404`), use FastAPI’s `status` module:

```python
from fastapi import HTTPException, status

@app.get("/admin")
def access_admin(user_role: str):
    if user_role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this resource"
        )
```

### ✅ Benefits:

* Improves code readability
* Avoids "magic numbers"
* Provides autocompletion in editors

---

## 🔄 Common Status Codes

| Status Code | Constant                                | Meaning                        |
| ----------- | --------------------------------------- | ------------------------------ |
| 200         | `status.HTTP_200_OK`                    | Success                        |
| 201         | `status.HTTP_201_CREATED`               | Resource created               |
| 204         | `status.HTTP_204_NO_CONTENT`            | Success, no body returned      |
| 400         | `status.HTTP_400_BAD_REQUEST`           | Client-side input error        |
| 401         | `status.HTTP_401_UNAUTHORIZED`          | Auth required                  |
| 403         | `status.HTTP_403_FORBIDDEN`             | Authenticated but forbidden    |
| 404         | `status.HTTP_404_NOT_FOUND`             | Resource not found             |
| 422         | `status.HTTP_422_UNPROCESSABLE_ENTITY`  | Validation error (by Pydantic) |
| 500         | `status.HTTP_500_INTERNAL_SERVER_ERROR` | Server error                   |

---

## 🔧 Custom Headers (Advanced)

You can even add custom headers to the exception:

```python
raise HTTPException(
    status_code=400,
    detail="Invalid request",
    headers={"X-Error": "Custom header message"}
)
```

---

## 🛡 Handling Exceptions Globally

You can create custom exception handlers for your own classes:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

class CustomAppException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(CustomAppException)
async def custom_handler(request: Request, exc: CustomAppException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} triggered a custom error."}
    )
```

> This makes FastAPI extremely flexible for advanced error handling.

---

## ✅ Summary

| Concept            | Use                                  |
| ------------------ | ------------------------------------ |
| `HTTPException`    | Raise errors with status and message |
| `status` module    | Use semantic HTTP status constants   |
| Custom headers     | Add metadata to error responses      |
| Exception handlers | Customize global error behavior      |

---

## 🧠 Final Tip

Use `HTTPException` anywhere you need to stop request handling with an error. Combine it with `status` for clean, maintainable, and meaningful APIs.

Good APIs don’t just return data — they **communicate clearly when things go wrong**.

