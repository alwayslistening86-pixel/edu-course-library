# S10_Ordinary_Differential_Equations - Test: Ordinary differential equations

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Solve the linear ODE dy/dx + (2/x)y = x^2 for x>0, given y(1)=1. [6 marks]
2. Solve y''-4y'+4y=e^{2x}, the resonance case worked in the lesson, fully justifying the choice of particular integral. [7 marks]
3. For the system x'=3x-2y, y'=2x-2y, find the general solution using eigenvalues/eigenvectors. [8 marks]
4. Classify the equilibrium at the origin for x'=-x+3y, y'=-3x-y using trace and determinant. [5 marks]
5. A tank contains 100 L of brine with 5 kg of salt dissolved. Brine with concentration 0.2 kg/L enters at 4 L/min and the well-mixed solution leaves at the same rate. Set up and solve the ODE for the salt mass S(t). [6 marks]
6. For x'=Ax (2x2), which pairings of eigenvalue type with phase-portrait name are correct? Choose every correct option.
   A. Real, both negative: stable node
   B. Real, opposite signs: saddle
   C. Purely imaginary: centre
   D. Complex with positive real part: stable spiral

## Answer key (for the tutor only)
1. [6] M1 identifies P(x)=2/x, integrating factor mu=e^{integral 2/x dx}=x^2; A1 mu=x^2; M1 d/dx[x^2 y] = x^4; A1 x^2 y = x^5/5 + C; M1 uses y(1)=1: 1=1/5+C, C=4/5; A1 y = x^3/5 + 4/(5x^2).
2. [7] M1 auxiliary m^2-4m+4=0 has repeated root m=2; A1 CF = (A+Bx)e^{2x}; M1 notes e^{2x} and xe^{2x} both already solve the homogeneous equation, so trial PI is Cx^2e^{2x}; M1 substitutes and differentiates (product rule twice) to find C; A1 C=1/2; A2 general solution y=(A+Bx)e^{2x}+(x^2/2)e^{2x} (matches sympy's dsolve).
3. [8] M1 matrix A=[[3,-2],[2,-2]]; M1 char eqn (3-lambda)(-2-lambda)+4=0 i.e. lambda^2-lambda-2=0; A1 lambda=2,-1; M1 for lambda=2: (A-2I)v=0 gives eigenvector (2,1); A1 for lambda=-1: (A+I)v=0 gives eigenvector (1,2); A1 general solution x(t)=C1 e^{2t}(2,1)+C2 e^{-t}(1,2); A2 correctly labelled components with both initial-eigenvector computations shown in full.
4. [5] M1 matrix A=[[-1,3],[-3,-1]]; M1 trace=-2, determinant=1+9=10; A1 Delta=10>0; M1 tau^2=4 < 4Delta=40; A1 stable spiral (trace negative, complex eigenvalues with negative real part).
5. [6] M1 sets up dS/dt = 0.2(4) - (S/100)(4) = 0.8 - 0.04S; A1 correct linear ODE; M1 integrating factor e^{0.04t}; A1 solves to S = 20 + Ce^{-0.04t}; M1 uses S(0)=5: C=-15; A1 S(t) = 20 - 15e^{-0.04t}.
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Ordinary_Differential_Equations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 33 marks in all; a pass needs at least 20 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Vector_Calculus.
