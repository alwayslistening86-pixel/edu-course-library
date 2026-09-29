# S18_Further_Integration - Test: Further integration

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the area enclosed between y = x^2 and y = 2x + 3. [5 marks]
2. Use the substitution u = 1 + sin x to find ∫ (0 to π/2) cos x (1 + sin x)^3 dx. [4 marks]
3. Find ∫ (1 to e) x^2 ln x dx, giving an exact answer. [5 marks]
4. Express (3x + 5)/((x + 1)(x + 3)) in partial fractions and hence find ∫ (0 to 1) (3x + 5)/((x + 1)(x + 3)) dx in the form ln k. [6 marks]
5. Find ∫ 4x/(x^2 + 5) dx. [2 marks]

## Answer key (for the tutor only)
1. [5] M1 x^2 = 2x + 3; A1 x = -1 and 3; M1 ∫ (2x + 3 - x^2) dx; A1 correct integration; A1 32/3.
2. [4] M1 du = cos x dx; M1 limits 1 to 2; A1 [u^4/4]; A1 15/4.
3. [5] M1 u = ln x, dv/dx = x^2; A1 (x^3/3) ln x - ∫x^2/3 dx; A1 (x^3/3) ln x - x^3/9; M1 limits; A1 1/9 + 2 e^(3)/9.
4. [6] M1 A(x + 3) + B(x + 1); A1 A = 1; A1 B = 2; M1 ln|x + 1| + 2 ln|x + 3|; M1 limits; A1 ln(32/9).
5. [2] M1 recognises f'(x)/f(x) form; A1 2 ln(x^2 + 5) + c.

## Grading
Apply `rubric.json`'s `stage_rubrics.S18_Further_Integration` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 22 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S19_Differential_Equations.
