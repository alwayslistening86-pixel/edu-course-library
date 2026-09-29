# S14_Inequality_Innovation_and_Environment - Lesson: Inequality, innovation and environmental economics

## Goal
The learner calculates and interprets the Gini coefficient and Lorenz curve, distinguishes absolute from relative poverty measures, applies Schumpeterian creative destruction and market structure to innovation, evaluates carbon pricing instruments, and contrasts mainstream and pluralist/heterodox approaches to these issues (Doing Economics: inequalities, innovation and environment).

## Syllabus items taught here
- DD320-1 - The Lorenz curve and Gini coefficient
- DD320-2 - Absolute vs relative poverty
- DD320-3 - Innovation economics and the Arrow replacement effect
- DD320-4 - Carbon taxes vs cap-and-trade
- DD320-5 - Pluralism: mainstream vs heterodox approaches

## How to teach this
Ask what a Gini coefficient of 0 and a Gini coefficient of 1 would each mean for how income is shared across a population. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### DD320-1 The Lorenz curve and Gini coefficient
The Lorenz curve plots the cumulative share of income (or wealth) against the cumulative share of the population, ranked from poorest to richest; perfect equality is the 45-degree line (the poorest X% always hold X% of income). The Gini coefficient = (area between the line of perfect equality and the Lorenz curve) / (total area under the line of perfect equality), ranging from 0 (perfect equality) to 1 (perfect inequality, one person has everything). *Example (simplified):* if the poorest 50% hold 20% of income and the richest 50% hold 80%, the distribution is far from the 45-degree line -- a rough two-group Gini approximation gives G = (0.5-0.2) = 0.3 for this stylised split, illustrating the direction (higher gap from equality = higher Gini), though real Gini calculation uses the full, finely-grouped Lorenz curve rather than two points.

#### DD320-2 Absolute vs relative poverty
Absolute poverty is defined against a fixed real standard (e.g. the World Bank's international poverty line, a fixed purchasing-power-adjusted income needed for basic subsistence), so it can in principle fall to zero as a country develops. Relative poverty is defined relative to the income distribution within a country at a point in time (commonly, below 60% of median household income), so it persists even as absolute living standards rise, because it measures inequality/exclusion relative to a society's own norms rather than physical subsistence. Both are used in policy: absolute measures track basic material progress (especially internationally); relative measures capture social exclusion within a given society.

#### DD320-3 Innovation economics and the Arrow replacement effect
Schumpeter's 'creative destruction' (introduced descriptively at A-level) is examined more formally here: innovation by one firm can destroy the profits and market position of incumbents, and market structure itself shapes the incentive to innovate. The Arrow replacement effect: an incumbent monopolist has a weaker incentive to innovate than a challenger, because innovating partly replaces its own existing profit (whereas a challenger goes from zero to positive profit) -- suggesting more competitive threat can spur more, not less, innovation, complicating the simple 'monopoly profits fund R&D' story. Patents grant temporary monopoly power to reward innovation, trading off a static deadweight loss against a dynamic incentive to invest in R&D -- the core efficiency/incentive tension in intellectual property policy.

#### DD320-4 Carbon taxes vs cap-and-trade
Environmental economics revisits the externality/Pigouvian tax logic (S06) for the specific case of carbon emissions and compares two main instruments. A carbon tax fixes the price per tonne of CO2 (e.g. £t per tonne) and lets the quantity emitted adjust; a cap-and-trade scheme fixes the total quantity of permitted emissions (the cap) and lets the price of permits adjust via trading. Under certainty about costs, both can achieve the same efficient outcome (per the Pigouvian logic); they differ in which variable (price or quantity) is directly controlled, which matters when costs are uncertain -- a tax gives price certainty (useful for business planning) while cap-and-trade gives quantity certainty (useful for meeting a fixed environmental target, e.g. a legislated emissions ceiling). *Example:* a carbon tax of £80/tonne applied to a firm emitting 500 tonnes raises its costs by £40,000.

#### DD320-5 Pluralism: mainstream vs heterodox approaches
This module explicitly teaches pluralism in economics: comparing how mainstream (neoclassical) analysis and heterodox traditions (institutional economics, post-Keynesian economics, ecological economics) each frame inequality, innovation and the environment differently -- e.g. neoclassical analysis often treats inequality as a by-product of efficient factor rewards to be addressed (if at all) by redistribution after the fact, while institutional and post-Keynesian approaches are more likely to treat power, bargaining and institutions as directly shaping the pre-tax distribution of income itself. The QAA benchmark statement explicitly notes economics graduates should be aware that economic problems may admit multiple analytical approaches, not only the mainstream one.

## Explicitly not here
International and global economics is S15.
