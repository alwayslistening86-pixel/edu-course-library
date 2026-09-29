# MA_S02_Data_Analysis_and_Statistical_Techniques - Lesson: Data analysis and statistical techniques

## Goal
The learner selects a sampling method, applies linear regression, correlation and time-series forecasting, calculates index numbers, and knows what spreadsheets are used for in management accounting.

## Syllabus items taught here
- MA.B1 - Sampling methods
- MA.B2 - Forecasting techniques
- MA.B3 - Summarising and analysing data
- MA.B4 - Spreadsheets

## How to teach this
Ask how a supermarket chain with 400 stores could sensibly survey customer satisfaction without visiting every store. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### MA.B1 Sampling methods
**Sampling methods**: simple random (every member of the population has an equal chance, e.g. drawn from random numbers); systematic (every nth item from a list, after a random start); stratified (population split into groups/strata sharing a characteristic, e.g. by department, then randomly sampled in proportion to strata size); cluster (population split into groups, then whole groups are randomly selected and sampled in full, useful when the population is geographically spread); quota (interviewers fill fixed quotas of respondent types, non-random, cheap and quick but can be biased).

#### MA.B2 Forecasting techniques
**Analytical techniques in budgeting and forecasting**. **Regression analysis** fits a line y = a + bx to paired data (x independent/causal variable, y dependent), by least squares; once a and b are estimated, the line **forecasts** y for a given x - but only reliably within the range of the original data (extrapolating beyond it is risky). The **correlation coefficient r** (-1 to +1) measures how closely the points fit a straight line: r near +1 or -1 is strong correlation, r near 0 is weak/no linear relationship; **r-squared** is the proportion of the variation in y explained by x; correlation does not prove causation. **Time series analysis** splits an observed value into a **trend** (T, the long-term direction, found by a moving average that smooths out fluctuations), **seasonal variations** (S, the regular short-term swing around the trend) and residual/random variation; the **additive model**: Actual = T + S, with each seasonal component found by averaging the actual-minus-trend differences for the same season across several cycles.
*Worked example, regression*: a line y = 40 + 6x (y = total cost £'000, x = output '000 units). At x = 10, forecast cost = 40 + 6 x 10 = £{40 + 6 * 10}'000 = £{(40 + 6 * 10) * 1000:,}.
*Worked example, time series*: the moving-average trend for Q3 is 500 units, and Q3's average seasonal variation is +80. Forecast for that Q3 = 500 + 80 = {500 + 80} units.

#### MA.B3 Summarising and analysing data
**Summarising and analysing data**: index numbers re-express a value relative to a base period (=100), to compare across time after allowing for a changing money value or quantity base. A simple **price index** = (current price / base price) x 100. *Worked example*: a material cost £4.50/kg in the base year and £5.40/kg now: price index = (5.40 / 4.50) x 100 = {5.40 / 4.50 * 100:.0f}, i.e. prices have risen {5.40 / 4.50 * 100 - 100:.0f}%. A chain-base index instead compares each period only with the one before it. Summary measures of a data set (mean, median, mode, range) and simple diagrams (as in MA.A4) are also used to describe and communicate a set of results concisely.

#### MA.B4 Spreadsheets
**Spreadsheets** (e.g. Excel) hold data in a grid of cells and are the standard tool for management accounting calculations: formulas that recalculate automatically (SUM, AVERAGE, IF, VLOOKUP/XLOOKUP), what-if analysis (changing one input and seeing every dependent total update, useful for budgeting and investment appraisal), charts, and sorting/filtering data. Their strengths are speed, accuracy of arithmetic and flexibility; their main risk is that a single formula error can propagate silently through a whole model, so checking and version control matter.

## Explicitly not here
Cost classification is MA_S01; using these techniques specifically for budget preparation is MA_S05.
