# 🛠️ Functions and Methods

Functions are the building blocks of clean code. Keeping them small and purposeful improves both readability and maintainability.

---

### 📌 1. Functions Should Be Small

Each function should do **one thing only**, and do it well.

#### Bad:

```python
def process_data(data):
    # validate
    if not data:
        return None

    # transform
    cleaned = [d.strip().lower() for d in data]

    # store
    save_to_db(cleaned)
```

#### Good:

```python
def validate_data(data):
    return bool(data)

def clean_data(data):
    return [d.strip().lower() for d in data]

def save_data(data):
    save_to_db(data)

def process_data(data):
    if not validate_data(data):
        return None

    cleaned = clean_data(data)
    save_data(cleaned)
```

---

### 📉 2. Fewer Arguments Is Better

Prefer 0-2 arguments. More than 3 usually indicates the need for refactoring or grouping into a data structure.

```python
# Prefer
def create_user(name, email): ...

# Avoid
def create_user(name, email, age, country, preferences, metadata): ...
```

---

### 🧪 3. Use Descriptive Names

Name functions after what they do.

```python
# Bad
def d(u): ...

# Good
def delete_user(user_id): ...
```

---

### 💥 4. Avoid Side Effects

Functions should ideally return outputs without modifying external state.

```python
# Bad (modifies global)
def add_user(user):
    users.append(user)

# Better (returns new list)
def add_user(users, user):
    return users + [user]
```

---

### 🧹 5. Single Responsibility

Each function should have **a single reason to change**. Don't mix concerns like UI, database, and business logic in one place.

---

> **\*Remember**: Short, well-named functions are easier to read, reuse, and test.\*
