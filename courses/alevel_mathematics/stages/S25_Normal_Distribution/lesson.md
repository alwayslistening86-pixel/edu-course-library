# S25_Normal_Distribution - Lesson: The normal distribution

## Goal
The learner uses the normal distribution as a model, finds probabilities and inverse values, relates it to histograms, and chooses between binomial and normal models, including the normal approximation to a binomial.

## Syllabus items taught here
- 2.04d - Using np and npq to choose a normal approximation to a binomial
- 2.04e - The normal distribution as a model
- 2.04f - Finding normal probabilities and inverse normal values
- 2.04g - Links between the normal distribution, histograms, mean and standard deviation
- 2.04h - Selecting an appropriate distribution for a context (binomial or normal)

## How to teach this
Ask what shape you would expect for a histogram of adult heights, and why. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 2.04d Using np and npq to choose a normal approximation to a binomial
B(n, p) can be approximated by N(np, np(1 - p)) when n is large and p is not too close to 0 or 1 (np > 5 and n(1 - p) > 5 is a common guide). Use a continuity correction: P(X ≤ 20) becomes P(Y < 20.5). *Example:* X ~ B(100, 0.4): Y ~ N(40, 24); P(X ≤ 35) ≈ P(Y < 35.5) = 0.1792 (exact binomial 0.1795).

#### 2.04e The normal distribution as a model
X ~ N(μ, σ^2) is a continuous, symmetric, bell-shaped distribution with mean μ and standard deviation σ. About 68% of values lie within 1σ of μ, 95% within 2σ and 99.7% within 3σ. Points of inflection of the curve are at μ ± σ. It suits continuous data clustered symmetrically around a mean (heights, measurement errors).

#### 2.04f Finding normal probabilities and inverse normal values
Use the calculator's normal functions. *Example:* X ~ N(50, 8^2): P(X < 60) = 0.8944; P(45 < X < 55) = 0.4680; P(X > a) = 0.1 gives a = 60.25. Standardising: Z = (X - μ)/σ ~ N(0, 1). Finding unknown μ or σ: P(X < 30) = 0.2 with σ = 5 means (30 - μ)/5 = -0.8416, so μ = 34.21. With two conditions, form simultaneous equations in μ and σ.

#### 2.04g Links between the normal distribution, histograms, mean and standard deviation
A histogram of normally distributed data is roughly symmetric and bell-shaped; the mean, median and mode coincide; about 95% of the data lies within 2 standard deviations. Use these to judge whether a normal model is reasonable (e.g. from summary statistics: if mean - 2sd would be negative for a quantity that can't be, the model is doubtful).

#### 2.04h Selecting an appropriate distribution for a context (binomial or normal)
Choose the distribution from the context and justify it: binomial for a count of successes in a fixed number of independent trials with constant probability; normal for a continuous measurement that is symmetric about a mean. Neither fits a skewed continuous variable (such as income) well.

## Explicitly not here
Hypothesis tests are S26.
