# S06_Practical_Modern_Statistics - Practice: Practical modern statistics

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
from math import comb
n, p, k = 10, 0.5, 5
print(round(comb(n, k) * p**k * (1 - p)**(n - k), 4))
```
2. A dataset of household incomes is strongly right-skewed (a few very high earners). State which measure of central tendency and which measure of spread are more appropriate than the mean and standard deviation, and explain why. [3 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
0.2461
```
2. [3] B1 median (more appropriate than the mean); B1 interquartile range (more appropriate than the standard deviation); B1 because both the mean and standard deviation are pulled/inflated by extreme high-earning outliers, whereas the median and IQR are robust to them and better reflect a 'typical' household.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
