# S10_Sequences_and_Series - Lesson: Sequences and series

## Goal
The learner works with sequences by formula and by recurrence, recognises increasing, decreasing and periodic sequences, uses sigma notation, sums arithmetic and geometric series (including to infinity), and models with them.

## Syllabus items taught here
- 1.04e - Sequences given by an nth-term formula or a recurrence relation
- 1.04f - Increasing, decreasing and periodic sequences
- 1.04g - Sigma notation
- 1.04h - Arithmetic sequences and series: nth term and sum to n terms
- 1.04i - Geometric sequences and series: nth term and sum of a finite series
- 1.04j - Sum to infinity of a convergent geometric series, |r| < 1
- 1.04k - Sequences and series in modelling

## How to teach this
Ask for the sum 1 + 2 + ... + 100 and how Gauss might have found it in seconds. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.04e Sequences given by an nth-term formula or a recurrence relation
A sequence can be given by a formula for the nth term (u_n = 3n^2 - 1 gives 2, 11, 26, ...) or by a recurrence relation u_(n+1) = f(u_n) with a first term (u1 = 2, u_(n+1) = 3u_n - 1 gives 2, 5, 14, 41, ...). *Example:* u_(n+1) = 5 - 2/u_n with u1 = 1 gives 1, 3, 13/3, ...; if it converges to L then L = 5 - 2/L, L^2 - 5L + 2 = 0.

#### 1.04f Increasing, decreasing and periodic sequences
Increasing: u_(n+1) > u_n for all n; decreasing: u_(n+1) < u_n; periodic with order k: u_(n+k) = u_n. *Example:* u_n = 2n + 3 is increasing (u_(n+1) - u_n = 2 > 0). *Example:* u_(n+1) = 1/(1 - u_n) with u1 = 2 gives 2, -1, 1/2, 2, -1, ...: periodic of order 3. *Example:* u_n = 1/n is decreasing and converges to 0.

#### 1.04g Sigma notation
Σ (r = 1 to n) f(r) means f(1) + f(2) + ... + f(n). *Example:* Σ (r = 1 to 5) (2r + 1) = 3 + 5 + 7 + 9 + 11 = 35. Useful facts: Σ (r = 1 to n) 1 = n; Σ (r = 1 to n) r = n(n + 1)/2. Take care with the limits: Σ (r = 3 to 10) has 8 terms. Σ (r = 11 to 20) r = Σ (1 to 20) - Σ (1 to 10) = 210 - 55 = 155.

#### 1.04h Arithmetic sequences and series: nth term and sum to n terms
Arithmetic: first term a, common difference d. u_n = a + (n - 1)d; S_n = n/2 (2a + (n - 1)d) = n/2 (a + l) where l is the last term. *Example:* 7, 11, 15, ...: u_20 = 7 + 19 × 4 = 83; S_20 = 10(7 + 83) = 900. *Example:* how many terms of 3 + 8 + 13 + ... are needed to exceed 1000? n/2 (6 + 5(n - 1)) > 1000 gives 5n^2 + n - 2000 > 0, n > 19.9, so 20 terms. Proof of S_n: write the sum forwards and backwards and add.

#### 1.04i Geometric sequences and series: nth term and sum of a finite series
Geometric: first term a, common ratio r. u_n = ar^(n - 1); S_n = a(1 - r^n)/(1 - r) (r ≠ 1). *Example:* 3, 6, 12, ...: u_10 = 3 × 2^9 = 1536; S_10 = 3(2^10 - 1)/(2 - 1) = 3069. Problems asking "the least n" lead to inequalities solved with logarithms: 3 × 2^(n-1) > 10 000 gives n - 1 > log2(3333.3) = 11.7, so n = 13. Proof of S_n: subtract r S_n from S_n.

#### 1.04j Sum to infinity of a convergent geometric series, |r| < 1
If |r| < 1 the series converges and S_∞ = a/(1 - r). *Example:* 18 + 12 + 8 + ... has r = 2/3, S_∞ = 18/(1/3) = 54. *Example:* a geometric series has S_∞ = 20 and first term 5: 5/(1 - r) = 20, r = 3/4. The condition |r| < 1 (i.e. -1 < r < 1) must be stated when asked for which values a series converges: for Σ (2x)^r, |2x| < 1 so -1/2 < x < 1/2.

#### 1.04k Sequences and series in modelling
Arithmetic series model constant increases (savings rising by £50 a month); geometric series model percentage changes (a salary rising 3% a year, a ball rebounding to 70% of its height). *Example:* a ball dropped from 10 m rebounds to 0.7 of its previous height each time; total distance travelled = 10 + 2(7 + 4.9 + ...) = 10 + 2 × 7/(1 - 0.7) = 56.7 m. Comment on the model: in reality the ball stops after finitely many bounces.

## Explicitly not here
Recurrence relations as numerical methods are S20.
