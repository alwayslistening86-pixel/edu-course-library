# S02_Consumer_Theory - Lesson: Intermediate consumer theory

## Goal
The learner uses indifference curves and the marginal rate of substitution, derives the consumer's optimum from tangency with the budget line, decomposes a price change into substitution and income effects (the Slutsky equation), and states the axioms of revealed preference.

## Syllabus items taught here
- D217-1 - Indifference curves and the marginal rate of substitution
- D217-2 - The consumer's optimum: tangency and Cobb-Douglas demand
- D217-3 - Substitution and income effects; Giffen goods
- D217-4 - The Slutsky equation
- D217-5 - Revealed preference theory (WARP)

## How to teach this
Ask why a consumer's optimal bundle sits where an indifference curve is tangent to the budget line, not just anywhere on the budget line. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-1 Indifference curves and the marginal rate of substitution
An indifference curve joins bundles giving a consumer equal utility; a whole map of curves represents preferences (assumed complete, transitive and monotonic). The marginal rate of substitution (MRS) is the rate at which a consumer will trade one good for another while keeping utility constant, MRS = MUx/MUy (the ratio of marginal utilities), and equals the slope of the indifference curve. Diminishing MRS (the curve becomes flatter moving rightward) reflects convex preferences: consumers value variety, so are willing to give up less and less of y for each extra unit of x as x increases.

#### D217-2 The consumer's optimum: tangency and Cobb-Douglas demand
The consumer maximises utility subject to the budget constraint Pxx + Pyy = I. The optimum is where the indifference curve is tangent to the budget line: MRS = Px/Py (the rate the consumer is willing to trade equals the rate the market requires). For Cobb-Douglas utility U = x^a y^(1-a), the optimal demands are x* = aI/Px and y* = (1-a)I/Py -- the consumer spends a fixed share (a and 1-a) of income on each good regardless of prices. *Example:* a = 0.4, I = 200, Px = 5: x* = 16.0.

#### D217-3 Substitution and income effects; Giffen goods
A price fall has two effects. The substitution effect: the good is now relatively cheaper, so the consumer substitutes toward it, holding utility (real income) constant -- always negative (price down, quantity demanded from this effect up). The income effect: the price fall raises real purchasing power, changing quantity demanded because the consumer is effectively richer -- positive for a normal good, negative for an inferior good. A Giffen good is a special inferior good where the negative income effect outweighs the substitution effect, so quantity demanded falls when price falls (an upward-sloping demand curve over some range) -- rare in practice, requiring a good that is both strongly inferior and a large share of the budget.

#### D217-4 The Slutsky equation
The Slutsky equation formalises this: the total effect of a price change on quantity demanded = the substitution effect + the income effect, dx/dPx|total = dx/dPx|utility constant - x(dx/dI). For a normal good both terms typically work in the same direction (demand curve slopes down); for an inferior good they work against each other, and only a Giffen good has the income effect dominate.

#### D217-5 Revealed preference theory (WARP)
Revealed preference theory infers preferences from observed choices rather than assuming a utility function exists. The Weak Axiom of Revealed Preference (WARP): if bundle A is chosen when B was affordable, then B must never be chosen when A is affordable -- consistent choice behaviour. This lets economists test whether observed consumption data is consistent with utility maximisation without ever specifying the underlying utility function, extending A-level's purely descriptive treatment of consumer choice.

## Explicitly not here
Producer theory is S03.
