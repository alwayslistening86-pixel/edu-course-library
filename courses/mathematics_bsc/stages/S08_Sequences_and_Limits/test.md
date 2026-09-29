# S08_Sequences_and_Limits - Test: Sequences and limits

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Using the epsilon-N definition, prove that (2n+1)/(n+3) -> 2. [5 marks]
2. Prove, using the algebra of limits (not epsilon-N directly), that if a_n -> 3 then (2a_n+1)/(a_n-1) -> 7/2. [4 marks]
3. Show the sequence a_1=2, a_(n+1) = (a_n + 3/a_n)/2 is monotone decreasing and bounded below by root3, hence converges, and find its limit. [7 marks]
4. Explain why the rational sequence a_n defined by a_1=1, a_(n+1)=(a_n+2/a_n)/2 is Cauchy in Q but does not converge within Q. [4 marks]
5. Which are true statements about sequences of real numbers? Choose every correct option.
   A. Every convergent sequence is Cauchy
   B. Every Cauchy sequence of reals converges
   C. Every bounded sequence converges
   D. Every bounded monotone sequence converges

## Answer key (for the tutor only)
1. [5] M1 computes |a_n-2| = |2n+1-2n-6|/(n+3) = 5/(n+3); M1 sets 5/(n+3) < epsilon and solves n > 5/epsilon - 3; A1 chooses N = max(0, 5/epsilon - 3); A1 for n>N, |a_n-2|<epsilon rigorously; B1 clear concluding statement referencing the definition.
2. [4] M1 numerator 2a_n+1 -> 2(3)+1=7 by algebra of limits; A1 denominator a_n-1 -> 3-1=2 (nonzero); M1 quotient rule for limits applies since denominator limit nonzero; A1 limit = 7/2.
3. [7] M1 shows a_n^2 >= 3 for all n by induction (AM-GM type argument); A1 base case a_1=2, 4>=3; M1 inductive step uses a_(n+1)^2 - 3 = (a_n-3/a_n)^2/4 >=0; A1 so a_n >= root3 for all n (bounded below); M1 shows a_(n+1)-a_n = (3/a_n - a_n)/2 <= 0 using a_n^2>=3; A1 decreasing and bounded below, converges by Monotone Convergence; B1 limit L satisfies L=(L+3/L)/2, giving L=root3.
4. [4] M1 notes the sequence converges (in R) to root2 by the same argument as Newton's method / AM-GM; A1 so it is Cauchy (convergent sequences are always Cauchy); M1 but root2 is irrational, not in Q; A1 so, viewed as a sequence in Q, it is Cauchy but has no limit in Q, showing Q is not complete.
5. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Sequences_and_Limits` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 21 marks in all; a pass needs at least 13 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Continuity_Differentiation_and_Integration.
