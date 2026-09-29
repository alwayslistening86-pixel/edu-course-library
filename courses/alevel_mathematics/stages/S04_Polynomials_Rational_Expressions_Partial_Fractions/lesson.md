# S04_Polynomials_Rational_Expressions_Partial_Fractions - Lesson: Polynomials, rational expressions and partial fractions

## Goal
The learner expands, factorises and divides polynomials, uses the factor theorem, simplifies rational expressions, and splits rational functions into partial fractions.

## Syllabus items taught here
- 1.02j - Manipulating polynomials: expanding, factorising, algebraic division and the factor theorem
- 1.02k - Simplifying rational expressions
- 1.02y - Partial fractions (denominators up to a squared linear term, at most three terms)

## How to teach this
Ask what f(2) = 0 tells you about the graph of y = f(x) and about the factors of f(x). Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.02j Manipulating polynomials: expanding, factorising, algebraic division and the factor theorem
**Factor theorem:** if f(a) = 0 then (x - a) is a factor of f(x) (and if f(b/a) = 0, then (ax - b) is a factor). *Example:* f(x) = x^3 - 2x^2 - 5x + 6: f(1) = 1 - 2 - 5 + 6 = 0, so (x - 1) is a factor. Divide (long division, or compare coefficients): f(x) = (x - 1)(x^2 - x - 6) = (x - 1)(x - 3)(x + 2). Algebraic division by a linear term also gives a remainder: dividing x^3 + 2x - 5 by (x - 2) gives quotient x^2 + 2x + 6 and remainder 7 (= f(2)). Expanding: (x + 2)(x^2 - 3x + 1) = x^3 - x^2 - 5x + 2.

#### 1.02k Simplifying rational expressions
Factorise numerator and denominator fully, then cancel common **factors** (never terms). *Example:* (x^2 - 9)/(x^2 + x - 6) = (x - 3)(x + 3)/((x + 3)(x - 2)) = (x - 3)/(x - 2), for x ≠ -3. Adding fractions needs a common denominator: 2/(x - 1) - 1/(x + 1) = (2(x + 1) - (x - 1))/((x - 1)(x + 1)) = (x + 3)/(x^2 - 1). Dividing: multiply by the reciprocal.

#### 1.02y Partial fractions (denominators up to a squared linear term, at most three terms)
Split a fraction with a factorised denominator into simpler fractions. Linear factors: A/(x - p) + B/(x - q). A repeated factor (x - p)^2 needs A/(x - p) + B/(x - p)^2. *Example:* (5x + 1)/((x + 1)(x - 1)^2) = A/(x + 1) + B/(x - 1) + C/(x - 1)^2. Multiply through: 5x + 1 = A(x - 1)^2 + B(x + 1)(x - 1) + C(x + 1). x = 1: 6 = 2C, C = 3. x = -1: -4 = 4A, A = -1. Compare x^2 coefficients: 0 = A + B, B = 1. So it is -1/(x + 1) + 1/(x - 1) + 3/(x - 1)^2. Partial fractions are used in integration (S18) and in binomial expansions (S09).

## Explicitly not here
Integrating with partial fractions is S18.
