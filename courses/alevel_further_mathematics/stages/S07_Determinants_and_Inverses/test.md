# S07_Determinants_and_Inverses - Test: Determinants and inverses

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. M = [[2, 0, 1], [1, 3, -1], [0, 1, 2]]. Find det M and M^(-1), showing the method. [6 marks]
2. Hence solve 2x + z = 3, x + 3y - z = 10, y + 2z = 4. [3 marks]
3. A triangle of area 6 is transformed by [[3, -1], [2, k]]. The image has area 42 and its orientation is preserved. Find k. [3 marks]
4. Given det A = 4 and det B = -3 (both 3 x 3), find det(AB), det(A^(-1)) and det(2A). [3 marks]
5. Prove that (AB)^(-1) = B^(-1)A^(-1) for non-singular square matrices A and B. [2 marks]

## Answer key (for the tutor only)
1. [6] M1 expands the determinant; A1 det M = 15; M1 cofactors; M1 transposes; A1 correct adjugate; A1 M^(-1) = (1/15)[[7, 1, -3], [-2, 4, 3], [1, -2, 6]].
2. [3] M1 x = M^(-1)b; A1 two correct; A1 (x, y, z) = (19/15, 46/15, 7/15).
3. [3] M1 det = 3k + 2; M1 3k + 2 = 7; A1 k = 5/3.
4. [3] B1 -12; B1 1/4; B1 2^3 x 4 = 32.
5. [2] M1 (AB)(B^(-1)A^(-1)) = A(BB^(-1))A^(-1); A1 = AA^(-1) = I, so B^(-1)A^(-1) is the inverse of AB.

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Determinants_and_Inverses` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Systems_of_Equations_and_Planes.
