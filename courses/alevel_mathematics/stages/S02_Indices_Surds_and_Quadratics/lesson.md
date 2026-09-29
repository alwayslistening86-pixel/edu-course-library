# S02_Indices_Surds_and_Quadratics - Lesson: Indices, surds and quadratics

## Goal
The learner applies the index laws with rational powers, simplifies and rationalises surds, completes the square, uses the discriminant, and solves quadratics including disguised quadratics.

## Syllabus items taught here
- 1.02a - Laws of indices for all rational exponents
- 1.02b - Surds, including rationalising the denominator
- 1.02d - Quadratic functions, their graphs and the discriminant (conditions for real and repeated roots)
- 1.02e - Completing the square
- 1.02f - Solving quadratic equations, including quadratics in a function of the unknown

## How to teach this
Ask what 8^(-2/3) means, step by step, before any rules are stated. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.02a Laws of indices for all rational exponents
a^m x a^n = a^(m+n); a^m / a^n = a^(m-n); (a^m)^n = a^(mn); a^0 = 1; a^(-n) = 1/a^n; a^(1/n) = nth root of a; a^(m/n) = (nth root of a)^m. *Examples:* 8^(-2/3) = 1/(cube root 8)^2 = 1/4. (27/64)^(2/3) = (3/4)^2 = 9/16. Simplify (4x^3)^(1/2) × 2x^(-1/2) = 2x^(3/2) × 2x^(-1/2) = 4x. Write roots and reciprocals as powers before differentiating or integrating: 3/root(x) = 3x^(-1/2).

#### 1.02b Surds, including rationalising the denominator
root(ab) = root(a) root(b) and root(a/b) = root(a)/root(b). Simplify by taking out square factors: root 72 = root 36 root 2 = 6 root 2. Rationalise: 5/root 3 = 5 root 3 / 3; for a binomial denominator multiply by the conjugate: 4/(3 - root 5) = 4(3 + root 5)/((3 - root 5)(3 + root 5)) = 4(3 + root 5)/4 = 3 + root 5. Surds are exact: keep them unless a decimal is asked for.

#### 1.02d Quadratic functions, their graphs and the discriminant (conditions for real and repeated roots)
For f(x) = ax^2 + bx + c the discriminant is b^2 - 4ac: positive means two distinct real roots, zero a repeated root (the graph touches the x-axis), negative no real roots. The graph is a parabola, U-shaped if a > 0, crossing the y-axis at c. *Example:* for what k does x^2 + kx + 9 = 0 have equal roots? k^2 - 36 = 0, so k = 6 or k = -6. *Example:* find k so that kx^2 + 4x + k = 0 has no real roots: 16 - 4k^2 < 0, so k^2 > 4, giving k < -2 or k > 2.

#### 1.02e Completing the square
ax^2 + bx + c = a(x + p)^2 + q. For a = 1: x^2 + bx + c = (x + b/2)^2 - (b/2)^2 + c. *Example:* x^2 - 6x + 11 = (x - 3)^2 + 2, so the minimum point is (3, 2) and the line of symmetry is x = 3; since the minimum value is 2 > 0 there are no real roots. With a ≠ 1 take the factor out first: 2x^2 + 8x + 5 = 2(x^2 + 4x) + 5 = 2(x + 2)^2 - 3, minimum point (-2, -3).

#### 1.02f Solving quadratic equations, including quadratics in a function of the unknown
Solve by factorising, completing the square or the formula x = (-b ± root(b^2 - 4ac))/(2a). *Example:* 2x^2 - 3x - 4 = 0 gives x = (3 ± root 41)/4 = 2.351 or -0.851 (3 d.p.). A **disguised quadratic** is a quadratic in some function of x. *Example:* x^4 - 5x^2 + 4 = 0: let u = x^2, so u^2 - 5u + 4 = 0, u = 1 or 4, so x = ±1 or ±2. *Example:* 2^(2x) - 6(2^x) + 8 = 0: u = 2^x gives u = 2 or 4, so x = 1 or 2. Reject any u values impossible for the substitution (e.g. 2^x = -3 has no solution).

## Explicitly not here
Inequalities and simultaneous equations are S03.
