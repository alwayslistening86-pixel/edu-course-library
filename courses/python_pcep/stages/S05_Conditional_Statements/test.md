# S05_Conditional_Statements - Test: Making decisions with if, elif and else

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
x = 7
if x > 5:
    print('A')
elif x > 3:
    print('B')
else:
    print('C')
```
2. What does this print? (If it raises an error, name the exception.)
```python
x = 7
if x > 5:
    print('A')
if x > 3:
    print('B')
else:
    print('C')
```
3. What does this print? (If it raises an error, name the exception.)
```python
a, b = 3, 8
if a > b:
    print('a')
else:
    if b > 5:
        print('b big')
    else:
        print('b small')
```
4. What does this print? (If it raises an error, name the exception.)
```python
s = ''
if s:
    print('non-empty')
else:
    print('empty')
```
5. Which are true of an if-elif-else chain? Choose every correct option.
   A. More than one branch can run
   B. At most one branch runs
   C. else must come last
   D. You may have several else branches
6. Write code that prints `leap` or `not leap` for a year `y`: divisible by 4, except centuries, unless divisible by 400.

## Answer key (for the tutor only)
1. Output (from running it):
```
A
```
2. Output (from running it):
```
A
B
```
3. Output (from running it):
```
b big
```
4. Output (from running it):
```
empty
```
5. Correct: B, C (exactly these options, no others)
6. The tutor runs the learner's code and checks: Correct for 2024 (leap), 1900 (not leap), 2000 (leap), 2023 (not leap).

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Conditional_Statements` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Loops.
