
# 08 – Defining Functions

Functions are reusable blocks of code designed to perform a specific task.

---

## 🔹 Defining Functions

Use the `def` keyword followed by the function name in snake_case, parentheses, and a colon.

```python
def greet():
    print("Hello, world!")
````

---

## 🔹 Function Arguments

Functions can accept parameters:

```python
def add(a, b):
    return a + b

result = add(3, 4)  # 7
```

---

## 🔹 Variable Number of Arguments

* `*args`: captures extra positional arguments as a tuple.
* `**kwargs`: captures extra keyword arguments as a dictionary.

```python
def func(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

func(1, 2, name="Alice", age=30)
# Positional args: (1, 2)
# Keyword args: {'name': 'Alice', 'age': 30}
```

---

## 🔹 Unpacking Arguments

If you have a list or tuple and want to pass elements as separate arguments, use `*`:

```python
def multiply(a, b):
    return a * b

pair = (3, 5)
multiply(*pair)  # 15
```

For dictionaries, use `**` to unpack:

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

info = {'name': 'Alice', 'age': 30}
greet(**info)
```

---

## 🔹 Scope and the `global` Keyword

* Variables defined inside functions have **local scope**.
* To modify a global variable inside a function, use the `global` keyword.

```python
x = 10

def change_x():
    global x
    x = 5

change_x()
print(x)  # 5
```

---

## ✅ Summary

* Functions are defined using `def`.
* Use `*args` and `**kwargs` for flexible argument lists.
* Use `*` and `**` to unpack iterables and dictionaries when calling functions.
* Understand scope rules to manage variables inside/outside functions.

