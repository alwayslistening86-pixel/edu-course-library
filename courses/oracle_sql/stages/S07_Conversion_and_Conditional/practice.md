# S07_Conversion_and_Conditional - Practice: Conversion functions, NULL functions, CASE and DECODE, nesting

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT NVL2(manager_id, 'managed', 'top') a, COALESCE(NULL, NULL, 'third') b, NULLIF(5, 5) c FROM employees WHERE employee_id = 100;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT TO_CHAR(DATE '2024-12-25', 'DD "of" fmMonth, YYYY') FROM dual;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
A       B              C
------- ----- ----------
top     third (null)
```
2. Actual result (from running it):
```
TO_CHAR(DATE'2024-12
--------------------
25 of December, 2024
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
