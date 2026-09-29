# S21_Inheritance - Lesson: Inheritance and the chi-squared test

## Goal
The learner uses genetic terms, genetic diagrams for monohybrid and dihybrid crosses including codominance, multiple alleles, sex linkage, autosomal linkage and epistasis, uses simple probability, and applies the chi-squared test.

## Syllabus items taught here
- 3.7.1 - Inheritance (A-level only)
- MS 1.4 - Understand simple probability
- MS 1.9 - Select and use a statistical test

## How to teach this
Ask why two brown-eyed parents can have a blue-eyed child, and how likely it is. Teach from structure to function: what the molecule, cell or organ is like, how that lets it work, then an example or data to interpret. Use AQA's precise terms (e.g. 'water potential', 'complementary', 'tertiary structure') and insist on them in answers. Every numerical answer and statistic here was computed when the course was built.

#### 3.7.1 Inheritance (A-level only)
Terms: genotype (alleles present), phenotype (expression of genotype and its interaction with the environment), dominant, recessive, codominant alleles, homozygous and heterozygous. Genetic diagrams: monohybrid (Aa x Aa → 3:1), dihybrid (AaBb x AaBb → 9:3:3:1 if unlinked), codominance (e.g. roan cattle, blood groups), multiple alleles (ABO: I^A, I^B codominant, I^O recessive). Sex linkage: genes on the X chromosome; males (XY) have one copy, so recessive X-linked conditions (haemophilia, red-green colour blindness) are more common in males. Autosomal linkage: genes on the same autosome are inherited together unless separated by crossing over, giving more parental-type offspring than expected. Epistasis: one gene's alleles affect the expression of another (ratios such as 9:3:4 or 12:3:1). The chi-squared test compares observed and expected results: χ^2 = Σ(O - E)^2/E; degrees of freedom = number of categories - 1; if χ^2 is less than the critical value at p = 0.05, the difference is not significant: accept the null hypothesis (any difference is probably due to chance). *Example:* a dihybrid cross gives [315, 108, 101, 32]; expected 9:3:3:1 = [312.75, 104.25, 104.25, 34.75]; χ^2 = 0.47; with 3 degrees of freedom the critical value is 7.82, so the difference is not significant: the results fit a 9:3:3:1 ratio.

#### MS 1.4 Understand simple probability
Probability: the chance of each offspring genotype is independent of other offspring. Aa x Aa: probability of aa = 1/4; two children both aa = 1/4 x 1/4 = 1/16. Multiply probabilities of independent events; add those of mutually exclusive outcomes.

#### MS 1.9 Select and use a statistical test
Choose the test by the data: chi-squared for comparing observed frequencies in categories with expected values; Student's t-test for comparing the means of two sets of continuous data; a correlation coefficient (e.g. Spearman's rank) for a relationship between two variables. State a null hypothesis (no difference/no association), calculate the statistic, compare with the critical value at p = 0.05 and conclude.

## Explicitly not here
Hardy-Weinberg is S22.
