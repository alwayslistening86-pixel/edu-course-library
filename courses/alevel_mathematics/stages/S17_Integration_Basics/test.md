# S17_Integration_Basics - Test: Integration: the basics and areas

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A curve has gradient function dy/dx = 3x^2 - 4/x^2 and passes through (2, 5). Find its equation. [4 marks]
2. Find the area enclosed between y = 4x - x^2 and the x-axis. [4 marks]
3. Find the total area between y = x^3 - 4x and the x-axis for -2 ≤ x ≤ 2. [5 marks]
4. Evaluate ∫ (1 to 2) (x^2 + 1)^2/x^2 dx, giving an exact answer. [4 marks]
5. Which are correct? Choose every correct option.
   A. `∫x^(-1/2) dx = 2x^(1/2) + c`
   B. `∫ (0 to 1) x^2 dx = 1/3`
   C. `∫ 5 dx = 5x + c`
   D. `∫x^(-1) dx = x^0/0 + c`

## Answer key (for the tutor only)
1. [4] M1 integrates; A1 y = x^3 + 4/x + c; M1 5 = 8 + 2 + c; A1 y = x^3 + 4/x - 5.
2. [4] M1 roots 0 and 4; M1 integrates 2x^2 - x^3/3; A1 substitutes limits; A1 32/3.
3. [5] M1 roots -2, 0, 2; M1 integrates separately; A1 ∫ (-2 to 0) = 4; A1 ∫ (0 to 2) = -4; A1 total area 8.
4. [4] M1 expands and divides: x^2 + 2 + x^(-2); M1 integrates; A1 [x^3/3 + 2x - 1/x]; A1 29/6.
5. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S17_Integration_Basics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S18_Further_Integration.
