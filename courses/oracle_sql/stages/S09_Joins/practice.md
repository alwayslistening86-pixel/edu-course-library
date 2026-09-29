# S09_Joins - Practice: Joins: equijoins, self, non-equi, outer and Cartesian

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT e.last_name, d.department_name FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE d.location_id = 1800;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT COUNT(*) FROM locations, job_grades;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Hartstein    Marketing
```
2. Actual result (from running it):
```
  COUNT(*)
----------
        15
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
