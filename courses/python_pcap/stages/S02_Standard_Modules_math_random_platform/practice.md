# S02_Standard_Modules_math_random_platform - Practice: The math, random and platform modules

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
import math
print(math.floor(-3.2), math.trunc(-3.2), math.ceil(-3.2), math.hypot(5, 12))
```
2. What does this print? (If it raises an error, name it.)
```python
import random
random.seed(3)
x = random.choice([1, 2, 3])
random.seed(3)
print(x == random.choice([1, 2, 3]))
```
3. Which platform function returns a tuple? Choose every correct option.
   A. `platform()`
   B. `python_version_tuple()`
   C. `system()`
   D. `machine()`

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
-4 -3 -3 13.0
```
2. Actual result (from running it):
```
True
```
3. Correct: B (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
