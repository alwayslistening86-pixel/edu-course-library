# S11_Subroutines_Structured_Programming - Test: Subroutines and structured programming

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
def greet(name):
    message = "Hello, " + name
    return message

print(greet("Sam"))
```
2. Explain what a parameter is and why it is useful. [2 marks]
3. Explain what a local variable is and why using local variables is good practice. [3 marks]
4. Explain what is meant by the structured approach to programming and state one advantage of it. [3 marks]
5. Which best describes a function, as opposed to a procedure? Choose every correct option.
   A. it returns a value to the code that called it
   B. it cannot take any parameters
   C. it can only be called once
   D. it must always print something to the screen

## Answer key (for the tutor only)
1. Actual result (from running it):
```
Hello, Sam
```
2. [2] B1 a value passed into a subroutine when it is called; B1 lets the same subroutine work on different data each time it is called, rather than needing a separate copy for each value.
3. [3] B1 a variable declared inside a subroutine, existing only while that subroutine runs; B1 it cannot be accessed from outside the subroutine; B1 this stops one part of the program accidentally overwriting a variable another part is relying on, making code more reliable/easier to debug.
4. [3] B1 building programs from sequence, selection and iteration, decomposed into subroutines, rather than jumping around unpredictably; B1 example structure, e.g. combining these constructs; B1 advantage: easier to read/test/debug/maintain/reuse (or easier for a team to divide the work).
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Subroutines_Structured_Programming` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Robust_Secure_Programming.
