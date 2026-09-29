# S19_Differential_Equations - Lesson: Differential equations

## Goal
The learner solves first-order separable differential equations, finds particular solutions, and interprets solutions in context including their limitations.

## Syllabus items taught here
- 1.08k - First-order differential equations with separable variables: general and particular solutions
- 1.08l - Interpreting the solution of a differential equation in context, including limitations

## How to teach this
Ask what family of curves all have gradient equal to their y-value. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.08k First-order differential equations with separable variables: general and particular solutions
Separable: dy/dx = f(x)g(y). Separate, integrate both sides, add one constant. *Example:* dy/dx = xy: ∫(1/y) dy = ∫x dx, ln|y| = x^2/2 + c, so y = Ae^(x^2/2). With y = 3 when x = 0: A = 3. *Example:* dP/dt = 0.2P with P = 50 at t = 0 gives P = 50e^(0.2t). *Example:* dy/dx = 2x(y + 1)^2 gives -1/(y + 1) = x^2 + c. Rearrange to make y the subject when asked to "find y in terms of x".

#### 1.08l Interpreting the solution of a differential equation in context, including limitations
Interpret constants and long-term behaviour. *Example:* Newton's law of cooling dT/dt = -k(T - 20), T(0) = 90: ∫1/(T - 20) dT = -∫k dt, ln(T - 20) = -kt + c, T = 20 + 70e^(-kt). If T = 60 after 10 minutes, k = (1/10) ln(70/40) = 0.0560. As t → ∞, T → 20 (room temperature). Limitations: the room temperature may not stay constant; k may vary. Criticise a model when it predicts impossible values (negative populations, unlimited growth).

## Explicitly not here
Numerical methods are S20.
