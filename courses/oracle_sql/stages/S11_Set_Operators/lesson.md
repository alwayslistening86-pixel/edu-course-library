# S11_Set_Operators - Lesson: UNION, UNION ALL, INTERSECT and MINUS

## Goal
The learner combines queries with UNION, UNION ALL, INTERSECT and MINUS, matching column counts and data type groups, and orders the combined result correctly.

## Syllabus items taught here
- 9.1 - Match the SELECT statements
- 9.2 - Use the ORDER BY clause in set operations
- 9.3 - Use the INTERSECT operator
- 9.4 - Use the MINUS operator
- 9.5 - Use the UNION and UNION ALL operators

## How to teach this
Ask which query's column names label the result of a UNION, and where ORDER BY may appear. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 9.1 Match the SELECT statements
Each SELECT in a compound query must have the **same number of columns**, and corresponding columns must be in the **same data type group** (numeric, character, date); names needn't match. Pad with `NULL`, literals or `TO_CHAR(NULL)` / `TO_NUMBER(NULL)` where one side has no equivalent column. Result column names come from the **first** query. Set operators all have equal precedence and are evaluated top to bottom unless parentheses say otherwise.
```sql
SELECT employee_id id, job_id, NULL dept_name FROM employees WHERE department_id = 60
UNION
SELECT department_id, TO_CHAR(NULL), department_name FROM departments WHERE department_id = 60;
```
Output:
```
        ID JOB_ID     DEPT_NAME
---------- ---------- --------------------
       103 IT_PROG    (null)
       104 IT_PROG    (null)
        60 (null)     IT
```
```sql
SELECT employee_id, last_name FROM employees UNION SELECT department_id FROM departments;
```
Output:
```
(error: ORA-01789: query block has incorrect number of result columns)
```
```sql
SELECT employee_id FROM employees UNION SELECT department_name FROM departments;
```
Output:
```
(error: ORA-01790: expression must have same datatype as corresponding expression)
```

#### 9.2 Use the ORDER BY clause in set operations
`ORDER BY` may appear **once**, at the very end, and sorts the whole result. It may refer to the first query's column names or aliases, or to positions. Referring to a name that appears only in a later query fails.
```sql
SELECT last_name name, salary FROM employees WHERE department_id = 60
UNION ALL
SELECT department_name, 0 FROM departments WHERE department_id = 60
ORDER BY 2 DESC, name;
```
Output:
```
NAME                     SALARY
-------------------- ----------
Hunold                     9000
Ernst                      6000
IT                            0
```
```sql
SELECT last_name, salary FROM employees WHERE department_id = 60
UNION
SELECT department_name, 0 dummy FROM departments
ORDER BY dummy;
```
Output:
```
(error: ORA-00904: "DUMMY": invalid identifier)
```

#### 9.3 Use the INTERSECT operator
`INTERSECT` returns the distinct rows present in **both** results. Swapping the queries doesn't change the result.
```sql
SELECT department_id FROM employees INTERSECT SELECT department_id FROM departments WHERE location_id = 1700;
```
Output:
```
DEPARTMENT_ID
-------------
           10
           50
           60
           90
```

#### 9.4 Use the MINUS operator
`MINUS` returns distinct rows of the first query that are **not** in the second (ANSI's EXCEPT). Order matters.
```sql
SELECT department_id FROM departments MINUS SELECT department_id FROM employees;
SELECT department_id FROM employees MINUS SELECT department_id FROM departments;
```
Output:
```
DEPARTMENT_ID
-------------
          110

DEPARTMENT_ID
-------------
(null)
```
(The second result is Grant's NULL department: for set operators, NULLs count as equal to each other, unlike in WHERE conditions.)

#### 9.5 Use the UNION and UNION ALL operators
`UNION` returns every distinct row from either query (duplicates removed); `UNION ALL` returns all rows, duplicates included, and is faster. Older Oracle releases returned UNION, INTERSECT and MINUS results sorted as a side effect of removing duplicates, and much older study material states that as a rule; no order is guaranteed without ORDER BY (the release used here often returns hash order, as the 9.1 example shows). Always add ORDER BY when order matters.
```sql
SELECT job_id FROM employees WHERE department_id = 80
UNION
SELECT job_id FROM employees WHERE department_id IS NULL;
SELECT job_id FROM employees WHERE department_id = 80
UNION ALL
SELECT job_id FROM employees WHERE department_id IS NULL;
SELECT COUNT(*) FROM (SELECT department_id FROM employees UNION SELECT department_id FROM departments);
```
Output:
```
JOB_ID
----------
SA_MAN
SA_REP

JOB_ID
----------
SA_MAN
SA_REP
SA_REP

  COUNT(*)
----------
         8
```

## Explicitly not here
DML is S12.
