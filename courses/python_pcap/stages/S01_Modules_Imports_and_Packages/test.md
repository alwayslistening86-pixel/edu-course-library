# S01_Modules_Imports_and_Packages - Test: Modules, imports and packages

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
import math
from math import pi
print(math.pi == pi, type(math).__name__)
```
2. Which statements make `sqrt` callable without a prefix? Choose every correct option.
   A. import math
   B. from math import sqrt
   C. `from math import *`
   D. import math as sqrt
3. What is `__name__` inside a module imported as `import shop.cart`? Choose every correct option.
   A. `__main__`
   B. `cart`
   C. `shop.cart`
   D. `__init__`
4. Which are true? Choose every correct option.
   A. __pycache__ holds compiled bytecode for imported modules
   B. A module's top-level code runs on every import statement
   C. sys.path is a list of directories searched in order
   D. A name starting with _ is skipped by from m import *
5. A package directory `pkg/sub/` is imported as `pkg.sub`. What must be true for a regular package? Choose every correct option.
   A. pkg/__init__.py exists
   B. pkg/sub/__init__.py exists
   C. pkg is listed in __all__
   D. sub.py exists
6. What does this print? (If it raises an error, name it.)
```python
import sys
print(isinstance(sys.path, list), 'path' in dir(sys))
```
7. Explain what goes wrong if a student names their own file random.py and then writes `import random` in another file in the same folder, and how to fix it.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
True module
```
2. Correct: B, C (exactly these options, no others)
3. Correct: C (exactly these options, no others)
4. Correct: A, C, D (exactly these options, no others)
5. Correct: A, B (exactly these options, no others)
6. Actual result (from running it):
```
True True
```
7. The tutor runs or reads the learner's answer and checks: Their file shadows the standard module because the script's directory is first on sys.path; rename the file (and delete its __pycache__ entry).

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Modules_Imports_and_Packages` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Standard_Modules_math_random_platform.
