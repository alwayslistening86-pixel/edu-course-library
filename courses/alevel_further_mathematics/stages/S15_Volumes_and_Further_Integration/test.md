# S15_Volumes_and_Further_Integration - Test: Volumes of revolution and further integration

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The region between y = x^2 and y = 2x is rotated about the x-axis. Find the exact volume. [5 marks]
2. Find ∫ 1/root(9 - 4x^2) dx. [3 marks]
3. Evaluate ∫ (1 to 2) 1/(x^2 - 2x + 2) dx exactly. [3 marks]
4. Show that d/dx (arcosh x) = 1/root(x^2 - 1) for x > 1. [3 marks]
5. Find ∫ (x + 7)/((x - 1)(x^2 + 4)) dx. [5 marks]

## Answer key (for the tutor only)
1. [5] M1 intersections x = 0, 2; M1 π∫(4x^2 - x^4) dx; A1 π[4x^3/3 - x^5/5]; A1 64pi/15; B1 washer method justified.
2. [3] M1 rewrites as (1/2)∫1/root(9/4 - x^2) dx; M1 arcsin form; A1 (1/2) arcsin(2x/3) + c.
3. [3] M1 completes the square: (x - 1)^2 + 1; M1 arctan(x - 1); A1 π/4.
4. [3] M1 x = cosh y, dx/dy = sinh y; M1 sinh y = root(cosh^2 y - 1) (positive for y > 0); A1 result.
5. [5] M1 partial fractions A/(x - 1) + (Bx + C)/(x^2 + 4); A1 -(8x + 3)/(5(x^2 + 4)) + 8/(5(x - 1)); M1 integrates the log term; M1 integrates the quadratic part; A1 (8/5) ln|x - 1| - (4/5) ln(x^2 + 4) - (3/10) arctan(x/2) + c.

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_Volumes_and_Further_Integration` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S16_Polar_Coordinates.
