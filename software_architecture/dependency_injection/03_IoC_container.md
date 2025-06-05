# 🧱 03. IoC Container

An **IoC (Inversion of Control) Container** is a tool that manages how dependencies are created and injected into your classes — so you don’t have to do it manually.

> It’s like a smart factory that knows what your classes need and wires everything together.

---

## 🔁 Reminder: What Is Inversion of Control?

Normally, a class might create its own dependencies:

```python
self.service = EmailService()
```

With **IoC**, the class *doesn’t* create its dependencies — the container does:

```python
self.service = container.resolve(EmailService)
```

---

## 🤖 Why Use an IoC Container?

* Automatically wires dependencies (like services, configs, DB clients)
* Reduces manual boilerplate (e.g. factory functions, `Depends` overload)
* Encourages **loose coupling** and **separation of concerns**
* Great for larger projects with many components

---

## 🧪 Example Using `dependency-injector`

We’ll use the [`dependency-injector`](https://python-dependency-injector.ets-labs.org/) package — a popular IoC library in Python.

### 📦 Installation

```bash
pip install dependency-injector
```

---

### 📌 Step-by-Step Setup

#### 1. Define your services

```python
class EmailService:
    def send_email(self, to: str, message: str) -> None:
        print(f"📧 Email sent to {to}: {message}")
```

#### 2. Create your container

```python
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    email_service = providers.Factory(EmailService)
```

#### 3. Use the container to inject dependencies

```python
class Notifier:
    def __init__(self, email_service: EmailService) -> None:
        self.email_service = email_service

    def send_alert(self, user_email: str) -> None:
        self.email_service.send_email(user_email, "Sent with DI container!")
```

```python
container = Container()
notifier = Notifier(email_service=container.email_service())
notifier.send_alert("user@example.com")
```

---

## 🚀 Using with FastAPI

FastAPI supports DI natively using `Depends`, but you can plug in a container like this:

```python
from fastapi import Depends, FastAPI
from dependency_injector.wiring import inject, Provide

app = FastAPI()
container = Container()

@app.get("/notify")
@inject
def notify_user(
    notifier: Notifier = Depends(lambda: Notifier(container.email_service()))
) -> dict:
    notifier.send_alert("user@example.com")
    return {"status": "sent"}
```

💡 This still uses FastAPI’s `Depends`, but now the actual wiring is handled by the container.

---

## 🟢 Pros

* Cleaner wiring in complex applications
* Centralized configuration
* Makes testing, swapping, and scaling easier
* Supports advanced features (scoped lifetimes, config loading, etc.)

---

## 🔴 Cons

* More abstraction = slightly higher learning curve
* Might feel like overkill for small projects

---

## 🧪 Testing with IoC Containers

Because you can override providers, testing becomes flexible:

```python
mock_email_service = MagicMock()

container = Container()
container.email_service.override(providers.Factory(lambda: mock_email_service))

notifier = Notifier(container.email_service())
notifier.send_alert("test@example.com")

mock_email_service.send_email.assert_called_once()
```

---

## 🔁 Recap

* IoC Containers manage dependency wiring for you
* Use one like `dependency-injector` in large FastAPI projects
* They reduce boilerplate, improve testability, and support clean architecture

👍 That wraps up the **core of Dependency Injection** in Python!

---

✅ Done with DI basics? You can now:

* Revisit [Constructor Injection](./01_constructor_injection.md)
* Compare [Service Locator](./02_service_locator.md)
* Or explore more on [`dependency-injector`](https://python-dependency-injector.ets-labs.org/)

