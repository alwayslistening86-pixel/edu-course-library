# S13_PC_Cost_Classification - Lesson: Cost classification, cost centres and the costing system

## Goal
The learner classifies costs by element, nature and behaviour, distinguishes product from period costs, explains how costing relates to financial accounting, describes cost/profit/investment centres, and explains coding and the manufacturing account.

## Syllabus items taught here
- PC1.1 - Collection and classification of costs: element (labour/materials/overheads), nature (direct/indirect), behaviour (fixed/variable/semi-variable/stepped), product vs period costs
- PC1.3 - Relationships between costing and financial accounting systems within organisations
- PC1.4 - Sources of information on income and expenditure: historic, actual and budgeted costs, planning and control
- PC1.5 - Differences between cost, profit and investment centres, and their use in different organisations
- PC1.6 - Classification and recording of labour and overheads: coding systems and the manufacturing account

## How to teach this
Ask the learner: if a bakery buys flour, is that cost the same 'kind' of cost as the rent on the bakery building? What's actually different about them? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PC1.1 Collection and classification of costs: element (labour/materials/overheads), nature (direct/indirect), behaviour (fixed/variable/semi-variable/stepped), product vs period costs
Costs are classified several ways. By **element**: **labour** (wages/salaries), **materials** (raw materials, components) and **overheads** (everything else, e.g. rent, utilities, indirect labour). By **nature**: **direct** (traceable to a specific unit/job, e.g. the flour in a specific batch of bread) or **indirect** (not traceable to one unit, shared across production, e.g. factory rent). By **behaviour**: **fixed** (stays the same in total regardless of output level, e.g. rent), **variable** (changes in direct proportion to output, e.g. materials per unit), **semi-variable** (has both a fixed and a variable element, e.g. a phone bill with a fixed line rental plus a per-call charge) and **stepped** (fixed within a range of output, then jumps to a new fixed level once a threshold is crossed, e.g. needing a second supervisor once output exceeds a certain level). **Product costs** are included in the value of inventory (materials, labour and overheads incurred in making the product) until it is sold; **period costs** are expensed in the period incurred regardless of sales (e.g. administrative or selling costs not tied to making the product).

#### PC1.3 Relationships between costing and financial accounting systems within organisations
**Costing systems** and **financial accounting systems** serve different purposes within the same organisation: the costing system uses many different classifications of cost (element, nature, behaviour, direct/indirect) to support internal planning, control and decision-making at a detailed level (e.g. per product, per department); financial accounting uses only **historic** (actual, already-incurred) costs, classified more simply, to produce the statutory financial statements required by law and external users.

#### PC1.4 Sources of information on income and expenditure: historic, actual and budgeted costs, planning and control
**Historic cost** (what was actually spent, from past transactions) is used for both external financial accounting/reporting and, alongside **budgeted** (planned) costs, for internal costing reports. Costing systems use **actual or budgeted costs** to determine the cost of a unit, job or batch. Comparing **budgeted and actual** costs and income supports **planning** (deciding what should happen) and **control** (checking what did happen against the plan, and acting on differences -- covered fully in S17).

#### PC1.5 Differences between cost, profit and investment centres, and their use in different organisations
A **cost centre** is a part of an organisation for which costs are separately collected and monitored (e.g. a department, a machine), but which does not directly generate revenue itself. A **profit centre** both incurs costs and generates its own revenue, so its performance can be judged on profit (revenue less its own costs). An **investment centre** goes further still: it is judged not just on profit but on the return generated relative to the capital/assets invested in it. Different types of organisation use different centres depending on how much autonomy and accountability each part of the business has -- e.g. a small production department is usually a cost centre, while a semi-autonomous division with its own customers and its own capital budget might be run as an investment centre.

#### PC1.6 Classification and recording of labour and overheads: coding systems and the manufacturing account
Costs are classified and recorded by **element, nature, behaviour and function** (e.g. production, administration, selling and distribution) and are **coded** using **numeric, alphabetic or alphanumeric coding systems** (the same principle as in Introduction to Bookkeeping, IB1.3), so costs can be collected, analysed and reported consistently. A **manufacturing account** brings together all costs of production to arrive at the cost of goods manufactured (direct costs plus factory overheads, adjusted for work-in-progress), which then feeds into the statement of profit or loss (see PC2.5 for the full worked calculation).

## Explicitly not here
Actually calculating inventory valuations, labour payments and overhead absorption is S14-S15.
