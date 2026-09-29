# S10_Ordinary_Differential_Equations - Lesson: Ordinary differential equations

## Goal
The learner solves separable and linear first-order ODEs, solves second-order linear ODEs with constant coefficients (including resonance cases), solves linear systems via eigenvalues/eigenvectors, classifies planar equilibria, and models with ODEs.

## Syllabus items taught here
- 10a - First-order ODEs: separable equations and integrating factors for linear equations
- 10b - Second-order linear ODEs with constant coefficients: complementary function and particular integral
- 10c - Systems of first-order linear ODEs; solution via eigenvalues/eigenvectors of the coefficient matrix
- 10d - Phase-plane classification of equilibria for 2x2 linear systems (node, saddle, spiral, centre)
- 10e - Modelling with ODEs: exponential growth/decay, damped harmonic motion, predator-prey

## How to teach this
Ask what differential equation describes a population growing at a rate proportional to its size, before solving it. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 10a First-order ODEs: separable equations and integrating factors for linear equations
A **separable** ODE dy/dx = f(x)g(y) is solved by writing dy/g(y) = f(x) dx and integrating both sides. A **linear** first-order ODE dy/dx + P(x)y = Q(x) is solved using the **integrating factor** mu(x) = e^{integral P(x)dx}: multiplying through gives d/dx[mu y] = mu Q(x), then integrate and divide by mu. *Example (separable):* dy/dx = xy, y(0)=2: integral dy/y = integral x dx gives ln|y| = x^2/2 + C, so y = 2e^{x^2/2}. *Example (linear):* dy/dx + 2y = e^{-x}: mu = e^{2x}, giving d/dx[e^{2x}y] = e^{x}, so e^{2x}y = e^x + C, y = e^{-x} + Ce^{-2x}.

#### 10b Second-order linear ODEs with constant coefficients: complementary function and particular integral
For ay''+by'+cy=0, the **auxiliary (characteristic) equation** am^2+bm+c=0 has roots m1,m2 giving the **complementary function**: distinct real roots -> y=Ae^{m1 x}+Be^{m2 x}; repeated root m -> y=(A+Bx)e^{mx}; complex roots p±qi -> y=e^{px}(A cos qx + B sin qx). For non-homogeneous ay''+by'+cy=f(x), add a **particular integral** found by trying a form matching f(x) (and multiplying by x, or x^2, if that form already solves the homogeneous equation -- resonance). *Example:* y''-5y'+6y=0 has auxiliary equation m^2-5m+6=0, roots 2,3, so sympy confirms the general solution (C1 + C2 e^(x)) e^(2x).

#### 10c Systems of first-order linear ODEs; solution via eigenvalues/eigenvectors of the coefficient matrix
A system x' = Ax (x a vector, A a constant matrix) is solved using A's eigenvalues/eigenvectors: if A has eigenvalue lambda with eigenvector v, then x(t) = e^{lambda t} v is a solution; the general solution is a linear combination of such solutions (one per eigenvalue, for a diagonalisable A). *Example:* for x'=Ax with A = Matrix([
[3, -2],
[2, -2]]): eigenvalues/eigenvectors are [('-1', 'Matrix([[1/2, 1]])'), ('2', 'Matrix([[2, 1]])')], so the general solution is x(t) = C1 e^{-1t}Matrix([[1/2, 1]]) + C2 e^{2t}Matrix([[2, 1]]).

#### 10d Phase-plane classification of equilibria for 2x2 linear systems (node, saddle, spiral, centre)
For x'=Ax (2x2), the **phase-plane** behaviour near the equilibrium at the origin is classified by A's eigenvalues: both real, same sign -> **node** (stable if both negative, unstable if both positive); real, opposite sign -> **saddle** (unstable); complex with nonzero real part -> **spiral** (stable if real part negative); purely imaginary -> **centre** (trajectories are closed orbits). Equivalently, using trace tau and determinant Delta of A: Delta<0 gives a saddle; Delta>0 and tau^2>4Delta gives a node; Delta>0 and tau^2<4Delta gives a spiral (stable if tau<0); Delta>0, tau=0 gives a centre. *Example:* A=[[0,1],[-1,0]] has trace 0, determinant 1>0, so tau^2=0<4Delta -- a centre (purely imaginary eigenvalues ±i, confirmed by the characteristic equation lambda^2+1=0).

#### 10e Modelling with ODEs: exponential growth/decay, damped harmonic motion, predator-prey
ODEs model many real systems: **exponential growth/decay** dN/dt = kN solves to N=N_0 e^{kt}; **damped harmonic motion** mx''+cx'+kx=0 (a spring-mass-damper) gives over-, under- or critically-damped behaviour depending on the discriminant c^2-4mk; the **Lotka-Volterra predator-prey** system dx/dt = ax-bxy, dy/dt = -cy+dxy is nonlinear but its linearisation near an equilibrium can be analysed with the eigenvalue methods above. *Example:* a radioactive substance with half-life 5730 years (carbon-14) has decay constant k = ln(2)/5730; if N(0)=N_0, the time for N to fall to 0.1N_0 is t = ln(10)/k, matching the standard dating calculation.

## Explicitly not here
Partial differential equations (which involve more than one independent variable) are beyond this stage's scope.
