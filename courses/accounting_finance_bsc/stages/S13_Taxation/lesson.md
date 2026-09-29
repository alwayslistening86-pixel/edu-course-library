# S13_Taxation - Lesson: Taxation

## Goal
The learner calculates a UK individual's income tax liability, a company's corporation tax liability (including marginal relief), an individual's capital gains tax liability, and the VAT due on a straightforward transaction, using current (2026/27) UK tax rates, thresholds and allowances -- matching Taxation (B353).

## Syllabus items taught here
- TAX-1 - UK income tax
- TAX-2 - UK corporation tax and marginal relief
- TAX-3 - UK capital gains tax
- TAX-4 - VAT

## How to teach this
Ask: why does the UK tax system use a system of bands and marginal rates, rather than one flat rate applied to all of a person's income? Teach each topic by building on what A-level Accounting and A-level Mathematics already gave the learner: name the A-level idea it extends (e.g. A-level Accounting's basic financial statements, before IAS 2/IAS 16/IFRS 15/IFRS 16 formalise specific standards), then show the IFRS-specific technical treatment or quantitative technique degree-level accounting/finance adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. UK tax figures (S13) are the 2026/27 tax year; always check HMRC's current published rates before relying on a real-world tax calculation, since UK tax rates/thresholds/allowances change at least annually.

#### TAX-1 UK income tax
**UK income tax (2026/27)**: an individual has a **personal allowance** of £12,570 (tax-free), tapered away by £1 for every £2 of income above £100,000, fully gone once income reaches £125,140. Taxable income above the allowance is taxed at **20% (basic rate)** up to £37,700 of taxable income, **40% (higher rate)** on taxable income from £37,700 to £112,570 (i.e. total income up to £125,140), and **45% (additional rate)** above that. *Worked example*: total income £60,000: taxable income = 60,000 - 12,570 = £47,430; the first £37,700 of that is taxed at 20% = £7,540; the remaining 9,730 is taxed at 40% = £3,892; total income tax = £11,432.

#### TAX-2 UK corporation tax and marginal relief
**UK corporation tax (2026/27)**: the **small profits rate** of **19%** applies where a company's taxable total profits are £50,000 or less; the **main rate** of **25%** applies above £250,000; between those thresholds, **marginal relief** tapers the effective rate smoothly using the formula: corporation tax = (profits x 25%) - (marginal relief fraction x (£250,000 - profits)), where the marginal relief fraction is 3/200. *Worked example*: taxable total profits £150,000 (between the two thresholds): tax before relief = 150,000 x 25% = £37,500; marginal relief = 3/200 x (250,000-150,000) = £1,500; corporation tax payable = 37,500 - 1,500 = £36,000 (an effective rate of 24.0%, between the 19% and 25% rates, as marginal relief is designed to achieve).

#### TAX-3 UK capital gains tax
**UK capital gains tax (2026/27)**: an individual's **annual exempt amount** is £3,000 (chargeable gains up to this in a tax year are tax-free); gains above it are taxed at **18%** to the extent the individual's taxable income and gains fall within their basic rate band, and **24%** on any excess (these are the current single set of rates applying uniformly across most chargeable asset types). *Worked example*: an individual has a chargeable gain of £18,000 on a disposal, with £20,000 of unused basic rate band remaining: taxable gain = 18,000 - 3,000 (annual exempt amount) = £15,000; since this falls entirely within the remaining basic rate band, CGT = 15,000 x 18% = £2,700.

#### TAX-4 VAT
**VAT**: a business must register for VAT once its taxable turnover exceeds £90,000 in a rolling 12-month period. **Output tax** is VAT charged on taxable supplies made (standard rate **20%** for most goods/services, a reduced rate of **5%** for some items, e.g. domestic energy, and a zero rate -- still taxable, but at 0% -- for items like most food and children's clothing); **input tax** is VAT paid on the business's own taxable purchases, reclaimable (subject to normal rules) against output tax. The **VAT return** liability = output tax charged - input tax reclaimable. *Worked example*: a VAT-registered business makes standard-rated sales of £50,000 (net of VAT) and standard-rated purchases of £30,000 (net of VAT) in a period: output tax = 50,000 x 20% = £10,000; input tax = 30,000 x 20% = £6,000; VAT payable to HMRC = 10,000 - 6,000 = £4,000.

## Explicitly not here
Applying these results within a single integrated business scenario is the capstone, S14. UK tax rates, thresholds and allowances change at least annually (normally from each 6 April, following a Budget/Autumn Statement) -- always check HMRC's current published rates before relying on a real-world calculation.
