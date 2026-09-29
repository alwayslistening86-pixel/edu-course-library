# S01_Quantitative_Bridge_for_Accounting_Finance - Lesson: Quantitative bridge for accounting and finance

## Goal
The learner summarises business data descriptively, uses probability and sampling ideas that underpin audit sampling, constructs confidence intervals and runs simple hypothesis tests on business figures, fits and interprets a simple linear regression/correlation for forecasting, and builds and interprets index numbers and a simple time-series trend/forecast -- the quantitative toolkit degree-level financial and management accounting assumes beyond A-level Mathematics.

## Syllabus items taught here
- BQ1 - Descriptive statistics and data types for business data
- BQ2 - Probability and sampling distributions for audit/business forecasting
- BQ3 - Confidence intervals and hypothesis testing for business decisions
- BQ4 - Correlation and simple linear regression for forecasting
- BQ5 - Index numbers and time-series forecasting

## How to teach this
Ask: if an auditor cannot check every single transaction in a large ledger, how can testing only a sample of them still give reasonable assurance about the whole population? Teach each topic by building on what A-level Accounting and A-level Mathematics already gave the learner: name the A-level idea it extends (e.g. A-level Accounting's basic financial statements, before IAS 2/IAS 16/IFRS 15/IFRS 16 formalise specific standards), then show the IFRS-specific technical treatment or quantitative technique degree-level accounting/finance adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. UK tax figures (S13) are the 2026/27 tax year; always check HMRC's current published rates before relying on a real-world tax calculation, since UK tax rates/thresholds/allowances change at least annually.

#### BQ1 Descriptive statistics and data types for business data
A-level Maths gives algebra and calculus but not business statistics. Degree-level accounting/finance data is usually summarised with the **mean** (arithmetic average), **median** (middle value, robust to outliers -- useful for skewed data like salaries or invoice values), and a measure of spread: the **standard deviation**, s = sqrt(sum((x-mean)^2)/(n-1)) for a sample. *Example*: monthly sales (£000) 40, 45, 38, 52, 50: mean = 45.0, sample standard deviation = 6.08 (2dp). Financial/business data is typically **quantitative** (measurable, e.g. revenue) or **categorical** (grouped, e.g. product line); a **skewed** distribution (e.g. many small invoices, a few very large ones) means the mean is pulled toward the tail and the median is often the more representative summary.

#### BQ2 Probability and sampling distributions for audit/business forecasting
**Probability and sampling** underpin audit sampling and risk-based testing: if an auditor selects items at random from a population, each item's chance of selection can be modelled, and for a large enough sample the **Central Limit Theorem** says the sample mean is approximately normally distributed even if the underlying population is not, with standard error = population standard deviation/sqrt(n). *Example*: a population of invoices has standard deviation £120; a sample of n=36 gives a standard error of the sample mean of 20.00. This is why a larger sample narrows the auditor's uncertainty about the true population figure -- the standard error shrinks with sqrt(n), not n.

#### BQ3 Confidence intervals and hypothesis testing for business decisions
A **confidence interval** gives a range likely to contain the true population value: sample mean +/- z x standard error (z=1.96 for 95% confidence, large sample). **Hypothesis testing** formalises a business decision under uncertainty: state a null hypothesis (no difference/no effect), calculate a test statistic, and compare to a critical value (or use the p-value) to decide whether to reject the null. *Example*: a sample of 50 invoices has mean value £340, standard deviation £70; 95% CI for the true mean = 340 +/- 1.96 x 70/sqrt(50) = 340 +/- 19.40, i.e. (320.60, 359.40).

#### BQ4 Correlation and simple linear regression for forecasting
**Correlation** (Pearson's r, between -1 and +1) measures the strength and direction of a linear relationship between two variables (e.g. advertising spend and sales); **simple linear regression**, y = a + bx (fitted by least squares), lets a finance team forecast one variable from another and quantifies the relationship's slope. *Example*: fitting sales (y, £000) against advertising spend (x, £000) for five months gives y = 20 + 3x; at x=10 (£10,000 spend), the forecast is y = 20 + 3x10 = £50k. Correlation does not imply causation, and a regression should only be used for forecasting within (or close to) the range of x-values actually observed.

#### BQ5 Index numbers and time-series forecasting
**Index numbers** rebase a series to a chosen base period (=100) so proportional change is easy to read: index = (current value/base value) x 100. *Example*: revenue was £200,000 in the base year and is £230,000 this year: index = 115.0, i.e. revenue has risen 15.0%. A simple **time-series forecast** decomposes a series into trend (long-run direction, often estimated by a moving average or linear regression on time) and, where relevant, seasonal variation; a naive trend forecast simply extrapolates the fitted trend line forward one or more periods.

## Explicitly not here
Applying these tools to specific financial statements and ratios begins in S02.
