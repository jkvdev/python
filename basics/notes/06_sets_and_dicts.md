# 06 – Sets and Dictionaries

This section covers two powerful built-in data structures in Python: `sets` and `dictionaries`.

---

## 🔹 Sets

Sets are unordered collections of **unique** elements.

### ✅ Key Features

- No duplicates
- Unordered
- Fast lookups: O(1) average time
- Mutable (can add or remove elements)

---

### 🛠 Creating Sets

```python
s = set()
s = {1, 2, 3, 3}   # {1, 2, 3}
```

> `{}` by itself creates a dictionary, **not** a set!

---

### 🧪 Common Set Methods

```python
s.add(4)            # Adds 4 to the set
s.remove(2)         # Removes 2 (raises error if not found)
s.discard(2)        # Removes 2 if found, no error otherwise
s.clear()           # Empties the set
```

---

### 🔀 Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)          # {1, 2, 3, 4, 5}
a.intersection(b)   # {3}
a.difference(b)     # {1, 2}
a.symmetric_difference(b)  # {1, 2, 4, 5}
```

---

## 🔸 Dictionaries

Dictionaries are collections of key-value pairs. Also called **hash maps**.

### ✅ Key Features

- Unordered (until Python 3.7; now insertion-ordered)
- Keys must be unique and hashable
- Values can be any type

---

### 🛠 Creating Dictionaries

```python
d = {}
d = {"name": "Alice", "age": 30}
```

---

### 🧪 Accessing & Modifying

```python
d["name"]           # "Alice"
d["age"] = 31       # Update value
d["city"] = "Paris" # Add new key-value pair
```

---

### 🔄 Iterating Through a Dictionary

```python
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)
```

---

### ⚙️ Common Methods

```python
d.get("age")            # Returns value or None if not found
d.keys()                # All keys
d.values()              # All values
d.items()               # All key-value pairs
d.pop("age")            # Removes and returns the value
```

---

## 🧠 Tip: Hash Collisions

Hash collisions can occur when two keys have the same hash value. Python handles this internally using buckets, but performance can be affected in rare cases.

---

## ✅ Summary

| Structure | Mutable | Unique | Ordered | Common Use           |
|-----------|---------|--------|---------|-----------------------|
| Set       | Yes     | Yes    | No      | Membership testing, fast lookups |
| Dict      | Yes     | Keys   | Yes     | Key-value mappings    |

Sets and dictionaries are foundational tools for fast and expressive Python code.
