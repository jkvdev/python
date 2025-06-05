# 🧩 03. Aggregate

In Domain-Driven Design, an **Aggregate** is a cluster of related objects (usually entities and value objects) that are treated as a single unit. Each aggregate has a **root entity** (called the Aggregate Root) that enforces consistency and encapsulates all access to the rest of the objects inside.

## ✅ Key Traits

- Composed of one or more **entities** and **value objects**
- Has a single **Aggregate Root** that acts as the entry point
- External objects are only allowed to interact with the **Aggregate Root**
- Helps enforce **invariants** and maintain **consistency**

---

## 🧠 Python Example: An `Order` Aggregate

This example models an `Order` entity (aggregate root) with `OrderItem`s as inner entities and `Money` as a value object.

```python
from uuid import UUID, uuid4
from typing import List
from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative.")
        if not self.currency:
            raise ValueError("Currency must be provided.")

class OrderItem:
    """Represents an item within an order."""
    def __init__(self, product_id: UUID, quantity: int, price: Money) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self._product_id = product_id
        self._quantity = quantity
        self._price = price

    def subtotal(self) -> Money:
        return Money(
            amount=self._price.amount * self._quantity,
            currency=self._price.currency
        )

class Order:
    """Aggregate root for managing an order and its items."""
    def __init__(self, order_id: UUID) -> None:
        self._id = order_id
        self._items: List[OrderItem] = []

    @property
    def id(self) -> UUID:
        return self._id

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)

    def total(self) -> Money:
        if not self._items:
            return Money(0.0, "USD")  # No items yet — return zero total
        currency = self._items[0]._price.currency
        total_amount = sum(item.subtotal().amount for item in self._items)
        return Money(amount=total_amount, currency=currency)
```

---

## 🧪 Example Usage

```python
from uuid import uuid4

order = Order(order_id=uuid4())  # Aggregate Root

item1 = OrderItem(product_id=uuid4(), quantity=2, price=Money(25.0, "USD"))
item2 = OrderItem(product_id=uuid4(), quantity=1, price=Money(50.0, "USD"))

order.add_item(item1)
order.add_item(item2)

print(order.total())  # Money(amount=100.0, currency='USD')
```

---

## 📌 Summary

* Aggregates help keep your domain **consistent and valid**
* They group related entities and value objects into a **cohesive unit**
* Only the **aggregate root** should expose public behavior and manage access to internal parts

➡️ Next: [04_repositories.md](./04_repositories.md)

