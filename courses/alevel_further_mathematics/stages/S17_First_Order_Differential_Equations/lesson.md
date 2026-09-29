# S17_First_Order_Differential_Equations - Lesson: First-order differential equations

## Goal
The learner distinguishes general and particular solutions, models with differential equations, and solves linear first-order equations with an integrating factor.

## Syllabus items taught here
- 4.10a - General and particular solutions of differential equations
- 4.10b - Differential equations in modelling, in kinematics and other contexts
- 4.10c - Integrating factors for dy/dx + P(x)y = Q(x)

## How to teach this
Ask why dy/dx + y = x can't be separated, and what multiplying by e^x does to it. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.10a General and particular solutions of differential equations
A general solution contains arbitrary constants (one for first order, two for second order): a family of curves. A particular solution uses initial or boundary conditions to fix them. Always check a solution by substituting back.

#### 4.10b Differential equations in modelling, in kinematics and other contexts
Model: set up the equation from a rate statement, solve, apply conditions, then interpret and critique (units, long-term behaviour, validity). *Example:* a raindrop's speed v satisfies dv/dt = 9.8 - 0.2v: the terminal speed is 49 m/s (where dv/dt = 0).

#### 4.10c Integrating factors for dy/dx + P(x)y = Q(x)
dy/dx + P(x)y = Q(x): multiply by the integrating factor e^(∫P dx); the left side becomes d/dx(y e^(∫P dx)). *Example:* dy/dx + 2y/x = x^2 (x > 0): IF = e^(2 ln x) = x^2; d/dx(x^2 y) = x^4; x^2 y = x^5/5 + c; y = x^3/5 + c/x^2. Rearrange into standard form first (divide by any coefficient of dy/dx).

## Explicitly not here
Second-order equations are S18.
