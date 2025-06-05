# 🆔 01. Entity

In Domain-Driven Design, an **Entity** is an object defined by its **identity**, not just its attributes. It has a unique identifier and maintains continuity throughout its lifecycle, even as its data changes.

## ✅ Key Traits

- Has a unique identifier (e.g. UUID)
- Can change state over time
- Equality is based on identity
- Encapsulates domain behavior, not just data

---

## 🧠 Python Example: A `User` Entity

```python
from uuid import UUID, uuid4


class User:
    """Represents a system user with a unique identity and domain behavior."""

    def __init__(self, user_id: UUID, username: str, email: str) -> None:
        self._id = user_id
        self._username = username
        self._email = email

    @property
    def id(self) -> UUID:
        """Return the unique ID of the user."""
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    def update_email(self, new_email: str) -> None:
        """Update the user's email with basic validation."""
        if "@" not in new_email:
            raise ValueError("Invalid email address.")
        self._email = new_email

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id

    def __repr__(self) -> str:
        return f"User(id={self._id}, username='{self._username}', email='{self._email}')"
```

---

## 🧪 Example Usage

```python
# Create two different users
user1 = User(user_id=uuid4(), username="alice", email="alice@example.com")
user2 = User(user_id=uuid4(), username="bob", email="bob@example.com")

# Print user representation
print(user1)
# Output: User(id=..., username='alice', email='alice@example.com')

# Update email (with validation)
user1.update_email("alice@newdomain.com")

# Identity check (not attribute-based)
duplicate = User(user_id=user1.id, username="alice", email="any@email.com")
print(user1 == duplicate)  # True – same ID, considered the same entity
```

---

## 📌 Summary

* Entities model **core business concepts** that have a lifecycle (e.g. `Order`, `Customer`, `Invoice`)
* Their **identity** is more important than their attributes
* They encapsulate **domain behavior** and not just data

➡️ Next: [02\_value\_objects.md](./02_value_objects.md)

```

---

Let me know when you're ready to move on to `02_value_objects.md` — I’ll prepare it with the same level of clarity and clean code.
```
