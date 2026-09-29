# S03_Handling_Exceptions_in_Depth - Test: Handling exceptions in depth

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
try:
    print('a')
    {}['k']
    print('b')
except KeyError:
    print('c')
else:
    print('d')
finally:
    print('e')
```
2. What does this print? (If it raises an error, name it.)
```python
try:
    assert 1 + 1 == 3, 'maths broke'
except AssertionError as e:
    print(e.args)
```
3. What does this print? (If it raises an error, name it.)
```python
try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError('converted')
except ValueError as e:
    print(e)
```
4. What does this print? (If it raises an error, name it.)
```python
e = ValueError('x', 'y')
print(e.args, len(e.args))
```
5. Which are subclasses of Exception? Choose every correct option.
   A. `KeyboardInterrupt`
   B. `AssertionError`
   C. `SystemExit`
   D. `FileNotFoundError`
6. What does this print? (If it raises an error, name it.)
```python
def g(n):
    try:
        return 10 // n
    except (ZeroDivisionError, TypeError) as e:
        return type(e).__name__
    finally:
        pass
print(g(5), g(0), g('a'))
```
7. When does an else block on a try statement run? Choose every correct option.
   A. `Always`
   B. Only when an exception was handled
   C. Only when the try block raised no exception
   D. Only when finally is absent
8. Write a function that opens a file name it is given and returns its first line; if the file is missing it returns None; and whatever happens, it prints 'done'.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
a
c
e
```
2. Actual result (from running it):
```
('maths broke',)
```
3. Actual result (from running it):
```
converted
```
4. Actual result (from running it):
```
('x', 'y') 2
```
5. Correct: B, D (exactly these options, no others)
6. Actual result (from running it):
```
2 ZeroDivisionError TypeError
```
7. Correct: C (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Uses try/except FileNotFoundError (or OSError)/finally; returns None on a missing file; prints done in every case.

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Handling_Exceptions_in_Depth` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Custom_Exceptions.
