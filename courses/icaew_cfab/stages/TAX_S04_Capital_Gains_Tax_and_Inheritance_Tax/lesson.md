# TAX_S04_Capital_Gains_Tax_and_Inheritance_Tax - Lesson: Capital gains tax and inheritance tax

## Goal
The learner identifies chargeable persons, assets and disposals, calculates a straightforward chargeable gain and an individual's capital gains tax, and explains the key principles of inheritance tax at an introductory level.

## Syllabus items taught here
- TAX.4a - CGT chargeable persons, assets and disposals
- TAX.4b - Calculating a chargeable gain
- TAX.4c - Total taxable gains and CGT liability
- TAX.4d - Inheritance tax key principles: PETs and CLTs
- TAX.4e - Lifetime and death IHT calculations (principles)

## How to teach this
Ask: if someone sells their only home at a large profit, do they normally pay capital gains tax on it? Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### TAX.4a CGT chargeable persons, assets and disposals
**Capital gains tax (CGT) - persons, assets and disposals**: CGT is charged on **chargeable persons** (broadly, UK-resident individuals, personal representatives and trustees - companies instead pay corporation tax on their chargeable gains) who make a **chargeable disposal** (a sale, gift, or other disposal, but not a disposal on death - assets instead pass to the estate) of a **chargeable asset**. Some assets are **exempt** (e.g. an individual's only or main private residence, in most circumstances; UK government gilts; and, importantly, most personal chattels sold for £6,000 or less).

#### TAX.4b Calculating a chargeable gain
**Calculating a chargeable gain**: gain = disposal proceeds (or market value, for a gift or a disposal to a connected person) less **allowable costs** (original acquisition cost, plus incidental costs of acquisition and disposal, plus qualifying capital enhancement expenditure). *Worked example*: an asset bought for £20,000 (plus £500 acquisition costs) is sold for £35,000 (less £700 disposal costs). Gain = (35,000 - 700) - (20,000 + 500) = £13,800.

#### TAX.4c Total taxable gains and CGT liability
**Total taxable gains and CGT liability**: an individual's chargeable gains in a tax year (after allowable losses) are compared against their **annual exempt amount** (a fixed tax-free allowance for gains each year, separate from the income tax personal allowance); any excess is taxable, generally at a lower rate on gains falling within the individual's remaining basic rate band and a higher rate on gains above it (the specific CGT rates differ from income tax rates and depend on the type of asset - the syllabus focuses on the overall computational approach rather than requiring every current rate to be memorised in detail).

#### TAX.4d Inheritance tax key principles: PETs and CLTs
**Inheritance tax (IHT) - key principles**: IHT is charged mainly on a person's **estate on death** and on certain **lifetime transfers**. Most straightforward lifetime gifts to individuals are **Potentially Exempt Transfers (PETs)** - entirely exempt if the donor survives 7 years from the gift, but becoming chargeable (with **taper relief** reducing the tax, not the value transferred, on a sliding scale for gifts made 3-7 years before death) if the donor dies within 7 years. Gifts to most trusts, in contrast, are **Chargeable Lifetime Transfers (CLTs)**, potentially taxed immediately as well as being reconsidered on death within 7 years.

#### TAX.4e Lifetime and death IHT calculations (principles)
**Lifetime and death tax calculations (principles)**: a lifetime transfer's value, after available exemptions (e.g. the annual exemption, and exemptions for gifts to a spouse/civil partner or to charity) and the available **nil rate band** (a threshold below which no IHT is due, cumulating chargeable transfers made in the prior 7 years), is taxed at the lifetime rate on a CLT if it exceeds the nil rate band; on death, the estate's value (after exemptions and reliefs, and after bringing in any earlier PETs/CLTs within 7 years of death, which use up the nil rate band first) above the available nil rate band is taxed at the death rate. Married couples/civil partners can generally transfer any unused nil rate band to the survivor, and a further **residence nil rate band** may be available where a main residence passes to direct descendants, subject to its own conditions and tapering for larger estates.

## Explicitly not here
Corporation tax (including a company's own chargeable gains) is TAX_S05.
