# S12_DML_and_Transactions - Practice: INSERT, UPDATE, DELETE, multi-table INSERT, MERGE and transactions

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
INSERT INTO locations VALUES (3000, 'Lyon', 'FR');
ROLLBACK;
SELECT COUNT(*) FROM locations;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
DELETE FROM employees WHERE employee_id = 100;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
1 row created.

Rollback complete.

  COUNT(*)
----------
         3

1 row selected.
```
2. Actual result (from running it):
```
(error: ORA-02292: integrity constraint (YOUR_SCHEMA.SYS_Cnnnnnn) violated - child record found)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
