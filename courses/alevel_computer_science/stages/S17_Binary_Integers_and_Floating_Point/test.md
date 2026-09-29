# S17_Binary_Integers_and_Floating_Point - Test: Unsigned and signed (two's complement) binary integers, and floating point

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
print(bin(58))
print(bin(256 - 58))
```
2. Explain why two's complement is used to represent negative integers, rather than simply using the leftmost bit as a plain sign flag on an unsigned magnitude. [3 marks]
3. Convert the 8-bit two's complement pattern 11110101 back to its signed decimal value, showing your working. [3 marks]
4. Explain what normalisation means for a floating-point number, and why range and precision trade off against each other for a fixed total number of bits. [3 marks]
5. Explain the difference between underflow and overflow in floating-point representation. [2 marks]
6. In 8-bit two's complement, which value does 10000000 represent? Choose every correct option.
   A. `-128`
   B. `128`
   C. `-1`
   D. `0`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
0b111010
0b11000110
```
2. [3] B1 with two's complement, ordinary binary addition gives the correct result for a mix of positive and negative numbers, with no special-case subtraction logic needed; B1 a simple sign-and-magnitude scheme needs separate addition/subtraction rules depending on the signs involved; B1 two's complement also has only one representation of zero, unlike sign-and-magnitude (which has +0 and -0).
3. [3] M1 leftmost bit's place value is negative: -128; M1 remaining bits 1110101 = 64+32+16+4+1=117; A1 total: -128+117 = -11.
4. [3] B1 normalisation adjusts the mantissa and exponent to a standard form (e.g. mantissa starting 0.1...) so every value has one unique representation; B1 more exponent bits allow a wider range of magnitudes to be represented; B1 for a fixed total bit budget, giving more bits to the exponent (range) leaves fewer for the mantissa (precision), and vice versa.
5. [2] B1 underflow: a number's magnitude is too small to be represented, and it rounds to zero; B1 overflow: a number's magnitude is too large for the available exponent range to represent at all.
6. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S17_Binary_Integers_and_Floating_Point` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S18_Character_Coding_and_Error_Checking.
