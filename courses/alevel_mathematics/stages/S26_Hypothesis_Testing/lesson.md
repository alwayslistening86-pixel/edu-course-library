# S26_Hypothesis_Testing - Lesson: Hypothesis testing

## Goal
The learner uses the language of hypothesis testing, carries out binomial tests for a proportion, normal tests for a mean with known variance, and tests for correlation using the PMCC, interpreting each in context.

## Syllabus items taught here
- 2.05a - Language of hypothesis testing: hypotheses, significance level, test statistic, critical value and region, acceptance region, p-value
- 2.05b - Hypothesis test for a binomial proportion, interpreted in context
- 2.05c - Inference from a sample; the significance level as the probability of wrongly rejecting H0
- 2.05d - The sample mean as a random variable: X-bar ~ N(mu, sigma^2/n)
- 2.05e - Hypothesis test for the mean of a normal distribution with known variance
- 2.05f - Pearson's product-moment correlation coefficient as a measure of linear fit
- 2.05g - Hypothesis test for zero correlation using the PMCC (critical value or p-value)

## How to teach this
Ask: if a coin gives 8 heads in 10 tosses, is it biased? How unlikely would that have to be before you'd say so? Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 2.05a Language of hypothesis testing: hypotheses, significance level, test statistic, critical value and region, acceptance region, p-value
**Null hypothesis H0**: the parameter has its assumed value (p = 0.3). **Alternative H1**: what you suspect (p > 0.3 one-tailed, p ≠ 0.3 two-tailed). **Significance level**: the threshold probability (5%). **Test statistic**: the value computed from the sample. **Critical region**: the values that lead to rejecting H0; **critical value**: its boundary; **acceptance region**: the rest. **p-value**: the probability, assuming H0, of a result at least as extreme as the one observed. **Actual significance level**: for discrete tests, the probability of landing in the critical region, usually a bit below the nominal level.

#### 2.05b Hypothesis test for a binomial proportion, interpreted in context
*Example:* a dice is thought to show six too often. 30 rolls give 9 sixes. H0: p = 1/6; H1: p > 1/6. Under H0, X ~ B(30, 1/6); P(X ≥ 9) = 0.0506 > 0.05, so do not reject H0: there is insufficient evidence at the 5% level that the dice is biased towards six. Critical region: the smallest c with P(X ≥ c) ≤ 0.05 is c = 10, since P(X ≥ 10) = 0.0197. For two-tailed tests, put half the significance level in each tail. Conclusions must be non-definite and in context ("there is evidence to suggest...", never "this proves...").

#### 2.05c Inference from a sample; the significance level as the probability of wrongly rejecting H0
A test uses a sample to infer about a population, so it can be wrong. The significance level is the probability of rejecting H0 when it is actually true (a false alarm). Lowering it makes a false alarm less likely but makes it harder to detect a genuine change.

#### 2.05d The sample mean as a random variable: X-bar ~ N(mu, sigma^2/n)
If X ~ N(μ, σ^2), the mean of a random sample of size n is itself a random variable: X̄ ~ N(μ, σ^2/n). Larger samples give a more tightly concentrated sample mean (standard error σ/root n).

#### 2.05e Hypothesis test for the mean of a normal distribution with known variance
*Example:* bags are labelled as having mean mass 500 g, with σ = 8 g. A sample of 25 bags has mean 496.5 g. Test at 5% whether the mean is lower. H0: μ = 500; H1: μ < 500. Under H0, X̄ ~ N(500, 8^2/25). P(X̄ ≤ 496.5) = 0.0144 < 0.05, so reject H0: there is evidence at the 5% level that the mean mass is below 500 g. Equivalently, the critical value is 497.37 g, and 496.5 lies below it.

#### 2.05f Pearson's product-moment correlation coefficient as a measure of linear fit
Pearson's product-moment correlation coefficient r measures how close the points lie to a straight line: r = 1 is perfect positive, r = -1 perfect negative, r = 0 no linear correlation. It's found on the calculator. It is only meaningful for roughly linear, bivariate data; it says nothing about causation.

#### 2.05g Hypothesis test for zero correlation using the PMCC (critical value or p-value)
Test for correlation in the population (ρ). H0: ρ = 0; H1: ρ > 0, ρ < 0 or ρ ≠ 0. Compare the sample r with the critical value for the sample size and significance level (from tables provided), or use a p-value. *Example:* n = 12, r = 0.62, one-tailed test for positive correlation at 5%: the critical value is 0.4973, and 0.62 > 0.4973, so reject H0: there is evidence of positive correlation in the population. The test assumes the data come from a bivariate normal distribution.

## Explicitly not here
Mechanics starts in S27.
