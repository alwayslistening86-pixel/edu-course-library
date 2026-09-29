# S03_Handling_Exceptions_in_Depth - Practice: Handling exceptions in depth

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
try:
    x = int('1')
except ValueError:
    print('except')
else:
    print('else')
finally:
    print('finally')
```
2. What does this print? (If it raises an error, name it.)
```python
try:
    raise IndexError('bad index', 7)
except LookupError as e:
    print(type(e).__name__, e.args)
```
3. What does this print? (If it raises an error, name it.)
```python
def f():
    try:
        return 'try'
    finally:
        print('finally runs first')
print(f())
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
else
finally
```
2. Actual result (from running it):
```
IndexError ('bad index', 7)
```
3. Actual result (from running it):
```
finally runs first
try
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
