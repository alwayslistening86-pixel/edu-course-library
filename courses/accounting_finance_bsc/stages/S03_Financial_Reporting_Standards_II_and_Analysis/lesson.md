# S03_Financial_Reporting_Standards_II_and_Analysis - Lesson: Financial reporting standards II and analysis

## Goal
The learner applies IAS 37 (provisions and contingencies), IFRS 15 (revenue) and IFRS 16 (leases, lessee accounting), prepares a statement of cash flows under IAS 7, and interprets a set of financial statements using ratio analysis, including its limitations.

## Syllabus items taught here
- B250-5 - IAS 37 Provisions, contingent liabilities and contingent assets
- B250-6 - IFRS 15 Revenue from Contracts with Customers (five-step model)
- B250-7 - IFRS 16 Leases (lessee accounting)
- B250-8 - IAS 7 Statement of cash flows
- B250-9 - Ratio analysis: profitability, liquidity and gearing
- B250-10 - Limitations of ratio analysis and published-accounts interpretation

## How to teach this
Ask: if a company is being sued and might have to pay damages, when (if at all) should that possible future cost appear in this year's financial statements? Teach each topic by building on what A-level Accounting and A-level Mathematics already gave the learner: name the A-level idea it extends (e.g. A-level Accounting's basic financial statements, before IAS 2/IAS 16/IFRS 15/IFRS 16 formalise specific standards), then show the IFRS-specific technical treatment or quantitative technique degree-level accounting/finance adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. UK tax figures (S13) are the 2026/27 tax year; always check HMRC's current published rates before relying on a real-world tax calculation, since UK tax rates/thresholds/allowances change at least annually.

#### B250-5 IAS 37 Provisions, contingent liabilities and contingent assets
**IAS 37 Provisions, Contingent Liabilities and Contingent Assets**: a **provision** (a liability of uncertain timing or amount) is recognised when there is a present obligation (legal or constructive) from a past event, an outflow of economic benefits is probable (more likely than not), and the amount can be estimated reliably. A **contingent liability** (possible obligation, or a present obligation where outflow is not probable or the amount cannot be reliably estimated) is disclosed in the notes, not recognised; a **contingent asset** is disclosed only if an inflow is probable, never recognised until virtually certain (at which point it is no longer contingent). *Worked example*: a company is being sued and legal advice puts the chance of losing at 70% with estimated damages of £200,000: recognise a provision of £200,000 (the best estimate; a single most-likely damages figure, not a probability-weighted mix, since a single most-likely outcome is being estimated here).

#### B250-6 IFRS 15 Revenue from Contracts with Customers (five-step model)
**IFRS 15 Revenue from Contracts with Customers** uses a **five-step model**: (1) identify the contract; (2) identify the separate performance obligations; (3) determine the transaction price; (4) allocate the transaction price to each performance obligation (based on relative standalone selling prices); (5) recognise revenue as (or when) each performance obligation is satisfied -- **over time** (e.g. a long-term construction contract, using an appropriate measure of progress) or **at a point in time** (e.g. control of goods passing to the customer). *Worked example*: a contract bundles equipment (standalone price £40,000) and two years of support (standalone price £20,000) for a total price of £54,000: allocated on a relative standalone-selling-price basis, equipment gets 36,000 (40000/60000 x 54,000) and support gets £18,000.

#### B250-7 IFRS 16 Leases (lessee accounting)
**IFRS 16 Leases (lessee accounting)**: with limited exceptions (short-term and low-value asset leases), a lessee recognises a **right-of-use asset** and a **lease liability** at the present value of future lease payments, discounted at the rate implicit in the lease (or the lessee's incremental borrowing rate). The right-of-use asset is depreciated (usually straight-line) over the lease term; the lease liability is unwound using the effective-interest method, splitting each payment between interest and capital repayment -- so a lease that used to be an off-balance-sheet operating lease expense (under the old standard) now shows an asset, a liability, a depreciation charge and a finance cost. *Worked example*: a 4-year lease has a present value of payments of £72,000; straight-line right-of-use depreciation = £18,000 a year; year 1 interest at 6% = £4,320.

#### B250-8 IAS 7 Statement of cash flows
**IAS 7 Statement of Cash Flows** classifies cash flows into **operating** (from the entity's core revenue-generating activities, usually reconciled from profit before tax via the **indirect method** -- add back non-cash items like depreciation, adjust for working-capital movements and interest/tax paid), **investing** (purchase/sale of non-current assets and investments) and **financing** (proceeds/repayments of borrowings and share issues, dividends paid). Unlike the statement of profit or loss, it is not distorted by accrual timing, which is why users compare profit and operating cash flow: a profitable but cash-poor business (e.g. one growing receivables or inventory quickly) is at real liquidity risk despite reporting a profit.

#### B250-9 Ratio analysis: profitability, liquidity and gearing
**Ratio analysis** interprets the statements: **gross profit margin** = gross profit/revenue; **operating profit margin** = operating profit/revenue; **current ratio** = current assets/current liabilities (short-term liquidity); **quick (acid-test) ratio** = (current assets - inventory)/current liabilities (a stricter liquidity test, excluding the least liquid current asset); **gearing** = debt/(debt + equity), or debt/equity (financial risk from borrowing); **return on capital employed (ROCE)** = operating profit/(total equity + non-current liabilities). *Worked example*: current assets £180,000 (including inventory £60,000), current liabilities £90,000: current ratio = 2.00:1; quick ratio = 1.33:1.

#### B250-10 Limitations of ratio analysis and published-accounts interpretation
**Limitations of ratio analysis**: ratios are only as reliable as the underlying figures (accounting policy choices -- e.g. FIFO vs AVCO, depreciation method/useful life estimates -- affect comparability between companies); historical cost figures may not reflect current values; seasonal businesses can show misleading year-end snapshots; and ratios say nothing directly about qualitative factors (management quality, market conditions, ESG risk). Meaningful interpretation compares a ratio over time (trend analysis) and against sector benchmarks/competitors, not in isolation.

## Explicitly not here
Company law affecting share capital, directors and insolvency is S04; group/consolidated accounts are Block 3 (S08-S09).
