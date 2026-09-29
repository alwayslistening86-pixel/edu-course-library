# S01_Quantitative_Tools_for_Economics - Test: Quantitative bridge: calculus and optimisation for economics

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A firm's total revenue is TR(Q) = 60Q - Q^2. Find MR(Q) and the output at which TR is maximised. [3 marks]
2. Maximise U(x,y) = x^0.5 y^0.5 subject to 3x + 6y = 90 using the Lagrange method, and state x* and y*. [5 marks]
3. A variable grows at 4% a year. Calculate the total percentage increase after 5 years, and explain why this is not simply 5 x 4%. [3 marks]
4. Q = 200 - 4P. Calculate the point price elasticity of demand at P = 30, and state whether demand is elastic, inelastic or unitary at that point. [3 marks]

## Answer key (for the tutor only)
1. [3] M1 MR = dTR/dQ = 60 - 2Q; M1 set MR = 0: 60 - 2Q = 0; A1 Q = 30.
2. [5] M1 L = x^0.5 y^0.5 + lambda(90 - 3x - 6y); M1 FOCs give MUx/MUy = Px/Py, i.e. y/x = 3/6 = 0.5; M1 so 3x = 6y, substitute into budget: 3x + 3x = 90; A1 x* = 15.0, A1 y* = 7.5.
3. [3] M1 (1.04)^5 = 1.2167; A1 total rise = 21.67%; B1 growth compounds -- each year's 4% applies to an already-larger base, so the total exceeds simple addition.
4. [3] M1 dQ/dP = -4; M1 Q at P=30 is 80; A1 PED = -4 x 30/80 = -1.500 -- elastic (|PED| > 1).

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Quantitative_Tools_for_Economics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Consumer_Theory.
