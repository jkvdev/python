# 12 – F-Strings (Formatted String Literals)

Python’s f-strings provide a concise and readable way to embed expressions inside string literals.

---

## 🔹 Basic Usage

Prefix a string with `f` or `F` and include expressions inside curly braces `{}`.

### Example:

```python
name = "Valentin"
age = 20
greeting = f"Hello, {name}. You are {age} years old."
print(greeting)  # Hello, Valentin. You are 20 years old.
````

---

## 🔹 Expressions Inside F-Strings

You can include any valid Python expression inside the braces:

```python
print(f"The sum of 8 and 9 is {8 + 9}.")  # The sum of 8 and 9 is 17.
```

---

## 🔹 Formatting Numbers

You can format numbers with format specifiers inside the braces:

```python
pi = 3.14159265
print(f"Pi rounded to 2 decimals: {pi:.2f}")  # Pi rounded to 2 decimals: 3.14
```

---

## ✅ Summary

* f-strings improve readability compared to older formatting methods (`%`, `.format()`).
* Expressions inside `{}` are evaluated at runtime.
* Useful for dynamic strings, logging, and debugging.
