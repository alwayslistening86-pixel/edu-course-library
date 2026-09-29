# S12_DML_and_Transactions - Test: INSERT, UPDATE, DELETE, multi-table INSERT, MERGE and transactions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
UPDATE employees SET salary = salary * 2 WHERE department_id = 50;
SAVEPOINT s1;
UPDATE employees SET salary = 0.01 WHERE department_id = 50;
ROLLBACK TO s1;
COMMIT;
SELECT SUM(salary) FROM employees WHERE department_id = 50;
```
2. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
INSERT INTO departments (department_id, department_name) VALUES (200, 'Legal');
CREATE INDEX d_name_ix ON departments (department_name);
ROLLBACK;
SELECT department_name FROM departments WHERE department_id = 200;
```
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
INSERT INTO departments (department_id, department_name) VALUES (210, 'R and D');
INSERT INTO departments (department_id, department_name) VALUES (210, 'Duplicate');
SELECT department_name FROM departments WHERE department_id = 210;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE big (id NUMBER);
CREATE TABLE small (id NUMBER);
INSERT FIRST WHEN employee_id > 150 THEN INTO big VALUES (employee_id) WHEN employee_id > 100 THEN INTO small VALUES (employee_id) SELECT employee_id FROM employees;
SELECT (SELECT COUNT(*) FROM big) b, (SELECT COUNT(*) FROM small) s FROM dual;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE TABLE grade_updates (grade_level CHAR(1), highest_sal NUMBER);
INSERT INTO grade_updates VALUES ('A', 3100);
INSERT INTO grade_updates VALUES ('F', 40000);
MERGE INTO job_grades g USING grade_updates u ON (g.grade_level = u.grade_level)
WHEN MATCHED THEN UPDATE SET g.highest_sal = u.highest_sal
WHEN NOT MATCHED THEN INSERT VALUES (u.grade_level, 25000, u.highest_sal);
SELECT * FROM job_grades WHERE grade_level IN ('A', 'F') ORDER BY 1;
```
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
INSERT INTO employees (employee_id, last_name, job_id, salary) VALUES (400, 'Temp', 'ST_CLERK', 2000);
```
7. Which events end a transaction? (choose three) Choose every correct option.
   A. `COMMIT`
   B. A CREATE TABLE statement
   C. `SAVEPOINT`
   D. `ROLLBACK`
   E. A SELECT statement

## Answer key (for the tutor only)
1. Actual result (from running it):
```
2 rows updated.

Savepoint created.

2 rows updated.

Rollback complete.

Commit complete.

SUM(SALARY)
-----------
      18600

1 row selected.
```
2. Actual result (from running it):
```
1 row created.

Index created.

Rollback complete.

DEPARTMENT_NAME
--------------------
Legal

1 row selected.
```
3. Actual result (from running it):
```
1 row created.
(error: ORA-00001: unique constraint (YOUR_SCHEMA.SYS_Cnnnnnn) violated on table YOUR_SCHEMA.DEPARTMENTS columns (DEPARTMENT_ID))
```
4. Actual result (from running it):
```
Table created.

Table created.

10 rows created.

         B          S
---------- ----------
         4          6

1 row selected.
```
5. Actual result (from running it):
```
Table created.

1 row created.

1 row created.

2 rows merged.

G LOWEST_SAL HIGHEST_SAL
- ---------- -----------
A       1000        3100
F      25000       40000

2 rows selected.
```
6. Actual result (from running it):
```
(error: ORA-01400: cannot insert NULL into ("YOUR_SCHEMA"."EMPLOYEES"."HIRE_DATE"))
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_DML_and_Transactions` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_DDL_Tables_and_Constraints.
