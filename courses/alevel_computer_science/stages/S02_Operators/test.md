# S02_Operators - Test: Arithmetic, relational and Boolean operators

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
print(2 ** 8)
print(int(7.9))
print(round(2.5))
```
2. A number n is 3.7. State the result of: (a) truncating n; (b) rounding n to the nearest whole number. [2 marks]
3. Explain the difference between XOR and OR, with a worked truth-table example covering all four input combinations. [4 marks]
4. Which expression evaluates to True? Choose every correct option.
   A. `NOT (5 > 10)`
   B. `5 == 6`
   C. `3 != 3`
   D. False AND True

## Answer key (for the tutor only)
1. Actual result (from running it):
```
256
7
2
```
2. [2] B1 (a) 3; B1 (b) 4.
3. [4] B1 OR is True if at least one input is True (including when both are True); B1 XOR is True only if exactly one input is True, and False when both are True; B1/B1 correct four-row comparison, e.g. (F,F)->OR F/XOR F; (F,T)->OR T/XOR T; (T,F)->OR T/XOR T; (T,T)->OR T/XOR F (award both marks only if all four rows for both operators are correct).
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Operators` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Constants_Strings_Random_Exceptions.
