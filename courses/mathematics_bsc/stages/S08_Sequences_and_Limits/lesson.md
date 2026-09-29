# S08_Sequences_and_Limits - Lesson: Sequences and limits

## Goal
The learner writes and applies the formal epsilon-N definition of a limit, uses the algebra of limits and the Sandwich Theorem, proves monotone bounded sequences converge, and works with Cauchy sequences and completeness.

## Syllabus items taught here
- 8a - The formal (epsilon-N) definition of the limit of a sequence
- 8b - Algebra of limits; the Sandwich (Squeeze) Theorem
- 8c - Monotone convergence; bounded monotonic sequences converge
- 8d - Cauchy sequences and completeness of R

## How to teach this
Ask what it would take to convince a sceptic that 1/n really does 'approach' 0 -- for ANY tiny target, not just approximately -- leading to the epsilon-N definition. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 8a The formal (epsilon-N) definition of the limit of a sequence
The sequence (a_n) **converges** to L, written a_n -> L, if: for every epsilon > 0, there exists a natural number N such that for all n > N, |a_n - L| < epsilon. The point: however small a tolerance epsilon is demanded, eventually (past some N, which may depend on epsilon) every term is within that tolerance of L. *Example:* prove 1/n -> 0. Given epsilon > 0, choose N = 1/epsilon (or any larger integer); then for n > N, |1/n - 0| = 1/n < 1/N = epsilon, as required. This N works for that epsilon and every subsequent n, exactly satisfying the definition.

#### 8b Algebra of limits; the Sandwich (Squeeze) Theorem
**Algebra of limits**: if a_n -> A and b_n -> B, then a_n+b_n -> A+B, a_n b_n -> AB, and (if B ≠ 0) a_n/b_n -> A/B. The **Sandwich (Squeeze) Theorem**: if a_n <= c_n <= b_n for all n beyond some point, and a_n -> L, b_n -> L, then c_n -> L too. *Example:* find lim (sin n)/n. Since -1 <= sin n <= 1, we have -1/n <= (sin n)/n <= 1/n; since -1/n -> 0 and 1/n -> 0, by the Sandwich Theorem (sin n)/n -> 0.

#### 8c Monotone convergence; bounded monotonic sequences converge
A sequence is **monotone increasing** if a_n <= a_(n+1) for all n (decreasing similarly), and **bounded above** if some M has a_n <= M for all n. The **Monotone Convergence Theorem**: every bounded monotone sequence of real numbers converges (this uses the completeness of R -- it fails, for instance, working only within the rationals). *Example:* a_1 = 1, a_(n+1) = root(2 + a_n). This sequence is increasing (by induction, using a_n < 2 implies root(2+a_n) > a_n when a_n<2) and bounded above by 2; so it converges, to a limit L satisfying L = root(2+L), giving L^2-L-2=0, so L=2 (rejecting the negative root).

#### 8d Cauchy sequences and completeness of R
A sequence is **Cauchy** if for every epsilon > 0 there is N such that |a_m - a_n| < epsilon for all m,n > N (terms get arbitrarily close to EACH OTHER, not to a pre-specified limit). The **completeness** of R is exactly the statement that every Cauchy sequence of reals converges (equivalently, every Cauchy sequence in R converges to a limit that is itself real -- this can fail in Q, e.g. rational approximations to root2 are Cauchy in Q but have no rational limit). *Example:* 2965821/2097152 is not exact, but the sequence 1, 1.4, 1.41, 1.414, ... of decimal truncations of root2 is Cauchy in Q (consecutive terms get closer) yet its limit root2 is irrational -- showing Q is not complete, while R (by construction/axiom) is.

## Explicitly not here
Continuity and differentiability, which build on the sequence definition of limit, are S09.
