# S05_Game_Theory_and_Strategic_Behaviour - Lesson: Game theory and strategic behaviour

## Goal
The learner represents strategic interaction in normal form, finds dominant strategies and Nash equilibria, applies this to the prisoner's dilemma and oligopoly collusion, and derives the Cournot-Nash equilibrium for quantity-competing duopolists.

## Syllabus items taught here
- D217-13 - Game theory: normal form, dominant strategies, Nash equilibrium
- D217-14 - The prisoner's dilemma and oligopoly collusion
- D217-15 - Cournot duopoly and reaction functions
- D217-16 - Bertrand competition and Stackelberg leadership

## How to teach this
Ask why two firms that would both be better off colluding often end up competing instead. Teach each topic by building on what GCSE and A-level Economics already gave the learner: name the A-level idea it extends, then show the calculus/formal derivation or statistical technique that intermediate/degree-level economics adds. Work every numerical example with the learner predicting a step before it is shown; every figure in this course was computed with Python when the course was built. For current economic data (interest rates, inflation, growth, exchange rates), check the latest official sources (ONS, Bank of England, IMF) rather than relying on any figure used here as illustration.

#### D217-13 Game theory: normal form, dominant strategies, Nash equilibrium
Game theory formalises the interdependent decision-making A-level's oligopoly topic only describes qualitatively. A game in normal form specifies players, their strategies, and payoffs for every strategy combination. A dominant strategy gives a player the best payoff regardless of what rivals do. A Nash equilibrium is a strategy combination where no player can improve their payoff by unilaterally changing strategy, given the others' choices -- it need not be the jointly best outcome.

#### D217-14 The prisoner's dilemma and oligopoly collusion
The prisoner's dilemma: two players each choose to cooperate or defect; each is individually better off defecting regardless of the other's choice (defect is dominant for both), yet mutual defection leaves both worse off than mutual cooperation -- the unique Nash equilibrium is inefficient. This models oligopoly: firms would jointly profit more by colluding (restricting output, keeping prices high) but each has an individual incentive to cheat (undercut/overproduce) if it can, which is why cartels are often unstable without external enforcement (e.g. OPEC production quotas being breached).

#### D217-15 Cournot duopoly and reaction functions
Cournot duopoly: two firms simultaneously choose quantities, each maximising profit given a guess about the rival's output, taking price from the inverse market demand P = a - b(q1+q2). Solving each firm's first-order condition gives a reaction function; the Nash-Cournot equilibrium is where the reaction functions intersect. For symmetric firms with demand P = 100 - (q1+q2) and MC = 10, each firm's reaction function is qi = (90 - qj)/2; solving simultaneously gives the symmetric equilibrium q1 = q2 = 30, total output 60, price 40 -- more output and a lower price than under collusion (monopoly), but less than under perfect competition.

#### D217-16 Bertrand competition and Stackelberg leadership
Bertrand competition (price, not quantity, as the strategic variable) with identical products and constant marginal cost drives price down to marginal cost even with only two firms (the 'Bertrand paradox') -- undercutting is always profitable until price = MC. Sequential games (e.g. Stackelberg leadership, where one firm commits to a quantity first) are solved by backward induction: work out the follower's best response to each possible leader quantity, then find the leader's optimal choice given that reaction, which typically yields the leader a first-mover advantage (larger output and profit share than under simultaneous Cournot play).

## Explicitly not here
Welfare implications of market power are S06.
