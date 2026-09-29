# S11_Vector_Calculus - Test: Vector calculus

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find curl F for F = (yz, xz, xy) and interpret the result. [5 marks]
2. Evaluate the line integral of F=(x^2, -xy) along the straight line from (0,0) to (1,2). [6 marks]
3. Use the Divergence Theorem to find the flux of F=(x^3,y^3,z^3) out of the sphere x^2+y^2+z^2=4. [6 marks]
4. Verify Green's Theorem for F=(P,Q)=(xy, x^2) round the boundary of the unit square [0,1]x[0,1], by computing both sides. [8 marks]
5. Which are true for a vector field F with continuous partial derivatives? Choose every correct option.
   A. div F is a scalar field
   B. curl F is a vector field
   C. `div(curl F) = 0 always`
   D. `curl(grad f) = 0 always for a scalar field f`

## Answer key (for the tutor only)
1. [5] M1 curl F = (d(xy)/dy - d(xz)/dz, d(yz)/dz-d(xy)/dx, d(xz)/dx-d(yz)/dy); M1 = (x-x, y-y, z-z); A2 = (0,0,0); A1 zero curl everywhere means F is (locally) conservative / irrotational.
2. [6] M1 parametrises r(t)=(t,2t), t in [0,1], r'(t)=(1,2); M1 F(r(t))=(t^2,-2t^2); A1 F.r'=t^2+(-2t^2)(2)=t^2-4t^2=-3t^2; M1 integral_0^1 -3t^2 dt; A2 = -1 (fully correct with the antiderivative -t^3 shown).
3. [6] M1 div F = 3x^2+3y^2+3z^2 = 3(x^2+y^2+z^2); M1 converts to spherical: 3rho^2, and integrates over the ball of radius 2; A1 integral_V 3rho^2 dV = 3 integral_0^{2pi}integral_0^{pi}integral_0^2 rho^2 (rho^2 sin phi) drho dphi dtheta; M1 radial integral integral_0^2 rho^4 drho = 32/5; A1 angular integrals give 4pi; A1 total flux = 3(32/5)(4pi) = 384pi/5.
4. [8] M1 double integral side: dQ/dx-dP/dy = 2x - x = x; A1 integral_0^1 integral_0^1 x dy dx = 1/2; M1 line integral side: four edges parametrised separately; A2 bottom (y=0): integral x(0)dx=0; A1 right (x=1): integral 1 dy from 0 to1 =1; A1 top (y=1, x from 1 to 0): integral x dx from 1 to 0 = -1/2; A1 left (x=0): 0; sum = 1-1/2=1/2, matching the double integral.
5. Correct: A, B, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Vector_Calculus` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 26 marks in all; a pass needs at least 16 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Rings_and_Fields.
