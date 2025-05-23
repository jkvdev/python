# ✨ 05 FastAPI Inventory Management API - Detailed Documentation

### Overview

This FastAPI application manages an inventory of items. It provides endpoints to:

* Retrieve items by ID or name.
* Create new items.
* Update existing items.

The code is structured to use **Pydantic models** for data validation and serialization, along with **FastAPI's path and query parameters** and **exception handling** to build a clean, reliable API.

---

### 1. Data Models (`Item` and `UpdateItem`)

* **`Item` model:**
  Represents a complete inventory item with mandatory fields:

  * `name` (str)
  * `price` (float)
  * `quantity` (int)

* **`UpdateItem` model:**
  Used for partial updates; all fields are optional. This model allows clients to send only the fields they want to update.

---

### 2. Inventory Storage

* The inventory is a **dictionary mapping item IDs (strings) to `Item` instances**:

  ```python
  inventory: Dict[str, Item]
  ```

* Storing Pydantic models (instead of plain dictionaries) ensures:

  * **Data validation:** Every item adheres to the defined schema.
  * **Consistency:** All inventory data is strongly typed and validated.
  * **Convenient methods:** Pydantic models provide helpful utilities like `.model_dump()` and `.model_copy()` to easily work with data copies and partial updates.

---

### 3. Endpoints

#### `GET /get-item/{item_id}`

* **Purpose:** Retrieve an item by its ID.
* **Parameters:**

  * `item_id` (path): The unique identifier for the item.
* **Behavior:**
  Attempts to get the item from the inventory dictionary.
  If not found, raises a `404` HTTPException.

---

#### `GET /get-by-name`

* **Purpose:** Retrieve an item by its name.
* **Parameters:**

  * `name` (query, required): Name of the item to search for (case-insensitive).
  * `test` (query, optional): A demonstration optional parameter.
* **Behavior:**
  Iterates over inventory items to find a name match.
  If no name is provided or no item matches, returns appropriate HTTP errors.

---

#### `GET /get-item-combined/{item_id}`

* **Purpose:** Retrieve an item by ID, optionally filtered by name.
* **Parameters:**

  * `item_id` (path)
  * `test` (query, optional)
  * `name` (query, optional)
* **Behavior:**
  Fetches the item by ID, then optionally verifies if the name matches (case-insensitive).
  Raises errors if not found or if the name does not match.

---

#### `POST /create-item/{item_id}`

* **Purpose:** Create a new inventory item.
* **Parameters:**

  * `item_id` (path)
  * `item` (request body): Complete `Item` model with required fields.
* **Behavior:**
  Checks if the item ID already exists. If yes, returns a `400` error.
  Otherwise, adds the new item to inventory.

---

#### `PUT /update-item/{item_id}`

* **Purpose:** Partially update an existing item.
* **Parameters:**

  * `item_id` (path)
  * `item` (request body): `UpdateItem` model with optional fields.
* **Behavior:**
  Retrieves the existing item from inventory.
  Uses `.model_dump(exclude_unset=True)` to extract only fields sent by the client (ignore unset fields).
  Creates a **copy of the existing model updated with new fields** via `.model_copy(update=...)`.
  Saves updated item back to inventory.
  Returns the updated item.

---

### 4. Key FastAPI and Pydantic Concepts Used

* **Path and Query Parameters:**
  Using `Path()` and `Query()` lets us declare and validate HTTP path and query parameters clearly, adding descriptions used in auto-generated API docs.

* **Error Handling with `HTTPException`:**
  When items are not found or input is invalid, the API raises meaningful HTTP errors with status codes and messages, improving API client experience.

* **Pydantic’s `model_dump` and `model_copy`:**

  * `.model_dump(exclude_unset=True)` extracts only fields explicitly set by the user in a partial update request, avoiding overwriting existing fields with `None`.
  * `.model_copy(update=...)` returns a **new Pydantic model instance** with updated fields, preserving immutability and making it easier to reason about state changes.

---

### 5. Why This Design is Clean and Maintainable

* **Separation of Concerns:**
  Models handle data validation; endpoints handle request logic and error handling.

* **Type Safety:**
  Using Pydantic ensures input/output data conforms to expected types, reducing runtime errors.

* **Self-Documenting:**
  FastAPI’s use of type hints and descriptions means documentation is auto-generated and always in sync with the code.

* **Partial Updates with Immutable Models:**
  The update logic is concise and safe, avoiding manual field checks and mutations.

* **Clear Error Responses:**
  Explicit exceptions improve client debugging and API usability.

---

### Summary

This FastAPI app demonstrates best practices for building a simple inventory API using Pydantic for data modeling, clear request validation, and structured error handling. It balances beginner-friendly readability with intermediate-level robustness and maintainability. The code can easily scale to add more endpoints, authentication, or persistence layers.

