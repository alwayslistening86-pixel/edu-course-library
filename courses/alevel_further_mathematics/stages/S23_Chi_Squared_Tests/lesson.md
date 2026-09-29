# S23_Chi_Squared_Tests - Lesson: Chi-squared tests

## Goal
The learner carries out chi-squared tests for independence in contingency tables and goodness-of-fit tests for given ratios, uniform, binomial, Poisson and other distributions, with correct degrees of freedom and expected-frequency rules.

## Syllabus items taught here
- 5.06a - Chi-squared test for independence in a contingency table
- 5.06b - Fitting a distribution given by a ratio, proportion or discrete uniform distribution
- 5.06c - Fitting other discrete and continuous distributions
- 5.06d - Chi-squared goodness-of-fit tests with the correct degrees of freedom

## How to teach this
Ask how different observed and expected counts have to be before you suspect a die is biased. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.06a Chi-squared test for independence in a contingency table
Test statistic X^2 = Σ (O - E)^2/E. For an r x c contingency table, E = (row total x column total)/grand total, and ν = (r - 1)(c - 1). H0: the variables are independent. *Example:* observed [[30, 20], [20, 30]]: all E = 25, X^2 = 4 x 25/25 = 4.00, ν = 1; the 5% critical value is 3.841, so reject H0: there is evidence of association. Combine cells so that every expected frequency is at least 5 (reduce ν accordingly). Interpret by comparing O with E in the largest contributions.

#### 5.06b Fitting a distribution given by a ratio, proportion or discrete uniform distribution
Goodness of fit to a given ratio or uniform distribution: E = total x hypothesised proportion. ν = number of cells - 1. *Example:* a die rolled 120 times: E = 20 in each of 6 cells, ν = 5.

#### 5.06c Fitting other discrete and continuous distributions
Fitting other distributions: binomial, Poisson, geometric or a given continuous distribution. If a parameter (e.g. λ) is estimated from the data, subtract one more degree of freedom: ν = cells - 1 - parameters estimated. *Example:* fitting Po(λ) with λ estimated from the sample, after combining to 5 cells: ν = 3.

#### 5.06d Chi-squared goodness-of-fit tests with the correct degrees of freedom
Compare X^2 with the chi-squared critical value (tables provided) or use a p-value. *Example:* ν = 3 at 5%: critical value 7.815. Reject H0 if X^2 exceeds it: the data do not fit the model. Mention which cells contribute most.

## Explicitly not here
Non-parametric tests are S24.
