# S20_Numerical_Methods - Test: Numerical methods

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. f(x) = x^3 - 3x - 5. Show that f(x) = 0 has a root α in (2, 3). Use Newton-Raphson with x1 = 2 to find α to 4 decimal places, justifying the accuracy. [6 marks]
2. Explain why Newton-Raphson fails for f(x) = x^3 - 3x - 5 with starting value x1 = 1. [2 marks]
3. Use the trapezium rule with 4 strips to estimate ∫ (0 to 1) e^(-x^2) dx to 4 decimal places. [4 marks]
4. The iteration x(n+1) = (x(n)^2 + 5)/6 is used to solve x^2 - 6x + 5 = 0. Starting from x1 = 2, find x2, x3, x4 and state which root it approaches. Explain, using g'(x), why it cannot converge to the other root. [5 marks]
5. For y = 1/x on [1, 3], does the trapezium rule over- or under-estimate the area? Give a reason. [2 marks]

## Answer key (for the tutor only)
1. [6] B1 f(2) = -3, f(3) = 13, sign change; M1 f'(x) = 3x^2 - 3; M1 x2 = 2 + 3/9; A1 x2 = 2.33333, x3 = 2.28056; A1 α = 2.2790; B1 f(2.27895) = -0.00087 < 0 and f(2.27905) = 0.00039 > 0, so α = 2.2790 to 4 d.p.
2. [2] M1 f'(1) = 3 - 3 = 0; A1 the tangent is horizontal, so it never meets the x-axis (division by zero).
3. [4] B1 h = 0.25; M1 correct y-values; M1 correct formula; A1 0.7430.
4. [5] M1 x2 = 1.5; A1 x3 = 1.2083, x4 = 1.0767; A1 approaches x = 1; M1 g'(x) = x/3; A1 |g'(5)| = 5/3 > 1, so it diverges from x = 5.
5. [2] B1 over-estimate; B1 the curve is convex (y'' = 2/x^3 > 0), so the chords lie above the curve.

## Grading
Apply `rubric.json`'s `stage_rubrics.S20_Numerical_Methods` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S21_Vectors.
