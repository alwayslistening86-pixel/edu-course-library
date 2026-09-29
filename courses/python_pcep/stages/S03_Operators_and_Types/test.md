# S03_Operators_and_Types - Test: Operators, priorities and types

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
print(9 // 2, 9 % 2, -9 // 2, 9 / 3)
```
2. What does this print? (If it raises an error, name the exception.)
```python
print(2 ** 3 ** 2 // 64, -2 ** 4)
```
3. What does this print? (If it raises an error, name the exception.)
```python
x = 5
x *= 2
x -= 3
x //= 2
print(x)
```
4. What does this print? (If it raises an error, name the exception.)
```python
print(10 & 6, 10 | 6, 10 ^ 6, 5 << 1, ~0)
```
5. What does this print? (If it raises an error, name the exception.)
```python
print(3 > 2 > 1, "" or 0 or "x", 4 and 0)
```
6. What does this print? (If it raises an error, name the exception.)
```python
print(0.1 * 3 == 0.3, int(-2.7), float('3'), str(2) * 2)
```
7. Which expressions raise an error? Choose every correct option.
   A. `"3" + 3`
   B. `"3" * 3`
   C. `int("3.5")`
   D. `float("3.5")`
8. Which operator has the highest priority? Choose every correct option.
   A. `*`
   B. `**`
   C. `and`
   D. unary -

## Answer key (for the tutor only)
1. Output (from running it):
```
4 1 -5 3.0
```
2. Output (from running it):
```
8 -16
```
3. Output (from running it):
```
3
```
4. Output (from running it):
```
2 14 12 10 -1
```
5. Output (from running it):
```
True x 0
```
6. Output (from running it):
```
False -2 3.0 22
```
7. Correct: A, C (exactly these options, no others)
8. Correct: B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Operators_and_Types` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Console_Input_and_Output.
