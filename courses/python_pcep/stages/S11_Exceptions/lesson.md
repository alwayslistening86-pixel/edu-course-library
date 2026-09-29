# S11_Exceptions - Lesson: Built-in exceptions and handling them

## Goal
The learner names the built-in exceptions on the syllabus, places them in the hierarchy, and writes and traces try-except code that handles errors at the right level.

## Syllabus items taught here
- 4.3a - BaseException at the root of the hierarchy
- 4.3b - Exception
- 4.3c - SystemExit
- 4.3d - KeyboardInterrupt
- 4.3e - Abstract (grouping) exceptions
- 4.3f - ArithmeticError and its children
- 4.3g - LookupError and its children
- 4.3h - IndexError
- 4.3i - KeyError
- 4.3j - TypeError
- 4.3k - ValueError
- 4.4a - try-except, and catching Exception
- 4.4b - Ordering except branches
- 4.4c - Exceptions propagating through function calls
- 4.4d - Deciding where an exception should be handled

## How to teach this
Ask which error each of these raises: `int('x')`, `[1][5]`, `{}['k']`, `1/0`, `'a' + 1`. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 4.3a BaseException at the root of the hierarchy
Every exception is a class in one tree. **BaseException** is the root. Handling BaseException catches absolutely everything, including attempts to exit, which is why it's almost never the right thing to catch.

#### 4.3b Exception
**Exception** sits directly under BaseException and is the parent of all ordinary runtime errors. `except Exception:` is the broad, normal catch-all.

#### 4.3c SystemExit
**SystemExit** is raised by `sys.exit()` (and `exit()`). It inherits from BaseException, **not** Exception, so `except Exception` deliberately doesn't stop a program from exiting.

#### 4.3d KeyboardInterrupt
**KeyboardInterrupt** is raised when the user presses Ctrl+C. It also inherits directly from BaseException, so `except Exception` doesn't swallow it either.
```python
print(issubclass(SystemExit, Exception), issubclass(KeyboardInterrupt, Exception))
print(issubclass(SystemExit, BaseException), issubclass(ValueError, Exception))
```
Output:
```
False False
True True
```

#### 4.3e Abstract (grouping) exceptions
Some exceptions are **abstract**: grouping classes that are rarely raised themselves but let you catch a family at once. On this syllabus they are ArithmeticError and LookupError (Exception is also a grouping class).

#### 4.3f ArithmeticError and its children
**ArithmeticError** groups calculation errors. Its main child is **ZeroDivisionError** (division, floor division or modulo by zero); OverflowError is another.
```python
try:
    print(10 // 0)
except ArithmeticError as e:
    print(type(e).__name__, "caught as ArithmeticError")
```
Output:
```
ZeroDivisionError caught as ArithmeticError
```

#### 4.3g LookupError and its children
**LookupError** groups failed lookups in a collection: its two children on this syllabus are IndexError and KeyError.

#### 4.3h IndexError
**IndexError**: a sequence index out of range, e.g. `[1, 2][5]` or `"ab"[9]`. (Slicing never raises it.)

#### 4.3i KeyError
**KeyError**: a missing dictionary key, e.g. `{"a": 1}["b"]`.
```python
for bad in ([1, 2], {"a": 1}):
    try:
        bad[5] if isinstance(bad, list) else bad["b"]
    except LookupError as e:
        print(type(e).__name__, "is a LookupError")
```
Output:
```
IndexError is a LookupError
KeyError is a LookupError
```

#### 4.3j TypeError
**TypeError**: an operation on the wrong type, e.g. `"a" + 1`, calling a non-function, assigning to a tuple item, or passing the wrong number of arguments.

#### 4.3k ValueError
**ValueError**: the right type but an unacceptable value, e.g. `int("abc")`, `[1, 2].index(9)` or `"x".index("y")`.
```python
for code in ('"a" + 1', 'int("abc")', '[1, 2].index(9)'):
    try:
        eval(code)
    except Exception as e:
        print(code, "->", type(e).__name__)
```
Output:
```
"a" + 1 -> TypeError
int("abc") -> ValueError
[1, 2].index(9) -> ValueError
```

#### 4.4a try-except, and catching Exception
`try:` holds code that might fail; `except SomeError:` runs if that error happens; `except SomeError as e:` also binds the exception object. If nothing fails, the except blocks are skipped. A bare `except:` catches everything, including SystemExit, and is discouraged; `except Exception:` is the usual broad form. Several types can share a branch: `except (ValueError, TypeError):`.
```python
def to_int(s):
    try:
        return int(s)
    except ValueError:
        return None
print(to_int("12"), to_int("twelve"))
```
Output:
```
12 None
```

#### 4.4b Ordering except branches
Except branches are checked **top to bottom**, and the first match wins. A parent class listed first catches its children too, so **specific exceptions must come before general ones**, or the specific branch can never run.
```python
try:
    [][1]
except IndexError:
    print("IndexError branch")
except LookupError:
    print("LookupError branch")
try:
    [][1]
except LookupError:
    print("LookupError first: the IndexError branch below is now unreachable")
except IndexError:
    print("never")
```
Output:
```
IndexError branch
LookupError first: the IndexError branch below is now unreachable
```

#### 4.4c Exceptions propagating through function calls
An exception not handled inside a function **propagates**: the function stops, and the exception passes up to the caller, and on up, until some `try` handles it. If nothing handles it, the program stops with a traceback.
```python
def inner():
    return 1 / 0
def middle():
    r = inner()
    print("never printed")
try:
    middle()
except ZeroDivisionError:
    print("handled in the caller")
```
Output:
```
handled in the caller
```

#### 4.4d Deciding where an exception should be handled
**Where to handle** an exception is a design choice. Handle it where you can actually do something sensible (retry, use a default, report it to the user); otherwise let it propagate to a level that can. A function can also handle part of a problem and re-raise with a bare `raise` so its caller still knows it happened.
```python
def parse(s):
    try:
        return int(s)
    except ValueError:
        print("parse: logging bad input", repr(s))
        raise
try:
    parse("x")
except ValueError:
    print("caller: using default 0")
```
Output:
```
parse: logging bad input 'x'
caller: using default 0
```

## Explicitly not here
Writing your own exception classes, finally and else on try belong to PCAP.
