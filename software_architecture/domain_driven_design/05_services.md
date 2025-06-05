# 🛠️ 05. Domain Service

In Domain-Driven Design, a **Domain Service** is a stateless object that performs **domain-specific operations** that don’t naturally fit within a single entity or value object.

Use a domain service when:
- The logic spans **multiple aggregates or entities**
- The operation is **not inherently owned** by a single object
- You want to **keep entities clean and focused**

## ✅ Key Traits

- Stateless  
- Contains **pure domain logic**, not infrastructure  
- Operates on one or more **entities or value objects**  
- Part of the **domain layer**, not the application layer  

---

## 🧠 Python Example: `OrderService`

The service lives in the **domain layer**, alongside entities and value objects — not in infrastructure or application layers.

This example checks whether two orders can be merged into one (e.g., for batch processing or optimization).

```python
class OrderService:
    """Domain service for operations involving Orders."""

    @staticmethod
    def can_merge_orders(order1: Order, order2: Order) -> bool:
        """Check if two orders can be merged (same currency & not empty)."""
        if not order1.total().amount or not order2.total().amount:
            return False
        return order1.total().currency == order2.total().currency
```

---

## 🧪 Example Usage

```python
order1 = Order(order_id=uuid4())
order2 = Order(order_id=uuid4())

item = OrderItem(product_id=uuid4(), quantity=1, price=Money(20.0, "USD"))

order1.add_item(item)
order2.add_item(item)

# Check if both orders are eligible to be merged (e.g. for batch fulfillment)
can_merge = OrderService.can_merge_orders(order1, order2)
print(can_merge)  # True
```

---

## ❓ Why Not Put This in the Entity?

Because this logic:

* **Requires two entities** (`order1`, `order2`)
* Doesn’t belong *to* either one exclusively
* Violates SRP if placed inside the `Order` class

A **Domain Service** allows you to **express this logic clearly** without polluting your entities.

---

## 📌 Summary

* Domain Services handle **business rules that don’t belong to any one entity**
* They should be **stateless**, reusable, and part of the **domain layer**
* Keep your entities clean — extract cross-cutting domain logic here

➡️ You're done with the DDD core! 🎉

Here are some optional next topics if you want to go deeper:

* `domain_events.md` – capturing things that happen in the domain
* `factories.md` – encapsulating complex object creation
* `bounded_contexts.md` – defining clear boundaries in large systems

