# S12_Robust_Secure_Programming - Test: Robust and secure programming: validation, authentication, testing

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a syntax error and a logic error, with an example of each. [4 marks]
2. Explain what validation is, and why passing validation does not guarantee data is correct. [3 marks]
3. A program requires a password of at least 8 characters. Suggest and justify one normal, one boundary and one erroneous test value. [3 marks]
4. Describe what an authentication routine checks, and why it matters for a program's security. [2 marks]
5. Which of these is a boundary test value for a field that must accept whole numbers from 1 to 10 inclusive? Choose every correct option.
   A. `10`
   B. `5`
   C. `-5`
   D. `"ten"`

## Answer key (for the tutor only)
1. [4] B1 syntax error: breaks the language's grammar rules so the code cannot run/compile; B1 e.g. a missing colon after an IF statement; B1 logic error: the code runs but produces the wrong result because the algorithm itself is flawed; B1 e.g. using subtraction instead of addition when totalling a bill.
2. [3] B1 an automatic check that input data is reasonable/sensible before use; B1 e.g. a range check, presence check, type check or length check; B1 validation only checks plausibility -- data can pass validation (e.g. a valid-looking age of 25) while still being factually wrong for that particular user.
3. [3] B1 normal: a plausible longer password, e.g. 'sunshine22' (accepted, well over the minimum); B1 boundary: exactly 8 characters, e.g. 'abcd1234' (tests the exact edge of the length check); B1 erroneous: fewer than 8 characters, e.g. 'cat' (should be rejected, tests the check correctly rejects short input).
4. [2] B1 checks that a username and password (or other credential) entered match a stored, correct pair before granting access; B1 without it, anyone could access data/functions meant only for an authorised user.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Robust_Secure_Programming` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Number_Bases_and_Conversion.
