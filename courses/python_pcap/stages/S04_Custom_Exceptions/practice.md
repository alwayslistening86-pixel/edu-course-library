# S04_Custom_Exceptions - Practice: Custom exceptions

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
class MyErr(Exception):
    pass
try:
    raise MyErr('boom', 1)
except Exception as e:
    print(type(e).__name__, e.args)
```
2. Define a TooColdError that is a kind of ValueError, raise it from a function when a temperature is below -50, and catch it as a ValueError.

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
MyErr ('boom', 1)
```
2. The tutor runs or reads the learner's answer and checks: class TooColdError(ValueError); raised with a message; caught by except ValueError.

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
