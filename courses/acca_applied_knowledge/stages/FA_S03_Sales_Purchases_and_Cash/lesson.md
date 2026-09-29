# FA_S03_Sales_Purchases_and_Cash - Lesson: Sales, purchases and cash

## Goal
The learner records sales and purchases including trade and settlement (cash) discounts and sales tax, and maintains cash book and petty cash records including an imprest system.

## Syllabus items taught here
- FA.D1 - Sales and purchases
- FA.D2 - Cash

## How to teach this
Ask: 'A supplier lists an item at £100 but offers 10% off for buying in bulk, and a further 2% off if paid within 10 days. What does the business actually record as the purchase, and when?' Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### FA.D1 Sales and purchases
**Sales and purchases**. A **trade discount** (e.g. for bulk buying, or to a particular class of customer) is deducted before the transaction is ever recorded - only the net amount is recorded as revenue/purchases. A **settlement (cash/early payment) discount** is offered for prompt payment; under current IFRS treatment it is recognised only if and when the customer actually takes it (revenue is initially recorded at the amount expected to be received, with an adjustment made if the discount is subsequently taken). **Sales tax (VAT)** charged on sales is collected on behalf of the tax authority, not revenue of the business - a business registered for sales tax records sales/purchases net of tax, with the tax element posted to a sales tax (output tax less input tax) control account, the balance of which is periodically paid to/reclaimed from the tax authority. *Worked example*: goods with a list price of £2,000 are sold, less a 15% trade discount; sales tax is then charged at 20% on the discounted amount. Discounted price = 2,000 x (1 - 0.15) = £{2000 * 0.85:,.2f}. Sales tax = {2000 * 0.85:,.2f} x 0.20 = £{2000 * 0.85 * 0.20:,.2f}. Total invoiced to the customer = £{2000 * 0.85 * 1.20:,.2f}, of which revenue recorded is £{2000 * 0.85:,.2f} and sales tax payable is £{2000 * 0.85 * 0.20:,.2f}.

#### FA.D2 Cash
**Cash**. The **cash book** records all receipts and payments of cash/cheques, acting as both a book of prime entry and (for the bank columns) part of the ledger. **Petty cash** covers small, low-value expenses (postage, milk, minor stationery) too impractical to process through the main system; the **imprest system** maintains a fixed float - petty cash is reimbursed periodically by exactly the amount spent, restoring the float to its fixed level, and every payment is evidenced by a voucher, giving good control and an easy check (float remaining + vouchers = the fixed imprest amount). *Worked example*: the imprest amount is £150. During the month, vouchers total £112. At month end the float is topped up by £112, restoring it to £150; if vouchers total £112 but cash remaining is only £30 (150 - 112 = £{150 - 112}), the shortfall of £{150 - 112 - 30} would need investigating before reimbursement.

## Explicitly not here
Inventory valuation is FA_S04; bank reconciliations are FA_S07.
