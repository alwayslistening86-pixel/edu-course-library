# S15_Volumes_and_Further_Integration - Lesson: Volumes of revolution and further integration

## Goal
The learner derives and computes volumes of revolution, integrates using partial fractions with quadratic factors, differentiates inverse trig and hyperbolic functions, and uses standard integrals with trig and hyperbolic substitutions.

## Syllabus items taught here
- 4.08d - Volumes of revolution about the x- and y-axes, including parametric and composite shapes
- 4.08f - Integration using partial fractions, including quadratic factors
- 4.08g - Derivatives of arcsin, arccos, arctan and the inverse hyperbolic functions
- 4.08h - Integrals of 1/(a^2 + x^2), 1/root(a^2 - x^2), 1/root(x^2 + a^2), 1/root(x^2 - a^2) with inverse trig or hyperbolic substitutions

## How to teach this
Ask how slicing a vase into thin discs could give its volume. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.08d Volumes of revolution about the x- and y-axes, including parametric and composite shapes
About the x-axis: V = π ∫ y^2 dx; about the y-axis: V = π ∫ x^2 dy (derived from summing thin discs, limit of a sum). *Example:* y = root x from 0 to 4 about the x-axis: π ∫ x dx = 8π. Parametric: V = π ∫ y^2 (dx/dt) dt. Composite volumes: add or subtract (a region between two curves gives a washer: π ∫ (y1^2 - y2^2) dx).

#### 4.08f Integration using partial fractions, including quadratic factors
With a quadratic factor: ∫ (Bx + C)/(x^2 + a^2) dx = (B/2) ln(x^2 + a^2) + (C/a) arctan(x/a). *Example:* (5x^2 + 2x + 3)/((x + 1)(x^2 + 1)) = 3/(x + 1) + 2x/(x^2 + 1), so the integral is 3 ln|x + 1| + ln(x^2 + 1) + c. With a constant in the numerator too, e.g. ∫ 1/(x^2 + 4) dx, an arctan term appears: (1/2) arctan(x/2) + c.

#### 4.08g Derivatives of arcsin, arccos, arctan and the inverse hyperbolic functions
d/dx arcsin x = 1/root(1 - x^2); arccos x: -1/root(1 - x^2); arctan x: 1/(1 + x^2); arsinh x: 1/root(x^2 + 1); arcosh x: 1/root(x^2 - 1); artanh x: 1/(1 - x^2). Derive by writing x = sin y, differentiating implicitly and using an identity. With the chain rule: d/dx arctan(2x) = 2/(1 + 4x^2).

#### 4.08h Integrals of 1/(a^2 + x^2), 1/root(a^2 - x^2), 1/root(x^2 + a^2), 1/root(x^2 - a^2) with inverse trig or hyperbolic substitutions
∫1/(a^2 + x^2) dx = (1/a) arctan(x/a); ∫1/root(a^2 - x^2) dx = arcsin(x/a); ∫1/root(x^2 + a^2) dx = arsinh(x/a); ∫1/root(x^2 - a^2) dx = arcosh(x/a) (x > a). Complete the square first: ∫1/(x^2 + 4x + 13) dx = ∫1/((x + 2)^2 + 9) dx = (1/3) arctan((x + 2)/3) + c. *Example:* ∫ (0 to 3) 1/root(x^2 + 9) dx = arsinh 1 = ln(1 + root2) ≈ 0.8814. Use x = a sin θ, x = a sinh u or x = a cosh u when the integral isn't in standard form.

## Explicitly not here
Polar coordinates are S16.
