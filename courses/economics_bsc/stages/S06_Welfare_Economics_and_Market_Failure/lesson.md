# S06_Welfare_Economics_and_Market_Failure - Lesson: Welfare economics and market failure

## Goal
The learner explains Pareto efficiency and the first welfare theorem, derives the Pigouvian tax that internalises an externality, states the Coase theorem and its conditions, and derives the Samuelson condition for efficient public-good provision.

## Syllabus items taught here
- D217-17 - Pareto efficiency and the first welfare theorem
- D217-18 - Externalities and the Pigouvian tax
- D217-19 - The Coase theorem
- D217-20 - Public goods, free-riding and the Samuelson condition

## How to teach this
Ask why a perfectly competitive market, left alone, is efficient in the textbook sense -- and what has to be true for that result to hold. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-17 Pareto efficiency and the first welfare theorem
A Pareto-efficient allocation is one where no one can be made better off without making someone else worse off. The first fundamental welfare theorem: under certain conditions (perfect competition, complete markets, no externalities, no public goods, no information asymmetries), any competitive equilibrium is Pareto efficient. This formalises A-level's 'markets allocate resources efficiently' claim and, crucially, makes explicit exactly which conditions must hold -- conditions that real markets routinely violate, which is why market failure matters.

#### D217-18 Externalities and the Pigouvian tax
An externality drives a wedge between private and social cost/benefit. For a negative production externality, marginal social cost MSC = MC + MEC (marginal external cost), and the free market produces where P = MC (too much, since the true social optimum is where P = MSC). A Pigouvian tax set equal to the marginal external cost at the socially optimal quantity, t = MEC(Q*), internalises the externality: after the tax, firms face MC+t = MSC, so the market outcome coincides with the social optimum. *Example:* MC = 2Q, demand P = 100-Q, MEC = 20 (constant): market equilibrium (P=MC) at 100-Q=2Q, Q=33.3; social optimum (P=MSC=2Q+20) at 100-Q=2Q+20, Q=26.7; optimal tax = £20 per unit.

#### D217-19 The Coase theorem
The Coase theorem: if property rights are clearly defined and transaction costs are zero, private bargaining between the affected parties will reach the efficient outcome regardless of who initially holds the property right (though it affects who pays whom) -- an alternative to government intervention (taxes/regulation) for correcting externalities. In practice, transaction costs (many affected parties, information costs, enforcement difficulty) are rarely zero, especially for diffuse externalities like pollution or climate change, which is why Pigouvian taxes and regulation remain the standard tools where bargaining is impractical.

#### D217-20 Public goods, free-riding and the Samuelson condition
A public good is non-excludable (can't stop people who don't pay from consuming it) and non-rival (one person's consumption doesn't reduce another's). This causes the free-rider problem: since no one can be excluded, individuals under-report their true willingness to pay, and the good is under-provided by private markets. The efficient quantity of a pure public good satisfies the Samuelson condition: the sum of individuals' marginal rates of substitution (marginal willingness to pay) equals marginal cost, sum(MRSi) = MC -- unlike a private good, where each individual's MRS alone equals MC.

## Explicitly not here
This closes Block 1 (intermediate microeconomics); Block 2 begins with macroeconomics in S07.
