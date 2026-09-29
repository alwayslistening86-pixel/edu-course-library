# S15_User_Access_and_Data_Dictionary - Practice: Privileges, roles and the data dictionary

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. Which is an object privilege? (choose one) Choose every correct option.
   A. SELECT on employees
   B. CREATE TABLE
   C. CREATE SESSION
   D. SELECT ANY TABLE
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT table_name FROM user_tables WHERE table_name LIKE 'J%' OR table_name LIKE 'L%' ORDER BY 1;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Correct: A (exactly these options, no others)
2. Actual result (from running it):
```
TABLE_NAME
--------------------
JOB_GRADES
LOCATIONS
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
