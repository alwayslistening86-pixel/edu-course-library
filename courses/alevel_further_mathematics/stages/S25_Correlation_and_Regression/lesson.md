# S25_Correlation_and_Regression - Lesson: Correlation and regression

## Goal
The learner calculates and tests the PMCC and Spearman's rank coefficient, chooses between them, understands coding effects, and calculates, uses and critiques the regression line of y on x.

## Syllabus items taught here
- 5.08a - Calculating the PMCC from raw or summarised data
- 5.08b - Correlation coefficients are unaffected by linear coding
- 5.08c - The PMCC as a measure of linear fit
- 5.08d - Hypothesis tests using the PMCC (critical value or p-value)
- 5.08e - Spearman's rank correlation coefficient
- 5.08f - Hypothesis test for association using Spearman's coefficient
- 5.08g - Choosing between the PMCC and Spearman's coefficient
- 5.09a - Independent (controlled) and dependent (response) variables
- 5.09b - Least squares and regression lines
- 5.09c - The regression line of y on x from raw or summarised data
- 5.09d - Effect of linear coding on a regression line
- 5.09e - Using a regression line for estimation, and the uncertainty of the estimates

## How to teach this
Ask whether a perfect curved relationship could have a PMCC below 1, and what Spearman's coefficient would say. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.08a Calculating the PMCC from raw or summarised data
r = S_xy / root(S_xx S_yy), where S_xx = Σx^2 - (Σx)^2/n, S_yy likewise and S_xy = Σxy - ΣxΣy/n. *Example:* x = [2, 4, 5, 7, 8, 10], y = [5, 9, 10, 15, 16, 21]: r = 0.9960.

#### 5.08b Correlation coefficients are unaffected by linear coding
Linear coding (u = (x - a)/b with b > 0) doesn't change r (a negative b reverses its sign). Spearman's coefficient is also unchanged.

#### 5.08c The PMCC as a measure of linear fit
r measures how close points lie to a straight line: ±1 perfect, 0 no linear relationship. It is sensitive to outliers and meaningless for clearly non-linear data.

#### 5.08d Hypothesis tests using the PMCC (critical value or p-value)
Test H0: ρ = 0 against H1: ρ > 0, < 0 or ≠ 0 by comparing r with the tabulated critical value for n and the significance level (or a p-value). Assumes a bivariate normal distribution.

#### 5.08e Spearman's rank correlation coefficient
Spearman's r_s = 1 - 6Σd^2/(n(n^2 - 1)), where d is the difference in ranks (no ties). It measures monotonic association. *Example:* for the data above, the ranks agree exactly, so r_s = 1.

#### 5.08f Hypothesis test for association using Spearman's coefficient
Test for association with r_s using tabulated critical values; this is non-parametric (no assumptions about the population distribution). H0: no association; H1: positive (or negative, or any) association.

#### 5.08g Choosing between the PMCC and Spearman's coefficient
Use the PMCC for linear correlation when the data look bivariate normal (an elliptical scatter); use Spearman's for ranked data, non-linear but monotonic relationships, or when normality is doubtful.

#### 5.09a Independent (controlled) and dependent (response) variables
The independent (explanatory, controlled) variable is set or chosen by the experimenter (x); the dependent (response) variable is measured (y).

#### 5.09b Least squares and regression lines
The least squares regression line of y on x minimises the sum of the squares of the vertical distances (residuals) from the points to the line. It passes through (x̄, ȳ).

#### 5.09c The regression line of y on x from raw or summarised data
y = a + bx with b = S_xy/S_xx and a = ȳ - bx̄. *Example:* for the data above, y = 0.810 + 1.976x.

#### 5.09d Effect of linear coding on a regression line
If x = (u - a)/b etc., find the regression line in the coded variables and substitute to get it in the original variables.

#### 5.09e Using a regression line for estimation, and the uncertainty of the estimates
Use the line to estimate y for a given x within the data range (interpolation is reliable if r is close to ±1); extrapolation beyond the data is unreliable. *Example:* at x = 6, y ≈ 12.67. The regression of y on x must not be used to predict x from y. Residual = observed - predicted.

## Explicitly not here
Mechanics begins in S26.
