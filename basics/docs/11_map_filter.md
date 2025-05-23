# 11 – Mapping and Filtering

Python provides powerful built-in functions `map()` and `filter()` to process iterables efficiently.

---

## 🔹 `map()` Function

Applies a function to every item in an iterable and returns a map object (an iterator).

### Syntax:

```python
map(function, iterable)
````

### Example:

```python
nums = [1, 2, 3, 4]
result = map(lambda x: x + 2, nums)
print(list(result))  # [3, 4, 5, 6]
```

---

## 🔹 `filter()` Function

Filters items in an iterable based on a function that returns `True` or `False`.

### Syntax:

```python
filter(function, iterable)
```

### Example:

```python
nums = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [2, 4, 6]
```

---

## 🔹 Using Named Functions

```python
def triple(i):
    return i * 3

mapped = map(triple, nums)
print(list(mapped))  # [3, 6, 9, 12]
```

---

## ✅ Summary

* `map()` transforms items using a function.
* `filter()` selects items matching a condition.
* Both return iterators; convert to list to see results.
