# FA_S05_Non_Current_Assets_Depreciation_and_Intangibles - Lesson: Non-current assets, depreciation and intangibles

## Goal
The learner accounts for the acquisition and disposal of tangible non-current assets, calculates depreciation under the straight-line and reducing balance methods, and accounts for intangible non-current assets and amortisation.

## Syllabus items taught here
- FA.D4 - Tangible non-current assets
- FA.D5 - Depreciation
- FA.D6 - Intangible non-current assets and amortisation

## How to teach this
Ask: 'A business buys a £20,000 machine expected to last 5 years. Should the whole £20,000 be an expense in year 1?' Use the answer to introduce depreciation as spreading a cost, not a valuation exercise. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### FA.D4 Tangible non-current assets
**Tangible non-current assets** (IAS 16 Property, Plant and Equipment) are recognised initially at **cost**: purchase price plus directly attributable costs of bringing the asset to the location and condition necessary for it to operate as intended (e.g. delivery, installation, professional fees) - but not general overheads or staff training costs. Subsequent expenditure that improves the asset (extends its life, increases capacity) is **capitalised** (added to the asset's cost); expenditure that merely maintains the asset in its existing condition (repairs) is expensed. On **disposal**, the asset (and its accumulated depreciation) is removed from the ledger, and a **profit or loss on disposal** = sale proceeds - carrying amount (cost - accumulated depreciation at disposal). *Worked example*: a machine costing £40,000 has accumulated depreciation of £28,000 at disposal (carrying amount £{40000 - 28000:,}) and is sold for £15,000: profit on disposal = 15,000 - {40000 - 28000:,} = £{15000 - (40000 - 28000):,} (a profit, since proceeds exceed carrying amount).

#### FA.D5 Depreciation
**Depreciation** systematically allocates an asset's depreciable amount (cost less residual value) over its useful life, reflecting consumption of economic benefit - it is not an attempt to show current market value. **Straight-line**: (cost - residual value) / useful life, an equal charge each year. **Reducing balance**: a fixed percentage applied each year to the asset's carrying amount (cost less accumulated depreciation to date), giving a higher charge in early years and a lower charge later. *Worked example, straight-line*: cost £50,000, residual value £5,000, useful life 5 years: annual depreciation = (50,000 - 5,000)/5 = £{(50000 - 5000) / 5:,.0f}/year. *Worked example, reducing balance*: cost £30,000, rate 20% per year. Year 1 depreciation = 30,000 x 0.20 = £{30000 * 0.20:,.0f}, carrying amount at end of year 1 = 30,000 - {30000 * 0.20:,.0f} = £{30000 - 30000 * 0.20:,.0f}. Year 2 depreciation = {30000 - 30000 * 0.20:,.0f} x 0.20 = £{(30000 - 30000 * 0.20) * 0.20:,.0f}, carrying amount at end of year 2 = £{(30000 - 30000 * 0.20) * 0.80:,.0f}.

#### FA.D6 Intangible non-current assets and amortisation
**Intangible non-current assets** (IAS 38) are identifiable non-monetary assets without physical substance, e.g. purchased patents, licences, trademarks and (only if purchased, not internally generated) goodwill. **Research** costs are always expensed as incurred (too uncertain to recognise as an asset); **development** costs are capitalised as an intangible asset only once strict criteria are met (technical feasibility, intention and ability to complete and use/sell it, probable future economic benefit, and reliable cost measurement) - before that point, development costs are also expensed. An intangible asset with a **finite** useful life is **amortised** (the same idea as depreciation, usually straight-line) over that life; one with an **indefinite** useful life (rare) is not amortised but tested annually for impairment. *Worked example*: a purchased patent costs £60,000 with a 10-year useful life: annual amortisation = 60,000/10 = £{60000 / 10:,.0f}/year.

## Explicitly not here
Accruals, prepayments, receivables, payables, provisions and capital structure are FA_S06.
