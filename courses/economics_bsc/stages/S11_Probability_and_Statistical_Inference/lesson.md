# S11_Probability_and_Statistical_Inference - Lesson: Probability and statistical inference

## Goal
The learner works with random variables and probability distributions (binomial, normal), the sampling distribution of the mean and the Central Limit Theorem, constructs confidence intervals, and carries out hypothesis tests including comparing two means -- the statistical toolkit economists use to analyse data (Analysing Data).

## Syllabus items taught here
- M248-1 - Random variables and probability distributions
- M248-2 - Sampling distributions and the Central Limit Theorem
- M248-3 - Confidence intervals
- M248-4 - Hypothesis testing, Type I/II errors and p-values
- M248-5 - The two-sample t-test

## How to teach this
Ask how a pollster can claim a survey of 1,000 people tells them something reliable about 50 million voters. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### M248-1 Random variables and probability distributions
A random variable's probability distribution describes the likelihood of each possible value. The binomial distribution models the number of successes in n independent trials each with success probability p: mean = np, variance = np(1-p). *Example:* n=100, p=0.3: mean = 30, variance = 21, standard deviation = 4.58. The normal distribution, characterised by its mean mu and standard deviation sigma, is used to model many continuous economic variables and, via the Central Limit Theorem, sample means generally.

#### M248-2 Sampling distributions and the Central Limit Theorem
The Central Limit Theorem: for a large enough sample size n, the sampling distribution of the sample mean is approximately normal, with mean equal to the population mean mu and standard error sigma/sqrt(n), regardless of the shape of the underlying population distribution. This is why inference based on the normal distribution is valid even when the underlying data (e.g. household income) is skewed, provided the sample is large enough. *Example:* population sigma = £8,000, n=64: standard error = 8000/sqrt(64) = £1000.

#### M248-3 Confidence intervals
A confidence interval gives a range of plausible values for a population parameter. For a large sample, a 95% CI for the mean is x-bar +/- 1.96 x (sigma/sqrt(n)). *Example:* sample mean £32,000, sigma = £6,000, n=100: standard error = 600, margin = 1.96 x 600 = £1176; 95% CI = (£30824, £33176). Interpretation: if we repeated the sampling procedure many times, about 95% of such intervals would contain the true population mean -- it is not a statement about the probability the true mean lies in this one particular interval.

#### M248-4 Hypothesis testing, Type I/II errors and p-values
Hypothesis testing: state a null hypothesis H0 (typically 'no effect' or 'no difference') and an alternative H1, choose a significance level (commonly 5%), compute a test statistic from the sample, and compare it (or its p-value) against the critical value. A Type I error is rejecting a true H0 (false positive); a Type II error is failing to reject a false H0 (false negative) -- there is a trade-off between them for a fixed sample size. The p-value is the probability of observing a test statistic at least as extreme as the one obtained, if H0 were true; reject H0 if the p-value is below the chosen significance level.

#### M248-5 The two-sample t-test
A t-test compares means when the population standard deviation is unknown (using the sample standard deviation instead) or samples are small; a two-sample t-test compares the means of two independent groups, e.g. testing whether average wages differ between two regions. Test statistic t = (x-bar1 - x-bar2)/SE(difference); this is compared against the t-distribution's critical value (which depends on degrees of freedom) rather than the normal distribution's, because using the sample standard deviation introduces extra uncertainty, especially in small samples.

## Explicitly not here
Regression analysis is S12.
