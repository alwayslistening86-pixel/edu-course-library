# S09_Lines_and_Planes - Test: Lines and planes

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Lines L1: r = (1, 2, -1) + λ(2, -1, 1) and L2: r = (3, 0, 3) + μ(0, 1, -2). Show that L1 and L2 are skew, and find the acute angle between their directions. [6 marks]
2. Show that the line (x - 1)/2 = (y + 1)/3 = z/(-1) is parallel to the plane 2x - y + z = 9 but does not lie in it. [4 marks]
3. Find, in cartesian form, the equation of the plane through A(1, 1, 0), B(2, 0, 3) and C(0, 2, 1). [4 marks]
4. Find the coordinates of the point where the line r = (2, 1, 0) + λ(1, -1, 3) meets the plane x + 2y - z = 10. [3 marks]

## Answer key (for the tutor only)
1. [6] M1 equates x: 1 + 2λ = 3, so λ = 1; M1 y: 2 - λ = μ, so μ = 1; A1 z: 0 vs 1, not equal, so they don't meet; B1 directions not parallel, so skew; M1 cos θ = |(2, -1, 1).(0, 1, -2)|/(root6 root5) = 3/root30; A1 56.8°.
2. [4] M1 direction (2, 3, -1), normal (2, -1, 1); A1 d.n = 4 - 3 - 1 = 0, so the line is parallel to the plane; M1 tests the point (1, -1, 0): 2 + 1 + 0 = 3; A1 3 ≠ 9, so the line is not in the plane.
3. [4] M1 AB = (1, -1, 3), AC = (-1, 1, 1); M1 normal perpendicular to both, e.g. (4, 4, 0)/4 = (1, 1, 0); A1 x + y = d; A1 x + y = 2.
4. [3] M1 substitutes: (2 + λ) + 2(1 - λ) - 3λ = 10; A1 λ = -3/2; A1 (1/2, 5/2, -9/2).

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Lines_and_Planes` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Vector_Product_and_Distances.
