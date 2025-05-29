# 🌟 Naming and Formatting

Good naming and consistent formatting are foundational elements of clean code. They make code easier to read, understand, and maintain.

---

## ✅ Good Naming

Use **descriptive**, **unambiguous**, and **intent-revealing** names.

### Bad Example:

```python
a = 10
b = 20
c = a + b
```

### Good Example:

```python
number_of_users = 10
number_of_guests = 20
total_people = number_of_users + number_of_guests
```

### Function Naming:

Use verbs for functions and actions.

```python
# Bad
def data(x): ...

# Good
def process_data(x): ...
```

---

## 🧱 Consistent Formatting

Use consistent indentation, line spacing, and blank lines to improve readability.

### Indentation

- Use 4 spaces per indent level (PEP 8 default for Python).

```python
def greet(name):
    if name:
        print(f"Hello, {name}")
```

### Spacing

- Add space around operators and after commas.

```python
# Bad
x=3+4

# Good
x = 3 + 4
```

---

## 🧼 Blank Lines

Use blank lines to separate code blocks logically. This helps group related logic and improves visual flow.

```python
def connect():
    # Connection logic
    pass

def disconnect():
    # Disconnect logic
    pass
```

---

## ✨ Rule of Thumb

> _Code should read like well-written prose. If you have to explain what a name means, it likely needs to be clearer._
