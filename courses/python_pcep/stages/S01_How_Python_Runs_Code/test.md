# S01_How_Python_Runs_Code - Test: How Python runs code: interpreters, keywords, indentation, comments

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which statements are true? Choose every correct option.
   A. CPython translates the whole program to machine code before running any of it
   B. A runtime error on the last line stops the earlier lines from running
   C. A syntax error anywhere in a file stops the file before any line runs
   D. print is a keyword
2. Which of these are keywords? Choose every correct option.
   A. `elif`
   B. `global`
   C. `input`
   D. `None`
   E. `len`
3. What does this print? (If it raises an error, name the exception.)
```python
x = 3
if x > 2:
    print("a")
print("b")
if x > 5:
    print("c")
    print("d")
print("e")
```
4. Which describes 'semantics'? Choose every correct option.
   A. The set of words and symbols a language allows
   B. The rules for arranging them legally
   C. What legal code actually means and does
5. What does this print? (If it raises an error, name the exception.)
```python
print("#not a comment")  # a comment
# print("x")
```
6. What happens when a file's second line is indented by one space more than its first, for no reason? Choose every correct option.
   A. It runs normally
   B. IndentationError before anything runs
   C. Only the first line runs
7. Write a two-line program with a comment explaining it, which prints `Python` and then `3`, on separate lines, using two print statements.

## Answer key (for the tutor only)
1. Correct: C (exactly these options, no others)
2. Correct: A, B, D (exactly these options, no others)
3. Output (from running it):
```
a
b
e
```
4. Correct: C (exactly these options, no others)
5. Output (from running it):
```
#not a comment
```
6. Correct: B (exactly these options, no others)
7. The tutor runs the learner's code and checks: Two print statements, correct output, a comment starting with #.

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_How_Python_Runs_Code` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Literals_Variables_and_Number_Systems.
