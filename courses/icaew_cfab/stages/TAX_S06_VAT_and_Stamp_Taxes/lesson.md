# TAX_S06_VAT_and_Stamp_Taxes - Lesson: VAT and stamp taxes

## Goal
The learner classifies supplies for VAT purposes, applies the VAT registration rules, determines the tax point, calculates VAT payable/repayable, and explains the basics of stamp taxes.

## Syllabus items taught here
- TAX.6a - Classifying supplies for VAT
- TAX.6b - Implications of supply classification for input VAT
- TAX.6c - VAT registration and deregistration
- TAX.6d - Tax point determination
- TAX.6e - Calculating VAT payable/repayable
- TAX.6f - VAT alternative schemes
- TAX.6g - Stamp taxes

## How to teach this
Ask: if a business sells only zero-rated goods (like most food), does it ever need to register for VAT, and can it still reclaim VAT on its own costs? Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### TAX.6a Classifying supplies for VAT
**Classifying supplies**: **standard-rated** supplies (most goods/services) are taxed at **20%**; **reduced-rated** supplies (e.g. domestic energy) at **5%**; **zero-rated** supplies (e.g. most food, children's clothing, books) at **0%** - critically, zero-rated is still a **taxable** supply (VAT is charged, just at 0%), so input VAT on related costs remains recoverable; **exempt** supplies (e.g. most insurance, many financial services, some education) are entirely outside the VAT system on the output side, and input VAT relating to exempt supplies generally cannot be reclaimed; supplies genuinely **outside the scope** of VAT (e.g. some transactions outside the UK, or a gift of a business as a going concern in some circumstances) don't count towards turnover at all.

#### TAX.6b Implications of supply classification for input VAT
**Implications of the classification**: a business making only exempt supplies cannot register for VAT and cannot recover input VAT on its costs (an absolute cost to it), whereas a business making zero-rated supplies can (and often should) register, since it charges no output VAT but can still recover its input VAT, potentially generating a VAT repayment. A business making a mix of taxable (standard/reduced/zero-rated) and exempt supplies is **partially exempt**, and can normally only recover a proportion of its input VAT relating to overheads, calculated by an apportionment method.

#### TAX.6c VAT registration and deregistration
**VAT registration**: a business must register for VAT if its taxable turnover (excluding exempt and outside-the-scope supplies) for the previous 12 months exceeds the registration threshold of **£90,000**, or is expected to exceed it in the next 30 days alone; a business below the threshold may still **voluntarily** register (e.g. to recover input VAT, or to appear VAT-registered to business customers). A registered business may **deregister** if it can satisfy HMRC that its taxable turnover for the next 12 months will not exceed the deregistration threshold (set below the registration threshold).

#### TAX.6d Tax point determination
**Tax point**: the **basic tax point** is normally the date goods are made available/services are completed; this is overridden by an **actual tax point** if a VAT invoice is issued, or payment received, before the basic tax point (whichever is earlier becomes the tax point), or if a VAT invoice is issued within 14 days after the basic tax point (then that invoice date is used instead) - the tax point determines which VAT period/return a supply falls into.

#### TAX.6e Calculating VAT payable/repayable
**Calculating VAT payable/repayable**: output VAT (charged on sales) less input VAT (reclaimable on purchases/expenses used for taxable supplies) = VAT payable to HMRC (if output exceeds input) or repayable by HMRC (if input exceeds output). *Worked example*: standard-rated sales (VAT-exclusive) £80,000: output VAT = 80,000 x 20% = £16,000. Standard-rated purchases/expenses (VAT-exclusive) £35,000: input VAT = 35,000 x 20% = £7,000. VAT payable to HMRC = 16,000 - 7,000 = £9,000.

#### TAX.6f VAT alternative schemes
**VAT alternative schemes** (introductory awareness): the **Flat Rate Scheme** lets a small business pay VAT as a fixed percentage of its VAT-inclusive turnover (simplifying record-keeping, but not always the cheapest option, since input VAT is generally not separately reclaimed); the **Cash Accounting Scheme** accounts for VAT when cash is actually received/paid rather than on invoice dates (helping cash flow and automatically giving bad debt relief); the **Annual Accounting Scheme** allows one VAT return a year with payments on account through the year, reducing administration.

#### TAX.6g Stamp taxes
**Stamp taxes**: **Stamp Duty Land Tax (SDLT)** is charged on land/property transactions in England and Northern Ireland (Scotland and Wales have their own equivalents), generally at rates increasing with the property's value (and, for the acquisition of additional residential property, a surcharge); **Stamp Duty** (on physical stock transfer forms) and **Stamp Duty Reserve Tax (SDRT)** (on paperless/electronic share transactions) apply to transfers of shares in UK companies, generally at a standard rate on the consideration paid, though this differs by transaction type and current rate rules should always be checked at the time of a transaction.

## Explicitly not here
Income tax, NIC and corporation tax computations are TAX_S03/TAX_S05.
