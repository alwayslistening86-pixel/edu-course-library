# S01_Complex_Numbers_Algebra_and_Series - Test: Complex numbers, algebra and series

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Find all solutions of z^4 = -16, giving answers in the form a+bi. [6 marks]
2. Use De Moivre's theorem to express sin(3 theta) in terms of sin theta. [5 marks]
3. Factorise x^4 + 4 completely over C, then over R. [6 marks]
4. Determine whether sum n!/n^n converges, using the ratio test. [4 marks]
5. Find the Maclaurin series of ln(1+x) up to and including the x^3 term, and state its radius of convergence. [4 marks]
6. Which of the following are true for a non-real root z of a real polynomial p? Choose every correct option.
   A. The complex conjugate of z is also a root of p
   B. z must have modulus 1
   C. p has even degree
   D. z can be written r e^{i theta} for some real r>0 and theta

## Answer key (for the tutor only)
1. [6] M1 writes -16 = 16 cis(pi); M1 fourth roots have modulus 2; A1 arguments (pi+2k pi)/4, k=0..3; A3 the four roots root2(1+i), root2(-1+i), root2(-1-i), root2(1-i) (one mark each pair, allow equivalent forms).
2. [5] M1 expands (cos theta + i sin theta)^3; M1 takes the imaginary part; A1 3cos^2(theta)sin(theta) - sin^3(theta); M1 uses cos^2=1-sin^2; A1 sin(3 theta) = 3 sin theta - 4 sin^3 theta.
3. [6] M1 finds roots by solving x^4=-4 (modulus root2, arguments pi/4+k pi/2); A2 four complex roots 1+i, -1+i, -1-i, 1-i (or equivalent); M1 over R pairs conjugates; A2 x^4+4 = (x^2-2x+2)(x^2+2x+2).
4. [4] M1 forms the ratio a_(n+1)/a_n = n^n/(n+1)^n = (n/(n+1))^n = 1/(1+1/n)^n; A1 this tends to 1/e as n -> infinity; A1 1/e < 1; A1 so the series converges.
5. [4] M1 differentiates repeatedly or recalls the series; A2 x - x^2/2 + x^3/3; A1 radius of convergence 1.
6. Correct: A, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Complex_Numbers_Algebra_and_Series` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 26 marks in all; a pass needs at least 16 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Multivariable_Calculus.
