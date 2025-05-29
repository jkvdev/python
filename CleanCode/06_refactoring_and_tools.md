# 🏭 Refactoring and Tools

Refactoring is the process of improving code structure without changing its behavior. It helps make code cleaner, simpler, and easier to maintain.

---

## 🔍 When to Refactor?

Look out for **code smells**:
- Duplicate code
- Long functions
- Large classes
- Inconsistent naming
- Multiple responsibilities

---

## 🔁 Refactoring Example

#### Before (hard to read and reason about):

```python
def is_valid(p):
    return p != "" and len(p) > 8 and any(c.isdigit() for c in p)
```

#### After (clean and self-explanatory):

```python
def is_valid(password: str) -> bool:
    if not password:
        return False

    if len(password) <= 8:
        return False

    if not any(c.isdigit() for c in password):
        return False
    return True
```

---

## 🛠️ Tools That Help

### **Formatters**

* `black` - Automatically formats Python code.
* `autopep8` - Applies PEP 8 formatting standards.

```bash
black app/
```

---

### **Linters**

* `flake8`, `ruff` - Check code for potential issues.

```bash
ruff check .  # Fast and modern alternative to flake8
```

---

### **Type Checkers**

* `mypy` - Static type checker for Python.

```bash
mypy src/
```

---

### **Other Helpers**

* `pylint` - More opinionated linter.
* `isort` - Sorts imports consistently.
* IDE tools like PyCharm or VSCode can suggest real-time improvements.

---

> *Refactoring isn't about perfection — it's about **continuous improvement**.*

