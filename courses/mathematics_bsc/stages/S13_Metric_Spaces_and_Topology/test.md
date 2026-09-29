# S13_Metric_Spaces_and_Topology - Test: Metric spaces and topology

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Prove that the discrete metric d(x,y) = 0 if x=y, 1 otherwise, satisfies all three metric axioms. [5 marks]
2. In C[0,1] with the sup-norm metric, let f(x)=x^2 and g(x)=x. Find d(f,g). [4 marks]
3. Find the interior, closure and boundary of A = {(x,y) in R^2 : x^2+y^2 <= 1} \ {(0,0)} (the closed unit disc with the origin removed). [6 marks]
4. Use sequential continuity to prove f(x,y)=xy is continuous at every point of R^2. [5 marks]
5. Explain why (0,1] is not compact in R, by exhibiting an open cover with no finite subcover. [4 marks]
6. Which are true (X a metric space)? Choose every correct option.
   A. A set can be neither open nor closed
   B. A set can be both open and closed
   C. Every compact subset of R^n is closed and bounded
   D. Every closed and bounded subset of every metric space is compact

## Answer key (for the tutor only)
1. [5] M1 non-negativity and d(x,y)=0 iff x=y: true by definition; A1 symmetry: clear from the definition (same value for (x,y) and (y,x)); M1 triangle inequality: if x=z, d(x,z)=0<=d(x,y)+d(y,z) trivially; M1 if x≠z, d(x,z)=1, and at least one of d(x,y),d(y,z) must be 1 (else x=y=z, contradiction); A1 so d(x,y)+d(y,z)>=1=d(x,z), confirming the inequality in all cases.
2. [4] M1 d(f,g)=sup|x^2-x| on [0,1]; M1 h(x)=x-x^2 (positive on (0,1)), h'(x)=1-2x=0 at x=1/2; A1 h(1/2)=1/2-1/4=1/4; A1 d(f,g)=1/4.
3. [6] M1 interior: every point with 0<x^2+y^2<1 has a small ball inside A; A1 interior = {0<x^2+y^2<1} (open disc minus origin); M1 closure: adds back the origin (a limit point of A) and the boundary circle; A1 closure = {x^2+y^2<=1} (full closed disc, including the origin); M1 boundary = closure minus interior; A1 boundary = the unit circle union {(0,0)}.
4. [5] M1 takes any sequence (x_n,y_n) -> (a,b); A1 so x_n->a and y_n->b (componentwise convergence in the Euclidean metric); M1 by the algebra of limits for real sequences, x_n y_n -> ab; A1 i.e. f(x_n,y_n) -> f(a,b); B1 since this holds for every convergent sequence, f is continuous at (a,b), and (a,b) was arbitrary.
5. [4] M1 proposes the cover {(1/n, 2) : n=1,2,3,...} (each an open interval, union covers (0,1]); A1 confirms every point of (0,1] lies in some (1/n,2); M1 argues any finite subcollection has a largest 1/n, say 1/N, so misses points in (0,1/N]; A1 so no finite subcover exists, confirming (0,1] is not compact (consistent with Heine-Borel: it is bounded but not closed).
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Metric_Spaces_and_Topology` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 25 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Complex_Analysis.
