# MA_S01_Management_Information_and_Cost_Classification - Lesson: Management information and cost classification

## Goal
The learner explains the purpose of management accounting versus financial accounting, the sources and qualities of good information, the main ways of classifying costs, and how costs are presented for management.

## Syllabus items taught here
- MA.A1 - Accounting for management
- MA.A2 - Sources of data
- MA.A3 - Cost classification
- MA.A4 - Presenting information

## How to teach this
Ask: 'A shareholder and a production manager both want figures from the same factory. Do they want the same report?' Use the answer to introduce management accounting. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### MA.A1 Accounting for management
**Management accounting** provides information to managers, inside the organisation, for planning, control and decision making; it is not bound by law or accounting standards, can be as detailed or forward-looking as needed, and need not follow a set format. **Financial accounting** produces statutory financial statements for external users (shareholders, HMRC, lenders), following accounting standards, historical and backward-looking. The data processing cycle (data -> information) turns raw facts into something useful: good information is Accurate, Complete, Cost-effective (worth more than it costs), User-targeted, Relevant, Authoritative, Timely, Easy to use (the mnemonic ACCURATE).

#### MA.A2 Sources of data
**Sources of data**: internal (payroll, stores records, previous budgets, sales ledger) and external (government statistics, trade journals, market research). Primary data is collected first-hand (a survey); secondary data already exists and is reused (published statistics). Sampling methods (systematic, simple random, stratified, cluster, quota) let a manageable subset represent a whole population when collecting primary data: simple random gives every member an equal chance; systematic takes every nth item after a random start; stratified samples each sub-group in proportion to its size; cluster randomly selects whole groups and samples them fully; quota fills fixed categories of respondent, non-randomly.

#### MA.A3 Cost classification
**Cost classification** groups costs by the question being asked. By **element**: materials, labour, expenses. By **nature**: direct (traceable to one cost unit, e.g. the wood in a chair) or indirect/overhead (shared, e.g. factory rent). By **function**: production, administration, selling and distribution. By **behaviour**: fixed (constant in total over the relevant range, e.g. rent), variable (constant per unit, total rises with output, e.g. direct material), semi-variable/mixed (a fixed element plus a variable element, e.g. a phone bill with a standing charge plus a per-minute rate), and stepped fixed (constant within a range, then jumps, e.g. adding a second supervisor once output passes a threshold). *Worked example, high-low method*: at 8,000 units total cost is £22,000; at 12,000 units it is £28,000. Variable cost per unit = (28,000 - 22,000) / (12,000 - 8,000) = £{(28000 - 22000) / (12000 - 8000):.2f}/unit; fixed cost = 28,000 - {(28000 - 22000) / (12000 - 8000):.2f} x 12,000 = £{28000 - (28000 - 22000) / (12000 - 8000) * 12000:,.0f}. Estimated total cost at 10,000 units = £{28000 - (28000 - 22000) / (12000 - 8000) * 12000:,.0f} + {(28000 - 22000) / (12000 - 8000):.2f} x 10,000 = £{(28000 - (28000 - 22000) / (12000 - 8000) * 12000) + (28000 - 22000) / (12000 - 8000) * 10000:,.0f}.

#### MA.A4 Presenting information
Information for management is presented as **reports** (tables, with commentary aimed at the reader), **charts** (bar charts for comparing discrete categories, pie charts for proportions of a whole, line graphs for trends over time, scatter diagrams for the relationship between two variables) and increasingly dashboards. Choose the form that answers the question with the least distortion; a report to a non-financial manager should avoid unexplained jargon.

## Explicitly not here
Statistical and forecasting techniques (regression, index numbers, time series) are MA_S02.
