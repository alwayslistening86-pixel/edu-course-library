# S15_Mathematical_Statistics - Test: Mathematical statistics

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems and proofs with marks shown, plus multiple-select conceptual items. Give the whole test at once, with no hints; the learner shows full working/proof. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. For X_1,...,X_n i.i.d. Poisson(lambda), derive the MLE of lambda. [6 marks]
2. Show that X-bar is an unbiased and consistent estimator of the population mean mu, given i.i.d. samples with finite variance sigma^2. [5 marks]
3. A sample of n=10 from a normal population gives sample mean 24.6 and sample standard deviation 3.2. Construct a 95% confidence interval for mu using the t-distribution (t_{0.025,9}=2.262). [5 marks]
4. Explain why, under normally distributed errors, the least-squares estimator in the general linear model coincides with the maximum likelihood estimator. [5 marks]
5. A 2x2 contingency table of smoking status (yes/no) vs disease status (yes/no) has observed counts 30,70 / 10,90 (rows: smoker/non-smoker, columns: disease/no disease), n=200. Test independence at 5% (critical value chi^2_{0.05,1}=3.841). [7 marks]
6. Which are true statements about estimators? Choose every correct option.
   A. An unbiased estimator always has the smallest possible variance
   B. Consistency concerns behaviour as sample size n -> infinity
   C. Maximum likelihood and least-squares estimators coincide under normal errors in the linear model
   D. The sample mean is always the MLE of the population mean, for any distribution

## Answer key (for the tutor only)
1. [6] M1 likelihood L(lambda) = product e^{-lambda}lambda^{x_i}/x_i!; M1 log-likelihood l(lambda) = -n lambda + (sum x_i) ln lambda - sum ln(x_i!); M1 dl/dlambda = -n + (sum x_i)/lambda; A1 sets to 0: lambda-hat = (sum x_i)/n = xbar; A1 checks second derivative -(sum x_i)/lambda^2 < 0, confirming a maximum; A1 clear final statement: MLE is the sample mean.
2. [5] M1 E[X-bar] = E[(1/n)sum X_i] = (1/n)sum E[X_i] = (1/n)(n mu) = mu; A1 unbiased confirmed; M1 Var(X-bar) = (1/n^2)sum Var(X_i) = sigma^2/n (independence used); A1 Var(X-bar) -> 0 as n -> infinity; A1 by Chebyshev's inequality, this convergence of variance to 0 (with unbiasedness) implies convergence in probability to mu, i.e. consistency.
3. [5] M1 uses X-bar ± t(S/root n); M1 S/root n = 1.012; A1 margin = 2.262(1.0119) = 2.289; A1 interval lower 22.311; A1 interval upper 26.889.
4. [5] M1 writes the normal likelihood for errors epsilon_i ~ N(0,sigma^2): L(beta) proportional to exp(-(1/(2sigma^2)) sum(y_i - x_i^T beta)^2); M1 log-likelihood l(beta) = const - (1/(2sigma^2)) sum(y_i-x_i^T beta)^2; A1 maximising l(beta) over beta is equivalent to MINIMISING sum(y_i-x_i^T beta)^2 (since the coefficient is negative); A1 that sum of squares is exactly the least-squares objective; A1 so the two estimators are identical, for any sigma^2.
5. [7] M1 row totals 100,100; column totals 40,160; M1 expected E_11=100(40)/200=20, E_12=100(160)/200=80, E_21=20, E_22=80; A1 all four expected values correct; M1 chi^2 = (30-20)^2/20+(70-80)^2/80+(10-20)^2/20+(90-80)^2/80; A1 = 12.500; A1 this exceeds 3.841; B1 reject independence: evidence of association between smoking and disease at 5%.
6. Correct: B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_Mathematical_Statistics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 29 marks in all; a pass needs at least 18 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
