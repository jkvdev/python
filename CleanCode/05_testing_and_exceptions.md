# 🧪 Testing and Exception Handling

Clean code includes clean tests and thoughtful exception handling. Tests should act as living documentation, and exceptions should help prevent system failure gracefully.

---

## ✅ Writing Clean Tests

### 1. Tests Should Be Clear and Specific

```python
def test_addition_should_return_correct_sum():
    result = add(2, 3)
    assert result == 5
```

Use meaningful names like `test_<function>_should_<expected_behavior>`.

---

### 2. Use AAA: Arrange, Act, Assert

```python
def test_discount_calculation():
    # Arrange
    price = 100
    discount = 0.2

    # Act
    final_price = apply_discount(price, discount)

    # Assert
    assert final_price == 80
```

---

### 3. Keep Tests Focused and Independent

Each test should check **one** behavior and not depend on the result of another test.

---

## ⚠️ Clean Exception Handling

### 1. Catch Only What You Can Handle

```python
try:
    process_payment()
except PaymentFailedError:
    log.error("Payment failed")
    notify_user()
```

Avoid generic `except Exception:` unless you're logging or re-raising.

---

### 2. Use Custom Exceptions for Specific Scenarios

```python
class InvalidProductError(Exception):
    pass

def get_product(product_id):
    if product_id not in catalog:
        raise InvalidProductError("Product not found")
```

---

### 3. Don't Swallow Exceptions Silently

```python
# Bad
try:
    update_inventory()
except:
    pass  # Nothing happens

# Good
try:
    update_inventory()
except InventoryServiceUnavailable as e:
    log.error(f"Inventory update failed: {e}")
    raise
```

---

> _Tests and exceptions are first-class citizens of clean code. Write them as if they will be read more than the actual implementation._
