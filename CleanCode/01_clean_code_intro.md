# 🧼 Introduction to Clean Code

Clean code is code that is easy to understand and easy to change.

---

## 🧭 Principles of Clean Code

- **Readable**: Easily understood by others (and your future self).
- **Maintainable**: Can be modified without introducing bugs.
- **Well-structured**: Follows consistent design patterns.

---

## ✨ Characteristics

- Descriptive naming
- Small functions
- Clear responsibility
- Minimal dependencies
- Follows consistent formatting
- Contains meaningful comments only when necessary

> "Clean code always looks like it was written by someone who cares." - Robert C. Martin

---

## 💡 Why Clean Code Matters

1. **Collaboration**: Easier for teams to understand and work with.
2. **Debugging**: Bugs are easier to trace and fix.
3. **Scalability**: Easier to extend features without breaking others.
4. **Maintainability**: Reduces technical debt over time.

---

## 💥 Example: Clean vs Dirty Code

**Dirty Code:**

```python
def d(x): return x*9/5+32
```

**Clean Code:**

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32
```
