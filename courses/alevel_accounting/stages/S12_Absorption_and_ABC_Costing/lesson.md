# S12_Absorption_and_ABC_Costing - Lesson: Absorption costing and activity based costing

## Goal
The learner calculates total product cost and selling price using absorption costing (an overhead absorption rate) and activity based costing (cost drivers), and evaluates the benefits and limitations of absorption, ABC and marginal costing.

## Syllabus items taught here
- 3.12a - Absorption costing and the overhead absorption rate
- 3.12b - Activity based costing and cost drivers
- QS7 - Total product cost and selling price (ABC and absorption)
- 3.12c - Benefits/limitations of absorption, ABC and marginal costing; pricing from cost

## How to teach this
Ask: two products use the same number of machine hours, but one needs many more machine setups than the other. Why might absorption costing, using a single machine-hour rate, give both products a misleadingly similar overhead cost? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.12a Absorption costing and the overhead absorption rate
**Absorption costing**: shares fixed production overheads across units using an **overhead absorption rate (OAR)** = budgeted overheads / budgeted level of activity (e.g. machine hours, labour hours, units), so every unit carries a fair share of the fixed overheads needed to make it, not just its direct (variable) costs - useful for full-cost-based pricing and for inventory valuation under UK/IFRS rules (which require overheads to be included in inventory). *Worked example*: budgeted production overheads £120,000, budgeted machine hours 24,000: OAR = 120,000/24,000 = £5/machine hour. Product X needs 3 machine hours/unit: overhead absorbed = 3 x £5 = £15/unit. With direct materials £20/unit and direct labour £12/unit: total absorption cost = 47 = £47/unit.

#### 3.12b Activity based costing and cost drivers
**Activity based costing (ABC)**: instead of one blanket rate, overheads are grouped into **cost pools** by activity (e.g. machine setups, quality inspections, order processing), each with its own **cost driver** (the factor that causes that cost to be incurred, e.g. number of setups, number of inspections) - giving a cost per unit of the driver, then charging each product for the actual amount of driver activity it causes. ABC is more accurate where overheads are not driven mainly by volume (machine/labour hours) but by the complexity/variety of what is made, at the cost of far more data collection and analysis than a single absorption rate. *Worked example*: setup cost pool £60,000, total setups 500: cost per setup = 60,000/500 = £120. Product Y is made in batches of 100 units and needs 4 setups per batch: setup cost per batch = 4 x £120 = £480, i.e. per unit = £4.80.

#### QS7 Total product cost and selling price (ABC and absorption)
QS7: **calculate total product cost and selling price using activity based costing and absorption costing** - the numerical skill applied in 3.12a-3.12b, extended to setting a selling price by adding a required markup or margin to the calculated total cost.

#### 3.12c Benefits/limitations of absorption, ABC and marginal costing; pricing from cost
**Benefits and limitations, and using cost to set a selling price**: **absorption costing** is simpler and satisfies external reporting requirements for inventory valuation, but a single blanket rate (especially based only on volume) can distort product costs when products consume overhead-driving activities very differently. **ABC** gives more accurate, activity-driven costs, especially useful for pricing and profitability decisions on a diverse product range, but is far more costly and time-consuming to set up and maintain, and choosing appropriate cost drivers itself involves judgement. **Marginal costing** (S10) is simplest for short-term decisions (it ignores fixed overhead absorption entirely) but understates the full cost of a product for long-term pricing, since fixed overheads still have to be covered eventually. *Worked example, pricing from cost*: using the absorption cost of £47/unit above, a 30% markup on cost gives a selling price of 47 x 1.30 = £61.10.

## Explicitly not here
Break-even analysis and marginal-costing decisions are S10; standard costing variances are S11.
