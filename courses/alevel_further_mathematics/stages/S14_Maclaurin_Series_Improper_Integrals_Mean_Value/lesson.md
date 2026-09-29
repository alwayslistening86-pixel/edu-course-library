# S14_Maclaurin_Series_Improper_Integrals_Mean_Value - Lesson: Maclaurin series, improper integrals and mean value

## Goal
The learner finds Maclaurin series (with general terms), uses the standard series to build others, evaluates improper integrals, and finds the mean value of a function.

## Syllabus items taught here
- 4.08a - Maclaurin series of a function, including the general term
- 4.08b - Standard Maclaurin series for e^x, sin x, cos x, ln(1 + x) and (1 + x)^n, and functions built from them
- 4.08c - Improper integrals: infinite ranges and integrands undefined in the range
- 4.08e - The mean value of a function

## How to teach this
Ask how a calculator could possibly compute sin(0.3) using only + and x. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.08a Maclaurin series of a function, including the general term
f(x) = f(0) + f'(0)x + f''(0)x^2/2! + ... + f^(r)(0)x^r/r! + ... *Example:* f(x) = ln(1 + e^x): f(0) = ln 2, f'(x) = e^x/(1 + e^x) = 1/2 at 0, f''(0) = 1/4, giving ln 2 + x/2 + x^2/8 + ...

#### 4.08b Standard Maclaurin series for e^x, sin x, cos x, ln(1 + x) and (1 + x)^n, and functions built from them
e^x = Σ x^r/r!; sin x = x - x^3/3! + x^5/5! - ...; cos x = 1 - x^2/2! + x^4/4! - ...; ln(1 + x) = x - x^2/2 + x^3/3 - ... (-1 < x ≤ 1); (1 + x)^n = 1 + nx + ... (|x| < 1); e^x, sin x, cos x valid for all x. Build others by substitution, multiplication or differentiation: e^(2x) sin x = x + 2x^2 + 11x^3/6 + ...

#### 4.08c Improper integrals: infinite ranges and integrands undefined in the range
An improper integral has an infinite limit or an integrand undefined at a point in the range: replace the problem point by a variable, integrate, and take the limit. ∫ (1 to ∞) 1/x^2 dx = lim (a → ∞) [-1/x] (1 to a) = 1 (converges). ∫ (0 to 1) 1/root x dx = lim (b → 0+) [2root x] = 2. ∫ (1 to ∞) 1/x dx diverges (ln a → ∞). Use lim x^k e^(-x) = 0 and lim x ln x = 0 as needed.

#### 4.08e The mean value of a function
The mean value of f on [a, b] is (1/(b - a)) ∫ (a to b) f(x) dx. *Example:* the mean of sin x on [0, π] is 2/π ≈ 0.6366. Adding k to f adds k to the mean; multiplying by k multiplies it.

## Explicitly not here
Volumes and further integration are S15.
