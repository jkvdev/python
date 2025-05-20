# 07 – Comprehensions

Python comprehensions are a concise way to create collections like lists, sets, and dictionaries using a single line of code.

---

## 🔹 List Comprehensions

### ✅ Syntax

```python
[expression for item in iterable if condition]
```

### 🧪 Example

```python
squares = [x**2 for x in range(5)]          # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
```

---

## 🔸 Set Comprehensions

Same as list comprehension but uses `{}`.

```python
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}
# {2, 3, 5}
```

---

## 🔸 Dictionary Comprehensions

```python
squared = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 🔸 Tuple Comprehensions?

There is **no native tuple comprehension**. If you write:

```python
x = (i for i in range(5))
```

This returns a **generator**.

You can convert it to a tuple explicitly:

```python
tuple(x)
```

---

## 🌀 Generators (Advanced Note)

Generator expressions are memory-efficient and lazy-evaluated:

```python
gen = (x**2 for x in range(1_000_000))
next(gen)  # 0
```

Generators don’t store the full list in memory and compute values on demand.

---

## ✅ Summary Table

| Type           | Syntax                     | Returns         |
|----------------|----------------------------|-----------------|
| List           | `[x for x in ...]`         | `list`          |
| Set            | `{x for x in ...}`         | `set`           |
| Dictionary     | `{k: v for k, v in ...}`   | `dict`          |
| Generator      | `(x for x in ...)`         | `generator obj` |

---

Comprehensions are elegant, fast, and a Pythonic way to write transformations and filters.
