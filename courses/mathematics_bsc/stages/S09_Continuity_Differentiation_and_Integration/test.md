# S09_Continuity_Differentiation_and_Integration - Test: Continuity, differentiation and integration

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Using the epsilon-delta definition, prove that f(x)=3x-2 is continuous at x=5. [5 marks]
2. Use the Mean Value Theorem to show that for x>0, ln(1+x) < x. [5 marks]
3. Using upper and lower sums with n equal subintervals, show that the Riemann integral of f(x)=x^2 on [0,1] is 1/3. [7 marks]
4. State and prove the Fundamental Theorem of Calculus Part 1 (that F(x)=integral_a^x f(t)dt has F'(x)=f(x) for continuous f). [6 marks]
5. Give an example of a sequence of continuous functions on [0,1] converging pointwise but not uniformly to a discontinuous limit, and justify both claims briefly. [5 marks]
6. Which are correct? Choose every correct option.
   A. Differentiability implies continuity
   B. Continuity implies differentiability
   C. Every continuous function on a closed bounded interval is Riemann integrable
   D. Uniform convergence of continuous functions preserves continuity of the limit

## Answer key (for the tutor only)
1. [5] M1 given epsilon>0, wants |3x-2-13|<epsilon i.e. |3x-15|<epsilon i.e. 3|x-5|<epsilon; A1 so |x-5|<epsilon/3; M1 chooses delta=epsilon/3; A1 then |x-5|<delta implies |f(x)-f(5)|=3|x-5|<3(epsilon/3)=epsilon; B1 clear reference to the definition throughout.
2. [5] M1 lets f(t)=ln(1+t) on [0,x], continuous and differentiable; M1 by MVT there is c in (0,x) with f'(c)=(f(x)-f(0))/x, i.e. 1/(1+c) = ln(1+x)/x; A1 since c>0, 1/(1+c)<1; A1 so ln(1+x)/x < 1, i.e. ln(1+x) < x; B1 correctly handles that x>0 so multiplying by x preserves the inequality.
3. [7] M1 partitions [0,1] into n subintervals of width 1/n; M1 upper sum uses M_i=(i/n)^2 (f increasing): U_n = sum_{i=1}^n (i/n)^2(1/n) = (1/n^3)sum i^2 = (n)(n+1)(2n+1)/(6n^3); A1 simplifies and takes n->infinity: U_n -> 1/3; M1 lower sum L_n=(1/n^3)sum_{i=0}^{n-1}i^2=(n-1)n(2n-1)/(6n^3); A1 L_n -> 1/3 also; A2 since U_n and L_n both tend to 1/3, the integral equals 1/3 (states the definition being applied).
4. [6] M1 correct statement; M1 forms difference quotient (F(x+h)-F(x))/h = (1/h)integral_x^{x+h} f(t)dt; M1 uses continuity of f: for h small, f(t) is close to f(x) for t in [x,x+h]; A1 bounds the average by min/max of f on the interval, both -> f(x) as h->0 by continuity; A1 applies the Sandwich Theorem to the difference quotient; A1 concludes F'(x)=f(x).
5. [5] M1 gives f_n(x)=x^n; A1 pointwise limit f(x)=0 for x in [0,1), f(1)=1; M1 notes each f_n is continuous but f is not (jump at x=1); A1 explains uniform convergence would force the limit to be continuous (standard theorem), contradiction; A1 so convergence is pointwise but not uniform.
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Continuity_Differentiation_and_Integration` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 29 marks in all; a pass needs at least 18 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Ordinary_Differential_Equations.
