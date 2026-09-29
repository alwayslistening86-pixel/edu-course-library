# S03_Probability_and_Statistical_Inference - Lesson: Probability and statistical inference

## Goal
The learner works with expectation/variance of random variables, uses the binomial, Poisson and normal distributions and the Central Limit Theorem, constructs confidence intervals, carries out hypothesis tests, and fits a simple linear regression.

## Syllabus items taught here
- 3a - Discrete and continuous random variables; expectation and variance
- 3b - The binomial, Poisson and normal distributions as models; the Central Limit Theorem
- 3c - Point estimation, confidence intervals and the sampling distribution of the mean
- 3d - Hypothesis testing: null/alternative hypotheses, significance level, Type I/II error, p-values
- 3e - Simple linear regression and the least-squares line

## How to teach this
Ask why the sample mean of many dice rolls is close to 3.5 even though no single roll is -- introducing the Central Limit Theorem informally. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 3a Discrete and continuous random variables; expectation and variance
For a discrete random variable X with P(X=x_i)=p_i, E[X] = sum x_i p_i and Var(X) = E[X^2] - (E[X])^2. For continuous X with density f(x), E[X] = integral x f(x) dx. Linearity: E[aX+b] = aE[X]+b, Var(aX+b) = a^2 Var(X). *Example:* a fair die has E[X] = (1+2+...+6)/6 = 3.5, E[X^2] = (1+4+9+16+25+36)/6 = 91/6, so Var(X) = 91/6 - 12.25 = 35/12 ≈ 2.917.

#### 3b The binomial, Poisson and normal distributions as models; the Central Limit Theorem
**Binomial** B(n,p): number of successes in n independent trials with success probability p; E[X]=np, Var(X)=np(1-p). **Poisson** Po(lambda): models rare events over a fixed interval; E[X]=Var(X)=lambda; the limit of B(n,p) as n -> infinity, p -> 0 with np = lambda fixed. **Normal** N(mu, sigma^2): the continuous bell-curve model; by the **Central Limit Theorem**, the sample mean of n i.i.d. observations (any distribution, finite variance) is approximately N(mu, sigma^2/n) for large n. *Example:* if claims arrive at rate 4 per hour (Poisson), P(exactly 2 in an hour) = e^{-4} 4^2/2! ≈ 0.147.

#### 3c Point estimation, confidence intervals and the sampling distribution of the mean
A **point estimate** of a parameter uses sample data (e.g. sample mean X-bar estimates population mean mu). By the CLT, X-bar ~approx N(mu, sigma^2/n) for large n, so a (1-alpha) **confidence interval** for mu (sigma known) is X-bar ± z_(alpha/2) sigma/root(n). *Example:* n=25, X-bar=41.2, sigma=3: a 95% CI uses z=1.96, margin = 1.96(3)/5 ≈ 1.176, giving (40.024, 42.376). With sigma unknown, replace sigma with the sample standard deviation s and z with the t-distribution's critical value on n-1 degrees of freedom.

#### 3d Hypothesis testing: null/alternative hypotheses, significance level, Type I/II error, p-values
A hypothesis test sets up H0 (no effect/status quo) and H1 (the claim being investigated), chooses a significance level alpha (often 0.05), computes a test statistic and compares it (or its p-value) with alpha. A **Type I error** rejects a true H0 (probability alpha); a **Type II error** fails to reject a false H0. *Example:* H0: mu=50 vs H1: mu>50, with X-bar=52.3, sigma=6, n=30. Test statistic z = (X-bar - mu0)/(sigma/root n) = 2.100; p-value = P(Z > 2.100) ≈ 0.0179, which is less than 0.05, so H0 is rejected at the 5% level: there is evidence mu > 50.

#### 3e Simple linear regression and the least-squares line
Simple linear regression fits y = a + bx to (x_i, y_i) data by **least squares**, minimising sum(y_i - a - bx_i)^2. The slope b = S_xy/S_xx where S_xy = sum(x_i-xbar)(y_i-ybar) and S_xx = sum(x_i-xbar)^2; the intercept a = ybar - b xbar. The correlation coefficient r measures the strength of the linear association (-1 <= r <= 1); r^2 is the proportion of variance in y explained by the linear model in x. *Example:* for data with S_xy=24, S_xx=10, xbar=5, ybar=12: b=2.4, a=12-2.4(5)=0, so the fitted line is y=2.4x.

## Explicitly not here
Multiple regression and the general linear model with matrix formulation is S15 (Mathematical Statistics).
