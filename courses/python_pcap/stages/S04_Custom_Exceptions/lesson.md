# S04_Custom_Exceptions - Lesson: Custom exceptions

## Goal
The learner defines custom exception classes, places them sensibly in the hierarchy, and catches them by class or by parent.

## Syllabus items taught here
- 2.2a - Defining custom exceptions
- 2.2b - Fitting custom exceptions into the existing hierarchy

## How to teach this
Ask why a bank program might want an InsufficientFundsError rather than a plain ValueError. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 2.2a Defining custom exceptions
A custom exception is a class that inherits from `Exception` (or one of its subclasses). The body can be just `pass`; the inherited constructor stores the arguments in `args`. You can also add your own `__init__`; call `super().__init__(...)` so `args` and `str()` still work.
```python
class OutOfStockError(Exception):
    pass
class PaymentError(Exception):
    def __init__(self, amount, reason):
        super().__init__(f"{reason}: {amount}")
        self.amount = amount
try:
    raise PaymentError(50, "card declined")
except PaymentError as e:
    print(e, "|", e.amount, "|", e.args)
```
Output:
```
card declined: 50 | 50 | ('card declined: 50',)
```

#### 2.2b Fitting custom exceptions into the existing hierarchy
Choose the parent class so that callers can catch at the right level. A family of your own errors usually shares one base class, which itself derives from `Exception` or a fitting built-in such as `ValueError` or `LookupError`. Catching the base then catches the whole family, and catching a built-in parent also catches your subclass.
```python
class ShopError(Exception): pass
class OutOfStock(ShopError): pass
class BadCode(ShopError, ValueError): pass
for exc in (OutOfStock("pens"), BadCode("X1")):
    try:
        raise exc
    except ShopError as e:
        print("ShopError family:", type(e).__name__, isinstance(e, ValueError))
try:
    raise BadCode("Z9")
except ValueError:
    print("also catchable as ValueError")
```
Output:
```
ShopError family: OutOfStock False
ShopError family: BadCode True
also catchable as ValueError
```

## Explicitly not here
Classes in general are S07 to S09; here only enough class syntax is used to define an exception.
