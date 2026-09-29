# S13_DDL_Tables_and_Constraints - Practice: Tables, data types, constraints, temporary and external tables

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE pets (id NUMBER PRIMARY KEY, name VARCHAR2(10) NOT NULL);
INSERT INTO pets VALUES (1, NULL);
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE t1 AS SELECT * FROM job_grades;
TRUNCATE TABLE t1;
ROLLBACK;
SELECT COUNT(*) FROM t1;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
Table created.
(error: ORA-01400: cannot insert NULL into ("YOUR_SCHEMA"."PETS"."NAME"))
```
2. Actual result (from running it):
```
Table created.

Table truncated.

Rollback complete.

  COUNT(*)
----------
         0

1 row selected.
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
