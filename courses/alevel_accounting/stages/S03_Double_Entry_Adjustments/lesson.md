# S03_Double_Entry_Adjustments - Lesson: Period-end adjustments: accruals, irrecoverable debts, depreciation

## Goal
The learner records period-end adjustments in ledger accounts: accruals and prepayments, irrecoverable debts and an allowance for doubtful debts, and depreciation (straight line and reducing balance) including on disposal.

## Syllabus items taught here
- 3.3d - Accruals and prepayments
- 3.3e - Irrecoverable debts and the allowance for doubtful debts
- 3.3f - Depreciation: straight line, reducing balance and disposal

## How to teach this
Ask: a business pays a full year's insurance in advance every January. Why would charging the whole payment as this January's expense misstate the year's profit? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.3d Accruals and prepayments
**Accruals and prepayments**: under the accruals concept, an expense is charged to the period it relates to, not the period it is paid in. An **accrual** (a cost incurred but not yet paid/invoiced) is added to the expense for the period and shown as a current liability; a **prepayment** (a cost paid in advance of the period it relates to) is deducted from the expense and shown as a current asset. *Worked example*: a business pays £3,600 for insurance on 1 October, covering the 12 months to 30 September next year; its year end is 31 December. Months used by the year end = 3 (Oct-Dec), so the expense for the year = 3,600 x 3/12 = £900; the remaining 9 months, £2,700, is a prepayment (current asset) carried forward.

#### 3.3e Irrecoverable debts and the allowance for doubtful debts
**Irrecoverable debts and the allowance for doubtful debts**: an **irrecoverable (bad) debt** is a specific receivable judged unlikely ever to be paid; it is written off - Debit Irrecoverable Debts Expense, Credit Receivables - removing it from the asset and charging it as an expense (applying prudence). An **allowance for doubtful debts** is a general provision against the remaining receivables that are not yet known to be irrecoverable but, based on experience, some will be; it reduces the receivables shown in the statement of financial position without removing any specific customer's balance, and a change in the allowance (up or down) is charged or credited to the statement of profit or loss. *Worked example*: receivables are £40,000 after writing off a £1,000 irrecoverable debt from the original £41,000; a 2% allowance for doubtful debts is then created: allowance = 40,000 x 0.02 = £800, so receivables are shown in the statement of financial position at 40,000 - 800 = £39,200.

#### 3.3f Depreciation: straight line, reducing balance and disposal
**Depreciation**: the systematic allocation of a tangible non-current asset's depreciable amount (cost less estimated residual value) over its useful life, reflecting the wearing out, obsolescence or use of the asset (not an attempt to show current market value). **Straight-line method**: annual depreciation = (cost - residual value) / useful life, giving an equal charge each year - suited to assets that wear evenly over time (e.g. a building, office furniture). **Reducing balance method**: annual depreciation = a fixed percentage x the asset's carrying amount (cost less accumulated depreciation to date) - giving a higher charge in early years, suited to assets that lose most value early or need more repairs as they age (e.g. vehicles, machinery, computers). *Worked example, straight line*: a machine costs £20,000, residual value £2,000, useful life 6 years: annual charge = (20,000 - 2,000) / 6 = £3,000. *Worked example, reducing balance*: a van costs £18,000, depreciated at 25% reducing balance: Year 1 charge = 18,000 x 0.25 = £4,500, carrying amount at the end of Year 1 = £13,500; Year 2 charge = 13,500 x 0.25 = £3,375. On **disposal**, the asset's carrying amount is compared with sale proceeds: proceeds exceeding carrying amount give a profit on disposal (credited to the statement of profit or loss); proceeds below carrying amount give a loss on disposal (debited).

## Explicitly not here
Correcting entries where the trial balance itself fails to balance, using a suspense account, is S04.
