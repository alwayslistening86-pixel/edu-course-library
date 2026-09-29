# S26_Hypothesis_Testing - Test: Hypothesis testing

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A firm claims 20% of its customers use its app. In a random sample of 25 customers, 10 use it. Test at the 5% level whether the proportion is greater than 20%. [6 marks]
2. For X ~ B(25, 0.2), find the critical region for a two-tailed test of H0: p = 0.2 at the 5% level (2.5% in each tail), and the actual significance level. [5 marks]
3. The lengths of rods are N(μ, 0.4^2) cm. The machine is set for μ = 12. A sample of 16 rods has mean 12.19 cm. Test at 5% whether μ ≠ 12. [6 marks]
4. A sample of 10 pairs has r = -0.58. The critical value for a one-tailed test at 5% with n = 10 is 0.5494. Test for negative correlation. [4 marks]
5. Explain what a 5% significance level means. [1 mark]

## Answer key (for the tutor only)
1. [6] B1 H0: p = 0.2, H1: p > 0.2; M1 X ~ B(25, 0.2); M1 P(X ≥ 10) = 1 - P(X ≤ 9); A1 0.0173; M1 compares with 0.05; A1 reject H0: evidence the proportion using the app is greater than 20%.
2. [5] M1 lower tail: largest c with P(X ≤ c) ≤ 0.025: P(X ≤ 0) = 0.0038 and P(X ≤ 1) = 0.0274; A1 lower region X ≤ 0; M1 upper tail: smallest c with P(X ≥ c) ≤ 0.025: P(X ≥ 10) = 0.0173 and P(X ≥ 9) = 0.0468; A1 upper region X ≥ 10; B1 actual significance level 0.0211.
3. [6] B1 H0: μ = 12, H1: μ ≠ 12; M1 X̄ ~ N(12, 0.4^2/16) = N(12, 0.01); M1 P(X̄ ≥ 12.19) = 0.0287; A1 compares with 0.025; A1 do not reject H0; A1 conclusion in context (insufficient evidence that the mean length has changed).
4. [4] B1 H0: ρ = 0, H1: ρ < 0; M1 compares |r| = 0.58 with 0.5494; A1 reject H0; A1 evidence of negative correlation in the population.
5. [1] B1 the probability of rejecting H0 when it is true is (at most) 0.05.

## Grading
Apply `rubric.json`'s `stage_rubrics.S26_Hypothesis_Testing` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 22 marks in all; a pass needs at least 14 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S27_Units_and_Kinematics.
