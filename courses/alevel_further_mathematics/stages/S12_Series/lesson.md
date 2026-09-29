# S12_Series - Lesson: Summation of series and the method of differences

## Goal
The learner uses the standard formulae for Σr, Σr^2 and Σr^3 to sum related series, and uses the method of differences (with partial fractions) for finite and infinite sums.

## Syllabus items taught here
- 4.06a - Standard sums of integers, squares and cubes, and related series
- 4.06b - The method of differences for finite and infinite series

## How to teach this
Ask why Σ (1/r - 1/(r + 1)) from r = 1 to 100 is so easy to work out. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.06a Standard sums of integers, squares and cubes, and related series
Σ (r = 1 to n) r = n(n + 1)/2; Σ r^2 = n(n + 1)(2n + 1)/6; Σ r^3 = n^2(n + 1)^2/4. Split and factorise: Σ (r = 1 to n) r(r + 3) = Σr^2 + 3Σr = n(n + 1)(2n + 1)/6 + 3n(n + 1)/2 = n(n + 1)(n + 5)/3. For Σ (r = n + 1 to 2n), subtract Σ (1 to n) from Σ (1 to 2n).

#### 4.06b The method of differences for finite and infinite series
If u_r = f(r) - f(r + 1), then Σ (r = 1 to n) u_r = f(1) - f(n + 1) (the middle terms cancel: write out the first few and last few terms). *Example:* 1/(r(r + 1)) = 1/r - 1/(r + 1): Σ (1 to n) = 1 - 1/(n + 1) = n/(n + 1); as n → ∞ the sum tends to 1. *Example:* Σ 2/(r(r + 2)) = Σ (1/r - 1/(r + 2)) = 1 + 1/2 - 1/(n + 1) - 1/(n + 2) (two terms survive at each end).

## Explicitly not here
Hyperbolic functions are S13.
