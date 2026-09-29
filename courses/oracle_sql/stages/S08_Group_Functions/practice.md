# S08_Group_Functions - Practice: Group functions, GROUP BY and HAVING

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT department_id, COUNT(*) FROM employees GROUP BY department_id HAVING COUNT(*) = 1 ORDER BY 1;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT COUNT(manager_id), COUNT(*) FROM employees;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
DEPARTMENT_ID   COUNT(*)
------------- ----------
           10          1
           20          1
(null)                 1
```
2. Actual result (from running it):
```
COUNT(MANAGER_ID)   COUNT(*)
----------------- ----------
               10         11
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
