# S10_Subqueries - Practice: Single-row, multiple-row and correlated subqueries

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'IT') ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
LAST_NAME
------------
Ernst
Hunold
```
2. Actual result (from running it):
```
LAST_NAME
------------
King
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
