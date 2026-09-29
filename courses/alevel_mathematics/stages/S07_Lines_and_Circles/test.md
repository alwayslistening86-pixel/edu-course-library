# S07_Lines_and_Circles - Test: Coordinate geometry: lines and circles

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The line L passes through (-2, 5) and is parallel to 4x - 2y = 7. Find where L meets the x-axis. [3 marks]
2. Circle C has equation x^2 + y^2 - 4x + 10y + 4 = 0. (a) Find its centre and radius. (b) Find the equation of the tangent to C at (5, -1), in the form ax + by + c = 0. [7 marks]
3. Show that the line y = x + 6 does not meet the circle x^2 + y^2 = 16. [3 marks]
4. A(0, 4), B(6, 4) and C(3, 1) lie on a circle. Find the centre and radius of the circle, and hence show that AB is a diameter. [5 marks]
5. A taxi fare F (pounds) is modelled as F = 2.4 + 1.6d for a journey of d miles. Interpret 2.4 and 1.6, and give one limitation of the model. [3 marks]

## Answer key (for the tutor only)
1. [3] B1 gradient 2; M1 y - 5 = 2(x + 2); A1 y = 0 gives x = -9/2.
2. [7] M1 completes the square; A1 centre (2, -5); A1 radius 5 (4 + 25 - 4 = 25); M1 radius gradient (-1 + 5)/(5 - 2) = 4/3; M1 tangent gradient -3/4; M1 y + 1 = -(3/4)(x - 5); A1 3x + 4y - 11 = 0.
3. [3] M1 x^2 + (x + 6)^2 = 16; A1 2x^2 + 12x + 20 = 0, i.e. x^2 + 6x + 10 = 0; A1 discriminant 36 - 40 < 0, so no intersection.
4. [5] M1 perpendicular bisector of AB is x = 3; M1 perpendicular bisector of AC: midpoint (1.5, 2.5), gradient of AC is -1, so the bisector is y = x + 1; A1 centre (3, 4); A1 radius 3; B1 the centre is the midpoint of AB, so AB is a diameter.
5. [3] B1 2.4: fixed charge in pounds before any distance; B1 1.6: cost per mile in pounds; B1 a valid limitation (e.g. ignores waiting time or traffic, fares are rounded, different night rates).

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Lines_and_Circles` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 21 marks in all; a pass needs at least 13 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Parametric_Equations.
