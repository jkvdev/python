# 02 – Control Flow: If, Elif, Else & Boolean Logic

## 🧭 What Is Control Flow?

Control flow allows your program to make decisions and execute specific blocks of code depending on conditions. In Python, this is handled with `if`, `elif`, and `else` statements.

## 🧱 Basic Structure

```python
if condition:
    # block of code
elif another_condition:
    # another block of code
else:
    # fallback block
```

**Example:**

```python
age = 18

if age >= 21:
    print("You can drink.")
elif age >= 18:
    print("You can vote.")
else:
    print("You're too young.")
```

## 🔗 Boolean Operators

Python provides several logical operators to build complex conditions:

| Operator | Description        | Example             |
|----------|--------------------|---------------------|
| `and`    | All must be True   | `x > 5 and y < 10`  |
| `or`     | At least one True  | `x > 5 or y < 10`   |
| `not`    | Negates condition  | `not x == 10`       |

**Order of Precedence:**

1. `not`
2. `and`
3. `or`

**Example:**

```python
is_admin = True
is_logged_in = False

if is_admin and not is_logged_in:
    print("Admin must log in.")
```

## 🧪 Comparison Operators

| Symbol | Meaning                  |
|--------|---------------------------|
| `==`   | Equal to                  |
| `!=`   | Not equal to              |
| `>`    | Greater than              |
| `<`    | Less than                 |
| `>=`   | Greater than or equal to  |
| `<=`   | Less than or equal to     |

**Example:**

```python
x = 10
y = 20

if x != y:
    print("Values are different")
```

## 🔍 Using `in` Keyword

You can check if a value exists in a list, string, or other iterable.

```python
name = "Valentin"

if "tin" in name:
    print("Substring found")
```

## ✅ Best Practices

- Always use consistent indentation (4 spaces per level).
- Use `elif` instead of multiple `if`s to keep logic efficient.
- Keep conditions readable; avoid nesting too deeply.

## 🧠 Summary

- `if`, `elif`, and `else` control which code runs.
- Use boolean logic (`and`, `or`, `not`) to combine conditions.
- Use comparison operators and the `in` keyword to evaluate values.
