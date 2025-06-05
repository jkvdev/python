# 🌀 Ports in Hexagonal Architecture

In Hexagonal Architecture, **ports are abstract interfaces** that define how the application communicates with the outside world — and how the outside world communicates with the application.

You can think of ports as the **contract** or **boundary** between your core logic and everything else.

---

## 🛂 Two Types of Ports

| Port Type      | Direction                 | Role                                                |
|----------------|---------------------------|-----------------------------------------------------|
| **Input Port** | Inbound (e.g., user input) | Defines *what your application can do*              |
| **Output Port**| Outbound (e.g., DB call)   | Defines *what your application depends on*          |

These are just interfaces — we’ll implement them with adapters later.

> 💡 **Note:** In some literature, you'll see "driving" (input) and "driven" (output) ports. These terms describe which side initiates the interaction.

---

## 🎯 Why Use Ports?

- ✅ Decouple core logic from frameworks (like FastAPI or SQLAlchemy)
- ✅ Make business rules easy to test
- ✅ Make your app flexible to change (swap DBs, APIs, etc.)

---

## 🔧 Input Port — Example

Let’s say you want your app to support creating pets. You’d define an **input port** for that use case:

```python
# ports/input_ports.py
from typing import Protocol
from domain.models import Pet

class CreatePetPort(Protocol):
    def create_pet(self, name: str, age: int) -> Pet:
        ...
```

This port defines what your app *offers* — but not *how* it does it.

---

## 🔌 Output Port — Example

Your app might need to save a `Pet` somewhere — to a DB, an API, or even memory. That’s where an **output port** comes in:

```python
# ports/output_ports.py
from typing import Protocol
from domain.models import Pet

class PetRepositoryPort(Protocol):
    def save(self, pet: Pet) -> None:
        ...
```

This tells your core logic what it *expects* — but not *how it gets it*.

---

## 🧠 Connecting the Dots

When we implement the use case later (e.g., in an `Application Service`), we’ll inject both ports:

```python
class CreatePetService(CreatePetPort):
    def __init__(self, repo: PetRepositoryPort):
        self.repo = repo

    def create_pet(self, name: str, age: int) -> Pet:
        pet = Pet(name=name, age=age)
        self.repo.save(pet)
        return pet
```

Note: We don’t import FastAPI or SQLAlchemy here — **just business logic and contracts**.

---

## 🧪 Testing with Fake Adapters

Because these are just interfaces, you can test your service without a DB:

```python
class InMemoryPetRepository(PetRepositoryPort):
    def __init__(self):
        self.pets = []

    def save(self, pet: Pet) -> None:
        self.pets.append(pet)
```

---

## 🧩 Recap

* **Ports** define the shape of communication in and out of your application.
* **Input ports** are used by primary adapters (like FastAPI controllers).
* **Output ports** are implemented by secondary adapters (like DBs or APIs).
* They enable clean separation of concerns — and clean code.

In the next section, we’ll look at **adapters**, which are the concrete implementations of these ports.

➡️ [Next: `02_adapters.md`](./02_adapters.md)
