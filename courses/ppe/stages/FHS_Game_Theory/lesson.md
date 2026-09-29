# FHS_Game_Theory - Lesson: Game Theory (Economics optional paper)

## Goal
The learner recognises the underlying strategic structure of an unfamiliar applied problem, identifies the correct solution concept, and works through the actual mathematics, answering both parts of the paper as its own structure requires.

## Syllabus items taught here
- GT.1 - Strategic-form games and dominant strategies: learn and apply: strategic-form games and dominant strategies
- GT.2 - Nash equilibrium: learn and apply: nash equilibrium
- GT.3 - Extensive-form games and subgame perfect equilibrium: learn and apply: extensive-form games and subgame perfect equilibrium
- GT.4 - Repeated games and cooperation: learn and apply: repeated games and cooperation
- GT.5 - Games with incomplete information (Bayesian games): learn and apply: bayesian games
- GT.6 - Bargaining theory: learn and apply: bargaining theory
- GT.7 - Auction theory: learn and apply: auction theory
- GT.8 - Evolutionary game theory: learn and apply: evolutionary game theory
- GT.9 - Global games and learning models: learn and apply: global games and learning models
- GT.10 - Applications in political science and exam technique: learn and apply: applications in political science and exam technique

## How to teach this
Open with the founding example: "Two suspects are held separately. Each can stay silent or betray the other. If both stay silent, both get light sentences. If both betray, both get moderate sentences. If one betrays and the other stays silent, the betrayer goes free and the silent one gets a heavy sentence. Individually, betraying is the better choice whatever the other does - yet if both reason this way, both do worse than if they'd cooperated. This is the Prisoner's Dilemma, and it's the starting point for almost everything in this paper." Note the paper's own structure: it is set in two parts, and candidates must show knowledge on both - build the teaching plan so foundational solution concepts (Part-one style) and applications (Part-two style) both get real depth.

#### GT.1 Strategic-form games and dominant strategies
A strategic-form (normal-form) game specifies players, their possible strategies, and the payoff each receives for every combination of strategies chosen, usually shown as a payoff matrix. A dominant strategy gives a player the best payoff regardless of what any other player does - in the Prisoner's Dilemma, betraying strictly dominates staying silent for each player individually, even though mutual silence would make both players better off. Teach the learner to build a payoff matrix from a word problem and check systematically for dominant strategies before reaching for equilibrium concepts, since a dominant-strategy equilibrium is the simplest and most robust prediction when one exists.

#### GT.2 Nash equilibrium
A Nash equilibrium is a set of strategies, one per player, such that no player can improve their own payoff by unilaterally changing strategy, given what everyone else is doing. In the Prisoner's Dilemma, mutual betrayal is the unique Nash equilibrium, even though mutual silence would make both players better off - the gap between individually rational choices and collectively better outcomes is the paper's recurring theme, not a one-off curiosity. Teach the learner the mechanical check (best-response analysis: for each strategy profile, does either player have an incentive to deviate) and to find equilibria in mixed strategies where no pure-strategy equilibrium exists.

#### GT.3 Extensive-form games and subgame perfect equilibrium
Extensive-form games represent situations with sequential moves as a game tree, which matters because timing and information change what is rational: a threat only works if it is genuinely credible. Subgame perfect equilibrium refines Nash equilibrium by requiring that strategies remain rational at every point in the game (every subgame), not just along the equilibrium path, ruling out equilibria that rely on incredible threats a rational player would never actually carry out once the moment to act arrived. Teach the learner to solve extensive-form games by backward induction, and to use it explicitly to identify and discard non-credible threats in a worked example (e.g. a market-entry deterrence game).

#### GT.4 Repeated games and cooperation
When the Prisoner's Dilemma (or a similar game) is played repeatedly rather than once, cooperation can become individually rational even though it is not in the one-shot game: strategies like tit-for-tat (cooperate first, then mirror the opponent's last move) can sustain cooperation as an equilibrium if players value future payoffs enough (the folk theorem shows a wide range of outcomes, including cooperative ones, can be sustained as equilibria of a sufficiently patient repeated game). Teach the learner why an indefinitely or infinitely repeated game differs sharply from a known, finite number of repetitions (where backward induction from the known final round can unravel cooperation entirely) - a genuinely important and often-missed distinction.

#### GT.5 Games with incomplete information (Bayesian games)
Real strategic situations often involve incomplete information - players do not know each other's payoffs, types, or preferences with certainty. Bayesian games model this using probability distributions over an opponent's possible "types," and Bayesian Nash equilibrium requires each player's strategy to be a best response given their beliefs about others' types, with those beliefs updated rationally (via Bayes' rule) as the game unfolds and new information arrives. Teach the learner to set up a simple Bayesian game (e.g. a seller who may be high- or low-quality, unknown to the buyer) and solve for equilibrium beliefs and strategies together, since neither can be solved independently of the other.

#### GT.6 Bargaining theory
Bargaining theory analyses how a surplus (a gain from trade or cooperation) gets divided between parties, depending on their relative patience, outside options (what each party gets if bargaining fails) and bargaining power. The Nash bargaining solution and Rubinstein's alternating-offers model are the paper's standard tools: the alternating-offers model shows how a specific division emerges from parties' discount factors (how much they value a dollar now versus later) even without appeal to arbitrary "fairness" assumptions. Teach the learner to solve a simple alternating-offers bargaining problem and to explain intuitively why greater patience (a higher discount factor) improves a party's bargained share.

#### GT.7 Auction theory
Auction theory studies how different auction formats - first-price sealed-bid, second-price sealed-bid (Vickrey), English (ascending), Dutch (descending) - affect bidders' optimal strategies and the seller's expected revenue. A key result is that in a second-price auction, bidding one's true value is a weakly dominant strategy (truth-telling), while in a first-price auction bidders should optimally shade their bid below their true value. Under fairly general conditions, the revenue equivalence theorem shows several of these formats yield the same expected revenue to the seller, a genuinely surprising result given how different the formats look. Teach the learner to derive the optimal bidding strategy in at least one format and to state the revenue equivalence result's key assumptions.

#### GT.8 Evolutionary game theory
Evolutionary game theory reinterprets equilibrium concepts biologically: strategies "compete" via reproductive success (or, in social/economic applications, imitation and payoff-driven adoption) rather than conscious individual reasoning, giving game theory genuine applications well beyond deliberate human strategic choice. The evolutionarily stable strategy (ESS) concept requires a strategy to resist invasion by any alternative "mutant" strategy once established in a population - a dynamic, population-level refinement related to, but distinct from, Nash equilibrium. Teach the learner to work through the Hawk-Dove game as the standard worked example and to explain what an ESS adds beyond a static Nash equilibrium.

#### GT.9 Global games and learning models
Global games examine how equilibria emerge, or fail to, when players have only noisy private information about a common underlying state (rather than full common knowledge), which can select a unique equilibrium in settings (like bank-run or currency-crisis models) that would otherwise have multiple equilibria under full common knowledge. Learning models examine how players adjust strategies gradually through repeated play and observed outcomes - converging toward equilibrium behaviour over time through trial and adaptation rather than reasoning to equilibrium instantly and fully rationally from the outset. Teach the learner why these approaches matter: they relax the demanding common-knowledge and full-rationality assumptions underlying GT.1-GT.2, and often produce sharper, more determinate predictions as a result.

#### GT.10 Applications in political science and exam technique
The paper's applications extend explicitly to political science (games in political science - such as models of voting, coalition formation, or conflict as strategic interaction), alongside the bargaining, auction, evolutionary and learning applications already covered. The paper is set in two parts, and candidates must show knowledge on both parts - meaning revision and practice must cover foundational solution concepts (GT.1-GT.5) and applied topics (GT.6-GT.9) with comparable depth, since strong performance on only one part will not compensate for a weak second part. Teach the learner, as exam technique, to always state which solution concept they are applying and why it is the right one for the strategic structure identified, since the paper explicitly rewards recognising structure in an unfamiliar setting, not just retelling a memorised classic example.

## Explicitly not here
The paper explicitly assumes prior study of Microeconomics (a Prelims/second-year prerequisite, see ECOP.MI1-MI3); this stage does not re-derive basic consumer or producer theory.
