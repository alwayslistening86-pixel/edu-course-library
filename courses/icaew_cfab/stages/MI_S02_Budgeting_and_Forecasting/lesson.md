# MI_S02_Budgeting_and_Forecasting - Lesson: Budgeting and forecasting

## Goal
The learner forecasts costs using the high-low method and simple time series analysis, prepares functional and cash budgets, selects a budgeting approach, and calculates the cash operating cycle.

## Syllabus items taught here
- MI.2a - Forecasting techniques (high-low, time series)
- MI.2b - Data analytics in budgeting and forecasting
- MI.2c - Preparing budgets
- MI.2d - Budgeting approaches
- MI.2e - Cash budgets and the cash operating cycle
- MI.2f - Managing cash surpluses and deficits

## How to teach this
Ask: why would a fast-growing business with healthy profit on paper still run out of cash if it never prepared a cash budget? Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### MI.2a Forecasting techniques (high-low, time series)
**Forecasting techniques**: the **high-low method** estimates the fixed and variable elements of a semi-variable cost from two activity levels: variable cost/unit = (cost at high activity - cost at low activity) / (high activity - low activity); fixed cost = total cost at either level - (variable cost/unit x that activity level). *Worked example*: total cost is £34,000 at 6,000 units and £42,000 at 9,000 units. Variable cost/unit = (42,000-34,000)/(9,000-6,000) = £2.67; fixed cost = 42,000 - 2.67 x 9,000 = £18,000. **Time series analysis** splits an observed value into a trend and a seasonal variation (Actual = Trend + Seasonal, the additive model); a moving average smooths out short-term fluctuation to reveal the underlying trend.

#### MI.2b Data analytics in budgeting and forecasting
**Data analytics in budgeting/forecasting**: using larger, more granular internal and external datasets (e.g. point-of-sale data, economic indicators) can improve forecast accuracy over simple historical extrapolation, but raises issues of data quality, relevance and the risk of spurious correlation (two variables moving together without one causing the other).

#### MI.2c Preparing budgets
**Preparing budgets**: from the **principal budget factor** (usually sales demand) outward: the sales budget drives the **production budget** (production = budgeted sales + desired closing inventory - opening inventory), which drives material, labour and overhead budgets. *Worked example*: budgeted sales 8,000 units, desired closing inventory 900 units, opening inventory 600 units: production required = 8,000 + 900 - 600 = 8,300 units.

#### MI.2d Budgeting approaches
**Budgeting approaches**: **top-down/imposed** (set by senior management, quick but may lack buy-in/realism) versus **bottom-up/participative** (built with input from those who will deliver it, improving commitment and realism, but slower and risking budgetary slack); **incremental budgeting** (starts from last year's budget/actuals, adjusted for expected changes - quick, but can perpetuate past inefficiency) versus **zero-based budgeting** (every cost must be justified from zero each period, regardless of the prior year - more rigorous and better at eliminating unnecessary spend, but far more time-consuming).

#### MI.2e Cash budgets and the cash operating cycle
**Cash budgets and working capital**: a **cash budget** forecasts cash receipts and payments period by period, to identify shortfalls (so finance can be arranged in advance) or surpluses (so they can be invested) in good time - distinct from the (accrual-based) budgeted income statement. The **cash operating cycle** = inventory holding period + receivables collection period - payables payment period, measuring how long cash is tied up in working capital before being converted back to cash. *Worked example*: inventory period 45 days, receivables period 60 days, payables period 35 days: cash operating cycle = 45 + 60 - 35 = {45+60-35} days.

#### MI.2f Managing cash surpluses and deficits
**Managing cash surpluses and deficits**: a forecast deficit can be met with an overdraft, a short-term loan, delaying non-essential capital spend, or tightening credit control (see MI.2e); a forecast surplus should be invested appropriately (e.g. short-term deposits) rather than left idle, balancing the returns available against the business's need for accessibility (liquidity) should the surplus be needed unexpectedly.

## Explicitly not here
Reporting actual results against budget is MI_S03.
