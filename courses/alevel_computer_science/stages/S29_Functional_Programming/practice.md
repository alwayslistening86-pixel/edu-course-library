# S29_Functional_Programming - Practice: Functional programming: concepts, higher-order functions and lists

## Goal
Low-stakes practice: the learner predicts or attempts each item first, then checks it (by running code, or against the model answer). Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
nums = [4, 9, 1, 6]
print(list(map(lambda x: x * 3, nums)))
print(list(filter(lambda x: x > 4, nums)))
```
2. A function add(x, y) returns x + y. Explain what partially applying add with x = 10 produces. [2 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
[12, 27, 3, 18]
[9, 6]
```
2. [2] B1 a new function expecting only the remaining argument, y; B1 that new function always adds 10 to whatever y it is given, e.g. calling it with 3 gives 13.

## How to run it
One item at a time. For code-output/trace items the learner commits to a prediction before running or checking anything. Offer a worked explanation only after a genuine attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
