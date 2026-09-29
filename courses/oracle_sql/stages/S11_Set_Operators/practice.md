# S11_Set_Operators - Practice: UNION, UNION ALL, INTERSECT and MINUS

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT location_id FROM locations MINUS SELECT location_id FROM departments WHERE department_id < 80;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT job_id FROM employees WHERE department_id = 60 UNION ALL SELECT job_id FROM employees WHERE department_id = 60;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
LOCATION_ID
-----------
       2500
```
2. Actual result (from running it):
```
JOB_ID
----------
IT_PROG
IT_PROG
IT_PROG
IT_PROG
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
