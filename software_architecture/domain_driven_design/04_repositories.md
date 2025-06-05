# 📦 04. Repository

In Domain-Driven Design, a **Repository** is a mechanism for **retrieving and storing aggregates**. It acts like a **collection**, but hides the details of the underlying data store.

Repositories help keep your **domain layer clean and persistence-agnostic**. Instead of worrying about SQL, ORM, or files, your domain logic just calls methods like `save(order)` or `get_by_id(order_id)`.

## ✅ Key Traits

- Acts like an in-memory collection for aggregates
- Provides methods to **add**, **retrieve**, and optionally **remove** aggregates
- Hides infrastructure and database details
- Focuses on **aggregate roots** only

---

## 🧠 Python Example: Repository Interface + In-Memory Implementation

```python
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Dict, Optional

# Reusing Order aggregate from before
class OrderRepository(ABC):
    """Abstract base class for an Order repository."""

    @abstractmethod
    def save(self, order: Order) -> None:
        """Store or update the given order."""
        pass

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Optional[Order]:
        """Retrieve an order by its ID, or None if not found."""
        pass
```

---

### 🧪 In-Memory Implementation

```python
class InMemoryOrderRepository(OrderRepository):
    """Simple in-memory implementation of the OrderRepository."""

    def __init__(self) -> None:
        self._storage: Dict[UUID, Order] = {}

    def save(self, order: Order) -> None:
        self._storage[order.id] = order

    def get_by_id(self, order_id: UUID) -> Optional[Order]:
        return self._storage.get(order_id)
```

---

## 🔄 Example Usage

```python
repo = InMemoryOrderRepository()

# Create and save a new order
order = Order(order_id=uuid4())

# Repositories hide storage logic — this could be a DB, but we don’t care here
repo.save(order)

# Retrieve the order
retrieved_order = repo.get_by_id(order.id)
print(retrieved_order == order)  # True
```

---

## 📌 Summary

* Repositories **abstract away persistence** so your domain logic stays clean
* They only operate on **aggregate roots**, never internal entities directly
* Use them to **store and retrieve aggregates** without polluting your domain with database logic

➡️ Next: [05_services.md](./05_services.md)

