# S01_Proof_by_Induction - Lesson: Proof by induction

## Goal
The learner writes complete proofs by induction for sums, divisibility, recurrence relations and matrix powers, and tackles conjecture-then-proof problems.

## Syllabus items taught here
- 4.01a - Proof by mathematical induction (sums of series, divisibility, matrix powers)
- 4.01b - Proofs of a more demanding nature, including conjecture followed by proof

## How to teach this
Ask how knowing 'if a domino falls, the next one falls' plus 'the first one falls' guarantees they all fall. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 4.01a Proof by mathematical induction (sums of series, divisibility, matrix powers)
Structure: (1) **basis**: show the statement true for n = 1 (or the first value); (2) **assumption**: assume true for n = k; (3) **inductive step**: prove it for n = k + 1 using the assumption; (4) **conclusion**: "since it is true for n = 1, and true for n = k implies true for n = k + 1, it is true for all positive integers n by induction." *Sum:* Σ (r = 1 to n) r^2 = n(n + 1)(2n + 1)/6. Basis: 1 = 1(2)(3)/6. Step: k(k + 1)(2k + 1)/6 + (k + 1)^2 = (k + 1)(2k^2 + k + 6k + 6)/6 = (k + 1)(k + 2)(2k + 3)/6, which is the formula with n = k + 1. *Divisibility:* 7^n - 1 is divisible by 6. f(1) = 6. f(k + 1) = 7 x 7^k - 1 = 7(7^k - 1) + 6, a multiple of 6 if 7^k - 1 is. *Matrix power:* if M = [[1, 2], [0, 1]] then M^n = [[1, 2n], [0, 1]]: M^(k+1) = M^k M = [[1, 2k + 2], [0, 1]].

#### 4.01b Proofs of a more demanding nature, including conjecture followed by proof
Harder induction: recurrence relations (u1 = 2, u_(n+1) = 3u_n - 2 gives u_n = 3^(n-1) + 1: step 3(3^(k-1) + 1) - 2 = 3^k + 1), inequalities (2^n > n^2 for n ≥ 5: basis 32 > 25; step 2^(k+1) = 2 x 2^k > 2k^2 ≥ (k + 1)^2 when k ≥ 3), and **conjecture then proof**: compute early cases, spot the pattern, then prove it. *Example:* Σ 1/(r(r + 1)) gives 1/2, 2/3, 3/4, so conjecture n/(n + 1), then prove it (also possible by differences, S12). Induction can also prove derivative results, e.g. d^n/dx^n (xe^x) = (x + n)e^x.

## Explicitly not here
Summation formulae and the method of differences are S12.
