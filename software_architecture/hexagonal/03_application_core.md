# 🧠 The Application Core

The **application core** is the beating heart of Hexagonal Architecture.

This is where your **business rules live** — your use cases, orchestrations, and domain logic — all **independent** of frameworks, databases, or delivery mechanisms.

If you stripped away FastAPI, SQLAlchemy, or external services, the application core should still work.

---

## 🧱 What Belongs in the Core?

| Layer                | Purpose                                                  |
|----------------------|----------------------------------------------------------|
| **Entities / Models**| Represent core domain concepts (e.g., `Pet`, `User`)     |
| **Use Cases**        | Application logic / orchestration (e.g., `CreatePet`)    |
| **Ports**            | Define communication boundaries                          |

> 🧼 Rule of Thumb: **No FastAPI, no SQLAlchemy, no HTTP logic** — only clean business logic and interfaces.

---

## 🧩 Example: The `Pet` Use Case

Let’s implement a **use case** that creates a new pet, using only ports and models.

---

### 1. Domain Model

```python
# domain/models.py
from pydantic import BaseModel

class Pet(BaseModel):
    name: str
    age: int
```

---

### 2. Input + Output Ports (Contracts)

```python
# application/ports/input_ports.py
from typing import Protocol
from domain.models import Pet

class CreatePetPort(Protocol):
    def create_pet(self, name: str, age: int) -> Pet:
        ...
```

```python
# application/ports/output_ports.py
from typing import Protocol
from domain.models import Pet

class PetRepositoryPort(Protocol):
    def save(self, pet: Pet) -> None:
        ...
```

---

### 3. The Application Service (Use Case Implementation)

```python
# application/use_cases/create_pet.py
from application.ports.input_ports import CreatePetPort
from application.ports.output_ports import PetRepositoryPort
from domain.models import Pet

class CreatePetService(CreatePetPort):
    def __init__(self, repo: PetRepositoryPort):
        self.repo = repo

    def create_pet(self, name: str, age: int) -> Pet:
        pet = Pet(name=name, age=age)
        self.repo.save(pet)
        return pet
```

✅ This class is:

* Decoupled from frameworks
* Easily testable
* Replaceable (you can swap repo, even mock it)

---

## 🧪 Bonus: Testing the Core

You can test the core without touching any real DB:

```python
# tests/test_create_pet.py
from application.use_cases.create_pet import CreatePetService
from domain.models import Pet
from application.ports.output_ports import PetRepositoryPort

class InMemoryPetRepo(PetRepositoryPort):
    def __init__(self):
        self.saved = []

    def save(self, pet: Pet):
        self.saved.append(pet)

def test_create_pet():
    repo = InMemoryPetRepo()
    service = CreatePetService(repo)
    pet = service.create_pet(name="Milo", age=2)

    assert pet.name == "Milo"
    assert pet.age == 2
    assert repo.saved == [pet]
```

---

## 🚫 What Does *Not* Belong in the Core?

* ❌ FastAPI-specific code (e.g., `Depends`, `APIRouter`)
* ❌ ORM models (e.g., SQLAlchemy `Base`)
* ❌ Frameworks or external service SDKs

These belong in **adapters** or **infrastructure** layers.

---

## 🧩 Summary

* The **application core** is where your clean, framework-free logic lives.
* It contains:

  * ✅ Domain models
  * ✅ Use case orchestration (application services)
  * ✅ Input/output ports (contracts)
* It depends on **nothing** — and everything else depends on it.

➡️ [Next: `04_integrating_frameworks.md`](./04_integrating_frameworks.md)

