# S14_Views_Indexes_Synonyms_Sequences - Practice: Views, indexes, synonyms and sequences

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE SEQUENCE sq START WITH 5 INCREMENT BY 5;
SELECT sq.NEXTVAL, sq.NEXTVAL, sq.CURRVAL FROM dual;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE VIEW v AS SELECT last_name, salary FROM employees WHERE salary > 10000 WITH READ ONLY;
UPDATE v SET salary = 1;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
Sequence created.

   NEXTVAL    NEXTVAL    CURRVAL
---------- ---------- ----------
         5          5          5

1 row selected.
```
2. Actual result (from running it):
```
View created.
(error: ORA-42399: cannot perform a DML operation on a read-only view)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
