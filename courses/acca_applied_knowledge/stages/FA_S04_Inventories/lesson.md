# FA_S04_Inventories - Lesson: Inventories

## Goal
The learner values inventory using FIFO and AVCO, applies the lower of cost and net realisable value rule under IAS 2, and explains the effect of inventory valuation and inventory counts on the financial statements.

## Syllabus items taught here
- FA.D3 - Inventories

## How to teach this
Ask: 'If a business bought the same product at three different prices this year, and has some left at the year end, which price is 'the' cost of what's left?' Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### FA.D3 Inventories
**Inventory (IAS 2)** is valued at the **lower of cost and net realisable value (NRV)**, applied item by item (or group of similar items): **cost** includes purchase price plus costs to bring inventory to its present location and condition (e.g. carriage inwards), but excludes selling costs; **NRV** = estimated selling price less estimated costs to complete and costs to sell. Where identical units were bought at different prices, cost is estimated using **FIFO** (first in, first out: units are assumed issued/sold in the order bought, so closing inventory is valued at the most recent purchase prices) or **AVCO** (weighted average cost, recalculated after each purchase, or periodically over the period) - **LIFO** is not permitted under IAS 2. *Worked example*: opening inventory nil; purchases 400 units @ £6.00, then 600 units @ £6.50; 700 units sold, 300 remain. FIFO closing inventory = 300 units at the most recent price, £6.50 = £{300 * 6.50:,.2f}. Periodic AVCO price = (400 x 6.00 + 600 x 6.50)/1,000 = £{(400 * 6.00 + 600 * 6.50) / 1000:.2f}/unit, so AVCO closing inventory = 300 x {(400 * 6.00 + 600 * 6.50) / 1000:.2f} = £{300 * (400 * 6.00 + 600 * 6.50) / 1000:,.2f}. *Worked example, NRV*: 200 units cost £9.00 each (£{200 * 9.00:,.2f} total) but, due to damage, are now expected to sell for only £7.50 each with £0.50/unit selling costs, giving NRV = 7.50 - 0.50 = £7.00/unit (£{200 * 7.00:,.2f} total); since NRV (£{200 * 7.00:,.2f}) is below cost (£{200 * 9.00:,.2f}), the inventory is written down and valued at £{200 * 7.00:,.2f}. An inventory **count** at the year end physically verifies quantities on hand; over/understating closing inventory directly over/understates both profit (via cost of sales) and current assets in that period.

## Explicitly not here
Non-current assets and depreciation are FA_S05.
