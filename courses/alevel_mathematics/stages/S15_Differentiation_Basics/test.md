# S15_Differentiation_Basics - Test: Differentiation: principles, tangents and stationary points

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove from first principles that the derivative of 5x^2 is 10x. [4 marks]
2. The curve C has equation y = 2x^3 + 3x^2 - 12x + 4. Find the coordinates of the stationary points and determine their nature. [7 marks]
3. Find the equation of the normal to y = 8/x at the point (2, 4), in the form ax + by + c = 0. [4 marks]
4. An open box has a square base of side x cm and volume 500 cm^3. Show that its surface area is A = x^2 + 2000/x and find the minimum area. [6 marks]
5. Find the set of values of x for which f(x) = x^3 - 3x^2 - 9x + 2 is decreasing. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 (5(x + h)^2 - 5x^2)/h; A1 (10xh + 5h^2)/h; A1 10x + 5h; A1 limit as h → 0 is 10x, stated correctly.
2. [7] M1 dy/dx = 6x^2 + 6x - 12; M1 = 0 gives x^2 + x - 2 = 0; A1 x = 1, x = -2; A1 (1, -3) and (-2, 24); M1 d^2y/dx^2 = 12x + 6; A1 at x = 1 it is 18 > 0, minimum; A1 at x = -2 it is -18 < 0, maximum.
3. [4] M1 dy/dx = -8x^(-2) = -2 at x = 2; M1 normal gradient 1/2; M1 y - 4 = (x - 2)/2; A1 x - 2y + 6 = 0.
4. [6] M1 height h = 500/x^2; A1 A = x^2 + 4xh = x^2 + 2000/x; M1 dA/dx = 2x - 2000/x^2 = 0; A1 x = 10; M1 d^2A/dx^2 = 2 + 4000/x^3 > 0, so minimum; A1 A = 300 cm^2.
5. [3] M1 f'(x) = 3x^2 - 6x - 9 < 0; A1 critical values -1 and 3; A1 -1 < x < 3.

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_Differentiation_Basics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 24 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S16_Further_Differentiation.
