# S02_Literals_Variables_and_Number_Systems - Test: Literals, variables and number systems

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
print(0b1111, 0o20, 0x2A)
```
2. What does this print? (If it raises an error, name the exception.)
```python
print(hex(255), bin(5), oct(8))
```
3. What does this print? (If it raises an error, name the exception.)
```python
print(1.5e3, 12e-2, type(1e0))
```
4. Which are legal names that also follow PEP 8 for a variable? Choose every correct option.
   A. `max_speed`
   B. `MaxSpeed`
   C. max speed
   D. `_count`
   E. `for`
5. What does this print? (If it raises an error, name the exception.)
```python
x = 7
x = 'seven'
y = x
print(y, type(y))
```
6. Which literals are floats? Choose every correct option.
   A. `7`
   B. `7.`
   C. `.7`
   D. `7e0`
   E. `0x7`
7. Convert 0b101101 and 0x3C to decimal by hand, showing the place values, then confirm with print().

## Answer key (for the tutor only)
1. Output (from running it):
```
15 16 42
```
2. Output (from running it):
```
0xff 0b101 0o10
```
3. Output (from running it):
```
1500.0 0.12 <class 'float'>
```
4. Correct: A, D (exactly these options, no others)
5. Output (from running it):
```
seven <class 'str'>
```
6. Correct: B, C, D (exactly these options, no others)
7. The tutor runs the learner's code and checks: 45 (32+8+4+1) and 60 (3*16+12); print(0b101101, 0x3C) shows 45 60.

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Literals_Variables_and_Number_Systems` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Operators_and_Types.
