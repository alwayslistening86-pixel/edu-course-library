# S21_Continuous_Random_Variables - Test: Continuous random variables

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. X has p.d.f. f(x) = x/4 for 1 ≤ x ≤ 3, and 0 otherwise. Find (a) E(X), (b) Var(X), (c) the c.d.f., (d) the median. [9 marks]
2. The c.d.f. of Y is F(y) = 1 - e^(-2y) for y ≥ 0. Find the p.d.f. and P(Y > 1). [3 marks]
3. X is uniform on [0, 1]. Find the p.d.f. of Y = X^3. [4 marks]

## Answer key (for the tutor only)
1. [9] M1 ∫x^2/4 dx; A1 E(X) = 13/6; M1 E(X^2) = 5; A1 Var(X) = 11/36; M1 F(x) = ∫ (1 to x) t/4 dt; A1 F(x) = (x^2 - 1)/8 for 1 ≤ x ≤ 3 (0 below, 1 above); M1 F(m) = 1/2; A1 m^2 = 5; A1 m = root5 ≈ 2.236.
2. [3] B1 f(y) = 2e^(-2y); M1 1 - F(1); A1 e^(-2) ≈ 0.1353.
3. [4] M1 G(y) = P(X^3 ≤ y) = P(X ≤ y^(1/3)); A1 G(y) = y^(1/3), 0 ≤ y ≤ 1; M1 differentiates; A1 g(y) = (1/3)y^(-2/3).

## Grading
Apply `rubric.json`'s `stage_rubrics.S21_Continuous_Random_Variables` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S22_Linear_Combinations_Estimation_and_Tests.
