# S04_Custom_Exceptions - Test: Custom exceptions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
class AppError(Exception): pass
class DbError(AppError): pass
try:
    raise DbError('down')
except AppError as e:
    print('AppError caught:', e)
```
2. What does this print? (If it raises an error, name it.)
```python
class E(Exception):
    def __init__(self, code):
        super().__init__('code ' + str(code))
        self.code = code
try:
    raise E(404)
except E as e:
    print(e, e.code, e.args)
```
3. What does this print? (If it raises an error, name it.)
```python
class A(Exception): pass
class B(A): pass
try:
    raise B
except A:
    print('A')
except B:
    print('B')
```
4. Given `class MissingItem(KeyError): pass`, which handlers catch `raise MissingItem('x')`? Choose every correct option.
   A. except KeyError
   B. except LookupError
   C. except ValueError
   D. except Exception
5. What does this print? (If it raises an error, name it.)
```python
class Weird(Exception):
    def __init__(self):
        self.note = 'no super call'
w = Weird()
print(w.args, w.note)
```
6. Design a small exception family for a library system: a base LibraryError and two specific errors. Show one handler that catches either specific error through the base.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
AppError caught: down
```
2. Actual result (from running it):
```
code 404 404 ('code 404',)
```
3. Actual result (from running it):
```
A
```
4. Correct: A, B, D (exactly these options, no others)
5. Actual result (from running it):
```
() no super call
```
6. The tutor runs or reads the learner's answer and checks: A base class deriving from Exception, two subclasses, and an except on the base that catches both.

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Custom_Exceptions` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Characters_and_String_Operations.
