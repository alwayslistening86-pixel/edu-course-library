# S03_Simultaneous_Equations_and_Inequalities - Test: Simultaneous equations and inequalities

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Solve simultaneously y = x + 3 and y = x^2 - 2x - 1. [5 marks]
2. Show that the line y = 2x + 5 does not meet the curve y = x^2 + 4x + 7. [3 marks]
3. Find the set of values of x for which 3(x - 2) < x + 4 and x^2 - 7x + 10 > 0. [5 marks]
4. Solve x^2 < 4x, giving your answer in set notation. [3 marks]
5. Sketch and describe (with inequalities) the region satisfying y ≥ x^2 - 4 and y ≤ 2 - x. Find the x-coordinates of the points where the boundaries meet. [4 marks]
6. Which correctly give the solution of x^2 - 9 > 0? Choose every correct option.
   A. `x < -3 or x > 3`
   B. `{x : x < -3} ∪ {x : x > 3}`
   C. `-3 > x > 3`
   D. `{x : x < -3} ∩ {x : x > 3}`

## Answer key (for the tutor only)
1. [5] M1 x^2 - 2x - 1 = x + 3; A1 x^2 - 3x - 4 = 0; M1 (x - 4)(x + 1) = 0; A1 x = 4, x = -1; A1 (4, 7) and (-1, 2).
2. [3] M1 x^2 + 4x + 7 = 2x + 5, so x^2 + 2x + 2 = 0; M1 discriminant 4 - 8 = -4; A1 negative, so no real roots, so no intersection.
3. [5] B1 first gives x < 5; M1 critical values 2 and 5; A1 second gives x < 2 or x > 5; M1 combines; A1 x < 2.
4. [3] M1 x^2 - 4x < 0, x(x - 4) < 0; A1 critical values 0 and 4; A1 {x : 0 < x < 4}.
5. [4] B1 parabola boundary solid, vertex (0, -4); B1 line solid through (0, 2) and (2, 0); M1 x^2 - 4 = 2 - x, x^2 + x - 6 = 0; A1 x = -3 and x = 2 (the region is above the parabola and below the line, between these).
6. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Simultaneous_Equations_and_Inequalities` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 21 marks in all; a pass needs at least 13 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Polynomials_Rational_Expressions_Partial_Fractions.
