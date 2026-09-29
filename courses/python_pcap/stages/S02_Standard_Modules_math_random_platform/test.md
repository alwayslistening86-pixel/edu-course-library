# S02_Standard_Modules_math_random_platform - Test: The math, random and platform modules

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
import math
print(math.ceil(4.0001), math.floor(4.9999), math.trunc(-0.5))
```
2. What does this print? (If it raises an error, name it.)
```python
import math
print(math.factorial(4), math.sqrt(2.25), type(math.sqrt(9)).__name__)
```
3. What does this print? (If it raises an error, name it.)
```python
import math
try:
    math.sqrt(-1)
except ValueError:
    print('ValueError')
```
4. What does this print? (If it raises an error, name it.)
```python
import random
random.seed(10)
a = random.sample(range(100), 5)
random.seed(10)
b = random.sample(range(100), 5)
print(a == b, len(set(a)))
```
5. Which calls can never return the same element twice in one call? Choose every correct option.
   A. `random.sample(seq, 3)`
   B. `random.choice(seq)`
   C. `[random.choice(seq) for _ in range(3)]`
6. Which are true of the platform module? Choose every correct option.
   A. system() returns a name such as 'Linux' or 'Windows'
   B. `python_implementation() may return 'CPython'`
   C. python_version_tuple() returns a tuple of ints
   D. `processor() can return an empty string`
7. What does this print? (If it raises an error, name it.)
```python
from math import *
print(floor(2.5) + ceil(2.5))
```

## Answer key (for the tutor only)
1. Actual result (from running it):
```
5 4 0
```
2. Actual result (from running it):
```
24 1.5 float
```
3. Actual result (from running it):
```
ValueError
```
4. Actual result (from running it):
```
True 5
```
5. Correct: A (exactly these options, no others)
6. Correct: A, B, D (exactly these options, no others)
7. Actual result (from running it):
```
5
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Standard_Modules_math_random_platform` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Handling_Exceptions_in_Depth.
