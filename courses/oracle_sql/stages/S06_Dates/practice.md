# S06_Dates - Practice: Date arithmetic and date functions

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT hire_date + 30 FROM employees WHERE employee_id = 200;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT ADD_MONTHS(DATE '2024-11-30', 3) a, LAST_DAY(DATE '2024-02-01') b FROM dual;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
HIRE_DATE+30
------------------
17-OCT-03
```
2. Actual result (from running it):
```
A                  B
------------------ ------------------
28-FEB-25          29-FEB-24
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
