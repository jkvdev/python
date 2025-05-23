# 01 – Variables, Data Types & Naming Conventions

## 🐍 What Is Python?

Python is a general-purpose, high-level programming language known for fast development. It's commonly used in web development, scripting, automation, and machine learning.

---

## 🧠 Naming Conventions

- Use `snake_case` for variable and function names.
- Avoid `camelCase` — it's not considered Pythonic.

```python
# ✅ Correct
user_name = "Alice"

# ❌ Not preferred
userName = "Bob"
```

---

## 🔢 Numbers

Python has two primary numeric types:

- **Integers** (`int`): whole numbers like `1`, `0`, `-99`
- **Floats** (`float`): decimal numbers like `3.14`, `0.0`

### Arithmetic Operations

```python
x = 5
y = 2

print(x + y)   # 7
print(x - y)   # 3
print(x * y)   # 10
print(x / y)   # 2.5 (always float)
print(x // y)  # 2 (floor division)
print(x % y)   # 1 (modulo)
print(x ** y)  # 25 (exponent)
```

---

## 🟢 Booleans

Booleans represent truth values:

```python
is_valid = True
is_admin = False
```

- `0`, `None`, empty strings/lists are considered `False`
- Everything else is `True`

---

## 🔤 Strings

Strings are sequences of characters enclosed in either single or double quotes.

```python
greeting = "Hello"
```

### Common String Methods

```python
greeting.lower()        # "hello"
greeting.upper()        # "HELLO"
greeting.capitalize()   # "Hello"
greeting.count("l")     # 2
```

### String Operations

```python
# Concatenation
"Hello" + " World"   # "Hello World"

# Repetition
"A" * 3              # "AAA"
```