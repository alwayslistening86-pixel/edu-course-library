# S13_Applied_Statistical_Modelling - Test: Applied statistical modelling

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what multicollinearity is and why it is a problem even when the overall regression has a high R-squared. [4 marks]
2. A regression models labour-force participation (1 = in the labour force, 0 = not) using logistic regression rather than ordinary least squares. Explain why OLS would be inappropriate here. [3 marks]
3. wage = b0 + b1(education) + b2(female) + e, with b2 = -3.2 (female=1 for women). Explain what b2 estimates, and one reason it might not represent the full causal effect of gender-based discrimination. [4 marks]
4. Explain the difference between trend and seasonality in a time series, using UK retail sales as an example. [3 marks]

## Answer key (for the tutor only)
1. [4] B1 multicollinearity is high correlation between two or more explanatory variables in the same regression; B1 it makes it statistically difficult to isolate each variable's individual effect on y, since they move together in the sample; B1 this inflates the standard errors of the affected coefficients, making them unstable and often statistically insignificant even if jointly important; B1 the overall fit (R-squared) can still be high because the variables jointly predict y well, even though their individual coefficients are unreliable.
2. [3] B1 the outcome is binary, but an OLS linear prediction is unbounded and can produce predicted values below 0 or above 1, which are meaningless as probabilities; B1 logistic regression instead maps the linear combination of explanatory variables through an S-shaped function bounded between 0 and 1; B1 giving valid predicted probabilities and better reflecting the non-linear way explanatory variables typically affect a probability near the extremes.
3. [4] B1 b2 estimates the average wage difference between women and men who have the same level of education (holding education constant) in this sample; B1 women earn on average £3.20/hour less than men with the same education; B1 this is a conditional association, not necessarily a pure discrimination effect; B1 other omitted factors correlated with gender (e.g. sector, hours worked, career breaks) could also drive part of this gap, so a causal discrimination claim needs those to be controlled for or otherwise ruled out.
4. [3] B1 trend is the underlying long-run direction of the series (e.g. retail sales gradually rising over years with overall economic growth); B1 seasonality is a regular, repeating within-year pattern (e.g. sales spiking every December for Christmas, then dipping in January); B1 both must be identified and accounted for separately, since comparing December to January directly would confuse a seasonal effect with genuine growth or decline.

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Applied_Statistical_Modelling` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Inequality_Innovation_and_Environment.
