# S11_Exceptions - Test: Built-in exceptions and handling them

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which inherit (directly or indirectly) from Exception? Choose every correct option.
   A. `ValueError`
   B. `KeyboardInterrupt`
   C. `ZeroDivisionError`
   D. `SystemExit`
   E. `KeyError`
2. Which are parents of KeyError? Choose every correct option.
   A. `LookupError`
   B. `ArithmeticError`
   C. `Exception`
   D. `IndexError`
3. What does this print? (If it raises an error, name the exception.)
```python
try:
    print(1)
    print(2 / 0)
    print(3)
except ZeroDivisionError:
    print('Z')
print(4)
```
4. What does this print? (If it raises an error, name the exception.)
```python
try:
    'a' + 1
except ValueError:
    print('V')
except TypeError:
    print('T')
except Exception:
    print('E')
```
5. What does this print? (If it raises an error, name the exception.)
```python
try:
    [][0]
except LookupError:
    print('lookup')
except IndexError:
    print('index')
```
6. What does this print? (If it raises an error, name the exception.)
```python
def a():
    b()
    print('a done')
def b():
    raise ValueError('bad')
try:
    a()
except ValueError as e:
    print('handled:', e)
```
7. What does this print? (If it raises an error, name the exception.)
```python
for v in ['3', 'x', '0']:
    try:
        print(10 // int(v))
    except (ValueError, ZeroDivisionError) as e:
        print(type(e).__name__)
```
8. Write a function `safe_div(a, b)` that returns a / b, returns None if b is zero, and lets any other error propagate to the caller. Show it with safe_div(6, 3), safe_div(1, 0) and a caller that catches the TypeError from safe_div('6', 3).

## Answer key (for the tutor only)
1. Correct: A, C, E (exactly these options, no others)
2. Correct: A, C (exactly these options, no others)
3. Output (from running it):
```
1
Z
4
```
4. Output (from running it):
```
T
```
5. Output (from running it):
```
lookup
```
6. Output (from running it):
```
handled: bad
```
7. Output (from running it):
```
3
ValueError
ZeroDivisionError
```
8. The tutor runs the learner's code and checks: Catches only ZeroDivisionError; returns 2.0 and None; the TypeError propagates and is caught by the caller.

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Exceptions` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
