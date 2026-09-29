# S18_Second_Order_and_Coupled_Differential_Equations - Test: Second-order and coupled differential equations

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Solve y'' + 2y' + 5y = 10, given y = 0 and dy/dx = 0 when x = 0. [7 marks]
2. A particle moves with x'' = -9x, x = 2 and x' = 0 at t = 0. Find x at time t, the period, and the maximum speed. [4 marks]
3. Find a particular integral of y'' - y' - 2y = 4e^(2x). [4 marks]
4. Two populations satisfy dx/dt = x + y, dy/dt = 4x + y. Show that d^2x/dt^2 - 2dx/dt - 3x = 0, and find x and y given x = 3, y = 2 at t = 0. [7 marks]

## Answer key (for the tutor only)
1. [7] M1 auxiliary m^2 + 2m + 5 = 0; A1 m = -1 ± 2i; A1 CF e^(-x)(A cos 2x + B sin 2x); B1 PI y = 2; M1 y(0) = 0 gives A = -2; M1 y'(0) = 0 gives -A + 2B = 0; A1 y = 2 - e^(-x)(2cos 2x + sin 2x).
2. [4] B1 x = 2cos 3t; B1 period 2π/3; M1 max speed aω; A1 6.
3. [4] M1 e^(2x) is in the CF (roots 2 and -1); M1 tries λxe^(2x); A1 3λ = 4; A1 PI (4/3)xe^(2x).
4. [7] M1 differentiates: x'' = x' + y'; M1 substitutes y' = 4x + y and y = x' - x; A1 x'' - 2x' - 3x = 0; M1 x = Ae^(3t) + Be^(-t); M1 y = x' - x = 2Ae^(3t) - 2Be^(-t); A1 A + B = 3, 2A - 2B = 2; A1 A = 2, B = 1: x = 2e^(3t) + e^(-t), y = 4e^(3t) - 2e^(-t).

## Grading
Apply `rubric.json`'s `stage_rubrics.S18_Second_Order_and_Coupled_Differential_Equations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 22 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S19_Combinatorics_and_Discrete_Random_Variables.
