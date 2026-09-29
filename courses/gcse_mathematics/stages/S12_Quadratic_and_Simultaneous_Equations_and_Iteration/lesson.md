# S12_Quadratic_and_Simultaneous_Equations_and_Iteration - Lesson: Quadratic equations, simultaneous equations and iteration

## Goal
The learner solves quadratic equations by factorising and by the formula, solves simultaneous equations (including a linear/quadratic pair), and uses sign-change and iteration to approximate roots.

## Syllabus items taught here
- 6.03b - Solve quadratics by factorising; quadratic formula (Higher): solve quadratic equations by more than one method
- 6.03c - Simultaneous equations; linear/quadratic pairs (Higher): solve two equations in two unknowns
- 6.03e - Iterative sign-change methods (Higher): locate a root by change of sign and iteration

## How to teach this
Ask: 'The product of two numbers is 0. What does that tell you about the numbers?' It leads to why factorised quadratics equal to zero give two answers.

#### 6.03b Solving quadratics by factorising and by the formula
Set the equation equal to zero first. Factorise x^2 - 5x + 6 = 0 into (x - 2)(x - 3) = 0 so x = 2 or x = 3. Higher: when factorising is not possible, use x = (-b +/- sqrt(b^2 - 4ac))/(2a). For 2x^2 + 3x - 4 = 0, a = 2, b = 3, c = -4: x = (-3 +/- sqrt(9 + 32))/4 = (-3 +/- sqrt(41))/4, so x = 0.85 or x = -2.35 to 2 decimal places. Put brackets round negative numbers in the formula. The discriminant b^2 - 4ac tells you how many real solutions there are.

#### 6.03c Simultaneous equations
Solve by substitution or elimination. Elimination: 2x + 3y = 12 and 4x - 3y = 6; add the equations to get 6x = 18, x = 3, then y = 2. If a variable does not match, multiply an equation first. Substitution: x - y = 2 and 3x + 2y = 16 give x = y + 2, so 3y + 6 + 2y = 16, y = 2 and x = 4. Higher: a linear/quadratic pair. Solve y = x^2 - 3 and y = x + 3: x^2 - 3 = x + 3, x^2 - x - 6 = 0, x = 3 or -2, so the points are (3, 6) and (-2, 1). Always find both coordinates and pair them up correctly.

#### 6.03e Approximating roots by change of sign and iteration
Higher only. If f(a) and f(b) have opposite signs and f is continuous, there is a root between a and b. For f(x) = x^3 + x - 3: f(1) = -1, f(2) = 7, so a root lies between 1 and 2; f(1.2) = -0.072 and f(1.3) = 0.497 narrow it to between 1.2 and 1.3. For an iterative formula such as x(n+1) = cube root of (3 - x(n)) starting at x1 = 1.2: x2 = 1.2164, x3 = 1.2129, x4 = 1.2135, settling at 1.213 to 3 decimal places. Use the calculator's answer key to repeat quickly, and give the answer to the requested accuracy.
