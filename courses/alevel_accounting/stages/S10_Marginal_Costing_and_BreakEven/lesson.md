# S10_Marginal_Costing_and_BreakEven - Lesson: Marginal costing and break-even analysis

## Goal
The learner categorises costs by behaviour, calculates contribution and the break-even point, interprets a break-even chart, and applies marginal costing to short-term decisions.

## Syllabus items taught here
- 3.10a - Cost behaviour and contribution
- QS3 - Cost, revenue, profit and break-even
- 3.10b - Break-even analysis and the break-even chart
- 3.10c - Marginal costing in decision-making

## How to teach this
Ask: a factory is already covering its fixed costs from existing sales. A one-off extra order arrives at a price below the full cost per unit. Could accepting it still increase profit? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.10a Cost behaviour and contribution
**Cost behaviour**: a **variable cost** changes in direct proportion to the level of activity (e.g. direct materials, direct labour paid per unit, sales commission); a **fixed cost** stays the same in total regardless of activity level, within a relevant range (e.g. factory rent, a manager's salary); a **semi-variable (mixed) cost** has both a fixed and a variable element (e.g. a phone bill with a fixed line rental plus a charge per call). **Contribution** per unit = selling price per unit - variable cost per unit; it "contributes" first towards covering fixed costs, and once fixed costs are covered, every further unit's contribution becomes profit.

#### QS3 Cost, revenue, profit and break-even
QS3: **calculate cost, revenue, profit and break-even** - the core numerical skill this stage builds: applying the contribution and break-even formulas below accurately, and reading the resulting figures correctly in context.

#### 3.10b Break-even analysis and the break-even chart
**Break-even analysis**: break-even point (units) = fixed costs / contribution per unit - the level of sales at which total contribution exactly equals fixed costs, so profit is nil. Break-even revenue = break-even units x selling price. **Margin of safety** = budgeted (or actual) sales - break-even sales, showing how far sales could fall before a loss is made. A **break-even chart** plots total cost and total revenue lines against output; they cross at the break-even point, with a "margin of safety" gap shown between that point and budgeted output, and the vertical gap between the lines at any output shows the profit or loss at that level. *Worked example*: selling price £50/unit, variable cost £30/unit: contribution = 20 per unit. Fixed costs £80,000: break-even units = 80,000/20 = 4,000 units; break-even revenue = 4,000 x £50 = £200,000. If budgeted sales are 5,000 units, margin of safety = 5,000 - 4,000 = 1,000 units (20% of budgeted sales).

#### 3.10c Marginal costing in decision-making
**Marginal costing in decision-making**: because fixed costs do not change with a short-term decision (they are already committed), decisions such as a **special order**, **make-or-buy**, or **which product to prioritise with limited capacity** are usually best made by comparing **contribution**, not full (absorption) cost - as long as there is spare capacity and the decision does not affect other sales at the normal price. *Worked example, special order*: a one-off order for 500 units is offered at £35/unit (below the normal £50 price and even below the full absorption cost per unit, which might be, say, £38); variable cost remains £30/unit and there is spare capacity. Contribution from the order = (35-30) x 500 = £2,500; since this is positive and fixed costs are unaffected, accepting the order increases profit by £2,500, even though the price is below full cost per unit - the "benefits and limitations" caveat: this ignores longer-term effects such as existing customers demanding the same low price, or capacity actually being needed elsewhere.

## Explicitly not here
Standard costing variances are S11; full absorption costing and activity based costing are S12.
