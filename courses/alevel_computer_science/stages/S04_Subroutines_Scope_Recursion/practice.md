# S04_Subroutines_Scope_Recursion - Practice: Subroutines, parameters and return values; scope, stack frames and recursion

## Goal
Low-stakes practice: the learner predicts or attempts each item first, then checks it (by running code, or against the model answer). Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
def f(n):
    if n == 0:
        return 1
    return n * f(n - 1)

print(f(5))
```
2. Explain why a recursive subroutine without a base case will not terminate correctly. [2 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
120
```
2. [2] B1 without a base case, every call makes a further recursive call, with no condition that ever stops the recursion; B1 this causes infinite recursion, which (in practice) exhausts the call stack and crashes with a stack-overflow-type error.

## How to run it
One item at a time. For code-output/trace items the learner commits to a prediction before running or checking anything. Offer a worked explanation only after a genuine attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
