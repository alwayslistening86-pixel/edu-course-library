# TAX_S03_Income_Tax_and_National_Insurance - Lesson: Income tax and national insurance contributions

## Goal
The learner calculates an individual's taxable income and income tax liability for 2026/27, including the personal allowance and its taper, and calculates employee, employer and self-employed National Insurance contributions.

## Syllabus items taught here
- TAX.3a - Income tax computation 2026/27
- TAX.3b - Personal allowance taper
- TAX.3c - Full income tax computation (worked)
- TAX.3d - Marriage allowance
- TAX.3e - Class 1 employee and employer NIC 2026/27
- TAX.3f - Class 4 self-employed NIC 2026/27

## How to teach this
Ask: why does someone earning £110,000 lose some of their personal allowance, while someone earning £90,000 does not? Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### TAX.3a Income tax computation 2026/27
**Income tax computation, 2026/27**: total income (employment income, trading profits, property income, savings and dividend income, etc.) less the **personal allowance** (**£12,570** for 2026/27, available to most UK taxpayers) gives taxable income, taxed through UK-wide bands (non-savings, non-dividend income): the first **£37,700** of taxable income at the **basic rate (20%)**, the next band (taxable income from £37,700 up to £112,570, i.e. total income from £50,270 to £125,140) at the **higher rate (40%)**, and taxable income/total income above £125,140 at the **additional rate (45%)**. The personal allowance itself has been frozen at £12,570 since 2021/22 (frozen further, to 2030/31, at the time of writing) - a 'fiscal drag' effect, since more income is pulled into higher bands as wages rise even though the allowance does not.

#### TAX.3b Personal allowance taper
**Personal allowance taper**: for total income above **£100,000**, the personal allowance is reduced by £1 for every £2 of income above that threshold, so it is fully withdrawn once income reaches £125,140 (£100,000 + 2 x £12,570). *Worked example*: total income £110,000. Excess over £100,000 = £10,000; allowance reduction = 10,000/2 = £5,000; tapered personal allowance = 12,570 - 5,000 = £7,570.

#### TAX.3c Full income tax computation (worked)
*Worked example, full income tax computation*: an employee has total income (salary) of £58,000 in 2026/27, below the £100,000 taper threshold, so the full personal allowance applies. Taxable income = 58,000 - 12,570 = £45,430. This falls partly in the basic rate band (£37,700) and partly above it: basic rate tax = 37,700 x 20% = £7,540; remaining taxable income at higher rate = 45,430 - 37,700 = £7,730; higher rate tax = 7,730 x 40% = £3,092. Total income tax = 7,540 + 3,092 = £10,632.

#### TAX.3d Marriage allowance
**Marriage allowance**: a spouse/civil partner who does not use all of their personal allowance may transfer a fixed fraction of it (10%, rounded up, i.e. £1,260 for 2026/27) to their spouse/civil partner, provided neither is a higher or additional rate taxpayer, reducing the recipient's tax bill by that transferred amount x 20%.

#### TAX.3e Class 1 employee and employer NIC 2026/27
**National Insurance contributions, 2026/27**: an **employee** pays **Class 1** NIC at **8%** on earnings between the primary threshold (**£12,570** a year) and the upper earnings limit (**£50,270** a year), and **2%** on earnings above the upper earnings limit. Their **employer** pays Class 1 (secondary) NIC at **15%** on earnings above the secondary threshold (**£5,000** a year) - with no upper limit. *Worked example*: an employee earns £45,000. Employee NIC = (45,000 - 12,570) x 8% = £2,594. Employer NIC = (45,000 - 5,000) x 15% = £6,000.

#### TAX.3f Class 4 self-employed NIC 2026/27
**Self-employed NIC**: **Class 4** NIC is paid by the self-employed on trading profits, at **6%** between the lower profits limit (**£12,570**) and the upper profits limit (**£50,270**), and **2%** above that. Compulsory **Class 2** NIC has been abolished for the self-employed (from 6 April 2024); those with profits below the Small Profits Threshold may still pay **voluntary Class 2** to protect their entitlement to the State Pension and other contributory benefits. *Worked example*: self-employed profits £40,000. Class 4 NIC = (40,000 - 12,570) x 6% = £1,646.

## Explicitly not here
Employment income specifics (benefits), trading income adjustments and partnership profit-splitting are TAX_S03 continued in practice questions; capital gains tax and inheritance tax are TAX_S04.
