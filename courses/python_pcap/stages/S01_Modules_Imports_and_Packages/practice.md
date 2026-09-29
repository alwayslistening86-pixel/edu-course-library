# S01_Modules_Imports_and_Packages - Practice: Modules, imports and packages

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
from math import floor as fl
import math as mt
print(fl(3.9), mt.ceil(3.1))
```
2. After `import os.path as op`, which names are bound? Choose every correct option.
   A. `op`
   B. `os`
   C. `path`
   D. `os.path`
3. Write a module `tools.py` with a function and a demo that runs only when the file is executed directly, not when imported.

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
3 4
```
2. Correct: A (exactly these options, no others)
3. The tutor runs or reads the learner's answer and checks: Uses `if __name__ == "__main__":` correctly around the demo.

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
