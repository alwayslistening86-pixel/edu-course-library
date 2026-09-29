# S13_DDL_Tables_and_Constraints - Test: Tables, data types, constraints, temporary and external tables

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE prices (item VARCHAR2(5), amt NUMBER(4, 1));
INSERT INTO prices VALUES ('pen', 12.36);
INSERT INTO prices VALUES ('ink', 999.95);
SELECT * FROM prices;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE kids (id NUMBER PRIMARY KEY, parent NUMBER REFERENCES kids ON DELETE CASCADE);
INSERT INTO kids VALUES (1, NULL);
INSERT INTO kids VALUES (2, 1);
INSERT INTO kids VALUES (3, 2);
DELETE FROM kids WHERE id = 1;
SELECT COUNT(*) FROM kids;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE u (a NUMBER UNIQUE, b NUMBER);
INSERT INTO u VALUES (NULL, 1);
INSERT INTO u VALUES (NULL, 2);
INSERT INTO u VALUES (5, 3);
INSERT INTO u VALUES (5, 4);
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE emp_names AS SELECT last_name, salary * 12 annual FROM employees;
SELECT column_name, nullable FROM user_tab_columns WHERE table_name = 'EMP_NAMES' ORDER BY column_id;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE c (x NUMBER);
INSERT INTO c VALUES (1);
ALTER TABLE c SET UNUSED COLUMN x;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE GLOBAL TEMPORARY TABLE gtt (n NUMBER);
INSERT INTO gtt VALUES (1);
SELECT COUNT(*) FROM gtt;
COMMIT;
SELECT COUNT(*) FROM gtt;
```
7. Which are true? (choose three) Choose every correct option.
   A. `A CHECK constraint can't refer to SYSDATE`
   B. `CTAS copies the source table's primary key`
   C. A UNIQUE constraint creates an index automatically
   D. NOT NULL can only be declared at column level
   E. TRUNCATE can be rolled back

## Answer key (for the tutor only)
1. Actual result (from running it):
```
Table created.

1 row created.
(error: ORA-01438: value 999.95 greater than specified precision (4, 1) for column)
```
2. Actual result (from running it):
```
Table created.

1 row created.

1 row created.

1 row created.

1 row deleted.

  COUNT(*)
----------
         0

1 row selected.
```
3. Actual result (from running it):
```
Table created.

1 row created.

1 row created.

1 row created.
(error: ORA-00001: unique constraint (YOUR_SCHEMA.SYS_Cnnnnnn) violated on table YOUR_SCHEMA.U columns (A))
```
4. Actual result (from running it):
```
Table created.

COLUMN_NAME      N
---------------- -
LAST_NAME        N
ANNUAL           Y

2 rows selected.
```
5. Actual result (from running it):
```
Table created.

1 row created.
(error: ORA-12983: cannot drop all columns in a table)
```
6. Actual result (from running it):
```
Table created.

1 row created.

  COUNT(*)
----------
         1

1 row selected.

Commit complete.

  COUNT(*)
----------
         0

1 row selected.
```
7. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_DDL_Tables_and_Constraints` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Views_Indexes_Synonyms_Sequences.
