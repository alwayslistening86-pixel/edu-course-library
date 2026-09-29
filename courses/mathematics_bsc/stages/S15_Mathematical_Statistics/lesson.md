# S15_Mathematical_Statistics - Lesson: Mathematical statistics

## Goal
The learner derives maximum likelihood estimators, discusses bias/consistency/efficiency of estimators, constructs confidence intervals via likelihood/pivotal methods, fits the general linear model by least squares/maximum likelihood, and applies chi-squared tests.

## Syllabus items taught here
- 15a - Likelihood and maximum likelihood estimation
- 15b - Properties of estimators: bias, consistency, efficiency; the Cramer-Rao bound (statement only)
- 15c - Confidence intervals via the likelihood/normal approximation and via pivotal quantities
- 15d - The general linear model; least squares as maximum likelihood under normal errors
- 15e - Chi-squared tests: goodness of fit and tests of independence in contingency tables

## How to teach this
Ask: given data and a family of candidate distributions, what makes one parameter value 'more likely' than another to have produced this exact data -- motivating the likelihood function. Work every proof and worked example with the learner line by line before revealing the next step; insist on full, rigorous justification (this is an honours-degree pure/applied mathematics course, not a procedural one). Every numerical or symbolic answer in these files was computed with sympy when the course was built.

#### 15a Likelihood and maximum likelihood estimation
The **likelihood function** L(theta) = product of f(x_i; theta) over the sample (the joint density/mass at the observed data, viewed as a function of the unknown parameter theta). The **maximum likelihood estimator (MLE)** theta-hat maximises L(theta) (equivalently, and usually more tractably, maximises the log-likelihood l(theta) = ln L(theta), since ln is increasing). *Example (Bernoulli/binomial):* for n independent Bernoulli(p) trials with x successes, L(p) = p^x (1-p)^{n-x}; l(p) = x ln p + (n-x) ln(1-p); dl/dp = x/p - (n-x)/(1-p) = 0 gives (sympy-verified) p-hat = x/n, the sample proportion.

#### 15b Properties of estimators: bias, consistency, efficiency; the Cramer-Rao bound (statement only)
An estimator theta-hat is **unbiased** if E[theta-hat] = theta (no systematic over/under-estimation); it is **consistent** if theta-hat -> theta in probability as n -> infinity (more data means the estimate settles down to the truth); given two unbiased estimators, the one with smaller variance is more **efficient**. The **Cramer-Rao lower bound** gives the smallest possible variance any unbiased estimator can achieve (stated, not derived, at this level); an estimator achieving it is called efficient. *Example:* for X-bar estimating a population mean mu from an i.i.d. sample, E[X-bar]=mu (unbiased) and Var(X-bar) = sigma^2/n -> 0 as n -> infinity (consistent, by Chebyshev's inequality).

#### 15c Confidence intervals via the likelihood/normal approximation and via pivotal quantities
A confidence interval can be built from a **pivotal quantity** -- a function of the data and theta whose distribution does not depend on theta -- by finding an interval for the pivot and inverting it to an interval for theta. *Example:* for X_1,...,X_n i.i.d. N(mu,sigma^2) with sigma UNKNOWN, T = (X-bar - mu)/(S/root n) has a t-distribution on n-1 degrees of freedom (a pivotal quantity, since its distribution does not involve mu or sigma); inverting P(-t_{alpha/2} < T < t_{alpha/2}) = 1-alpha gives the CI X-bar ± t_{alpha/2} S/root n. For large n, or when using the **likelihood-based (Wald) approximation**, theta-hat ± z_{alpha/2}/root(nI(theta-hat)) uses the (estimated) Fisher information I(theta) from the log-likelihood's curvature.

#### 15d The general linear model; least squares as maximum likelihood under normal errors
The **general linear model** y = X beta + epsilon (y an n-vector of observations, X the n x p design matrix, beta the parameters, epsilon i.i.d. errors) generalises simple linear regression to multiple predictors. The **least-squares estimator** beta-hat = (X^T X)^{-1} X^T y minimises the residual sum of squares ||y - X beta||^2. If the errors are additionally assumed N(0, sigma^2), least squares and **maximum likelihood** coincide: maximising the normal likelihood is equivalent to minimising the sum of squared residuals (since the exponent of the normal density is -(1/2sigma^2) times the sum of squares). *Example:* simple regression y = a + bx is the special case X = [1, x_i] (a column of 1s and the x-values), and (X^T X)^{-1}X^T y reduces exactly to the familiar a = ybar - b xbar, b = S_xy/S_xx formulas from S03.

#### 15e Chi-squared tests: goodness of fit and tests of independence in contingency tables
A **chi-squared goodness-of-fit test** compares observed frequencies O_i with expected frequencies E_i under a hypothesised distribution, using the statistic chi^2 = sum (O_i-E_i)^2/E_i, compared against the chi-squared distribution on (categories - 1 - estimated parameters) degrees of freedom. A **test of independence** in an r x c contingency table uses the same statistic with E_ij = (row total)(column total)/(grand total), on (r-1)(c-1) degrees of freedom. *Example:* rolling a die 60 times, expecting 10 of each face under fairness; if observed are 8,12,7,11,13,9, chi^2 = sum (O-10)^2/10 = (2.800); compared to chi-squared on 5 df, critical value at 5% is 11.070, so this value does not exceed it -- do not reject the hypothesis of fairness at 5%.

## Explicitly not here
Bayesian inference (prior/posterior distributions) is not covered by this course's frequentist statistics strand.
