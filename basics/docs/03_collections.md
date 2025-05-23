# 03 – Collections: Lists, Tuples, Dictionaries, and Sets

## 🧺 Python Collections Overview

Collections are used to store groups of related data. Python offers several built-in types:

- Lists → ordered, mutable sequences
- Tuples → ordered, immutable sequences
- Dictionaries → key-value pairs (hash maps)
- Sets → unordered, unique elements

---

## 📋 Lists

### ✅ Features

- Ordered
- Mutable (can be changed)
- Can contain mixed data types

### 🧪 Examples

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list[0])       # Access first element
print(len(my_list))     # Get length
my_list.pop()           # Removes and returns last element
```

### 🔄 Copying Lists

```python
x = [1, 2, 3]
y = x       # Reference to same memory
z = x[:]    # Creates a new copy (memory-safe)
```

---

## 📦 Tuples

### ✅ Features

- Ordered
- Immutable (cannot be changed after creation)

### 🧪 Examples

```python
my_tuple = (1, 2, 3)
print(my_tuple[1])      # Access by index
```

Useful when data should not change (e.g., coordinates, config settings).

---

## 🗺️ Dictionaries

### ✅ Features

- Key-value pairs
- Unordered (in older Python versions)
- Fast lookups

### 🧪 Examples

```python
person = {
    "name": "Alice",
    "age": 30
}
print(person["name"])        # Access by key
for key, value in person.items():
    print(key, value)
```

### 🔄 Dictionary Methods

- `.items()` → key-value pairs
- `.keys()` → keys only
- `.values()` → values only

---

## 🧩 Sets

### ✅ Features

- Unordered
- No duplicate elements
- Fast membership testing (O(1))

### 🧪 Examples

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(3 in my_set)      # True
```

### ⚠️ Note

Empty set must be created with `set()` — `{}` creates an empty dictionary.

### 🔄 Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)         # {1, 2, 3, 4, 5}
a.intersection(b)  # {3}
a.difference(b)    # {1, 2}
```

---

## ✅ Best Practices

- Use lists when you need order and mutability.
- Use tuples for fixed data you don't want changed.
- Use dictionaries when associating keys with values.
- Use sets when you need fast membership tests and uniqueness.

## 🧠 Summary

| Type        | Ordered | Mutable | Duplicates | Key-Based |
|-------------|---------|---------|------------|-----------|
| List        | ✅      | ✅      | ✅         | ❌        |
| Tuple       | ✅      | ❌      | ✅         | ❌        |
| Dictionary  | ❌/✅    | ✅      | ❌         | ✅        |
| Set         | ❌      | ✅      | ❌         | ❌        |
