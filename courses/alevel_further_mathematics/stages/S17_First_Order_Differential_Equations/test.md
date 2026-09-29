# S17_First_Order_Differential_Equations - Test: First-order differential equations

## How to run this
A real checkpoint in the style of OCR's Further Mathematics papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the general solution of x dy/dx - 3y = x^5 for x > 0. [5 marks]
2. A tank holds 100 litres of water with 5 kg of salt. Brine with 0.2 kg/litre flows in at 3 litres/min and the mixture flows out at 3 litres/min. Show that the mass of salt S satisfies dS/dt = 0.6 - 0.03S, solve it, and describe the long-term behaviour. [7 marks]
3. Verify that y = x^2 + A/x is the general solution of x dy/dx + y = 3x^2. [2 marks]

## Answer key (for the tutor only)
1. [5] M1 standard form dy/dx - 3y/x = x^4; M1 IF x^(-3); A1 d/dx(y/x^3) = x; A1 y/x^3 = x^2/2 + c; A1 y = x^5/2 + cx^3.
2. [7] M1 in: 0.2 x 3 = 0.6 kg/min; M1 out: 3S/100; A1 given equation; M1 IF e^(0.03t) (or separates); A1 S = 20 + Ae^(-0.03t); A1 S = 20 - 15e^(-0.03t); B1 S → 20 kg (concentration tends to 0.2 kg/litre).
3. [2] M1 dy/dx = 2x - A/x^2; A1 x(2x - A/x^2) + x^2 + A/x = 3x^2.

## Grading
Apply `rubric.json`'s `stage_rubrics.S17_First_Order_Differential_Equations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S18_Second_Order_and_Coupled_Differential_Equations.
