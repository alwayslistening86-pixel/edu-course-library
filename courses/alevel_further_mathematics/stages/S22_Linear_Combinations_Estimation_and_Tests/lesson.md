# S22_Linear_Combinations_Estimation_and_Tests - Lesson: Linear combinations, estimation, tests and confidence intervals

## Goal
The learner combines random variables linearly (especially normals), uses the distribution of the sample mean and the central limit theorem, finds unbiased estimates, and carries out z-tests and confidence intervals for a population mean.

## Syllabus items taught here
- 5.04a - E(aX + bY + c) and Var(aX + bY + c) for independent X and Y
- 5.04b - Linear combinations of independent normal variables are normal
- 5.05a - The distribution of the sample mean: mean μ, variance σ^2/n, approximately normal for large n (central limit theorem)
- 5.05b - Unbiased estimates of the population mean and variance
- 5.05c - Hypothesis tests for a population mean using a normal distribution (known variance, or large samples)
- 5.05d - Confidence intervals for a population mean using a normal distribution

## How to teach this
Ask whether 'X1 + X2' and '2X' have the same variance, where X1 and X2 are independent copies of X. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.04a E(aX + bY + c) and Var(aX + bY + c) for independent X and Y
E(aX + bY + c) = aE(X) + bE(Y) + c (always). If X and Y are independent, Var(aX + bY + c) = a^2 Var(X) + b^2 Var(Y); note Var(X - Y) = Var(X) + Var(Y). Distinguish X1 + X2 (two independent observations: variance 2σ^2) from 2X (one observation doubled: variance 4σ^2).

#### 5.04b Linear combinations of independent normal variables are normal
If X is normal, aX + b is normal; if X and Y are independent normals, aX + bY is normal. *Example:* apples A ~ N(150, 20^2), pears P ~ N(180, 25^2) grams, independent: P(a pear weighs more than an apple) = P(P - A > 0) with P - A ~ N(30, 1025): 0.8256. The total mass of 4 apples ~ N(600, 4 x 400).

#### 5.05a The distribution of the sample mean: mean μ, variance σ^2/n, approximately normal for large n (central limit theorem)
For a random sample of size n from a population with mean μ and variance σ^2: E(X̄) = μ, Var(X̄) = σ^2/n; X̄ is normal if the population is, and approximately normal for large n (n > 25 as a guide) whatever the population (the central limit theorem).

#### 5.05b Unbiased estimates of the population mean and variance
Unbiased estimates: x̄ = Σx/n for μ; s^2 = (Σx^2 - (Σx)^2/n)/(n - 1) for σ^2. *Example:* n = 10, Σx = 48, Σx^2 = 260: x̄ = 4.8, s^2 = (260 - 230.4)/9 = 3.289.

#### 5.05c Hypothesis tests for a population mean using a normal distribution (known variance, or large samples)
z-test for a mean using X̄ ~ N(μ0, σ^2/n): (1) normal population with known variance; (2) a large sample from any population with known variance (CLT); (3) a large sample with unknown variance, using s^2 for σ^2. *Example:* H0: μ = 50, H1: μ ≠ 50; n = 40, x̄ = 51.6, s = 4.5: z = 1.6/(4.5/root40) = 2.249; the critical values at 5% are ±1.96, so reject H0.

#### 5.05d Confidence intervals for a population mean using a normal distribution
A 95% confidence interval for μ is x̄ ± 1.96 σ/root n (use s for σ with large samples); 99% uses 2.576. *Example:* x̄ = 51.6, s = 4.5, n = 40: 51.6 ± 1.96 x 4.5/root40 = (50.21, 52.99). Interpretation: 95% of intervals constructed this way contain μ. A value outside the interval would be rejected by a two-tailed test at 5%.

## Explicitly not here
Chi-squared tests are S23.
