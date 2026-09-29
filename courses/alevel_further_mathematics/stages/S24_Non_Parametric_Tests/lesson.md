# S24_Non_Parametric_Tests - Lesson: Non-parametric tests

## Goal
The learner chooses and carries out sign tests, Wilcoxon signed-rank tests (single-sample and paired) and Wilcoxon rank-sum tests, including large-sample normal approximations.

## Syllabus items taught here
- 5.07a - Non-parametric tests: when they are useful and choosing one
- 5.07b - The basis of the sign test, Wilcoxon signed-rank test and Wilcoxon rank-sum test
- 5.07c - Single-sample sign test and Wilcoxon signed-rank test for a median
- 5.07d - Paired-sample versus two-sample tests
- 5.07e - Paired-sample sign test, Wilcoxon matched-pairs signed-rank test and Wilcoxon rank-sum test
- 5.07f - Normal approximations for the Wilcoxon tests with large samples

## How to teach this
Ask what you can test if the data are clearly not normal and the sample is small. Work each example with the learner line by line, insist on full working (OCR awards method marks and 'show that' questions need every step), and allow a calculator as the exam does. Every numerical answer here was computed with sympy or scipy when the course was built.

#### 5.07a Non-parametric tests: when they are useful and choosing one
Non-parametric tests make no assumption about the population's distribution (beyond, e.g., symmetry for Wilcoxon), so they're used when normality is doubtful or the data are ranks. They test medians rather than means. They're generally less powerful than parametric tests when the parametric assumptions hold.

#### 5.07b The basis of the sign test, Wilcoxon signed-rank test and Wilcoxon rank-sum test
**Sign test:** count values above and below the hypothesised median; under H0 the count of + signs ~ B(n, 0.5). **Wilcoxon signed-rank:** rank the absolute differences from the median, sum the ranks of positive (W+) and negative (W-) differences; the test statistic T is the smaller (or the one relevant to H1); assumes a symmetric distribution. **Wilcoxon rank-sum (Mann-Whitney):** rank the two samples together; W is the sum of the ranks of the smaller sample (use the smaller of W and m(m + n + 1) - W). Tables give critical values; reject H0 if the statistic is less than or equal to the critical value.

#### 5.07c Single-sample sign test and Wilcoxon signed-rank test for a median
*Example:* is the median of [12.1, 13.4, 11.2, 14.8, 12.9, 15.2, 13.9, 16.0, 11.8, 14.4] greater than 12.5? Differences from 12.5: 7 positive, 3 negative. Sign test: P(X ≥ 7) for B(10, 0.5) = 0.1719 > 0.05: not significant. Signed-rank: W+ = 45.5, W- = 9.5; T = W- = 9.5; for n = 10, one-tailed 5%, the critical value is 10, so reject H0. The signed-rank test uses more information than the sign test.

#### 5.07d Paired-sample versus two-sample tests
Paired samples: two measurements on the same individuals (before/after), so test the differences (one-sample methods on d). Two independent samples: different individuals in each group, so use the rank-sum test.

#### 5.07e Paired-sample sign test, Wilcoxon matched-pairs signed-rank test and Wilcoxon rank-sum test
Paired-sample sign test or Wilcoxon matched-pairs signed-rank test: apply the single-sample methods to the differences, with H0: median difference = 0. Rank-sum test: H0: the two populations are identical (or have equal medians). *Example:* samples of 5 and 6: rank all 11 values together, W = sum of ranks of the sample of 5; compare the smaller of W and 5(12) - W with the table value.

#### 5.07f Normal approximations for the Wilcoxon tests with large samples
For large samples: signed-rank T is approximately N(n(n + 1)/4, n(n + 1)(2n + 1)/24); rank-sum W (smaller sample size m, other n) is approximately N(m(m + n + 1)/2, mn(m + n + 1)/12). Use a continuity correction of 0.5. *Example:* n = 30, T = 150: mean 232.5, variance 2363.75; z = (150.5 - 232.5)/48.6 = -1.69.

## Explicitly not here
Correlation and regression are S25.
