# S23_Probability - Lesson: Probability

## Goal
The learner calculates probabilities for mutually exclusive and independent events using tree diagrams, Venn diagrams and two-way tables, finds conditional probabilities from first principles, and critiques probability models.

## Syllabus items taught here
- 2.03a - Mutually exclusive and independent events
- 2.03b - Diagrams to calculate probabilities
- 2.03c - Conditional probability using tree diagrams, Venn diagrams and two-way tables
- 2.03d - Conditional probability from first principles: P(A|B) = P(A and B)/P(B)
- 2.03e - Modelling with probability and critiquing assumptions

## How to teach this
Ask whether 'rain today' and 'rain tomorrow' are independent, and what would make them so. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 2.03a Mutually exclusive and independent events
Mutually exclusive: P(A and B) = 0, so P(A or B) = P(A) + P(B). Independent: P(A and B) = P(A) × P(B). In general P(A ∪ B) = P(A) + P(B) - P(A ∩ B). *Example:* P(A) = 0.4, P(B) = 0.5, independent: P(A ∩ B) = 0.2, P(A ∪ B) = 0.7. Test for independence by checking the product rule.

#### 2.03b Diagrams to calculate probabilities
Tree diagrams (multiply along branches, add the paths you need), Venn diagrams (fill in the intersection first), two-way tables and sample-space diagrams. *Example:* two dice: P(total 8) = 5/36 from the 6 × 6 sample space.

#### 2.03c Conditional probability using tree diagrams, Venn diagrams and two-way tables
Conditional probability on a tree: the second-stage branches are conditional on the first. In a Venn diagram, P(A | B) = P(A ∩ B)/P(B): restrict attention to the B circle. In a two-way table, use the row or column total of the given condition. *Example:* of 200 students, 120 take maths and 70 take physics, and 50 take both: P(physics | maths) = 50/120 = 5/12.

#### 2.03d Conditional probability from first principles: P(A|B) = P(A and B)/P(B)
P(A | B) = P(A ∩ B)/P(B). A and B are independent exactly when P(A | B) = P(A). *Example:* a test is 95% accurate for people with a disease (prevalence 2%) and gives false positives for 4% of healthy people. P(positive) = 0.02 × 0.95 + 0.98 × 0.04 = 0.0582; P(disease | positive) = 0.019/0.0582 ≈ 0.326: most positives are false.

#### 2.03e Modelling with probability and critiquing assumptions
Probability models rest on assumptions (equally likely outcomes, independence, constant probability). Critique them: are trials really independent (a player's confidence may change after a win)? Is the probability constant? Suggest the likely effect of more realistic assumptions.

## Explicitly not here
Probability distributions are S24.
