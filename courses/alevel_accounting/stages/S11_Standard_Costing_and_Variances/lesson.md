# S11_Standard_Costing_and_Variances - Lesson: Standard costing and variance analysis

## Goal
The learner explains the purpose of standard costing, calculates material and labour price/rate and usage/efficiency variances, and reconciles budgeted profit/cost to actual via a variance statement.

## Syllabus items taught here
- 3.11a - Purpose, advantages and disadvantages of standard costing
- QS6 - Variances
- 3.11b - Material price and usage variances
- 3.11c - Labour rate and efficiency variances; reconciliation statement

## How to teach this
Ask: a factory used more material than the standard cost card said it should, but paid less per kilogram than standard. Could the total material variance still be adverse overall? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.11a Purpose, advantages and disadvantages of standard costing
**Purpose of standard costing**: a **standard cost** is a predetermined, carefully estimated cost per unit for materials, labour and overheads, set out on a standard cost card, used as a benchmark against which actual costs are compared. **Advantages**: it supports budgeting, pricing and performance measurement, highlights variances needing investigation (management by exception - only significant deviations need attention), and can motivate staff towards a clear cost target. **Disadvantages**: setting realistic standards is time-consuming and requires ongoing revision (an outdated standard gives misleading variances); it may not suit a business with highly variable or bespoke output where no single "standard" unit exists; and an excessive focus on cost variances can encourage short-term behaviour that harms quality or long-term relationships (e.g. buying cheaper, lower-quality material to generate a favourable price variance).

#### QS6 Variances
QS6: **calculate and interpret variances** - the numerical skill built across 3.11: computing each variance correctly, labelling it favourable (F) or adverse (A), and explaining in words what it suggests happened.

#### 3.11b Material price and usage variances
**Material variances**: **material price variance** = (standard price - actual price) x actual quantity purchased, i.e. (standard cost of actual quantity) - (actual cost); **material usage variance** = (standard quantity for actual output - actual quantity used) x standard price. *Worked example*: standard cost card: 5kg of material per unit at £3/kg = £15/unit standard material cost. Actual output 1,000 units used 5,300kg costing £16,000 in total (actual price = £3.0189/kg). Standard quantity for actual output = 5,000kg. Material price variance = (3 x 5300) - 16000 = -100 = £100 **adverse** (paid more per kg than standard, since actual cost exceeds the standard cost of the actual quantity). Material usage variance = (5,000 - 5300) x 3 = -900 = £900 **adverse** (used more material than the standard allowed). Total material variance = standard cost of output - actual cost = (15,000) - 16000 = £-1,000 adverse, which equals the price and usage variances added together (-100 + -900 = -1,000).

#### 3.11c Labour rate and efficiency variances; reconciliation statement
**Labour variances and the reconciliation statement**: **labour rate variance** = (standard rate - actual rate) x actual hours; **labour efficiency variance** = (standard hours for actual output - actual hours) x standard rate. *Worked example*: standard cost card: 2 hours/unit at £10/hour = £20/unit. Actual output 1,000 units took 2,100 hours costing £20,500 (actual rate = £9.7619/hour). Standard hours for actual output = 2,000 hours. Labour rate variance = (10 x 2100) - 20500 = £500 **favourable** (paid less per hour than standard). Labour efficiency variance = (2,000 - 2100) x 10 = £-1,000 **adverse** (took more hours than standard allowed). Total labour variance = (20,000) - 20500 = £-500 adverse (= 500 + -1,000). A **reconciliation statement** starts with standard (budgeted flexed) cost, lists each variance (favourable variances added back, adverse variances deducted, since they raised the actual cost above standard), and arrives at the actual cost - a single document showing management exactly where and why actual cost diverged from standard.

## Explicitly not here
Absorption and activity based costing are S12; interpreting variances as part of wider performance evaluation, alongside ratios, is S17.
