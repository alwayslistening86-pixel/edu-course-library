# S01_Proof - Lesson: Proof

## Goal
The learner writes clear proofs by deduction and exhaustion, uses implies / if and only if correctly, disproves statements with a counter-example, and proves by contradiction.

## Syllabus items taught here
- 1.01a - Structure of mathematical proof: from assumptions through logical steps to a conclusion (proof by deduction and by exhaustion)
- 1.01b - Logical connectives: implies, is implied by, if and only if; language of necessary and sufficient
- 1.01c - Disproof by counter-example
- 1.01d - Proof by contradiction (including irrationality of root 2 and infinitely many primes)

## How to teach this
Ask whether checking n = 1 to 10 proves that n^2 + n + 41 is always prime, then show n = 40. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 1.01a Structure of mathematical proof: from assumptions through logical steps to a conclusion (proof by deduction and by exhaustion)
A proof starts from stated assumptions or known facts and reaches the conclusion through steps that each follow logically, ending with a concluding statement. **Proof by deduction**: work algebraically in general. *Example:* prove the sum of any three consecutive integers is a multiple of 3. Let them be n, n + 1, n + 2; the sum is 3n + 3 = 3(n + 1), a multiple of 3 because n + 1 is an integer. **Proof by exhaustion**: split into every possible case and prove each. *Example:* prove n^2 + n is even for all integers n. If n is even, n = 2m, so n^2 + n = 4m^2 + 2m = 2(2m^2 + m), even. If n is odd, n = 2m + 1, so n^2 + n = (2m + 1)(2m + 2) = 2(2m + 1)(m + 1), even. Both cases are covered, so the result holds. Always define your variables ("let n be an integer") and write a conclusion.

#### 1.01b Logical connectives: implies, is implied by, if and only if; language of necessary and sufficient
P => Q means "if P then Q" (P is **sufficient** for Q; Q is **necessary** for P). P <= Q means Q => P. P <=> Q ("P if and only if Q") means both directions hold. *Examples:* x = 3 => x^2 = 9 is true, but x^2 = 9 => x = 3 is false (x could be -3), so the correct connective is x = 3 => x^2 = 9, not <=>. For integers, "n is even <=> n^2 is even" is true in both directions. To prove an "if and only if" statement you must prove both directions separately. The symbol ∴ means "therefore" and ∈ means "is a member of" (e.g. n ∈ ℤ).

#### 1.01c Disproof by counter-example
One counter-example is enough to show that a general statement is false; a single example never proves a general statement true. *Example:* "for all real x, x^2 > x" is disproved by x = 0.5, since 0.25 < 0.5. *Example:* "2^n + 1 is prime for every positive integer n" is disproved by n = 3: 2^3 + 1 = 9 = 3 × 3. State the counter-example clearly and show explicitly why it breaks the statement.

#### 1.01d Proof by contradiction (including irrationality of root 2 and infinitely many primes)
Assume the statement is false, then deduce something impossible (a contradiction), so the assumption was wrong. *Proof that root 2 is irrational:* assume root 2 = a/b with a, b integers with no common factor. Then a^2 = 2b^2, so a^2 is even, so a is even: a = 2c. Then 4c^2 = 2b^2, so b^2 = 2c^2, so b is even too. Then a and b share the factor 2, contradicting "no common factor", so root 2 is irrational. *Infinitely many primes:* assume there are finitely many, p1, ..., pk. Let N = p1 × p2 × ... × pk + 1. N leaves remainder 1 when divided by each pi, so none of them divides N; so N is prime or has a prime factor not in the list, contradicting the list being complete. Start with "Assume, for contradiction, that ..." and finish by naming the contradiction.

## Explicitly not here
Proof using trigonometric identities is S13.
