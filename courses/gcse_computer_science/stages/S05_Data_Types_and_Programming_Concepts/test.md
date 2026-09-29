# S05_Data_Types_and_Programming_Concepts - Test: Data types and core programming concepts

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
total = 0
n = 1
while n <= 4:
    total = total + n
    n = n + 1
print(total)
```
2. Explain the difference between a variable and a constant. [2 marks]
3. Explain the difference between definite and indefinite iteration, and give a situation suited to each. [4 marks]
4. Explain why using meaningful identifier names is good practice. [2 marks]
5. Which is an example of nested selection? Choose every correct option.
   A. an IF statement inside another IF statement
   B. a FOR loop that repeats 10 times
   C. a variable declared inside a subroutine
   D. two separate IF statements one after the other

## Answer key (for the tutor only)
1. Actual result (from running it):
```
10
```
2. [2] B1 a variable's value can change while the program runs; B1 a constant's value is fixed once set and cannot change.
3. [4] B1 definite (count-controlled): repeats a known, fixed number of times; B1 e.g. printing the 12-times table (12 repeats known in advance); B1 indefinite (condition-controlled): repeats until a condition changes, number of repeats not known in advance; B1 e.g. keep asking for a password until the correct one is entered.
4. [2] B1 makes the code's purpose clear/easier to read and understand (by the programmer and others); B1 reduces the risk of confusing one variable for another, making the code easier to maintain and debug.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Data_Types_and_Programming_Concepts` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Operators.
