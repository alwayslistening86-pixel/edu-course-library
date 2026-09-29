# S12_DML_and_Transactions - Lesson: INSERT, UPDATE, DELETE, multi-table INSERT, MERGE and transactions

## Goal
The learner inserts, updates and deletes rows (including from subqueries and with constraint violations), writes unconditional and conditional multi-table inserts and MERGE statements, and controls transactions with COMMIT, ROLLBACK and SAVEPOINT, knowing exactly when Oracle commits implicitly.

## Syllabus items taught here
- 10.1 - Manage database transactions
- 10.2 - Control transactions
- 10.3 - Perform insert, update and delete operations
- 10.4 - Perform multi-table inserts
- 10.5 - Perform MERGE statements

## How to teach this
Ask what happens to uncommitted changes when a CREATE TABLE statement runs in the same session. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 10.1 Manage database transactions
A **transaction** is a logical unit of work: it begins with the first DML statement and ends with COMMIT, ROLLBACK, a DDL or DCL statement (which **commits implicitly**, before and after itself), a normal exit from the tool (commit) or a failure or abnormal end (rollback). Until commit, only your session sees your changes (**read consistency**: other sessions see the last committed data, and readers don't block writers); the changed rows are **locked** against other writers. A failing statement is rolled back on its own (statement-level rollback); earlier work in the transaction survives.
```sql
SET FEEDBACK ON
UPDATE employees SET salary = 1 WHERE employee_id = 100;
CREATE TABLE audit_note (txt VARCHAR2(20));
ROLLBACK;
SELECT salary FROM employees WHERE employee_id = 100;
```
Output:
```
1 row updated.

Table created.

Rollback complete.

    SALARY
----------
         1

1 row selected.
```
The CREATE TABLE committed the salary change, so the ROLLBACK had nothing to undo.

#### 10.2 Control transactions
`COMMIT` makes changes permanent and visible, and releases locks. `ROLLBACK` undoes everything since the last commit. `SAVEPOINT name` marks a point; `ROLLBACK TO [SAVEPOINT] name` undoes work after it, keeps the transaction open, and discards later savepoints (rolling back to a discarded savepoint gives ORA-01086). `SELECT ... FOR UPDATE` locks the selected rows until the transaction ends.
```sql
SET FEEDBACK ON
UPDATE employees SET salary = salary + 1000 WHERE employee_id = 200;
SAVEPOINT a;
DELETE FROM employees WHERE employee_id = 141;
SAVEPOINT b;
UPDATE employees SET salary = 0.5 WHERE employee_id = 104;
ROLLBACK TO a;
SELECT employee_id, salary FROM employees WHERE employee_id IN (104, 141, 200) ORDER BY 1;
COMMIT;
ROLLBACK TO b;
```
Output:
```
1 row updated.

Savepoint created.

1 row deleted.

Savepoint created.

1 row updated.

Rollback complete.

EMPLOYEE_ID     SALARY
----------- ----------
        104       6000
        141       3500
        200       5400

3 rows selected.

Commit complete.
(error: ORA-01086: savepoint 'B' never established in this session or is invalid)
```

#### 10.3 Perform insert, update and delete operations
`INSERT INTO t [(cols)] VALUES (...)` adds one row: list columns to be safe; omitted columns get their DEFAULT or NULL; `DEFAULT` can be written explicitly. `INSERT INTO t [(cols)] SELECT ...` copies rows (no VALUES keyword). `UPDATE t SET col = expr [, ...] [WHERE ...]` (without WHERE, every row). `DELETE [FROM] t [WHERE ...]`. Constraint violations roll back just the failing **statement**, with an error: ORA-00001 (unique), ORA-01400 (NULL into NOT NULL), ORA-02290 (check), ORA-02291 (parent key not found), ORA-02292 (child record found).
```sql
SET FEEDBACK ON
INSERT INTO departments (department_id, department_name, location_id) VALUES (120, 'Treasury', 1800);
INSERT INTO departments VALUES (130, 'Payroll', DEFAULT, NULL);
CREATE TABLE sales_reps AS SELECT employee_id id, last_name name, salary FROM employees WHERE 1 = 0;
INSERT INTO sales_reps (id, name, salary) SELECT employee_id, last_name, salary FROM employees WHERE job_id LIKE 'SA%';
UPDATE employees SET salary = (SELECT MAX(salary) FROM sales_reps), department_id = 120 WHERE employee_id = 104;
DELETE employees WHERE department_id IS NULL;
SELECT last_name, salary, department_id FROM employees WHERE employee_id IN (104, 178);
```
Output:
```
1 row created.

1 row created.

Table created.

3 rows created.

1 row updated.

1 row deleted.

LAST_NAME        SALARY DEPARTMENT_ID
------------ ---------- -------------
Ernst             11000           120

1 row selected.
```
```sql
UPDATE employees SET department_id = 999 WHERE employee_id = 104;
```
Output:
```
(error: ORA-02291: integrity constraint (YOUR_SCHEMA.SYS_Cnnnnnn) violated - parent key not found)
```
```sql
DELETE FROM departments WHERE department_id = 60;
```
Output:
```
(error: ORA-02292: integrity constraint (YOUR_SCHEMA.SYS_Cnnnnnn) violated - child record found)
```
```sql
INSERT INTO employees (employee_id, last_name, hire_date, job_id, salary) VALUES (300, 'New', DATE '2024-01-01', 'IT_PROG', -5);
```
Output:
```
(error: ORA-02290: check constraint (YOUR_SCHEMA.SYS_Cnnnnnn) violated)
```

#### 10.4 Perform multi-table inserts
**Multi-table INSERT** copies rows from one subquery into several tables. `INSERT ALL INTO t1 VALUES (...) INTO t2 VALUES (...) SELECT ...` (unconditional: every row into every target). Conditional `INSERT ALL WHEN cond THEN INTO ... [ELSE INTO ...] SELECT ...` inserts into every target whose condition is true; `INSERT FIRST` inserts into only the **first** matching WHEN. The VALUES clauses can use the subquery's columns and aliases. INSERT ALL can also insert several literal rows: `INSERT ALL INTO t VALUES (1) INTO t VALUES (2) SELECT * FROM dual`.
```sql
SET FEEDBACK ON
CREATE TABLE high_paid (id NUMBER, sal NUMBER);
CREATE TABLE mid_paid (id NUMBER, sal NUMBER);
CREATE TABLE commissioned (id NUMBER, pct NUMBER);
INSERT ALL
  WHEN salary >= 10000 THEN INTO high_paid VALUES (employee_id, salary)
  WHEN salary >= 7000 THEN INTO mid_paid VALUES (employee_id, salary)
  WHEN commission_pct IS NOT NULL THEN INTO commissioned VALUES (employee_id, commission_pct)
SELECT employee_id, salary, commission_pct FROM employees;
ROLLBACK;
INSERT FIRST
  WHEN salary >= 10000 THEN INTO high_paid VALUES (employee_id, salary)
  WHEN salary >= 7000 THEN INTO mid_paid VALUES (employee_id, salary)
  ELSE INTO commissioned VALUES (employee_id, NVL(commission_pct, 0))
SELECT employee_id, salary, commission_pct FROM employees;
SELECT (SELECT COUNT(*) FROM high_paid) hi, (SELECT COUNT(*) FROM mid_paid) mid, (SELECT COUNT(*) FROM commissioned) other FROM dual;
```
Output:
```
Table created.

Table created.

Table created.

15 rows created.

Rollback complete.

11 rows created.

        HI        MID      OTHER
---------- ---------- ----------
         5          2          4

1 row selected.
```

#### 10.5 Perform MERGE statements
`MERGE INTO target t USING source s ON (join condition) WHEN MATCHED THEN UPDATE SET ... [WHERE ...] [DELETE WHERE ...] WHEN NOT MATCHED THEN INSERT (cols) VALUES (...) [WHERE ...]` updates matching rows and inserts new ones in one statement (an 'upsert'). You can't update a column used in the ON condition, and a target row matched by more than one source row raises ORA-30926.
```sql
SET FEEDBACK ON
CREATE TABLE pay_changes (employee_id NUMBER, new_salary NUMBER, last_name VARCHAR2(12));
INSERT INTO pay_changes VALUES (104, 6500, 'Ernst');
INSERT INTO pay_changes VALUES (141, 1, 'Rajs');
INSERT INTO pay_changes VALUES (300, 4000, 'Newhire');
MERGE INTO employees e
USING pay_changes p ON (e.employee_id = p.employee_id)
WHEN MATCHED THEN UPDATE SET e.salary = p.new_salary WHERE p.new_salary > 100
WHEN NOT MATCHED THEN INSERT (employee_id, last_name, hire_date, job_id, salary) VALUES (p.employee_id, p.last_name, DATE '2024-09-01', 'ST_CLERK', p.new_salary);
SELECT employee_id, last_name, salary FROM employees WHERE employee_id IN (104, 141, 300) ORDER BY 1;
```
Output:
```
Table created.

1 row created.

1 row created.

1 row created.

2 rows merged.

EMPLOYEE_ID LAST_NAME        SALARY
----------- ------------ ----------
        104 Ernst              6500
        141 Rajs               3500
        300 Newhire            4000

3 rows selected.
```

## Explicitly not here
Creating tables properly is S13.
