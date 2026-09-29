# S02_Multivariable_Calculus - Test: Multivariable calculus

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. For f(x,y) = x^3 - 3xy + y^3, find all stationary points and classify each. [8 marks]
2. Given z = x^2 e^{y}, x = t^2, y = sin t, find dz/dt at t=0 using the chain rule. [5 marks]
3. Find dy/dx by implicit differentiation for x^3+y^3=6xy at the point (3,3). [5 marks]
4. Use Lagrange multipliers to find the minimum value of f(x,y)=x^2+y^2 subject to x+2y=5. [6 marks]
5. At a stationary point of f(x,y) with Hessian determinant D and f_xx given, which correctly identify the point's nature? Choose every correct option.
   A. `D>0, f_xx>0: local minimum`
   B. `D>0, f_xx<0: local maximum`
   C. `D<0: always a local minimum`
   D. `D<0: saddle point`

## Answer key (for the tutor only)
1. [8] M1 f_x=3x^2-3y=0, f_y=-3x+3y^2=0; M1 solves y=x^2 and x=y^2; A1 (0,0) and (1,1); M1 f_xx=6x, f_yy=6y, f_xy=-3; A1 at (0,0), D=0-9=-9<0, saddle; A1 at (1,1), D=36-9=27>0 and f_xx=6>0, local minimum; A2 clear justification of both classifications shown, both stationary points found and correctly named.
2. [5] M1 z_x=2xe^y, z_y=x^2e^y; M1 dx/dt=2t, dy/dt=cos t; A1 dz/dt=2xe^y(2t)+x^2e^y cos t; M1 at t=0, x=0,y=0; A1 dz/dt=0.
3. [5] M1 differentiates: 3x^2+3y^2 y' = 6y+6x y'; M1 rearranges y'(3y^2-6x) = 6y-3x^2; A1 y' = (6y-3x^2)/(3y^2-6x); M1 substitutes x=y=3; A1 y' = (18-27)/(27-18) = -1.
4. [6] M1 grad f=(2x,2y)=lambda(1,2); A1 2x=lambda, 2y=2lambda so y=2x; M1 substitutes into constraint x+2(2x)=5; A1 x=1, y=2; M1 f(1,2)=1+4=5; A1 minimum value 5.
5. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Multivariable_Calculus` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 25 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Probability_and_Statistical_Inference.
