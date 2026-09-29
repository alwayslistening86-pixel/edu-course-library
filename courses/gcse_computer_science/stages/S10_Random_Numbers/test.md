# S10_Random_Numbers - Test: Random number generation

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why random number generation might be used in a simple dice game. [2 marks]
2. What does this print? (If it raises an error, name it.)
```python
import random
random.seed(2)
for i in range(3):
    print(random.randint(1, 10))
```
3. Write a line of code that stores a random whole number from 1 to 100 inclusive in a variable called ticket. [2 marks]

## Answer key (for the tutor only)
1. [2] B1 so the game produces an unpredictable roll each time it is played; B1 e.g. random.randint(1, 6) picks a whole number from 1 to 6 inclusive to simulate a die.
2. Actual result (from running it):
```
1
2
2
```
3. [2] B1 imports/uses the random module; B1 correct call with bounds 1 and 100 inclusive, e.g. ticket = random.randint(1, 100).

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Random_Numbers` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 5 marks in all; a pass needs at least 3 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Subroutines_Structured_Programming.
