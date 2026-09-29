# S06_Practical_Modern_Statistics - Lesson: Practical modern statistics

## Goal
The learner applies the binomial, Poisson and normal distributions to computing-relevant data problems, constructs confidence intervals and hypothesis tests at degree depth, fits and interprets a simple linear regression, and chooses appropriate descriptive statistics/summaries for a dataset.

## Syllabus items taught here
- 6a - Probability distributions for data analysis: binomial, Poisson and normal, applied to real data problems
- 6b - Statistical inference: confidence intervals, hypothesis testing and p-values at degree depth
- 6c - Correlation and simple linear regression: least squares, the correlation coefficient, R-squared, residuals
- 6d - Data analysis in practice: descriptive statistics, choosing an appropriate summary/visualisation for a dataset

## How to teach this
Ask the learner: if a website's server crashes on average twice a day, how would you estimate the probability it crashes exactly five times tomorrow -- which distribution is that? Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 6a Probability distributions for data analysis: binomial, Poisson and normal, applied to real data problems
**Probability distributions.** The **binomial distribution** B(n,p) models the number of successes in n independent trials each with success probability p (e.g. the number of users, out of 50, who click a button with a known 10% click-through rate); P(X=k) = C(n,k) p^k (1-p)^(n-k). The **Poisson distribution** models the number of independent events in a fixed interval given a known average rate lambda (e.g. server crashes per day, requests per second); P(X=k) = lambda^k e^{-lambda} / k!; it is the limiting case of the binomial as n grows large and p small with np held roughly constant (rare events, many trials). The **normal distribution** N(mu, sigma^2) is the symmetric bell curve fully described by its mean and standard deviation, and by the Central Limit Theorem, the distribution of a sample mean approaches normal as sample size grows, regardless of the underlying population's distribution -- the basis for most inferential statistics.
```python
from math import comb, exp, factorial

# binomial: P(exactly 6 of 50 users click, if click-through rate is 10%)
n, p, k = 50, 0.10, 6
p_binom = comb(n, k) * p**k * (1 - p)**(n - k)
print("P(X=6) binomial:", round(p_binom, 4))

# poisson: P(exactly 3 server crashes today, if average rate is 2/day)
lam, k2 = 2, 3
p_poisson = lam**k2 * exp(-lam) / factorial(k2)
print("P(X=3) poisson:", round(p_poisson, 4))
```
Output:
```
P(X=6) binomial: 0.1541
P(X=3) poisson: 0.1804
```

#### 6b Statistical inference: confidence intervals, hypothesis testing and p-values at degree depth
**Statistical inference.** A **confidence interval** for a population mean mu, from a sample of size n with sample mean x-bar and (known or estimated) standard deviation, is x-bar +/- z* (sigma/root(n)) for large n (using z*=1.96 for 95% confidence); this interval is expected to contain the true population mean in 95% of repeated samples, not 'a 95% chance the true mean is in this specific interval'. **Hypothesis testing**: state a null hypothesis H0 (no effect/no difference) and an alternative H1; choose a significance level alpha (commonly 0.05); compute a test statistic and its p-value (the probability of observing a result at least as extreme as the sample, assuming H0 is true); if p < alpha, reject H0 in favour of H1. A **Type I error** rejects a true H0 (a false positive, with probability alpha); a **Type II error** fails to reject a false H0 (a false negative).
```python
import math

# 95% CI for a sample: n=100, sample mean 4.8s page load time, sample std dev 1.2s
n, xbar, s = 100, 4.8, 1.2
se = s / math.sqrt(n)
margin = 1.96 * se
print("95% CI:", (round(xbar - margin, 3), round(xbar + margin, 3)))
```
Output:
```
95% CI: (4.565, 5.035)
```

#### 6c Correlation and simple linear regression: least squares, the correlation coefficient, R-squared, residuals
**Correlation and simple linear regression.** The **Pearson correlation coefficient** r measures the strength and direction of a *linear* relationship between two variables, ranging from -1 (perfect negative) to +1 (perfect positive), with 0 indicating no linear relationship (though a strong non-linear relationship can still exist). **Simple linear regression** fits a line y = b0 + b1.x minimising the sum of squared residuals (the *least squares* criterion); b1 is the slope, b0 the intercept. **R-squared** (the coefficient of determination) is the proportion of variance in y explained by the model (0 to 1; higher means a better linear fit, though a high R-squared does not by itself imply the relationship is causal). A **residual** is the difference between an observed value and the value the model predicts for it.
```python
xs = [1, 2, 3, 4, 5]
ys = [2.1, 3.9, 6.2, 7.8, 10.1]
n = len(xs)
xbar, ybar = sum(xs) / n, sum(ys) / n
sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
sxx = sum((x - xbar) ** 2 for x in xs)
b1 = sxy / sxx
b0 = ybar - b1 * xbar
print("slope b1 =", round(b1, 3), " intercept b0 =", round(b0, 3))
preds = [b0 + b1 * x for x in xs]
ss_res = sum((y - p) ** 2 for y, p in zip(ys, preds))
ss_tot = sum((y - ybar) ** 2 for y in ys)
print("R^2 =", round(1 - ss_res / ss_tot, 4))
```
Output:
```
slope b1 = 1.99  intercept b0 = 0.05
R^2 = 0.9973
```

#### 6d Data analysis in practice: descriptive statistics, choosing an appropriate summary/visualisation for a dataset
**Choosing a descriptive summary.** The **mean** is sensitive to outliers/skew; the **median** (middle value) is robust to outliers and better summarises skewed data (e.g. income, response times with occasional very slow outliers). **Standard deviation** summarises spread around the mean and is appropriate alongside the mean for roughly symmetric data; the **interquartile range (IQR)**, the spread of the middle 50% of data, pairs naturally with the median for skewed data and is used to define outliers (commonly, a value more than 1.5 x IQR beyond the nearest quartile). Choosing a chart follows the same logic: a **histogram** shows a single variable's distribution shape; a **scatter plot** shows the relationship between two numeric variables (motivating a correlation/regression analysis); a **box plot** compares the median/IQR/outliers of several groups side by side; a **bar chart** compares a summary statistic (e.g. count or mean) across categories, and must not be used where a line chart (showing a trend over an ordered/time axis) is actually appropriate.

## Explicitly not here
Statistical/probabilistic reasoning specific to machine learning model evaluation is S11.
