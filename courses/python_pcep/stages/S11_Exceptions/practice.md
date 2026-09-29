# S11_Exceptions - Practice: Built-in exceptions and handling them

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
try:
    print(int('12a'))
except ValueError:
    print('bad number')
```
2. What does this print? (If it raises an error, name the exception.)
```python
try:
    x = [1, 2][3]
except LookupError as e:
    print(type(e).__name__)
```
3. What does this print? (If it raises an error, name the exception.)
```python
def f():
    return {}['k']
try:
    f()
except KeyError:
    print('caught outside f')
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
bad number
```
2. Output (from running it):
```
IndexError
```
3. Output (from running it):
```
caught outside f
```

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
