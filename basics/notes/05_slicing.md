# 05 – Slicing in Python

Slicing lets you extract a portion of a sequence such as a string, list, or tuple using a specific syntax.

---

## 🧪 Syntax

```python
sequence[start:stop:step]
```

- `start`: index to begin the slice (inclusive)
- `stop`: index to end the slice (exclusive)
- `step`: how many items to skip

---

## 📌 Examples

### Basic List Slicing

```python
x = [0, 1, 2, 3, 4, 5]
x[1:4]      # [1, 2, 3]
x[:3]       # [0, 1, 2]
x[2:]       # [2, 3, 4, 5]
```

### Skipping Elements (Step)

```python
x[::2]      # [0, 2, 4]
x[1::2]     # [1, 3, 5]
```

### Reversing a Sequence

```python
x[::-1]     # [5, 4, 3, 2, 1, 0]
```

---

## 🧵 String Slicing

```python
s = "Python"
s[0:3]      # 'Pyt'
s[::-1]     # 'nohtyP'
```

String slicing works the same way as list slicing.

---

## 💡 Advanced Tricks

### Negative Indexes

You can use negative indexes to start counting from the end.

```python
x[-1]       # Last element
x[-3:-1]    # Elements from the third-last to second-last
```

---

## ✅ Summary

| Expression     | Result              | Description                       |
|----------------|---------------------|-----------------------------------|
| `x[:]`         | Entire sequence     | Full copy                         |
| `x[:n]`        | First `n` elements  | From beginning to `n-1`           |
| `x[n:]`        | From `n` to end     | From index `n` to end             |
| `x[::2]`       | Every 2nd element   | With step of 2                    |
| `x[::-1]`      | Reversed            | Entire sequence reversed          |

Slicing is powerful for data manipulation, cleaning, and transformation. Use it often!
