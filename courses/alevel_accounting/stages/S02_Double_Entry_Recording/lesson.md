# S02_Double_Entry_Recording - Lesson: Recording transactions by double entry

## Goal
The learner records transactions from source documents through books of prime entry into ledger accounts using double entry, distinguishes capital from revenue items, and extracts a trial balance.

## Syllabus items taught here
- 3.3a - Source documents and books of prime entry
- 3.3b - Double entry: the accounting equation and ledger posting
- 3.3c - Capital vs revenue expenditure/income; the trial balance

## How to teach this
Ask: if every transaction is recorded twice, in opposite directions, why does that guarantee the books stay in balance rather than just doubling any errors? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.3a Source documents and books of prime entry
**Source documents and books of prime entry**: every transaction starts with a source document (sales/purchase invoice, credit note, cheque, receipt, bank statement). These are first listed in a **book of prime entry** - the sales day book, purchases day book, sales/purchases returns day books, the cash book (cash and bank), and the general journal (for entries with no other day book, e.g. correcting errors or recording a non-current asset purchase on credit) - before being **posted** to the ledger accounts.

#### 3.3b Double entry: the accounting equation and ledger posting
**Double entry in the ledger**: every transaction is entered as a **debit** in one account and an equal **credit** in another, keeping the accounting equation (**Assets = Liabilities + Equity**) in balance. The rule: debit entries increase assets and expenses (and decrease liabilities, equity and income); credit entries increase liabilities, equity and income (and decrease assets and expenses). *Worked example*: a business buys inventory for £3,000 cash: Debit Purchases £3,000 (expense increases), Credit Cash £3,000 (asset decreases). It then sells goods on credit for £5,000: Debit Receivables £5,000 (asset increases), Credit Sales £5,000 (income increases).

#### 3.3c Capital vs revenue expenditure/income; the trial balance
**Capital versus revenue items, and the trial balance**: **capital expenditure** buys or improves a non-current asset (e.g. a delivery van, an extension to a building) and appears in the statement of financial position; **revenue expenditure** is the day-to-day running cost of the business (wages, rent, purchases of inventory for resale) and appears in the statement of profit or loss. The same distinction applies to income: **capital income** (e.g. proceeds of a share issue) versus **revenue income** (e.g. sales revenue). After posting all transactions, a **trial balance** lists every ledger account's balance in a debit or credit column; if double entry has been applied correctly, total debits equal total credits (though this does not prove there are no errors - see S04). *Worked example*: a business buys a machine for £15,000 (capital expenditure, debited to Non-current Assets) and pays £800 to have it installed and £200 for its first service six months later (installation is capital expenditure, part of getting the asset ready for use, so added to the asset at £15,800; the later service is revenue expenditure, an expense, because it merely maintains the asset rather than improving it).

## Explicitly not here
Adjustments made after the initial trial balance (accruals, depreciation, irrecoverable debts) are S03; correcting errors found via a suspense account is S04.
