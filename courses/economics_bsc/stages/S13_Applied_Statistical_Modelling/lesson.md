# S13_Applied_Statistical_Modelling - Lesson: Applied statistical modelling

## Goal
The learner extends simple regression to multiple regression with ceteris paribus interpretation, recognises multicollinearity and heteroscedasticity from diagnostics, uses dummy variables, is introduced to logistic regression for binary outcomes, and identifies trend, seasonality and autocorrelation in time series (Applied Statistical Modelling).

## Syllabus items taught here
- M348-1 - Multiple regression and ceteris paribus interpretation
- M348-2 - Multicollinearity and heteroscedasticity
- M348-3 - Dummy variables
- M348-4 - Logistic regression for binary outcomes
- M348-5 - Trend, seasonality and autocorrelation in time series

## How to teach this
Ask why an economist studying the gender pay gap needs to control for education and experience before comparing raw average pay. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### M348-1 Multiple regression and ceteris paribus interpretation
Multiple regression extends simple regression to several explanatory variables: y = b0 + b1x1 + b2x2 + ... + e. Each coefficient bi is interpreted ceteris paribus -- the average change in y for a one-unit change in xi, holding all other included variables constant. This matters because it lets an economist separate the effect of one factor from others that are correlated with it. *Example:* a wage regression wage = b0 + b1(education) + b2(experience), with b1 = 1.8: an extra year of education is associated with £1.80/hour higher wages, holding experience fixed -- unlike a simple regression of wage on education alone, which would also pick up any correlation between education and experience.

#### M348-2 Multicollinearity and heteroscedasticity
Model diagnostics check whether OLS assumptions hold. Multicollinearity: two or more explanatory variables are highly correlated with each other, making it hard to separate their individual effects (large standard errors, unstable coefficients) even if the overall model fits well. Heteroscedasticity: the variance of the error term is not constant across observations (e.g. errors in a spending regression might grow with income); it doesn't bias the coefficients but makes the standard errors (and hence significance tests) unreliable unless corrected (e.g. robust standard errors). Residual plots (residuals against fitted values or against each x) are the standard way to spot these issues visually.

#### M348-3 Dummy variables
A dummy (indicator) variable takes the value 1 for one category and 0 otherwise, letting a regression include categorical information (e.g. sex, region, before/after a policy change). In wage = b0 + b1(education) + b2(female), where female=1 for women and 0 for men, b2 estimates the average wage gap between women and men holding education constant. *Example:* b2 = -2.5: women earn on average £2.50/hour less than men with the same education in this sample -- this is an association conditional on the included controls, not necessarily the full causal effect of discrimination, since other omitted factors (e.g. sector, hours) may still differ systematically.

#### M348-4 Logistic regression for binary outcomes
Generalised linear models extend regression beyond continuous outcomes. Logistic regression models a binary outcome (e.g. whether an individual is in the labour force, 1 or 0) as a function of explanatory variables via the logistic function, giving a predicted probability between 0 and 1 rather than an unbounded linear prediction; coefficients are typically interpreted via odds ratios (how the odds of the outcome change with each explanatory variable) rather than as a direct marginal effect on the probability, because the relationship between x and the probability is non-linear (an S-shaped curve).

#### M348-5 Trend, seasonality and autocorrelation in time series
A time series is a sequence of observations over time (e.g. quarterly GDP). Trend is the long-run direction; seasonality is a regular within-year pattern (e.g. retail sales rising every December); autocorrelation is correlation between a series and its own past values (today's inflation being related to last quarter's). Naive forecasting methods extrapolate the recent trend; more careful methods explicitly model and remove trend/seasonality before analysing the remaining (stationary) series. *Example:* quarterly sales index 100, 108, 96, 112 (year 1) repeating a similar pattern in year 2 (104, 113, 101, 118) shows both an upward trend (each quarter roughly 20/4 = 5.0 points higher year-on-year on average) and a seasonal dip in quarter 3 both years.

## Explicitly not here
Inequality and environmental applications are S14.
