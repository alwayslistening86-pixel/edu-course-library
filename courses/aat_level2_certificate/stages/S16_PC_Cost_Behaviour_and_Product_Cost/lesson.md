# S16_PC_Cost_Behaviour_and_Product_Cost - Lesson: Cost behaviour and the cost of a product

## Goal
The learner uses cost behaviour to calculate total and unit costs at different levels of output, and calculates the direct cost, manufacturing cost, cost of goods manufactured and cost of goods sold of a product (and equivalent costs for a service).

## Syllabus items taught here
- PC2.4 - Use cost behaviour to calculate total and unit costs at different levels of output
- PC2.5 - Calculate the costs of a product: direct cost, manufacturing cost, cost of goods manufactured and sold, in manufacturing and service organisations

## How to teach this
Ask the learner: if fixed costs stay the same in total as output rises, what happens to the fixed cost *per unit*? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PC2.4 Use cost behaviour to calculate total and unit costs at different levels of output
**Variable cost per unit stays the same** at different output levels, but total variable cost rises with output; **fixed cost in total stays the same**, but fixed cost **per unit falls** as output rises (the same fixed total is spread over more units) -- so total cost per unit changes with output even though the underlying costs haven't changed in nature. *Worked example:* fixed costs are £20,000 and variable cost is £8 per unit. At an output of 2,000 units: total cost = £20,000 + (£8 x 2,000) = £20,000 + £16,000 = **£36,000**; cost per unit = £36,000 / 2,000 = **£18.00**. At an output of 4,000 units: total cost = £20,000 + (£8 x 4,000) = £20,000 + £32,000 = **£52,000**; cost per unit = £52,000 / 4,000 = **£13.00** -- lower, because the same £20,000 fixed cost is now spread across twice as many units.

#### PC2.5 Calculate the costs of a product: direct cost, manufacturing cost, cost of goods manufactured and sold, in manufacturing and service organisations
**Direct cost** = direct materials + direct labour + direct expenses (also called **prime cost**). **Manufacturing cost** = prime cost + factory (production) overheads. **Cost of goods manufactured (COGM)** = manufacturing cost + opening work-in-progress (WIP) - closing WIP (adjusting for partly-finished goods still in production). **Cost of goods sold (COGS)** = COGM + opening finished goods inventory - closing finished goods inventory. *Worked example:* direct materials £12,000, direct labour £8,000, direct expenses £1,000 -- prime cost = £21,000; factory overheads £6,000 -- manufacturing cost = £21,000 + £6,000 = **£27,000**; opening WIP £2,000, closing WIP £2,500 -- COGM = £27,000 + £2,000 - £2,500 = **£26,500**; opening finished goods £3,000, closing finished goods £3,600 -- COGS = £26,500 + £3,000 - £3,600 = **£25,900**. If 500 units were manufactured, the manufacturing cost per unit = £27,000 / 500 = **£54.00**. **Service organisations** have no physical inventory to value, so their "cost of the service" is typically built from direct labour, direct expenses and an appropriate share of overheads, without a manufacturing-account/WIP/finished-goods stage.

## Explicitly not here
Comparing these costs against a budget, and reporting variances, is S17.
