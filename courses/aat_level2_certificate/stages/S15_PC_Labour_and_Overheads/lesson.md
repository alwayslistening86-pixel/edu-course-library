# S15_PC_Labour_and_Overheads - Lesson: Labour costing and overhead absorption

## Goal
The learner calculates labour payments (time-rate, overtime, piecework, bonuses, guaranteed minimum) and overhead absorption rates per unit, per labour hour and per machine hour.

## Syllabus items taught here
- PC2.2 - Calculate labour payments: time-rate, overtime, piecework, bonuses, guaranteed minimum payments
- PC2.3 - Calculate overhead absorption rates: per unit, per labour hour, per machine hour

## How to teach this
Ask the learner: if someone works their normal hours plus some extra ('overtime') hours at a higher rate, how would you work out their total pay? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PC2.2 Calculate labour payments: time-rate, overtime, piecework, bonuses, guaranteed minimum payments
**Time-rate** pay = hours worked x rate per hour. *Worked example:* 38 hours at £12.50/hour = 38 x £12.50 = **£475.00**. **Overtime** pay adds a premium (e.g. time-and-a-half = x1.5) on top of the basic rate for hours worked beyond the standard week. *Worked example:* a standard 37-hour week at £11.00/hour, plus 6 hours of overtime at time-and-a-half: basic pay = 37 x £11.00 = £407.00; overtime pay = 6 x £11.00 x 1.5 = **£99.00**; total pay = £407.00 + £99.00 = **£506.00**. **Piecework** pays a fixed rate per unit produced, sometimes with a **guaranteed minimum payment** if output (and so piecework pay) falls below a set floor. *Worked example:* 250 units at £0.80/unit = £200.00, which exceeds a guaranteed minimum of £150 -- the employee is paid the higher figure, **£200.00**. If only 150 units were produced: 150 x £0.80 = £120.00, which is *below* the £150 guaranteed minimum -- the employee is paid the guaranteed minimum, **£150.00**. **Individual and team bonus payments** are additional amounts paid for meeting or exceeding a target (individually or as a group), on top of basic/piecework pay.

#### PC2.3 Calculate overhead absorption rates: per unit, per labour hour, per machine hour
**Overhead absorption** shares indirect (overhead) costs across units of production, using an **overhead absorption rate (OAR)**, calculated as: budgeted overheads / budgeted activity level, where activity can be measured **per unit**, **per labour hour** or **per machine hour**. *Worked example:* budgeted overheads are £45,000 and budgeted labour hours are 9,000. OAR per labour hour = £45,000 / 9,000 = **£5.00 per labour hour**. A job taking 14 labour hours absorbs 14 x £5.00 = **£70.00** of overhead. If instead budgeted machine hours are 15,000: OAR per machine hour = £45,000 / 15,000 = **£3.00 per machine hour**. The most appropriate basis (units, labour hours or machine hours) depends on what best reflects how the overhead is actually incurred, e.g. a highly automated department may absorb overhead more sensibly per machine hour than per labour hour.

## Explicitly not here
Using these figures to build total and unit product costs is S16.
