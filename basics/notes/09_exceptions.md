# 09 – Exceptions and Error Handling

Python uses exceptions to handle errors and unusual situations gracefully.

---

## 🔹 Raising Exceptions

You can manually raise exceptions using `raise`:

```python
raise Exception('Something went wrong!')
````

You can create custom exceptions by subclassing `Exception`.

---

## 🔹 Try, Except, Finally

Use `try` to wrap code that might throw an exception.

```python
try:
    x = 7 / 0
except Exception as e:
    print("Error:", e)
finally:
    print("This runs no matter what")
```

* `except` catches exceptions.
* `finally` always executes, whether an exception occurred or not.

---

## 🔹 Common Exception Types

* `ZeroDivisionError`
* `ValueError`
* `TypeError`
* `IndexError`

Catch specific exceptions to handle them differently:

```python
try:
    int("abc")
except ValueError:
    print("Invalid integer!")
```

---

## 🔹 Else Clause

`else` block runs if no exceptions were raised:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Divide by zero!")
else:
    print("Result is", result)
```

---

## ✅ Summary

* Use `raise` to throw exceptions.
* Handle errors with `try`, `except`, `else`, and `finally`.
* Catch specific exceptions for precise error handling.
* Always clean up resources in `finally` if needed.

