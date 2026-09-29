# S10_Subqueries - Lesson: Single-row, multiple-row and correlated subqueries

## Goal
The learner writes single-row and multiple-row subqueries in WHERE, HAVING and FROM, uses IN, ANY, ALL and EXISTS correctly (including the NOT IN and NULL trap), and updates and deletes rows with correlated subqueries.

## Syllabus items taught here
- 8.1 - Use single-row subqueries
- 8.2 - Use multiple-row subqueries
- 8.3 - Update and delete rows using correlated subqueries

## How to teach this
Ask what happens when a subquery used with `=` returns two rows, and what `NOT IN (subquery)` returns if the subquery returns a NULL. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 8.1 Use single-row subqueries
A **subquery** is a SELECT inside another statement, in parentheses; it runs before (or, if correlated, for each row of) the outer query. A **single-row** subquery returns at most one row and is used with `= <> < > <= >=`. If it returns more than one row you get ORA-01427; if it returns no rows the comparison is with NULL, so nothing matches. Subqueries can appear in WHERE, HAVING, FROM (an **inline view**), the SELECT list (a **scalar subquery**) and a `WITH` clause. ORDER BY isn't allowed inside a subquery used in a condition.
```sql
SELECT last_name, salary FROM employees
WHERE  salary > (SELECT salary FROM employees WHERE last_name = 'Abel') ORDER BY salary;
SELECT department_id, MIN(salary) FROM employees GROUP BY department_id
HAVING MIN(salary) > (SELECT MIN(salary) FROM employees WHERE department_id = 60) ORDER BY 1;
SELECT last_name, (SELECT department_name FROM departments d WHERE d.department_id = e.department_id) dept FROM employees e WHERE employee_id IN (100, 178) ORDER BY 1;
WITH dept_avg AS (SELECT department_id, AVG(salary) avg_sal FROM employees GROUP BY department_id)
SELECT e.last_name, e.salary, ROUND(a.avg_sal) avg_sal FROM employees e JOIN dept_avg a ON e.department_id = a.department_id WHERE e.salary > a.avg_sal ORDER BY 1;
SELECT last_name FROM employees WHERE job_id = (SELECT job_id FROM employees WHERE last_name = 'Nobody');
```
Output:
```
LAST_NAME        SALARY
------------ ----------
Hartstein         13000
Kochhar           17000
King              24000

DEPARTMENT_ID MIN(SALARY)
------------- -----------
           20       13000
           80       10500
           90       17000
(null)               7000

LAST_NAME    DEPT
------------ --------------------
Grant        (null)
King         Executive

LAST_NAME        SALARY    AVG_SAL
------------ ---------- ----------
Abel              11000      10750
Hunold             9000       7500
King              24000      20500
Mourgos            5800       4650

no rows selected
```
```sql
SELECT last_name FROM employees WHERE salary = (SELECT salary FROM employees WHERE department_id = 60);
```
Output:
```
(error: ORA-01427: single-row subquery returns more than one row)
```

#### 8.2 Use multiple-row subqueries
A **multiple-row** subquery uses `IN`, `NOT IN`, `ANY`/`SOME` (compare with at least one value: `> ANY` means more than the minimum) or `ALL` (compare with every value: `> ALL` means more than the maximum, `< ALL` less than the minimum). `= ANY` is the same as `IN`. **NOT IN** with a subquery that returns any NULL returns **no rows**, because `x <> NULL` is unknown; filter out the NULLs or use `NOT EXISTS`. `EXISTS` is true if the subquery returns any row. Multiple-column subqueries compare pairs: `WHERE (a, b) IN (SELECT ...)`.
```sql
SELECT last_name, salary FROM employees WHERE salary < ANY (SELECT salary FROM employees WHERE job_id = 'IT_PROG') ORDER BY salary;
SELECT last_name, salary FROM employees WHERE salary > ALL (SELECT salary FROM employees WHERE department_id = 80) ORDER BY salary;
SELECT COUNT(*) not_managers_wrong FROM employees WHERE employee_id NOT IN (SELECT manager_id FROM employees);
SELECT COUNT(*) not_managers_right FROM employees WHERE employee_id NOT IN (SELECT manager_id FROM employees WHERE manager_id IS NOT NULL);
SELECT department_name FROM departments d WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.department_id);
SELECT last_name FROM employees WHERE (job_id, department_id) IN (SELECT job_id, department_id FROM employees WHERE last_name = 'Ernst') ORDER BY 1;
```
Output:
```
LAST_NAME        SALARY
------------ ----------
Rajs               3500
Whalen             4400
Mourgos            5800
Ernst              6000
Grant              7000

LAST_NAME        SALARY
------------ ----------
Hartstein         13000
Kochhar           17000
King              24000

NOT_MANAGERS_WRONG
------------------
                 0

NOT_MANAGERS_RIGHT
------------------
                 6

DEPARTMENT_NAME
--------------------
Accounting

LAST_NAME
------------
Ernst
Hunold
```

#### 8.3 Update and delete rows using correlated subqueries
A **correlated** subquery refers to a column of the outer statement, so it runs once per outer row. In `UPDATE ... SET col = (correlated subquery)` each row gets its own value; in `DELETE ... WHERE ... (correlated subquery)` each row is tested. If the SET subquery returns no row for some outer row, that column becomes NULL.
```sql
SET FEEDBACK ON
ALTER TABLE departments ADD (staff_count NUMBER(3));
UPDATE departments d SET staff_count = (SELECT COUNT(*) FROM employees e WHERE e.department_id = d.department_id);
SELECT department_name, staff_count FROM departments ORDER BY staff_count DESC, department_name;
UPDATE employees e SET salary = salary + 100 WHERE salary < (SELECT AVG(salary) FROM employees x WHERE x.department_id = e.department_id);
DELETE FROM departments d WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.department_id);
ROLLBACK;
```
Output:
```
Table altered.

7 rows updated.

DEPARTMENT_NAME      STAFF_COUNT
-------------------- -----------
Executive                      2
IT                             2
Sales                          2
Shipping                       2
Administration                 1
Marketing                      1
Accounting                     0

7 rows selected.

4 rows updated.

1 row deleted.

Rollback complete.
```

## Explicitly not here
Set operators are S11.
