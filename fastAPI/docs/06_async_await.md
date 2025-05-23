# ⚡ 06 - Async and Await in FastAPI

## 🧠 What Is `async` / `await`?

`async` and `await` are part of Python’s **asynchronous programming model**.

They allow your app to **pause execution** while waiting for slow operations (like network calls or file I/O) — **without blocking** other requests.

---

## 🚀 Why Does It Matter in FastAPI?

FastAPI is built on **Starlette**, which uses **ASGI (Asynchronous Server Gateway Interface)**. This allows FastAPI to:

- Handle **many requests concurrently**
- Serve responses without blocking others
- Integrate with **async libraries** (like databases, HTTP clients, etc.)

---

## 🧪 Basic Comparison

### ✅ Synchronous Route

```python
@app.get("/sync")
def read_sync():
    return {"type": "sync"}
```

### ⚡ Asynchronous Route

```python
@app.get("/async")
async def read_async():
    return {"type": "async"}
```

They behave the same for simple return values — but only `async` functions can use `await`.

---

## 🕸 When to Use `async def`

Use `async def` if your route:

* Calls **external APIs** (e.g., `httpx`, `aiohttp`)
* Interacts with **async database libraries** (e.g., `encode/databases`, `SQLModel`, `Tortoise ORM`)
* Performs any I/O operation you want to **non-block**

---

## ⏱ Simulating Latency with `asyncio.sleep`

```python
import asyncio

@app.get("/delayed")
async def delayed_response():
    await asyncio.sleep(3)  # Simulates 3-second delay
    return {"message": "Waited 3 seconds"}
```

You can't use `await` inside a regular `def` route — it must be `async def`.

---

## ⚠️ Do You Always Need `async`?

No. Use regular `def` routes when:

* You are doing only **CPU-bound logic** (calculations, dict lookups, etc.)
* You aren’t calling anything async

**Mixing both** in your app is totally fine. FastAPI handles both seamlessly.

---

## ✅ Summary

| Feature            | `def`                | `async def`                    |
| ------------------ | -------------------- | ------------------------------ |
| Runs synchronously | ✅ Yes                | ❌ No                           |
| Can use `await`    | ❌ No                 | ✅ Yes                          |
| For I/O operations | ❌ Blocking           | ✅ Non-blocking                 |
| Common use cases   | Quick logic, sync DB | Async DB, API calls, I/O waits |

---

## 🧠 Final Tip

If you're using async libraries (like `httpx`, `databases`, etc.), always make your route handlers `async def`. Otherwise, stick with `def` for simplicity.

FastAPI is flexible enough to support both — and switching from one to the other is as easy as changing the function keyword.

```python
# Just switch from this:
def my_handler(): ...

# To this:
async def my_handler(): ...
```

This makes scaling your app from simple to advanced extremely easy.
