# S06_Matrices_and_Transformations - Test: Matrices and transformations

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A = [[1, 2], [3, -1]], B = [[0, 1], [2, 4]]. Find AB and BA and comment. [3 marks]
2. Describe fully the transformation with matrix [[1, 0], [3, 1]]. [2 marks]
3. Find the matrix for a rotation of 90° about the x-axis in three dimensions and the image of (1, 2, 3). [3 marks]
4. M = [[4, 1], [2, 3]]. Find the invariant lines of M that pass through the origin. [5 marks]
5. Find the invariant points of the transformation [[2, -1], [1, 0]]. [3 marks]

## Answer key (for the tutor only)
1. [3] B1 AB = [[4, 9], [-2, -1]]; B1 BA = [[3, -1], [14, 0]]; B1 AB ≠ BA, so multiplication is not commutative.
2. [2] B1 shear; B1 y-axis invariant, (1, 0) maps to (1, 3).
3. [3] B1 [[1, 0, 0], [0, 0, -1], [0, 1, 0]]; M1 multiplies; A1 (1, -3, 2).
4. [5] M1 image of (x, mx): (4x + mx, 2x + 3mx); M1 2 + 3m = m(4 + m); A1 m^2 + m - 2 = 0; A1 m = 1: y = x; A1 m = -2: y = -2x.
5. [3] M1 2x - y = x and x = y; A1 same equation y = x; A1 every point on y = x is invariant (a line of invariant points).

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Matrices_and_Transformations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Determinants_and_Inverses.
