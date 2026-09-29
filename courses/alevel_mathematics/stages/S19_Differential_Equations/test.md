# S19_Differential_Equations - Test: Differential equations

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find the general solution of dy/dx = (y + 2)/x for x > 0, giving y in terms of x. [4 marks]
2. A population P satisfies dP/dt = 0.04P and P = 2500 when t = 0. (a) Solve the equation. (b) Find when the population reaches 5000. (c) Give one limitation of the model. [6 marks]
3. Water leaks from a tank so that dh/dt = -0.5 root h (h in metres, t in hours), and h = 4 when t = 0. Find h in terms of t and the time when the tank is empty. [6 marks]

## Answer key (for the tutor only)
1. [4] M1 separates: ∫1/(y + 2) dy = ∫1/x dx; A1 ln|y + 2| = ln x + c; M1 removes logs; A1 y = Ax - 2.
2. [6] M1 separates; A1 P = 2500e^(0.04t); M1 e^(0.04t) = 2; A1 t = 17.329; B1 unlimited growth is unrealistic (resources, space); B1 a second valid comment, e.g. births and deaths are not continuous.
3. [6] M1 separates: ∫h^(-1/2) dh = -∫0.5 dt; A1 2root h = -0.5t + c; A1 c = 4; M1 root h = 2 - t/4; A1 h = (2 - t/4)^2; A1 empty at t = 8 hours.

## Grading
Apply `rubric.json`'s `stage_rubrics.S19_Differential_Equations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S20_Numerical_Methods.
