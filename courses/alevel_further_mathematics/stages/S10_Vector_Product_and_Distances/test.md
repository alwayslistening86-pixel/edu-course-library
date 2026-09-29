# S10_Vector_Product_and_Distances - Test: The vector product and shortest distances

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the shortest distance between the skew lines r = (2, 1, 0) + λ(1, 0, 2) and r = (0, 3, 1) + μ(1, 1, 0). [5 marks]
2. Find the shortest distance from P(4, 0, 1) to the line r = (1, 1, 1) + λ(2, -1, 2). [4 marks]
3. Find a cartesian equation of the plane containing the lines r = (1, 0, 1) + λ(2, 1, 0) and r = (1, 0, 1) + μ(0, 1, 3). [3 marks]

## Answer key (for the tutor only)
1. [5] M1 n = (1, 0, 2) x (1, 1, 0) = (-2, 2, 1); M1 b - a = (-2, 2, 1); M1 |(b - a).n|/|n|; A1 |9|/3; A1 3.
2. [4] M1 foot F = (1 + 2λ, 1 - λ, 1 + 2λ); M1 PF.d = 0: (2λ - 3)2 - (1 - λ) + 2(2λ) = 0 gives 9λ = 7; A1 λ = 7/9; A1 distance root(41)/3.
3. [3] M1 n = (2, 1, 0) x (0, 1, 3) = (3, -6, 2); M1 uses (1, 0, 1); A1 3x - 6y + 2z = 5.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Vector_Product_and_Distances` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Roots_of_Polynomials_and_Partial_Fractions.
