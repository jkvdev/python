# 🧩 Dependency Injection (DI)

**Dependency Injection (DI)** is a way to give an object the things it needs to work — instead of having it create them by itself.

This is especially useful in **clean code**, **clean architecture**, and **Domain-Driven Design (DDD)**. With DI, we keep things **modular**, **easier to test**, and **easier to maintain**.

---

## 🎯 Why Use DI?

- ✅ Encourages **loose coupling**
- 🧪 Simplifies **unit testing** by allowing easy mocking
- ♻️ Promotes **clarity** and **reusability**
- 🔁 Enables **Inversion of Control (IoC)**

> **Inversion of Control** means: *don't build your own dependencies — let someone else give them to you*.

---

## 🧱 Common Types of Injection

| Type                  | Description                              |
|-----------------------|------------------------------------------|
| Constructor Injection | Pass dependencies when creating objects  |
| Service Locator       | Look up dependencies from a registry     |
| IoC Container         | Let a framework or tool handle injection |

We'll cover these in:

- [`01_constructor_injection.md`](./01_constructor_injection.md)
- [`02_service_locator.md`](./02_service_locator.md)
- [`03_IoC_container.md`](./03_IoC_container.md)

---

## ⚙️ Simple Example (Python)

```python
class EmailService:
    def send_email(self, recipient: str, message: str) -> None:
        print(f"📧 Email sent to {recipient}: {message}")

class Notifier:
    def __init__(self, email_service: EmailService) -> None:
        self.email_service = email_service

    def send_alert(self, user_email: str) -> None:
        self.email_service.send_email(user_email, "You have a new alert!")

# Dependency Injection in action
email_service = EmailService()
notifier = Notifier(email_service)

notifier.send_alert("user@example.com")
```

### 👎 Without DI

```python
class Notifier:
    def __init__(self) -> None:
        self.email_service = EmailService()  # tightly coupled
```

* Hard to test
* Can’t replace `EmailService` with a mock or alternative

### ✅ With DI

* `Notifier` doesn’t care **how** the service is built — it just uses it.

---

## 🚀 DI in FastAPI (The Clean Way)

FastAPI supports DI out of the box using the `Depends` function:

```python
from fastapi import Depends, FastAPI

app = FastAPI()

# Our service class
class EmailService:
    def send_email(self, recipient: str, message: str) -> str:
        return f"📨 Sent to {recipient}: {message}"

# Dependency provider function
def get_email_service() -> EmailService:
    return EmailService()

@app.get("/notify")
def notify_user(
    email_service: EmailService = Depends(get_email_service),
) -> dict:
    result = email_service.send_email("user@example.com", "Hello from FastAPI!")
    return {"message": result}
```

### 💡 What’s happening:

* `EmailService` is created **outside** the route handler
* FastAPI automatically **injects** it via `Depends`
* Easy to **mock** in tests or **swap out** later

---

## 🧪 Bonus: Easier Testing with DI

```python
from unittest.mock import MagicMock

mock_service = MagicMock()
notifier = Notifier(email_service=mock_service)

notifier.send_alert("test@example.com")

mock_service.send_email.assert_called_once_with("test@example.com", "You have a new alert!")
```

---

## 📌 Summary

* Dependency Injection helps you write **cleaner**, **more flexible**, and **more testable** code
* It’s a core part of **modern Python backends**, especially with **FastAPI**
* Start with **constructor injection** and adopt more advanced patterns as your app grows

👉 Continue learning:

* [Constructor Injection](./01_constructor_injection.md)
* [Service Locator](./02_service_locator.md)
* [IoC Containers](./03_IoC_container.md)
