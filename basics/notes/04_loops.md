# 04 – Loops in Python

Python provides two main types of loops: `for` and `while`. These allow you to iterate over sequences or repeat code while a condition is true.

---

## 🔁 For Loops

Used for iterating over sequences like lists, strings, ranges, etc.

### 🧪 Basic Usage

```python
for i in range(5):
    print(i)
```

### 🔍 Range Function

The `range()` function is commonly used in for loops. It can take:

- `range(stop)` – starts from 0
- `range(start, stop)`
- `range(start, stop, step)`

```python
range(5)          # 0 to 4
range(2, 5)       # 2 to 4
range(10, 2, -2)  # 10, 8, 6, 4
```

### 🧠 Looping Through a List

```python
x = [10, 20, 30]
for item in x:
    print(item)
```

### 🧮 Using `range(len(x))`

Useful when you need indices:

```python
for i in range(len(x)):
    print(i, x[i])
```

### 🔢 Enumerate

Use `enumerate()` to access both index and value:

```python
for i, element in enumerate(x):
    print(i, element)
```

---

## 🔄 While Loops

Repeats code while a condition is true.

### 🧪 Example

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

⚠️ **Important**: Ensure the loop eventually breaks, or it may run forever!

---

## 🚪 Loop Control Statements

- `break` → exit the loop early
- `continue` → skip the current iteration and continue with the next
- `pass` → do nothing (placeholder)

```python
for i in range(5):
    if i == 2:
        continue  # skips 2
    if i == 4:
        break     # stops at 4
    print(i)
```

---

## ✅ Summary

| Feature        | `for` Loop                      | `while` Loop                  |
|----------------|----------------------------------|-------------------------------|
| Use Case       | Known number of iterations       | Unknown, condition-based      |
| Sequence-based | ✅                                | ❌ (needs condition manually) |
| Easy to read   | ✅                                | ✅                            |

Choose `for` when iterating through items.  
Use `while` when looping based on a condition.
