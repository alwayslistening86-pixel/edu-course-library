# S03_Probability_and_Statistical_Inference - Test: Probability and statistical inference

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A discrete random variable X takes values 0,1,2,3 with probabilities 0.1,0.3,0.4,0.2. Find E[X] and Var(X). [5 marks]
2. X~N(20,25). Find P(X>27) and the value k such that P(X<k)=0.10. [5 marks]
3. A sample of n=16 from a normal population with sigma=8 has X-bar=105. Construct a 99% confidence interval for mu. [5 marks]
4. A coin is tested for fairness: H0: p=0.5, H1: p≠0.5. In 100 tosses, 62 heads occur. Test at the 5% level using a normal approximation. [6 marks]
5. Bivariate data give S_xy=45, S_xx=25, S_yy=100, n=8. Find the least-squares slope, the correlation coefficient, and interpret r^2. [5 marks]
6. Which are correctly matched (distribution: defining feature)? Choose every correct option.
   A. Binomial: fixed number of independent trials, constant success probability
   B. Poisson: mean equals variance
   C. `Normal: bounded support on [0,1]`
   D. CLT: sample mean is approximately normal for large n regardless of the population's distribution (finite variance)

## Answer key (for the tutor only)
1. [5] M1 E[X]=0(.1)+1(.3)+2(.4)+3(.2)=1.7; A1 E[X]=1.7; M1 E[X^2]=0+.3+1.6+1.8=3.7; A1 Var=3.7-1.7^2=0.81; A1 fully correct with working shown.
2. [5] M1 standardises Z=(27-20)/5=1.4; A1 P(X>27)=0.0808; M1 finds z_0.10=-1.282; A1 k=20+5(-1.282); A1 k=13.59.
3. [5] M1 z_0.005=2.576; M1 margin = z sigma/root n; A1 margin=5.15; A1 interval lower 99.85; A1 interval upper 110.15.
4. [6] M1 under H0, X~approx N(50,25); M1 z=(62-50)/5=2.4; A1 two-tailed p-value = 0.0164; A1 this is less than 0.05; A1 reject H0; B1 conclude evidence the coin is not fair.
5. [5] M1 slope b=S_xy/S_xx=1.8; A1 b=1.8; M1 r=S_xy/root(S_xx S_yy)=45/root(2500); A1 r=0.9; B1 r^2=0.81 means 81% of the variation in y is explained by the linear relationship with x.
6. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Probability_and_Statistical_Inference` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 27 marks in all; a pass needs at least 17 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Groups_and_Subgroups.
