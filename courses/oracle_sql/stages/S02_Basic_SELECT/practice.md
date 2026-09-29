# S02_Basic_SELECT - Practice: The SELECT statement, aliases, literals, DISTINCT, arithmetic and NULL

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT last_name || ' earns ' || salary AS "Pay Line" FROM employees WHERE employee_id = 104;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT DISTINCT department_id FROM employees WHERE job_id LIKE 'SA%' ORDER BY 1;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
Pay Line
-----------------------------------------------------------
Ernst earns 6000
```
2. Actual result (from running it):
```
DEPARTMENT_ID
-------------
           80
(null)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
