# S21_Continuous_Random_Variables - Lesson: Continuous random variables

## Goal
The learner works with probability density and cumulative distribution functions (including piecewise), calculates means, variances, E(g(X)), medians and percentiles, and finds distributions of related variables.

## Syllabus items taught here
- 5.03a - Continuous random variables, probability density functions and cumulative distribution functions
- 5.03b - Probabilities from a p.d.f., including piecewise definitions
- 5.03c - Mean and variance of a continuous random variable
- 5.03d - E(g(X)) for a continuous random variable
- 5.03e - Finding and using a cumulative distribution function, including piecewise
- 5.03f - Relationship between the p.d.f. and the c.d.f.; medians and percentiles
- 5.03g - Cumulative distribution functions of related variables

## How to teach this
Ask why P(X = 2) is zero for a continuous variable, and what a density can mean instead. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.03a Continuous random variables, probability density functions and cumulative distribution functions
A continuous random variable X has a p.d.f. f(x) ≥ 0 with ∫ f(x) dx = 1 over its range; probabilities are areas: P(a < X < b) = ∫ (a to b) f(x) dx. The c.d.f. is F(x) = P(X ≤ x). P(X = a) = 0, so < and ≤ give the same probabilities.

#### 5.03b Probabilities from a p.d.f., including piecewise definitions
*Example:* f(x) = (3/32)x(4 - x) for 0 ≤ x ≤ 4 (0 otherwise). Check it integrates to 1: 1. P(X < 1) = ∫ (0 to 1) f dx = 5/32. Piecewise p.d.f.s: integrate each piece over its own interval and add. Find unknown constants from the total area being 1.

#### 5.03c Mean and variance of a continuous random variable
E(X) = ∫ x f(x) dx; Var(X) = ∫ x^2 f(x) dx - μ^2. For the example: E(X) = 2 (by symmetry too), E(X^2) = 24/5, Var(X) = 4/5.

#### 5.03d E(g(X)) for a continuous random variable
E(g(X)) = ∫ g(x) f(x) dx over the range. For the example f(x) = (3/32)x(4 - x): E(X^3) = 64/5 and E(root X) = 1.3714. Linear results still hold: E(aX + b) = aE(X) + b, Var(aX + b) = a^2 Var(X).

#### 5.03e Finding and using a cumulative distribution function, including piecewise
F(x) = ∫ (from the lower limit to x) f(t) dt; F is 0 below the range and 1 above it, and continuous. For the example: F(x) = -x^3/32 + 3x^2/16 for 0 ≤ x ≤ 4. For piecewise p.d.f.s, carry the accumulated probability into each new piece.

#### 5.03f Relationship between the p.d.f. and the c.d.f.; medians and percentiles
f(x) = F'(x). The median m satisfies F(m) = 0.5; the upper quartile F(q) = 0.75; the nth percentile F(x) = n/100. The mode is where f is greatest. *Example:* F(x) = x^3/8 on [0, 2]: median m = 4^(1/3) ≈ 1.587.

#### 5.03g Cumulative distribution functions of related variables
For Y = g(X) with g increasing, G(y) = P(Y ≤ y) = P(X ≤ g^(-1)(y)) = F(g^(-1)(y)), then differentiate for the p.d.f. *Example:* X uniform on [0, 2] (F(x) = x/2), Y = X^2: G(y) = P(X ≤ root y) = root(y)/2 for 0 ≤ y ≤ 4, so g(y) = 1/(4root y). Take care with the new range.

## Explicitly not here
Linear combinations and estimation are S22.
