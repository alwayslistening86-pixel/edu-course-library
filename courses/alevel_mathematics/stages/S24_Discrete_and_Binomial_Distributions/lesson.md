# S24_Discrete_and_Binomial_Distributions - Lesson: Discrete and binomial distributions

## Goal
The learner uses discrete distributions given by a table or formula, recognises when a binomial model is appropriate, and calculates binomial probabilities (exact and cumulative).

## Syllabus items taught here
- 2.04a - Simple finite discrete probability distributions given by a table or formula
- 2.04b - The binomial distribution as a model
- 2.04c - Calculating binomial probabilities

## How to teach this
Ask for the conditions under which 'the number of sixes in 10 rolls' can be modelled by a binomial distribution. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 2.04a Simple finite discrete probability distributions given by a table or formula
A discrete random variable X takes values with probabilities summing to 1. *Example:* P(X = x) = kx for x = 1, 2, 3, 4: k(1 + 2 + 3 + 4) = 1, so k = 1/10. P(X ≥ 3) = 0.3 + 0.4 = 0.7. A discrete uniform distribution gives each value equal probability.

#### 2.04b The binomial distribution as a model
X ~ B(n, p) models the number of successes in n trials when: there is a fixed number of trials; each is success or failure; trials are independent; and the probability of success p is constant. State the conditions **in context** ("each seed germinates independently of the others with the same probability 0.3"). The mean is np.

#### 2.04c Calculating binomial probabilities
P(X = r) = nCr p^r (1 - p)^(n - r). Use the calculator for cumulative values P(X ≤ r). *Example:* X ~ B(12, 0.3): P(X = 4) = 0.2311; P(X ≤ 4) = 0.7237; P(X ≥ 5) = 1 - P(X ≤ 4) = 0.2763; P(2 ≤ X ≤ 6) = P(X ≤ 6) - P(X ≤ 1) = 0.8764. Take care translating words: "more than 5" is X ≥ 6; "at most 5" is X ≤ 5.

## Explicitly not here
The normal distribution is S25.
