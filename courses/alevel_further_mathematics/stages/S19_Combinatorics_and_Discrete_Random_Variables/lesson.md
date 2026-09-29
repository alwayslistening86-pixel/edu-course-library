# S19_Combinatorics_and_Discrete_Random_Variables - Lesson: Combinatorial probability and discrete random variables

## Goal
The learner counts arrangements and selections (with repetition and restrictions) to find probabilities, works with discrete distributions including E(X), Var(X) and E(g(X)), applies linear coding, and uses the binomial and discrete uniform distributions' mean and variance.

## Syllabus items taught here
- 5.01a - Probabilities using permutations and combinations (nPr, nCr)
- 5.01b - Probabilities in selection and arrangement problems, including repetition and restriction
- 5.02a - Discrete probability distributions
- 5.02b - Expectation and variance of a discrete random variable, including E(g(X))
- 5.02c - Effect of linear coding on the mean and variance of a random variable
- 5.02d - Mean np and variance np(1 - p) of a binomial distribution
- 5.02e - The discrete uniform distribution: conditions, probabilities, mean and variance

## How to teach this
Ask how many ways the letters of STRAIT can be arranged, and why it isn't 6!. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.01a Probabilities using permutations and combinations (nPr, nCr)
nPr = n!/(n - r)! ordered selections; nCr = n!/(r!(n - r)!) unordered. Probabilities by counting equally likely outcomes. *Example:* 3 people chosen from 5 men and 4 women: P(2 men, 1 woman) = 5C2 x 4C1 / 9C3 = 40/84 = 10/21.

#### 5.01b Probabilities in selection and arrangement problems, including repetition and restriction
Arrangements in a line: n! for distinct objects; divide by the factorials of repeated letters (STRAIT has two Ts: 6!/2! = 360). Restrictions: treat items that must be together as a block (multiply by internal arrangements); for 'not together', use total minus together, or place the others and slot into gaps. *Example:* P(the two Ts are adjacent in a random arrangement of STRAIT) = (5!)/(6!/2!) = 120/360 = 1/3. Selection problems: 'at least one' is often easiest as 1 - P(none).

#### 5.02a Discrete probability distributions
A discrete random variable's distribution is a table or formula of P(X = x), with probabilities summing to 1. Construct one from a situation (e.g. the larger score when two dice are thrown).

#### 5.02b Expectation and variance of a discrete random variable, including E(g(X))
E(X) = Σ x P(X = x); Var(X) = E(X^2) - (E(X))^2 = Σ x^2 P(X = x) - μ^2; E(g(X)) = Σ g(x)P(X = x). *Example:* X takes 1, 2, 3 with probabilities 0.2, 0.5, 0.3: E(X) = 2.1, E(X^2) = 4.9, Var(X) = 4.9 - 4.41 = 0.49; E(1/X) = 0.2 + 0.25 + 0.1 = 0.55.

#### 5.02c Effect of linear coding on the mean and variance of a random variable
E(aX + b) = aE(X) + b; Var(aX + b) = a^2 Var(X). *Example:* winnings W = 5X - 3 with E(X) = 2.1, Var(X) = 0.49: E(W) = 7.5, Var(W) = 12.25.

#### 5.02d Mean np and variance np(1 - p) of a binomial distribution
For X ~ B(n, p): E(X) = np, Var(X) = np(1 - p). *Example:* B(40, 0.3): mean 12, variance 8.4, sd 2.90. Use these to check whether a binomial model fits data (compare the sample mean and variance).

#### 5.02e The discrete uniform distribution: conditions, probabilities, mean and variance
Discrete uniform on 1, ..., n: P(X = r) = 1/n; E(X) = (n + 1)/2; Var(X) = (n^2 - 1)/12. Conditions: finitely many equally likely values. *Example:* a fair 8-sided die: mean 4.5, variance 63/12 = 5.25. For values a, a + 1, ..., b, shift.

## Explicitly not here
Geometric and Poisson distributions are S20.
