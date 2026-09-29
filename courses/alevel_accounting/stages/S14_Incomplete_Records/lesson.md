# S14_Incomplete_Records - Lesson: Accounting for organisations with incomplete records

## Goal
The learner calculates profit for a business with incomplete records using the net assets (change-in-capital) method, and reconstructs missing figures (e.g. sales, purchases, expenses) from partial information.

## Syllabus items taught here
- 3.14a - Net assets (change-in-capital) method
- 3.14b - Reconstructing missing figures from control accounts
- 3.14c - Benefits and limitations of incomplete records

## How to teach this
Ask: a small trader has kept no proper books all year but can list what the business owns and owes at the start and end of the year. Can profit still be worked out? Teach each topic with a worked numerical example wherever the content is calculation-based (ledger entries, ratios, variances, investment appraisal): have the learner attempt the calculation before seeing the worked answer. For evaluative content (S17-S21), always pair a calculated figure with the qualitative/contextual factors that should be weighed against it - AQA's Section C marking specifically rewards this. All numerical worked examples were computed with Python when the course was built.

#### 3.14a Net assets (change-in-capital) method
**The net assets (change-in-capital) method**: where full double-entry records were not kept, profit can still be calculated because capital = net assets (assets - liabilities), and capital only changes because of profit, drawings, or capital introduced: **profit for the year = (closing net assets - opening net assets) + drawings - capital introduced**. *Worked example*: opening assets £52,000, opening liabilities £10,000: opening net assets (capital) = 52,000 - 10,000 = £42,000. Closing assets £68,000, closing liabilities £14,000: closing net assets = 68,000 - 14,000 = £54,000. Drawings during the year £16,000, no additional capital introduced: profit = (54,000 - 42,000) + 16,000 - 0 = £28,000.

#### 3.14b Reconstructing missing figures from control accounts
**Reconstructing missing figures from control account totals**: where the sales or purchases figure itself is missing, it is found by reconstructing a total receivables or payables account (or, for a cash-based business, a total cash/bank summary), since the closing balance is known and most other figures (cash received, opening balance) usually are. *Worked example, missing credit sales*: opening receivables £9,000; cash received from customers during the year £140,000; closing receivables £11,000. Total receivables account: opening balance + credit sales - cash received = closing balance, so credit sales = closing balance - opening balance + cash received = 11,000 - 9,000 + 140,000 = £142,000.

#### 3.14c Benefits and limitations of incomplete records
**Benefits and limitations of incomplete/single-entry records**: keeping only incomplete records is quicker and cheaper for a very small business, and the net assets method still allows a profit figure to be produced for the tax authorities or a bank. However, it is far more prone to error and omission (with no double entry, there is no built-in cross-check that debits equal credits), it relies heavily on accurately valuing assets and liabilities at two points in time, and it cannot easily reconstruct a full statement of profit or loss (showing revenue, cost of sales and each expense separately) without additional reconstruction work such as that shown in 3.14b - a business that grows in size or complexity will generally need to move to full double entry.

## Explicitly not here
Full double-entry bookkeeping and preparing statements from a trial balance are S02/S03/S06.
