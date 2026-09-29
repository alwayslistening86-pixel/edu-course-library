# S04_Console_Input_and_Output - Test: Console input and output

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
print(1, 2, 3, sep=", ", end=".\n")
```
2. What does this print? (If it raises an error, name the exception.)
```python
print("A", end="")
print("B", end="")
print()
print("C")
```
3. What does this print? (If it raises an error, name the exception.)
```python
x = print("hi")
print(x)
```
4. input() always returns a value of which type? Choose every correct option.
   A. `int`
   B. `str`
   C. whatever the user typed
   D. `float`
5. What does this print? (If it raises an error, name the exception.)
```python
a = "2"
b = "3"
print(a + b, int(a) + int(b), a * 3)
```
6. Write a program that asks for a price (which may have pence) and a quantity (whole number), then prints `Total: ` followed by price times quantity.

## Answer key (for the tutor only)
1. Output (from running it):
```
1, 2, 3.
```
2. Output (from running it):
```
AB
C
```
3. Output (from running it):
```
hi
None
```
4. Correct: B (exactly these options, no others)
5. Output (from running it):
```
23 5 222
```
6. The tutor runs the learner's code and checks: float() on the price, int() on the quantity, correct label; for inputs 2.5 and 4 it prints Total: 10.0

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Console_Input_and_Output` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Conditional_Statements.
