# ✨ 05 FastAPI Inventory Management API - Detailed Documentation

## 📦 Overview

This FastAPI application manages an inventory of items. It provides endpoints to:

* Retrieve items by ID or name
* Create new items
* Update existing items
* Delete items

The code is structured using **Pydantic models** for data validation, **FastAPI's path and query parameters**, and clean **exception handling** to build a reliable, well-documented API.

---

## 📐 1. Data Models

### `Item`

Defines a complete inventory item with required fields:

```python
name: str
price: float
quantity: int
```

### `UpdateItem`

Used for partial updates (all fields are optional). Clients can send only the fields they want to change.

---

## 🗃 2. Inventory Storage

The inventory is a simple **in-memory dictionary**:

```python
inventory: Dict[str, Item]
```

* ✅ Type-safe and schema-validated using Pydantic
* 🔄 Easily copy/update models using `.model_copy()` and `.model_dump()`
* 🧪 Great for learning and testing without needing a database

---

## 🛠 3. API Endpoints

### ✅ `GET /get-item/{item_id}`

* **Purpose:** Retrieve an item by ID
* **Params:** `item_id` (path)
* **Returns:** `ItemResponse`
* **Errors:** `404` if item not found

---

### 🔍 `GET /get-by-name`

* **Purpose:** Retrieve item by name
* **Params:**

  * `name` (query, required)
  * `test` (query, optional)
* **Behavior:** Case-insensitive match
* **Errors:** `400` if no name given, `404` if item not found

---

### 🔀 `GET /get-item-combined/{item_id}`

* **Purpose:** Retrieve item by ID and optionally verify name
* **Params:**

  * `item_id` (path)
  * `name` (query, optional)
  * `test` (query, optional)
* **Behavior:** Returns item only if name matches (if provided)

---

### ➕ `POST /create-item/{item_id}`

* **Purpose:** Create a new item
* **Params:**

  * `item_id` (path)
  * `Item` (body)
* **Behavior:** Adds new item to inventory
* **Errors:** `400` if item already exists

---

### 🔁 `PUT /update-item/{item_id}`

* **Purpose:** Update existing item (partial update)
* **Params:**

  * `item_id` (path)
  * `UpdateItem` (body)
* **Behavior:**

  * Uses `.model_dump(exclude_unset=True)` to extract only provided fields
  * Updates model with `.model_copy(update=...)`
* **Errors:** `404` if item not found

---

### ❌ `DELETE /delete-item/{item_id}`

* **Purpose:** Delete an item by ID
* **Params:** `item_id` (path)
* **Returns:** Confirmation message
* **Errors:** `404` if item does not exist

---

## 🧠 4. Key Concepts Demonstrated

### 🔸 Path & Query Parameters

Use of `Path()` and `Query()` provides built-in validation and automatic docs via Swagger UI.

### 🔸 HTTPException Handling

Returns appropriate `404` or `400` errors with meaningful messages for invalid input or missing items.

### 🔸 Pydantic Utilities

* `.model_dump(exclude_unset=True)` for extracting only the fields sent by the client
* `.model_copy(update=...)` to create updated model instances safely

---

## ✅ 5. Design Benefits

* **Modular & Readable**: Each concept is clearly separated
* **Type-Safe**: Strong typing via Pydantic reduces runtime bugs
* **Beginner-Friendly**: Easy to understand and extend
* **Auto-Documented**: Every route is described and visible in FastAPI’s built-in Swagger UI
* **Clean Update Logic**: Avoids mutation and overwriting with `None`

---

## 🚀 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

Then open your browser to:
👉 [http://localhost:8000/docs](http://localhost:8000/docs) – Interactive Swagger UI
👉 [http://localhost:8000/redoc](http://localhost:8000/redoc) – Redoc-style documentation

---

## 📚 Additional Notes

For concept-level explanations, refer to the `learning_notes/` folder. It contains individual tutorials on:

* Path vs Query parameters
* Pydantic model features
* Handling partial updates
* Error handling with `HTTPException`
* Project structure and modular design

---

## 🧠 Summary

This API project combines **clarity, structure, and best practices** for learning and demonstrating FastAPI fundamentals. It's an ideal starting point for building more complex APIs or integrating features like authentication, databases, or LangChain.

---

