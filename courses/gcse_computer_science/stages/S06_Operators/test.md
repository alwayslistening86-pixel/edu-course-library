# S06_Operators - Test: Arithmetic, relational and Boolean operators

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
x = 3
y = 7
print(x < y and x != 3)
```
2. A number n is 29. State the result of: (a) n // 5; (b) n % 5. [2 marks]
3. Explain the difference between real division and integer division, with an example of each applied to 22 and 6. [3 marks]
4. Write a Boolean expression that is True only when a mark is at least 40 and at most 100. [2 marks]
5. Which expression evaluates to True when x = 4? Choose every correct option.
   A. `NOT (x == 5)`
   B. `x < 4`
   C. `x == 5 AND x == 4`
   D. `NOT (x > 0)`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
False
```
2. [2] B1 (a) 5; B1 (b) 4.
3. [3] B1 real division gives a decimal/fractional result; B1 22 / 6 = 3.6666... (accept 3.67); B1 integer division discards the remainder and gives only the whole quotient: 22 // 6 = 3.
4. [2] B1 correct use of AND combining two relational tests; B1 e.g. mark >= 40 AND mark <= 100.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Operators` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 9 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Data_Structures.
