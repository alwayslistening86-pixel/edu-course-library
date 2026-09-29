# S12_Regression_Analysis_and_Econometric_Basics - Lesson: Regression analysis and econometric basics

## Goal
The learner fits and interprets a simple linear regression by ordinary least squares, interprets R-squared and residuals, tests hypotheses about a regression coefficient, and distinguishes correlation from causation including omitted variable bias.

## Syllabus items taught here
- M248-6 - Simple linear regression by OLS
- M248-7 - R-squared and residuals
- M248-8 - Hypothesis tests on regression coefficients
- M248-9 - Correlation, causation and omitted variable bias

## How to teach this
Ask why a strong positive correlation between ice cream sales and drowning deaths doesn't mean ice cream causes drowning. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### M248-6 Simple linear regression by OLS
Simple linear regression fits y = b0 + b1x + e by ordinary least squares (OLS), choosing b0, b1 to minimise the sum of squared residuals (differences between observed y and the fitted line). b1 estimates the average change in y associated with a one-unit change in x. *Example:* a regression of household spending (£) on income (£'000) gives b1 = 0.65: each additional £1,000 of income is associated with £650 more spending, on average, in this sample.

#### M248-7 R-squared and residuals
R-squared measures the proportion of the variation in y explained by the regression: R^2 = 1 - (sum of squared residuals / total sum of squares), ranging from 0 (no explanatory power) to 1 (perfect fit). *Example:* total sum of squares = 500, residual sum of squares = 120: R^2 = 1 - 120/500 = 0.76, i.e. the model explains 76% of the variation in y. A high R^2 shows good in-sample fit but does not by itself establish that the relationship is causal, correctly specified, or will hold out of sample.

#### M248-8 Hypothesis tests on regression coefficients
The estimated coefficient b1 has a standard error reflecting sampling uncertainty; the t-statistic t = b1/SE(b1) is compared against the t-distribution to test H0: the true coefficient (beta1) = 0 (no relationship) against H1: beta1 not equal to 0. If the p-value is below the chosen significance level (or |t| exceeds the critical value), the coefficient is statistically significant -- there is evidence of a relationship in the population, not just in this particular sample.

#### M248-9 Correlation, causation and omitted variable bias
Correlation measures association, not causation. Omitted variable bias arises when a variable that affects y and is also correlated with x is left out of the regression: its effect is wrongly attributed to x, biasing b1. Classic example: a regression of exam scores on private tutoring hours might show a positive coefficient partly reflecting omitted parental income/motivation (which funds tutoring and independently helps scores), not a pure causal effect of tutoring. Reverse causality (y causing x, not x causing y) and confounding third variables are the main threats economists must consider before interpreting a regression coefficient causally.

## Explicitly not here
Multiple regression and richer applied models are S13.
