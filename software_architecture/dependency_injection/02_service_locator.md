# 📡 02. Service Locator

The **Service Locator** pattern is a way to centralize the creation and access of dependencies.

Instead of passing dependencies directly (like in constructor injection), you **register them** in a "locator" and ask for them when needed.

> Think of it like a shared toolbox where any class can look up the tool it needs.

---

## 🧰 Basic Structure

```python
class ServiceLocator:
    _services = {}

    @classmethod
    def register(cls, key: str, service: object) -> None:
        cls._services[key] = service

    @classmethod
    def get(cls, key: str) -> object:
        return cls._services[key]
```

Now we can register and fetch services:

```python
ServiceLocator.register("email", EmailService())
email_service = ServiceLocator.get("email")
```

---

## 📬 Example: Notifier with Service Locator

```python
class EmailService:
    def send_email(self, to: str, message: str) -> None:
        print(f"📧 Email sent to {to}: {message}")

class Notifier:
    def send_alert(self, user_email: str) -> None:
        email_service = ServiceLocator.get("email")
        email_service.send_email(user_email, "This came from the Service Locator!")
```

Usage:

```python
ServiceLocator.register("email", EmailService())

notifier = Notifier()
notifier.send_alert("user@example.com")
```

---

## 🟢 Pros

* Easy to wire things without deep constructor chains
* Central registry = fewer arguments passed around
* Useful in very large codebases

---

## 🔴 Cons

* **Hidden dependencies** — classes don’t declare what they need
* **Harder to test** — requires patching the locator or mocking globally
* **Tight coupling** to the locator — makes code less flexible

> ⚠️ In clean architecture, this is generally **discouraged** in favor of constructor injection or IoC containers.

---

## 🧪 Testing Consideration

To test classes that use a Service Locator, you'll often need to patch the service:

```python
from unittest.mock import MagicMock

mock_service = MagicMock()
ServiceLocator.register("email", mock_service)

notifier = Notifier()
notifier.send_alert("test@example.com")

mock_service.send_email.assert_called_once()
```

It works — but it’s not as clean as injecting the dependency directly.

---

## 🤔 When to Use It?

Use Service Locator if:

* You're building a **quick prototype**
* You want to **reduce constructor bloat** in a big legacy system
* You're okay with **lower transparency** for faster wiring

But avoid it when:

* You need **high testability**
* You're following **clean architecture or DDD strictly**
* You want your code to declare its **explicit dependencies**

---

## 🔁 Recap

* Service Locator is a global registry for resolving dependencies
* Convenient, but hides what's being used
* Use with caution — it trades off clarity and testability for flexibility

👉 Next: [03 - IoC Container](./03_IoC_container.md)
