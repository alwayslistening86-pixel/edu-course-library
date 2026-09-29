# S11_Probability_and_Statistical_Inference - Test: Probability and statistical inference

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A survey of n=225 households has sample mean weekly spend £480 and population sigma=£90. Construct a 95% confidence interval for the true mean. [4 marks]
2. Explain the difference between a Type I and a Type II error, and how lowering the significance level from 5% to 1% affects the risk of each, other things equal. [4 marks]
3. n=100, p=0.4 for a binomial random variable (e.g. the share of firms reporting rising costs). Calculate the mean and standard deviation. [3 marks]
4. Explain what the Central Limit Theorem allows an economist to assume about the sampling distribution of a sample mean, even when household income itself is highly skewed. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 SE = 90/sqrt(225) = 6; M1 margin = 1.96x6 = 11.76; A1 CI = (468.24, 491.76); B1 interpretation: about 95% of such intervals, calculated this way over repeated sampling, would contain the true population mean.
2. [4] B1 Type I error: rejecting a true null hypothesis (false positive); B1 Type II error: failing to reject a false null hypothesis (false negative); B1 lowering the significance level to 1% makes it harder to reject H0, reducing the Type I error rate; B1 but, for a fixed sample size, this increases the Type II error rate (a genuine effect is now more likely to be missed).
3. [3] M1 mean = np = 100x0.4 = 40; M1 variance = np(1-p) = 100x0.4x0.6 = 24; A1 sd = 4.90.
4. [3] B1 the CLT says the sampling distribution of the sample mean is approximately normal for a sufficiently large sample size; B1 this holds regardless of the shape of the underlying population distribution (even a skewed one like income); B1 so normal-distribution-based inference (confidence intervals, hypothesis tests) remains valid for the mean, provided the sample is reasonably large.

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Probability_and_Statistical_Inference` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Regression_Analysis_and_Econometric_Basics.
