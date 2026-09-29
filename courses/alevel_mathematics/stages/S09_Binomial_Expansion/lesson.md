# S09_Binomial_Expansion - Lesson: The binomial expansion

## Goal
The learner expands (a + bx)^n for positive integers n using nCr, links coefficients to binomial probabilities, expands for rational n, states validity and uses expansions to approximate.

## Syllabus items taught here
- 1.04a - Binomial expansion of (a + bx)^n for positive integer n; n!, nCr notation
- 1.04b - Link between binomial coefficients and binomial probabilities
- 1.04c - Binomial expansion of (a + bx)^n for any rational n, including approximations
- 1.04d - Validity of the expansion: |bx/a| < 1

## How to teach this
Ask how Pascal's triangle and nCr are the same thing, then ask what happens if n is -1. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.04a Binomial expansion of (a + bx)^n for positive integer n; n!, nCr notation
(a + b)^n = a^n + nC1 a^(n-1) b + nC2 a^(n-2) b^2 + ... + b^n, with nCr = n!/(r!(n - r)!). *Example:* (2 + 3x)^4 = 16 + 96x + 216x^2 + 216x^3 + 81x^4: the x^2 term is 4C2 (2^2)(3x)^2 = 6 × 4 × 9x^2 = 216x^2. To find one term, write the general term nCr a^(n-r) (bx)^r. *Example:* the coefficient of x^3 in (1 - 2x)^7 is 7C3 (-2)^3 = 35 × (-8) = -280.

#### 1.04b Link between binomial coefficients and binomial probabilities
If X ~ B(n, p) then P(X = r) = nCr p^r (1 - p)^(n - r): each term of (q + p)^n with q = 1 - p is a probability, and they sum to (q + p)^n = 1. *Example:* for 5 fair coins, P(exactly 2 heads) = 5C2 (1/2)^5 = 10/32. Links to S24.

#### 1.04c Binomial expansion of (a + bx)^n for any rational n, including approximations
For rational n (negative or fractional), (1 + x)^n = 1 + nx + n(n - 1)x^2/2! + n(n - 1)(n - 2)x^3/3! + ..., an infinite series. For (a + bx)^n take a^n out first: (a + bx)^n = a^n (1 + (b/a)x)^n. *Example:* (1 - 2x)^(-1/2) = 1 + x + 3x^2/2 + 5x^3/2 + ... *Example:* root(4 + x) = 2(1 + x/4)^(1/2) = 2 + x/4 - x^2/64 + ... Approximate root 4.1 by x = 0.1: 2 + 0.025 - 0.00015625 = 2.024844, against root 4.1 = 2.024846. Expansions combine with partial fractions: expand each fraction separately and add.

#### 1.04d Validity of the expansion: |bx/a| < 1
(1 + x)^n for non-integer n is valid only when |x| < 1; (a + bx)^n is valid when |bx/a| < 1, i.e. |x| < |a/b|. *Example:* (1 - 2x)^(-1/2) is valid for |2x| < 1, i.e. |x| < 1/2; root(4 + x) for |x| < 4. For a sum of expansions the valid range is the intersection of the individual ranges. An approximation is only sensible for x inside the range, and better the smaller |x| is.

## Explicitly not here
Sequences and series are S10.
