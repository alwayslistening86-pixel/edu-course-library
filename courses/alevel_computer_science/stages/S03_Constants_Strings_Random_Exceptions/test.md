# S03_Constants_Strings_Random_Exceptions - Test: Constants/variables, string handling, random numbers and exception handling

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
print(ord('A'))
print(chr(97))
print("5" + str(3))
```
2. Explain what exception handling is for, and describe what a TRY/CATCH block does. [3 marks]
3. Write (in Python or pseudo-code) a TRY/CATCH that attempts to convert user input to an integer, and prints an error message instead of crashing if it fails. [3 marks]
4. Which is the best reason to use a named constant rather than a literal value repeated through a program? Choose every correct option.
   A. a single change updates every use, and the name documents its meaning
   B. constants run faster than variables in every language
   C. a constant can change value while the program runs, a variable cannot
   D. literals cannot be used in arithmetic expressions

## Answer key (for the tutor only)
1. Actual result (from running it):
```
65
a
53
```
2. [3] B1 lets a program detect and respond to a runtime error without the whole program crashing; B1 the TRY block contains code that might raise an exception; B1 the CATCH (or EXCEPT) block runs instead if that specific exception occurs, allowing recovery (e.g. re-prompting for input).
3. [3] M1 correct TRY/attempt structure around the conversion; M1 correct CATCH/EXCEPT naming or catching the relevant error; A1 a sensible message printed in the except branch instead of the program crashing.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Constants_Strings_Random_Exceptions` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Subroutines_Scope_Recursion.
