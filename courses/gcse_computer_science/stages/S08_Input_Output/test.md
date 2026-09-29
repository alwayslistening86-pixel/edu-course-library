# S08_Input_Output - Test: Input and output

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why input read from the keyboard usually needs to be converted before it can be used in a calculation. [2 marks]
2. What does this print? (If it raises an error, name it.)
```python
age = 12
print("You are", age, "years old")
```
3. Write a line of pseudo-code (or Python) that reads a whole number typed by the user into a variable called total. [2 marks]

## Answer key (for the tutor only)
1. [2] B1 input from the keyboard is read as a string (text) by default; B1 it must be converted to an integer/real before arithmetic operators can be used on it correctly.
2. Actual result (from running it):
```
You are 12 years old
```
3. [2] B1 uses an input statement; B1 converts to an integer and stores it in total, e.g. total = int(input()).

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Input_Output` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 5 marks in all; a pass needs at least 3 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_String_Handling.
