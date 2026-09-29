# S12_Regression_Analysis_and_Econometric_Basics - Test: Regression analysis and econometric basics

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A regression of wages (£/hour) on years of education gives b1 = 1.2 with SE(b1) = 0.3. Calculate the t-statistic and state, using a rough critical value of 1.96, whether b1 is statistically significant at the 5% level. [3 marks]
2. Explain omitted variable bias using an example of a regression of economic growth on foreign aid received, where 'quality of institutions' is omitted. [4 marks]
3. Total sum of squares = 800, residual sum of squares = 200. Calculate R-squared and interpret it in one sentence. [3 marks]
4. A regression finds a statistically significant positive correlation between a country's coffee consumption and its number of Nobel laureates. Which are valid cautions before concluding coffee causes scientific achievement? Choose every correct option.
   A. A third variable, such as national income, could drive both
   B. Statistical significance does not by itself establish causation
   C. Reverse causality is implausible here so causation can be assumed
   D. The direction of any causal link (if real) has not been established by correlation alone

## Answer key (for the tutor only)
1. [3] M1 t = b1/SE = 1.2/0.3 = 4.0; A1 |t| = 4.0 > 1.96; A1 so b1 is statistically significant at the 5% level (reject H0: beta1=0).
2. [4] B1 omitted variable bias occurs when a variable affecting the dependent variable is correlated with the included regressor but left out of the model; B1 institutions plausibly affect both growth directly and the amount/effectiveness of aid a country attracts or is given; B1 if institutions are omitted, some of their true effect on growth is wrongly attributed to aid in the estimated coefficient; B1 so the aid coefficient may be biased (e.g. showing a spuriously weak or even negative link) rather than reflecting aid's true causal effect.
3. [3] M1 R^2 = 1 - 200/800; A1 = 0.75; B1 the model explains 75% of the variation in the dependent variable within this sample.
4. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Regression_Analysis_and_Econometric_Basics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Applied_Statistical_Modelling.
