# TAX_S05_Corporation_Tax - Lesson: Corporation tax

## Goal
The learner identifies a company's accounting period, adjusts trading profit for tax purposes at an introductory level, and calculates a UK-resident company's corporation tax liability for 2026/27, including marginal relief.

## Syllabus items taught here
- TAX.5a - Company accounting periods and associated companies
- TAX.5b - Adjustment of trading profit
- TAX.5c - Taxable total profits and corporation tax rates 2026/27
- TAX.5d - Marginal relief worked example

## How to teach this
Ask: why might a company with exactly £250,000 of taxable profit pay tax at a different effective rate than one with £50,000 of profit, given corporation tax officially has just two headline rates? Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### TAX.5a Company accounting periods and associated companies
**Company accounting periods**: a company's **accounting period** for corporation tax cannot exceed 12 months - a longer period of account is split into a first 12-month accounting period and a second, shorter one. Corporation tax is assessed and self-assessed separately for each accounting period. **Associated companies** (broadly, companies under common control) each get a proportionately reduced share of the small profits/main rate thresholds (e.g. two associated companies each have a £25,000 small profits limit and a £125,000 main rate threshold, rather than the full £50,000/£250,000 each), which can also affect how many instalments larger companies must pay corporation tax in.

#### TAX.5b Adjustment of trading profit
**Adjustment of trading profit** (introductory level): a company's accounting (statement of profit or loss) profit is adjusted to arrive at **taxable trading profit** by adding back **disallowable expenditure** (e.g. entertaining clients, donations to non-qualifying causes, depreciation - which is replaced for tax purposes by **capital allowances**, a standardised tax depreciation regime) and deducting income that is not taxable as trading income (e.g. profit on disposal of a fixed asset, which may instead be a chargeable gain) or other tax-specific reliefs. *Worked example*: accounting profit £180,000, including £6,000 of client entertaining (disallowable) and £15,000 of depreciation (disallowable, replaced by capital allowances of £18,000). Adjusted trading profit = 180,000 + 6,000 + 15,000 - 18,000 = £183,000.

#### TAX.5c Taxable total profits and corporation tax rates 2026/27
**UK resident company's taxable total profits and corporation tax, 2026/27**: taxable total profits = adjusted trading profit + the company's own chargeable gains (computed similarly to individual CGT principles, but taxed at the corporation tax rate rather than a separate CGT rate) + other income, less qualifying reliefs. The **small profits rate** of **19%** applies where taxable total profits are **£50,000** or less; the **main rate** of **25%** applies where profits exceed **£250,000**; between those thresholds, **marginal relief** tapers the effective rate smoothly from 19% up to 25%. *Worked example (profits within the small profits limit)*: taxable total profits £40,000: corporation tax = 40,000 x 19% = £7,600.

#### TAX.5d Marginal relief worked example
*Worked example (profits above the main rate threshold)*: taxable total profits £300,000: corporation tax = 300,000 x 25% = £75,000 (the full main rate applies, since profits exceed £250,000). *Worked example (marginal relief band, simplified - single company, no dividends from other companies, 12-month period)*: taxable total profits £150,000, which falls between £50,000 and £250,000. Tax at the main rate on the full amount = 150,000 x 25% = £37,500; marginal relief = (upper limit - profits) x marginal relief fraction (standard fraction 3/200) = (250,000 - 150,000) x 3/200 = £1,500; corporation tax payable = 37,500 - 1,500 = £36,000 (an effective rate of 24.0%, between the 19% and 25% headline rates, as intended).

## Explicitly not here
VAT and stamp taxes are TAX_S06; a company's own capital gains computation mechanics mirror TAX_S04's individual principles.
