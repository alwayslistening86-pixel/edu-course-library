# S05_Character_and_Number_Functions - Practice: Character functions and ROUND, TRUNC and MOD

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT UPPER(SUBSTR(last_name, 1, 3)) a, LENGTH(first_name) b, INSTR(last_name, 'o') c FROM employees WHERE employee_id = 124;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT ROUND(1234.567, -2) a, TRUNC(1234.567, 1) b, MOD(10, 3) c FROM dual;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
A                     B          C
------------ ---------- ----------
MOU                   5          2
```
2. Actual result (from running it):
```
         A          B          C
---------- ---------- ----------
      1200     1234.5          1
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
