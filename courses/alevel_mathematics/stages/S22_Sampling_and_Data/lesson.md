# S22_Sampling_and_Data - Lesson: Sampling and data presentation

## Goal
The learner distinguishes population and sample, chooses and critiques sampling methods, interprets and critiques data presentations (including histograms and scatter diagrams), calculates and interprets summary statistics, and identifies outliers and cleans data.

## Syllabus items taught here
- 2.01a - Population and sample
- 2.01b - Using samples to make informal inferences about the population
- 2.01c - Sampling techniques: simple random, stratified, systematic, quota, cluster and opportunity
- 2.01d - Selecting and critiquing sampling techniques; different samples lead to different conclusions
- 2.02a - Interpreting tables and diagrams for single-variable data
- 2.02b - Histograms: area represents frequency
- 2.02c - Scatter diagrams and regression lines for bivariate data, including distinct sections
- 2.02d - Informal interpretation of correlation
- 2.02e - Correlation does not imply causation
- 2.02f - Measures of central tendency and variation: mean, median, mode, percentiles, quartiles, IQR, standard deviation and variance
- 2.02g - Mean and standard deviation from raw data, summary statistics or a frequency distribution
- 2.02h - Recognising and interpreting possible outliers
- 2.02i - Selecting or critiquing data presentation techniques
- 2.02j - Cleaning data: missing data, errors and outliers

## How to teach this
Ask how you could find the average height of students at a large school without measuring everyone, and what could go wrong. Work each example with the learner before showing the next line, insist on full working (OCR awards method marks), and let them use a calculator exactly as the exam allows. Every numerical answer in these files was computed with sympy when the course was built.

#### 2.01a Population and sample
A **population** is the whole set of items of interest; a **sample** is a subset of it. A census surveys the whole population (accurate but costly or impossible when testing destroys items). A **sampling frame** is a list of the population's members from which a sample is drawn.

#### 2.01b Using samples to make informal inferences about the population
A sample statistic (e.g. the sample mean) estimates the population parameter. Informal inference: with a random, reasonably large sample, the population value is likely to be close to the sample's; a small or biased sample gives unreliable conclusions. Different samples give different estimates (sampling variability).

#### 2.01c Sampling techniques: simple random, stratified, systematic, quota, cluster and opportunity
**Simple random**: every sample of size n equally likely (number the frame, use random numbers). **Systematic**: every kth item after a random start. **Stratified**: split into groups (strata) and sample each in proportion to its size. **Quota**: the interviewer fills quotas for each group, non-randomly. **Cluster**: randomly choose whole groups (clusters) and sample within them. **Opportunity (convenience)**: whoever is available. *Example:* a school of 600 Year 12 and 400 Year 13 students, sample of 50 stratified: 30 from Year 12 and 20 from Year 13.

#### 2.01d Selecting and critiquing sampling techniques; different samples lead to different conclusions
Choose a method to suit the context and critique it: random methods need a sampling frame but avoid bias; opportunity samples are quick but may be unrepresentative (surveying people at a gym about exercise). Stratified samples represent groups fairly. Larger samples reduce variability but not bias. Different samples can lead to different conclusions, so a single sample's result is uncertain.

#### 2.02a Interpreting tables and diagrams for single-variable data
Read and interpret tables, bar charts, pie charts, stem-and-leaf diagrams, box plots and cumulative frequency graphs. Compare distributions using a measure of location **and** a measure of spread, in context ("the median time for group A is higher, so A were generally slower; the IQR is smaller, so their times were more consistent").

#### 2.02b Histograms: area represents frequency
In a histogram the **area** of each bar is proportional to frequency; the height is the frequency density = frequency / class width. *Example:* a class 10 ≤ t < 25 with frequency 30 has frequency density 2. If a histogram's scale is not given, use one known bar to find the area-to-frequency factor. Estimate frequencies in part of a class by assuming the data are spread evenly within it.

#### 2.02c Scatter diagrams and regression lines for bivariate data, including distinct sections
A scatter diagram plots bivariate data. The regression line of y on x (y = a + bx) predicts y from x; interpret b as the change in y per unit increase in x. Only interpolate (predict within the data's range); extrapolation is unreliable. Look for distinct sections or clusters that suggest the data come from different groups, in which case one line for all of them is misleading.

#### 2.02d Informal interpretation of correlation
Informal correlation: positive (both increase together), negative, or none; strong if the points lie close to a straight line. The PMCC (S26) quantifies linear correlation. Correlation describes linear association only: a strong curved relationship can have weak linear correlation.

#### 2.02e Correlation does not imply causation
Correlation does not imply causation: ice-cream sales and drownings correlate because both rise in hot weather (a confounding variable). Only a controlled experiment can suggest causation.

#### 2.02f Measures of central tendency and variation: mean, median, mode, percentiles, quartiles, IQR, standard deviation and variance
Location: mean, median, mode. Spread: range, interquartile range (Q3 - Q1), percentiles, variance and standard deviation. Variance = Σx^2/n - (mean)^2 (the course uses the divisor n unless a question asks for the sample estimate with n - 1). *Example:* for the data [12, 15, 15, 18, 21, 22, 25, 29, 31, 60]: mean = 24.8, median = 21.5, standard deviation = 13.11. The median and IQR resist outliers; the mean and standard deviation don't. Coding: if y = (x - a)/b then mean_y = (mean_x - a)/b and sd_y = sd_x/b.

#### 2.02g Mean and standard deviation from raw data, summary statistics or a frequency distribution
Use the calculator's statistics mode or the formulae. From summary statistics: n = 20, Σx = 340, Σx^2 = 6200 give mean 17 and sd = root(6200/20 - 17^2) = root 21 ≈ 4.58. Grouped data: use class midpoints. *Example:* midpoints 5, 15, 25, 35 with frequencies 4, 9, 12, 5: mean = 21.00, sd = 9.17 (estimates, since the midpoints stand in for the raw values).

#### 2.02h Recognising and interpreting possible outliers
A common rule: an outlier lies more than 1.5 × IQR below Q1 or above Q3 (or more than 2 standard deviations from the mean; the question will say which). *Example:* in [12, 15, 15, 18, 21, 22, 25, 29, 31, 60], Q1 = 15, Q3 = 29, IQR = 14, so the upper limit is 29 + 21 = 50 and 60 is an outlier. Decide in context whether an outlier is an error (remove it) or a genuine extreme value (keep it).

#### 2.02i Selecting or critiquing data presentation techniques
Choose the right display: histograms for continuous grouped data, box plots to compare distributions, scatter diagrams for bivariate data, bar charts for categories. Critique misleading presentations: truncated axes, unequal class widths drawn as equal heights, 3D effects, pie charts with too many sectors.

#### 2.02j Cleaning data: missing data, errors and outliers
Real data sets (like OCR's large data set) contain missing values, typing errors and outliers. Cleaning means identifying impossible values (a negative age, a percentage over 100), deciding what to do with missing entries (exclude them and say so), and making units consistent. Report what was removed and why, since cleaning changes the results.

## Explicitly not here
Probability starts in S23.
