# S20_Geometric_and_Poisson_Distributions - Lesson: Geometric and Poisson distributions

## Goal
The learner models with geometric and Poisson distributions, stating conditions in context, calculates their probabilities, uses their means and variances, and adds independent Poisson variables.

## Syllabus items taught here
- 5.02f - Conditions for a geometric distribution
- 5.02g - Geometric probabilities, including P(X > x) = q^x
- 5.02h - Mean 1/p and variance (1 - p)/p^2 of a geometric distribution
- 5.02i - The Poisson distribution as a model for random events
- 5.02j - The Poisson formula P(X = x) = e^(-λ) λ^x / x!
- 5.02k - Calculating Poisson probabilities
- 5.02l - Conditions for a Poisson model
- 5.02m - Mean and variance of a Poisson distribution both equal λ
- 5.02n - The sum of independent Poisson variables is Poisson

## How to teach this
Ask how many rolls you expect to wait for a six, and why. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.02f Conditions for a geometric distribution
X ~ Geo(p) counts the number of trials up to and including the first success, when trials are independent with constant success probability p.

#### 5.02g Geometric probabilities, including P(X > x) = q^x
P(X = x) = (1 - p)^(x - 1) p; P(X > x) = (1 - p)^x (the first x trials all fail); P(X ≤ x) = 1 - (1 - p)^x. *Example:* rolling for a six: P(first six on the 4th roll) = (5/6)^3 (1/6) = 0.0965; P(more than 6 rolls needed) = (5/6)^6 = 0.335.

#### 5.02h Mean 1/p and variance (1 - p)/p^2 of a geometric distribution
E(X) = 1/p; Var(X) = (1 - p)/p^2. *Example:* p = 1/6: mean 6, variance 30.

#### 5.02i The Poisson distribution as a model for random events
The Poisson distribution models the number of random events in a fixed interval of time or space (calls per hour, flaws per metre) when events occur singly, independently and at a constant average rate. It also approximates B(n, p) for large n and small p (λ = np).

#### 5.02j The Poisson formula P(X = x) = e^(-λ) λ^x / x!
P(X = x) = e^(-λ) λ^x / x!, x = 0, 1, 2, ... *Example:* λ = 3.2: P(X = 2) = e^(-3.2)(3.2)^2/2.

#### 5.02k Calculating Poisson probabilities
Use the calculator's Poisson functions for cumulative probabilities. *Example:* X ~ Po(3.2): P(X = 2) = 0.2087; P(X ≤ 4) = 0.7806; P(X ≥ 5) = 0.2194. Rescale λ for a different interval: 3.2 per hour means 1.6 per half hour.

#### 5.02l Conditions for a Poisson model
Conditions (in context): events occur randomly, independently, singly (not simultaneously), at a constant average rate. Evidence for a Poisson model: sample mean ≈ sample variance.

#### 5.02m Mean and variance of a Poisson distribution both equal λ
For X ~ Po(λ): E(X) = Var(X) = λ.

#### 5.02n The sum of independent Poisson variables is Poisson
If X ~ Po(λ) and Y ~ Po(μ) are independent, X + Y ~ Po(λ + μ). *Example:* calls to two desks, Po(2) and Po(1.5) per hour: total ~ Po(3.5); P(total ≤ 2) = 0.3208.

## Explicitly not here
Continuous random variables are S21.
