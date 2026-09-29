# S06_Functions_Modulus_and_Transformations - Test: Functions, modulus and transformations

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. f(x) = (2x + 1)/(x - 3), x > 3. (a) Find f^(-1)(x) and state its domain. (b) Find the value of x for which f(x) = 3. [6 marks]
2. Solve |2x - 5| > 3. [3 marks]
3. Solve |x - 4| = |2x + 1|. [4 marks]
4. The curve y = f(x) has a maximum at (2, 6). Write down the coordinates of the maximum of (a) y = f(x + 4), (b) y = 3f(x), (c) y = f(2x) - 1. [3 marks]
5. Describe fully a sequence of two transformations that maps y = x^2 onto y = (x - 1)^2 + 4. [2 marks]
6. g(x) = x^2 - 4x, x ≥ k. State the smallest value of k for which g has an inverse, and find g^(-1)(x) for that k. [4 marks]
7. Which transformations map y = f(x) to y = f(-x) + 2? Choose every correct option.
   A. Reflection in the y-axis then translation up 2
   B. Translation up 2 then reflection in the y-axis
   C. Reflection in the x-axis then translation up 2
   D. `Translation by vector (2, 0)`

## Answer key (for the tutor only)
1. [6] M1 y(x - 3) = 2x + 1; M1 xy - 2x = 3y + 1; A1 f^(-1)(x) = (3x + 1)/(x - 2); B1 domain x > 2 (range of f); M1 2x + 1 = 3x - 9; A1 x = 10.
2. [3] M1 2x - 5 > 3 or 2x - 5 < -3; A1 x > 4; A1 x < 1 (answer x < 1 or x > 4).
3. [4] M1 squares both sides or considers two cases; A1 x^2 - 8x + 16 = 4x^2 + 4x + 1, so 3x^2 + 12x - 15 = 0; A1 x = 1; A1 x = -5.
4. [3] B1 (a) (-2, 6); B1 (b) (2, 18); B1 (c) (1, 5).
5. [2] B1 translation by vector (1, 0) (or right 1); B1 translation by vector (0, 4); or a single translation by (1, 4) for both marks.
6. [4] B1 k = 2 (the vertex, so g is one-one); M1 completes the square: y = (x - 2)^2 - 4; M1 x = 2 + root(y + 4); A1 g^(-1)(x) = 2 + root(x + 4), x ≥ -4.
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Functions_Modulus_and_Transformations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 23 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Lines_and_Circles.
