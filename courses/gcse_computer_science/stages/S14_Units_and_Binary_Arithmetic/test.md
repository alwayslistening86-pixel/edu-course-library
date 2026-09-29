# S14_Units_and_Binary_Arithmetic - Test: Units of information and binary arithmetic

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Which is larger: 4 megabytes, or 3,900 kilobytes? Show your working. [2 marks]
2. Add the following three 8-bit binary numbers: 00010010, 00001001, 00000110. [3 marks]
3. An 8-bit register holds 01000110. State the result, and its decimal value, of shifting it left by 1 place. [2 marks]
4. Explain what a binary overflow is and why it happens. [2 marks]
5. Shifting an 8-bit binary number 3 places to the left (with no overflow) has what effect on its decimal value? Choose every correct option.
   A. multiplies it by 8
   B. divides it by 8
   C. adds 3 to it
   D. multiplies it by 3

## Answer key (for the tutor only)
1. [2] M1 converts to the same unit, e.g. 4 MB = 4,000 KB; A1 4 megabytes (4,000 KB) is larger than 3,900 KB.
2. [3] M1 correct column addition process shown; M1 carries handled correctly; A1 00100001.
3. [2] B1 10001100; B1 decimal 140 (= 70 x 2).
4. [2] B1 occurs when the true result of a calculation needs more bits than are available to store it; B1 the extra (most significant) bit(s) are lost, giving an incorrect stored result.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Units_and_Binary_Arithmetic` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Character_Encoding.
