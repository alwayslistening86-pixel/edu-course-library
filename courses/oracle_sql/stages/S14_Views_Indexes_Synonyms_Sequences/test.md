# S14_Views_Indexes_Synonyms_Sequences - Test: Views, indexes, synonyms and sequences

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE SEQUENCE c3 START WITH 1 MAXVALUE 3 CYCLE NOCACHE;
SELECT c3.NEXTVAL FROM employees WHERE ROWNUM <= 5;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE SEQUENCE s9 MINVALUE 1 MAXVALUE 2 NOCYCLE NOCACHE;
SELECT s9.NEXTVAL FROM employees WHERE ROWNUM <= 3;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE VIEW rich AS SELECT employee_id, last_name, salary FROM employees WHERE salary > 12000 WITH CHECK OPTION;
UPDATE rich SET salary = salary + 1000;
UPDATE rich SET salary = 5000 WHERE employee_id = 100;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE VIEW emp_v AS SELECT employee_id, last_name FROM employees;
INSERT INTO emp_v VALUES (500, 'Ghost');
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE dup (a NUMBER PRIMARY KEY);
CREATE INDEX dup_ix ON dup (a);
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE SYNONYM e FOR employees;
DROP TABLE employees CASCADE CONSTRAINTS;
SELECT COUNT(*) FROM e;
```
7. Which statements about sequences are true? (choose two) Choose every correct option.
   A. Rolled-back NEXTVAL values are not reused
   B. CURRVAL can be referenced before NEXTVAL in a new session
   C. NEXTVAL may be used as a column DEFAULT
   D. A sequence is tied to one table

## Answer key (for the tutor only)
1. Actual result (from running it):
```
Sequence created.

   NEXTVAL
----------
         1
         2
         3
         1
         2

5 rows selected.
```
2. Actual result (from running it):
```
Sequence created.
(error: ORA-08004: Sequence S9.NEXTVAL exceeds MAXVALUE and cannot be instantiated.)
```
3. Actual result (from running it):
```
View created.

3 rows updated.
(error: ORA-01402: view WITH CHECK OPTION where-clause violation)
```
4. Actual result (from running it):
```
View created.
(error: ORA-01400: cannot insert NULL into ("YOUR_SCHEMA"."EMPLOYEES"."HIRE_DATE"))
```
5. Actual result (from running it):
```
Table created.
(error: ORA-01408: such column list already indexed)
```
6. Actual result (from running it):
```
Synonym created.

Table dropped.
(error: ORA-00980: synonym translation is no longer valid)
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Views_Indexes_Synonyms_Sequences` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_User_Access_and_Data_Dictionary.
