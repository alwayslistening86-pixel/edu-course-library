# S09_Joins - Lesson: Joins: equijoins, self, non-equi, outer and Cartesian

## Goal
The learner writes and predicts every join form the exam uses: NATURAL, USING, ON, self, non-equi, LEFT/RIGHT/FULL OUTER (including Oracle's (+) syntax), CROSS and accidental Cartesian products.

## Syllabus items taught here
- 7.1 - Use self-joins
- 7.2 - Use various types of joins
- 7.3 - Use non-equijoins
- 7.4 - Use OUTER joins
- 7.5 - Understand and use Cartesian products

## How to teach this
Ask why `employees NATURAL JOIN departments` returns fewer rows than a join ON department_id. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 7.1 Use self-joins
A **self-join** joins a table to itself using two aliases, typically to follow a recursive relationship (employee to manager).
```sql
SELECT w.last_name employee, m.last_name manager
FROM   employees w JOIN employees m ON w.manager_id = m.employee_id
WHERE  m.last_name IN ('Kochhar', 'Zlotkey') ORDER BY 2, 1;
```
Output:
```
EMPLOYEE     MANAGER
------------ ------------
Hunold       Kochhar
Whalen       Kochhar
Abel         Zlotkey
Grant        Zlotkey
```

#### 7.2 Use various types of joins
**ANSI join types:** `NATURAL JOIN` joins on **every** column with the same name in both tables (here that's department_id *and* manager_id, which is rarely what you want). `JOIN ... USING (col)` joins on the named columns only, and those columns can't be qualified with a table name anywhere in the statement. `JOIN ... ON condition` joins on any condition; qualify ambiguous columns (ORA-00918). `JOIN` means `INNER JOIN`. Several joins chain left to right. Oracle's older syntax lists tables in FROM with the join condition in WHERE.
```sql
SELECT COUNT(*) natural_rows FROM employees NATURAL JOIN departments;
SELECT COUNT(*) on_rows FROM employees e JOIN departments d ON e.department_id = d.department_id;
SELECT last_name, department_id, department_name, city
FROM   employees JOIN departments USING (department_id) JOIN locations USING (location_id)
WHERE  department_id IN (20, 60) ORDER BY last_name;
SELECT e.last_name, d.department_name FROM employees e, departments d WHERE e.department_id = d.department_id AND d.department_id = 10;
```
Output:
```
NATURAL_ROWS
------------
           4

   ON_ROWS
----------
        10

LAST_NAME    DEPARTMENT_ID DEPARTMENT_NAME      CITY
------------ ------------- -------------------- --------------------
Ernst                   60 IT                   Seattle
Hartstein               20 Marketing            Toronto
Hunold                  60 IT                   Seattle

LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Whalen       Administration
```
```sql
SELECT e.last_name, d.department_id FROM employees e JOIN departments d USING (department_id);
```
Output:
```
(error: ORA-25154: column part of USING clause cannot have qualifier)
```
```sql
SELECT last_name, department_id FROM employees e JOIN departments d ON e.department_id = d.department_id;
```
Output:
```
(error: ORA-00918: DEPARTMENT_ID: column ambiguously specified - appears in  and)
```
(Older releases word ORA-00918 as 'column ambiguously defined'. Error wording varies by release; the error number and the reason are what matter.)

#### 7.3 Use non-equijoins
A **non-equijoin** uses an operator other than `=`, usually `BETWEEN` or `<`/`>` against a range table.
```sql
SELECT e.last_name, e.salary, g.grade_level
FROM   employees e JOIN job_grades g ON e.salary BETWEEN g.lowest_sal AND g.highest_sal
WHERE  e.department_id IN (50, 90) ORDER BY e.salary;
```
Output:
```
LAST_NAME        SALARY G
------------ ---------- -
Rajs               3500 B
Mourgos            5800 B
Kochhar           17000 E
King              24000 E
```

#### 7.4 Use OUTER joins
An **outer join** also returns rows with no match: `LEFT [OUTER] JOIN` keeps every row of the left table, `RIGHT` of the right, `FULL` of both, filling the missing side with NULLs. Oracle's proprietary syntax puts `(+)` on the side that may be **missing** (the deficient side): `WHERE e.department_id = d.department_id(+)` is a left outer join from e. `(+)` can't do a full outer join, can't be used with `OR` or `IN`, and can't be mixed with ANSI JOIN syntax in the same query block. A WHERE condition on the outer-joined table can quietly turn an outer join back into an inner one; put it in the ON clause instead.
```sql
SELECT e.last_name, d.department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id WHERE e.job_id LIKE 'SA%' ORDER BY 1;
SELECT d.department_name, COUNT(e.employee_id) staff FROM employees e RIGHT OUTER JOIN departments d ON e.department_id = d.department_id GROUP BY d.department_name HAVING COUNT(e.employee_id) < 2 ORDER BY 1;
SELECT e.last_name, d.department_name FROM employees e FULL JOIN departments d ON e.department_id = d.department_id WHERE e.employee_id IS NULL OR d.department_id IS NULL ORDER BY 1, 2;
SELECT e.last_name, d.department_name FROM employees e, departments d WHERE e.department_id = d.department_id(+) AND e.employee_id IN (178, 200) ORDER BY 1;
SELECT COUNT(*) filtered_in_where FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id WHERE e.salary > 10000;
SELECT COUNT(*) filtered_in_on FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id AND e.salary > 10000;
```
Output:
```
LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Abel         Sales
Grant        (null)
Zlotkey      Sales

DEPARTMENT_NAME           STAFF
-------------------- ----------
Accounting                    0
Administration                1
Marketing                     1

LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Grant        (null)
(null)       Accounting

LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Grant        (null)
Whalen       Administration

FILTERED_IN_WHERE
-----------------
                5

FILTERED_IN_ON
--------------
             9
```

#### 7.5 Understand and use Cartesian products
A **Cartesian product** pairs every row of one table with every row of another (rows = m × n). You get one by accident when a join condition is missing or invalid, or on purpose with `CROSS JOIN`.
```sql
SELECT COUNT(*) FROM employees, departments;
SELECT COUNT(*) FROM job_grades CROSS JOIN locations;
SELECT l.city, g.grade_level FROM locations l CROSS JOIN job_grades g WHERE g.grade_level IN ('A', 'B') AND l.country_id <> 'US' ORDER BY 1, 2;
```
Output:
```
  COUNT(*)
----------
        77

  COUNT(*)
----------
        15

CITY                 G
-------------------- -
Oxford               A
Oxford               B
Toronto              A
Toronto              B
```

## Explicitly not here
Subqueries are S10.
