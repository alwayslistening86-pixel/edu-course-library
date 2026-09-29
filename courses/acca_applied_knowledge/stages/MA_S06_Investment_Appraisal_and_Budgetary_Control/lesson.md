# MA_S06_Investment_Appraisal_and_Budgetary_Control - Lesson: Investment appraisal and budgetary control

## Goal
The learner appraises a capital project using payback, accounting rate of return and net present value, compares actual results against a flexed budget, and explains the behavioural effects of imposed versus participative budgeting.

## Syllabus items taught here
- MA.D4 - Investment appraisal
- MA.D5 - Budgetary control and reporting
- MA.D6 - Behavioural aspects of budgeting

## How to teach this
Ask: would you rather have £1,000 today or £1,000 in three years? Use the answer to introduce discounting. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### MA.D4 Investment appraisal
**Asset budgeting and investment appraisal**. **Payback period**: the time for cumulative net cash inflows to repay the initial investment; simple and cash-focused, but ignores what happens after payback and ignores the time value of money. **Accounting Rate of Return (ARR)** = average annual accounting profit / average investment x 100%, compared against a target rate; it uses profit (not cash) and, like payback, ignores the time value of money. **Net Present Value (NPV)** discounts every future cash flow to today's value using a discount factor 1/(1+r)^n (r = the cost of capital, n = years from now), then sums them, netting off the initial investment (year 0); NPV accounts for the time value of money, and a **positive NPV** means the project is worth undertaking at that cost of capital - NPV is regarded as the technically best appraisal method taught at this level.
*Worked example*: initial investment £10,000; net cash inflows £3,000, £4,000, £5,000, £3,000 in years 1-4. Cumulative: year 1 -£{10000 - 3000:,}, year 2 -£{10000 - 3000 - 4000:,}, year 3 +£{-10000 + 3000 + 4000 + 5000:,}. Payback occurs during year 3: 2 years + £{10000 - 3000 - 4000:,}/£5,000 = 2 + {(10000 - 3000 - 4000) / 5000:.1f} = {2 + (10000 - 3000 - 4000) / 5000:.1f} years. Average annual profit (net of the £10,000 spread over 4 years) = ({3000 + 4000 + 5000 + 3000} - 10,000)/4 = £{(3000 + 4000 + 5000 + 3000 - 10000) / 4:,.0f}; average investment = 10,000/2 = £{10000 / 2:,}; ARR = {(3000 + 4000 + 5000 + 3000 - 10000) / 4:,.0f}/{10000 / 2:,.0f} x 100 = {((3000 + 4000 + 5000 + 3000 - 10000) / 4) / (10000 / 2) * 100:.0f}%. At 10%, discount factors are 1.000, 0.909, 0.826, 0.751, 0.683: NPV = -10,000 + 3,000(0.909) + 4,000(0.826) + 5,000(0.751) + 3,000(0.683) = -10,000 + {3000 * .909:.0f} + {4000 * .826:.0f} + {5000 * .751:.0f} + {3000 * .683:.0f} = £{-10000 + 3000 * .909 + 4000 * .826 + 5000 * .751 + 3000 * .683:,.0f}, a positive NPV, so the project is worthwhile at 10%.

#### MA.D5 Budgetary control and reporting
**Budgetary control and reporting** compares actual results against the **flexed** budget (see MA_S05) period by period, reports the variances to the managers responsible, and distinguishes controllable variances (within a manager's power, e.g. wastage) from uncontrollable ones (e.g. a general market price rise), and favourable variances (better than budget) from adverse ones. Timely, clear reporting lets management take corrective action or revise future budgets (management by exception: investigate only material variances).

#### MA.D6 Behavioural aspects of budgeting
**Behavioural aspects of budgeting**: a **top-down/imposed** budget is set by senior management with little input from those who must achieve it - quicker, and keeps strategic control, but can demotivate and may be unrealistic since it misses local knowledge. A **bottom-up/participative** budget involves the managers who will be responsible for it - improves commitment, realism and motivation, but takes longer and risks **budgetary slack** (a manager deliberately understating expected performance, or overstating needed resources, to make the target easier to hit). Budgets used punitively can encourage dysfunctional behaviour (e.g. spending a whole year-end budget just to avoid a cut next year); a well-designed process balances control with motivation.

## Explicitly not here
Standard costing variances are MA_S07.
