# S14_PC_Inventory_Valuation - Lesson: Inventory valuation: FIFO, LIFO and AVCO

## Goal
The learner explains inventory valuation and overhead absorption methods used in organisations, and calculates the cost of inventory issues and closing inventory valuations using FIFO, LIFO and AVCO.

## Syllabus items taught here
- PC1.2 - Costing techniques used in organisations: how product cost is determined, inventory valuation methods, labour costing methods, overhead absorption methods
- PC2.1 - Calculate cost of inventory issues and inventory valuations using FIFO, LIFO and AVCO

## How to teach this
Ask the learner: if a shop bought 100 tins of paint at £5 each, then later bought 50 more at £8 each, and then sold 120 tins, which tins were 'sold' -- the cheap ones first, the expensive ones first, or an average? Have the learner attempt every calculation (VAT, discounts, control-account reconciliations, bank reconciliations, FIFO/LIFO/AVCO, labour pay, overhead absorption, product costs, budget variances) with full workings before checking the model answer -- these are computer-marked numeric-entry items in the real AAT assessment, so exact figures matter. Every numeric example in this course was computed and verified in Python when the course was built. UK VAT is taken at the standard rate of 20% throughout unless an item states otherwise; check the current rate at gov.uk if it may have changed. AAT's assessments use a mix of multiple-choice, numeric gap-fill and journal/ledger-entry question tools; this course's items mirror the same calculation-and-entry style using clearly marked short-answer and multiple-choice items.

#### PC1.2 Costing techniques used in organisations: how product cost is determined, inventory valuation methods, labour costing methods, overhead absorption methods
**Inventory valuation methods**: **first-in-first-out (FIFO)** assumes the oldest (first-received) units are issued/sold first, so closing inventory is valued at the most recent prices; **last-in-first-out (LIFO)** assumes the newest (most recently received) units are issued first, so closing inventory is valued at the oldest prices (used for internal/management accounting purposes only at this level, not for financial reporting); **weighted average cost (AVCO)** recalculates a new average cost per unit each time new inventory is received, and issues are valued at that average. **Labour costing methods** (time-rate, overtime, piecework, bonuses, guaranteed minimum) and **overhead absorption methods** (per unit, per labour hour, per machine hour) are covered fully in S15.

#### PC2.1 Calculate cost of inventory issues and inventory valuations using FIFO, LIFO and AVCO
*Worked example:* opening inventory is 100 units at £5.00 each; a further 50 units are received at £8.00 each; 120 units are then issued. **FIFO**: issue the 100 oldest units at £5.00, then the next 20 units at £8.00 -- issue cost = (100 x £5.00) + (20 x £8.00) = £500 + £160 = **£660.00**; closing inventory = 30 units at £8.00 = **£240.00**. **LIFO**: issue the 50 newest units at £8.00, then 70 units at £5.00 -- issue cost = (50 x £8.00) + (70 x £5.00) = £400 + £350 = **£750.00**; closing inventory = 30 units at £5.00 = **£150.00**. **AVCO**: total units = 150, total value = (100 x £5.00) + (50 x £8.00) = £500 + £400 = £900; average cost per unit = £900 / 150 = **£6.00**; issue cost = 120 x £6.00 = **£720.00**; closing inventory = 30 x £6.00 = **£180.00**. Note that FIFO and LIFO give the same closing *quantity* (30 units) but different closing *values*, and AVCO gives a value between the two. For internal (management accounting) purposes, any of the three may be used; **LIFO is for internal use only**.

## Explicitly not here
Calculating labour payments and overhead absorption rates is S15.
