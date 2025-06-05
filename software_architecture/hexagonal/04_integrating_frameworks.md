# 🧩 Integrating Frameworks the Right Way

Frameworks like **FastAPI**, **SQLAlchemy**, and other tools are powerful — but they **don’t belong in your application core**.

Instead, we plug them in **from the outside**, using **adapters** and **dependency injection**.

This keeps your core clean, testable, and flexible.

---

## 🛠️ Plugging in FastAPI (Primary Adapter)

Here's how to expose your `CreatePetService` via a FastAPI controller — using the **input port**:

```python
# adapters/primary/pet_api.py
from fastapi import APIRouter, Depends
from domain.models import PetRequest, Pet
from application.ports.input_ports import CreatePetPort

router = APIRouter()

@router.post("/pets", response_model=Pet)
def create_pet(
    request: PetRequest,
    use_case: CreatePetPort = Depends()
) -> Pet:
    return use_case.create_pet(name=request.name, age=request.age)
```

✅ This controller:

* Uses `Depends()` to inject the use case
* Talks only to the input port (not directly to implementation)
* Has no business logic inside

---

## 🗃️ Plugging in SQLAlchemy (Secondary Adapter)

Now let's wire up a repository that saves pets to a database using SQLAlchemy.

```python
# adapters/secondary/sqlalchemy_pet_repo.py
from domain.models import Pet
from application.ports.output_ports import PetRepositoryPort
from infrastructure.database import SessionLocal

class SqlAlchemyPetRepository(PetRepositoryPort):
    def save(self, pet: Pet) -> None:
        with SessionLocal() as session:
            session.add(pet)
            session.commit()
```

✅ This secondary adapter:

* Implements the output port
* Wraps database logic using SQLAlchemy
* Keeps SQLAlchemy out of the application core

---

## 🔄 Dependency Injection: Wiring It All Together

Here’s how to **connect your adapters to your FastAPI app**:

```python
# main.py
from fastapi import FastAPI, Depends
from adapters.primary.pet_api import router
from adapters.secondary.sqlalchemy_pet_repo import SqlAlchemyPetRepository
from application.use_cases.create_pet import CreatePetService

app = FastAPI()

# Create instances
pet_repo = SqlAlchemyPetRepository()
create_pet_use_case = CreatePetService(repo=pet_repo)

# Provide use case to FastAPI via dependency override
def get_create_pet_use_case() -> CreatePetService:
    return create_pet_use_case

# Inject router + DI
app.include_router(router, dependencies=[Depends(get_create_pet_use_case)])
```

✅ This setup:

* Creates real adapter instances
* Injects them into the use case
* Exposes the use case to the FastAPI router without any leaks into the core

---

## 🧪 Bonus: Swapping Implementations for Testing

Because you’re using **ports**, you can easily test or mock any part of the system:

```python
# Swap out repo for testing
from tests.fakes import InMemoryPetRepository

test_repo = InMemoryPetRepository()
use_case = CreatePetService(repo=test_repo)
```

This is what **hexagonal flexibility** looks like.

---

## 🚫 What Not to Do

❌ Avoid injecting FastAPI stuff (like `Depends`) into your core
❌ Don’t let SQLAlchemy models into your domain
❌ Never import a framework inside your core logic

---

## 🧩 Summary

* Plug frameworks in **from the outside**, don’t bake them into your core
* Use **primary adapters** to receive input (e.g., FastAPI controllers)
* Use **secondary adapters** to send output (e.g., DB repos)
* Wire them together using **dependency injection**
* Your application core stays clean, testable, and tech-agnostic

You now have a working hexagonal architecture using Python, FastAPI, and clean code principles ✅
