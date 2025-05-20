# 10 – Lambda Functions

Lambda functions are anonymous, small, single-expression functions defined with the `lambda` keyword.

---

## 🔹 Syntax

```python
lambda arguments: expression
````

Example:

```python
add_five = lambda x: x + 5
print(add_five(10))  # 15
```

---

## 🔹 Use Cases

* Short functions used as arguments to higher-order functions.
* Avoids defining full `def` functions for simple operations.

Example with `map`:

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]
```

---

## 🔹 Multiple Arguments

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12
```

---

## ✅ Summary

* Lambdas are concise, one-expression anonymous functions.
* Useful for quick, small functions passed as arguments.
* Avoid complex logic inside lambdas for readability.

