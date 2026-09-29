# S16_Further_Differentiation - Test: Further differentiation

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Differentiate y = (2x - 1)^3/(x + 1)^2, simplifying your answer. [4 marks]
2. A curve has equation x^2 + 3xy - y^2 = 3. Find the gradient at (1, 1) and the equation of the tangent there. [5 marks]
3. Find the x-coordinates of the points of inflection of y = x^4 - 4x^3 + 2, and show they are points of inflection. [5 marks]
4. The volume of a cube is increasing at 12 cm^3/s. Find the rate of increase of its side when the side is 4 cm. [4 marks]
5. Show that the curve y = e^x cos x has a stationary point at x = π/4 and find whether it is a maximum or minimum. [5 marks]
6. The rate at which a rumour spreads, dN/dt, is proportional to the product of the number who have heard it, N, and the number who have not, (1000 - N). Write a differential equation for N. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 quotient rule; M1 chain rule for (2x - 1)^3; A1 correct unsimplified; A1 2(x + 4)(2x - 1)^2/(x + 1)^3.
2. [5] M1 differentiates implicitly with product rule on 3xy; A1 2x + 3y + 3x dy/dx - 2y dy/dx = 0; A1 dy/dx = -5 at (1, 1); M1 y - 1 = -5(x - 1); A1 y = -5x + 6.
3. [5] M1 y'' = 12x^2 - 24x; M1 = 0; A1 x = 0, x = 2; M1 checks the sign change of y'' either side; A1 both confirmed.
4. [4] M1 V = x^3, dV/dx = 3x^2; M1 dx/dt = (dV/dt)/(dV/dx); A1 12/48; A1 0.25 cm/s.
5. [5] M1 dy/dx = e^x(cos x - sin x); A1 = 0 at x = π/4; M1 d^2y/dx^2 = -2e^x sin x; A1 negative at π/4; A1 maximum.
6. [2] M1 proportional to N(1000 - N); A1 dN/dt = kN(1000 - N), k > 0.

## Grading
Apply `rubric.json`'s `stage_rubrics.S16_Further_Differentiation` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 25 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S17_Integration_Basics.
