# S03_Handling_Exceptions_in_Depth - Lesson: Handling exceptions in depth

## Goal
The learner writes complete try statements with except-as, grouped handlers, else and finally, raises and re-raises exceptions, uses assert, and reads an exception's args.

## Syllabus items taught here
- 2.1a - try/except: ordering branches, except-as, grouped exceptions
- 2.1b - The hierarchy of exceptions
- 2.1c - raise, re-raising, and assert
- 2.1d - Exception objects and the args property
- 2.1e - else and finally in exception handling

## How to teach this
Ask in what order the blocks of try/except/else/finally run when no error happens, and when one does. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 2.1a try/except: ordering branches, except-as, grouped exceptions
Handlers are tried top to bottom and the first matching one runs, so specific classes go before their parents. `except (A, B) as e:` groups types and binds the exception object. An unmatched exception propagates outwards.

#### 2.1b The hierarchy of exceptions
The root is `BaseException`, with children including `Exception`, `SystemExit`, `KeyboardInterrupt` and `GeneratorExit`. Under `Exception` are the everyday groups: `ArithmeticError` (ZeroDivisionError), `LookupError` (IndexError, KeyError), `OSError`, `ValueError`, `TypeError`, `AssertionError`, `NameError` and more. `ClassName.__mro__` or `issubclass` shows where a class sits.
```python
print([c.__name__ for c in ZeroDivisionError.__mro__])
print(issubclass(FileNotFoundError, OSError), issubclass(AssertionError, Exception))
```
Output:
```
['ZeroDivisionError', 'ArithmeticError', 'Exception', 'BaseException', 'object']
True True
```

#### 2.1c raise, re-raising, and assert
`raise SomeError("message")` raises a new exception; `raise SomeError` works too, since the class is instantiated for you. Inside an `except`, a bare `raise` re-raises the current exception unchanged. `assert condition, message` raises AssertionError when the condition is false, and is meant for checking assumptions while developing.
```python
def check_age(a):
    assert a >= 0, "age cannot be negative"
    return a
try:
    check_age(-1)
except AssertionError as e:
    print("AssertionError:", e)
try:
    try:
        raise ValueError("inner")
    except ValueError:
        print("logging, then re-raising")
        raise
except ValueError as e:
    print("outer caught:", e)
```
Output:
```
AssertionError: age cannot be negative
logging, then re-raising
outer caught: inner
```

#### 2.1d Exception objects and the args property
Exceptions are objects. `e.args` is a **tuple** of the arguments given when the exception was created, and `str(e)` is the message (for several arguments it looks like the tuple).
```python
try:
    raise ValueError("bad", 42)
except ValueError as e:
    print(e.args, e.args[1], str(e))
try:
    raise KeyError("k")
except KeyError as e:
    print(e.args)
```
Output:
```
('bad', 42) 42 ('bad', 42)
('k',)
```

#### 2.1e else and finally in exception handling
`else:` runs only if the try block raised **nothing**; `finally:` runs **always**: after success, after a handled error, even after a `return` in the try. Order: try, then either a matching except or else, then finally.
```python
def f(x):
    try:
        r = 10 / x
    except ZeroDivisionError:
        print("except")
        return None
    else:
        print("else")
        return r
    finally:
        print("finally")
print(f(2))
print(f(0))
```
Output:
```
else
finally
5.0
except
finally
None
```

## Explicitly not here
Defining your own exception classes is S04.
