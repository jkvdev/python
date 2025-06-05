# 🧾 02. Value Object

In Domain-Driven Design, a **Value Object** is a simple object that is **defined only by its attributes**, not by any identity. It is **immutable** and **interchangeable** with another object if all its values are equal.

Value Objects are great for modeling things like currency, dates, coordinates, addresses, etc.

## ✅ Key Traits

- No unique identity
- Equality is based on **data**, not identity
- **Immutable** by design
- Typically small and simple

---

## 🧠 Python Example: A `Money` Value Object

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    """Represents a value object for monetary amounts."""
    amount: float
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative.")
        if not self.currency:
            raise ValueError("Currency must be provided.")

    def add(self, other: "Money") -> "Money":
        """Return a new Money object after adding two amounts of the same currency."""
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies.")
        return Money(amount=self.amount + other.amount, currency=self.currency)
```

---

## 🧪 Example Usage

```python
# Create two money objects
price1 = Money(amount=50.0, currency="USD")
price2 = Money(amount=50.0, currency="USD")
price3 = Money(amount=30.0, currency="EUR")

# Equality based on attributes, not identity
print(price1 == price2)  # True — same values
print(price1 == price3)  # False — different amount and currency

# Immutability check (this would raise an error)
# price1.amount = 100.0  # ❌ Frozen dataclass prevents modification

# Adding money
total = price1.add(price2)
print(total)  # Money(amount=100.0, currency='USD')
```

---

## 📌 Summary

* Value Objects are used to model **descriptive concepts** without identity
* They are **interchangeable** when their values are equal
* Always aim to make them **immutable** and self-validating
* Help keep domain models simple and clean

➡️ Next: [03_aggregates.md](./03_aggregates.md)

