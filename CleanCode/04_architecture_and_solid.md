# 🏗️ Architecture and SOLID Principles

Clean code at the architectural level is about organizing components for clarity, scalability, and separation of concerns. The **SOLID** principles are a widely adopted foundation.

---

## 🧱 What Is Architecture in Code?

Software architecture refers to how your codebase is structured and how components interact. Clean architecture favors **layers** and **boundaries**, minimizing dependencies and coupling.

---

## 🧭 The SOLID Principles

#### 1. S – Single Responsibility Principle (SRP)
A class should have only one reason to change.

```python
# Bad
class Report:
    def calculate(self): ...
    def format(self): ...
    def save(self): ...

# Good
class ReportCalculator: ...
class ReportFormatter: ...
class ReportSaver: ...
```

---

#### 2. O – Open/Closed Principle

Software entities should be open for extension but closed for modification.

```python
# Bad
def get_area(shape):
    if shape['type'] == 'circle':
        return 3.14 * shape['radius']**2

# Good
class Shape:
    def area(self): raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * self.radius ** 2
```

---

#### 3. L – Liskov Substitution Principle

Subtypes must be substitutable for their base types without altering correctness.

```python
class Bird:
    def fly(self): ...

class Duck(Bird):
    def fly(self): ...

# If Penguin is a Bird but can't fly, LSP is violated.
```

---

#### 4. I – Interface Segregation Principle

Don't force clients to depend on methods they don’t use.

```python
# Instead of one large interface:
class Worker:
    def work(self): ...
    def eat(self): ...

# Prefer smaller, specific ones:
class Workable: def work(self): ...
class Eatable: def eat(self): ...
```

---

#### 5. D – Dependency Inversion Principle

Depend on abstractions, not on concretions.

```python
# Bad
class EmailService:
    def send(self, message): ...

class OrderProcessor:
    def __init__(self):
        self.email = EmailService()

# Good
class NotificationService:
    def send(self, message): ...

class EmailService(NotificationService): ...

class OrderProcessor:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier
```

---

> *Clean architecture isn't about frameworks — it's about decoupling and clarity.*

---

