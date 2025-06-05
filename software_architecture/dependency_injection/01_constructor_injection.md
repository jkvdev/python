# 🔧 01. Constructor Injection

**Constructor Injection** is the most common and beginner-friendly form of Dependency Injection.

It simply means you pass the dependencies into the class through its constructor (`__init__` method):

---

## 📦 Basic Structure

Instead of doing this:

```python
class Notifier:
    def __init__(self):
        self.email_service = EmailService()
```

You do this:

```python
class Notifier:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
```

Now `Notifier` doesn’t care how `EmailService` is built — it just uses it.

---

## ✅ Benefits of Constructor Injection

* Makes classes **easy to test**
* Supports the **Single Responsibility Principle**
* Encourages **explicit dependencies**
* Works great with **mocking frameworks**
* Ideal for **application services**, **use cases**, and **controllers**

---

## 💻 Full Example (Python)

```python
class EmailService:
    def send_email(self, to: str, message: str) -> None:
        print(f"📧 Email to {to}: {message}")

class Notifier:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def send_alert(self, user_email: str) -> None:
        self.email_service.send_email(user_email, "You have a new alert!")
```

Usage:

```python
email_service = EmailService()
notifier = Notifier(email_service)

notifier.send_alert("user@example.com")
```

---

## 🧪 Unit Testing with a Mock

Constructor injection makes it easy to replace real services with mocks:

```python
from unittest.mock import MagicMock

mock_email_service = MagicMock()
notifier = Notifier(mock_email_service)

notifier.send_alert("test@example.com")

mock_email_service.send_email.assert_called_once_with("test@example.com", "You have a new alert!")
```

No need to patch or dig into internals — just inject and assert. ✅

---

## 🚀 Constructor Injection in FastAPI

Even in FastAPI, constructor injection fits nicely — especially for **services** or **repositories** inside your domain/application layer.

Here’s an example that connects constructor injection with FastAPI's `Depends`:

```python
from fastapi import Depends, FastAPI

app = FastAPI()

class EmailService:
    def send_email(self, to: str, message: str) -> str:
        return f"📧 Email sent to {to}: {message}"

class Notifier:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def notify(self, user_email: str) -> str:
        return self.email_service.send_email(user_email, "Dependency injection is cool!")

# Factory function for DI
def get_notifier() -> Notifier:
    return Notifier(EmailService())

@app.get("/notify")
def notify_user(notifier: Notifier = Depends(get_notifier)):
    return {"result": notifier.notify("user@example.com")}
```

💡 You're still using constructor injection — FastAPI just helps **wire the pieces together**.

---

## 🔁 Recap

* Pass dependencies into the class constructor
* Works great in Python and is naturally compatible with FastAPI
* Keeps classes **clean**, **testable**, and **explicit**
* First and best DI technique to master

👉 Next: [02 - Service Locator](./02_service_locator.md)
