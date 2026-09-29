# MA_S07_Standard_Costing_and_Variance_Analysis - Lesson: Standard costing and variance analysis

## Goal
The learner sets up a standard costing system, calculates material, labour, variable overhead, fixed overhead and sales variances, and reconciles budgeted profit to actual profit using them.

## Syllabus items taught here
- MA.E1 - Standard costing system
- MA.E2 - Variance calculations and analysis
- MA.E3 - Reconciliation of budgeted and actual profit

## How to teach this
Ask: if a bakery's standard recipe uses 500g of flour per loaf but the actual batch used 550g, is that a price problem or a quantity problem? Use the answer to split cost variances into two parts. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### MA.E1 Standard costing system
A **standard cost** is a predetermined, carefully estimated unit cost (standard quantities of material, labour hours and overhead per unit, and standard prices/rates), set from technical specifications and past experience, used as a benchmark. A **standard costing system** compares actual costs/revenues against the flexed standard (standard cost x actual output) to generate variances that explain the difference between budgeted and actual profit.

#### MA.E2 Variance calculations and analysis
**Variance calculations and analysis**. **Material variances**: total material variance = (standard cost of actual output) - (actual cost); split into **price variance** = (standard price - actual price) x actual quantity purchased, and **usage variance** = (standard quantity for actual output - actual quantity used) x standard price. **Labour variances**: **rate variance** = (standard rate - actual rate) x actual hours paid, and **efficiency variance** = (standard hours for actual output - actual hours worked) x standard rate. A positive result (standard exceeds actual, or fewer resources used than standard) is **favourable**; a negative result is **adverse**. **Variable overhead variances** mirror labour: expenditure variance = (standard rate - actual rate) x actual hours, efficiency variance = (standard hours for actual output - actual hours) x standard rate. **Fixed overhead variances** (absorption costing) split the total fixed overhead variance (under/over-absorbed overhead) into an **expenditure variance** (budgeted fixed overhead - actual fixed overhead incurred) and a **volume variance** (actual output - budgeted output, in units) x standard fixed OAR per unit. **Sales variances**: **sales price variance** = (actual price - standard price) x actual quantity sold, and **sales volume variance** = (actual quantity sold - budgeted quantity) x standard profit (or contribution) per unit.
*Worked example, materials*: standard is 5 kg @ £3.00/kg per unit; 1,000 units are made using 5,100 kg costing £15,300 in total (average £{15300 / 5100:.2f}/kg). Price variance = (3.00 - {15300 / 5100:.2f}) x 5,100 = £{(3.00 - 15300 / 5100) * 5100:,.0f} ({'favourable' if (3.00 - 15300 / 5100) * 5100 >= 0 else 'adverse'}). Usage variance = (5,000 - 5,100) x 3.00 = £{(5000 - 5100) * 3.00:,.0f} ({'adverse' if (5000 - 5100) * 3.00 < 0 else 'favourable'}). Total material variance = £{(3.00 - 15300 / 5100) * 5100 + (5000 - 5100) * 3.00:,.0f}, which equals standard cost of output (5,000 x £3.00 = £15,000) minus actual cost (£15,300) = £{5000 * 3.00 - 15300:,.0f}.

#### MA.E3 Reconciliation of budgeted and actual profit
**Reconciling budgeted profit to actual profit**: start with budgeted profit, add favourable variances and subtract adverse variances for sales (price, volume) and every cost variance (material price/usage, labour rate/efficiency, variable overhead expenditure/efficiency, fixed overhead expenditure and volume), to arrive at actual profit. This operating statement is the standard way ACCA presents a full set of variances together, and shows management exactly where performance differed from plan.

## Explicitly not here
Budgeting and flexed budgets themselves are MA_S05/MA_S06.
