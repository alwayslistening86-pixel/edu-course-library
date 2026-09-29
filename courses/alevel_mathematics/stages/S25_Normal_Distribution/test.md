# S25_Normal_Distribution - Test: The normal distribution

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. The masses of apples are modelled as N(150, 20^2) grams. Find (a) the probability an apple weighs more than 180 g, (b) the proportion between 130 g and 160 g, (c) the mass exceeded by 90% of apples. [6 marks]
2. X ~ N(μ, σ^2) with P(X < 35) = 0.1 and P(X > 60) = 0.05. Find μ and σ. [5 marks]
3. X ~ B(60, 0.5). Use a normal approximation to estimate P(X ≥ 35), justifying its use. [4 marks]
4. The times people spend in a shop have mean 12 minutes and standard deviation 9 minutes. Explain why a normal model is unsuitable. [2 marks]

## Answer key (for the tutor only)
1. [6] M1 standardises or uses calculator; A1 0.0668; M1 difference of cumulative values; A1 0.5328; M1 inverse normal for 0.1; A1 124.4 g.
2. [5] M1 (35 - μ)/σ = -1.2816; M1 (60 - μ)/σ = 1.6449; M1 solves simultaneously; A1 σ = 8.54; A1 μ = 45.95.
3. [4] B1 np = n(1 - p) = 30 > 5, p = 0.5 so symmetric; M1 N(30, 15); M1 continuity correction P(Y > 34.5); A1 0.1226.
4. [2] M1 mean - 2sd is negative (-6); A1 times cannot be negative, so the distribution must be skewed, not normal.

## Grading
Apply `rubric.json`'s `stage_rubrics.S25_Normal_Distribution` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S26_Hypothesis_Testing.
