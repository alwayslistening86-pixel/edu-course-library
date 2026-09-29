# S04_Substitution_Variables - Lesson: Substitution variables, DEFINE and VERIFY

## Goal
The learner uses & and && substitution variables in SQL*Plus-style tools, quotes them correctly, and controls them with DEFINE, UNDEFINE and SET VERIFY.

## Syllabus items taught here
- 3.3 - Use substitution variables
- 3.4 - Use the DEFINE and VERIFY commands

## How to teach this
Ask what the tool does when it meets `&dept` in a statement, and what changes with `&&dept`. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 3.3 Use substitution variables
A **substitution variable** (`&name`) is replaced by text *before* the statement is sent to the server, so it can stand for a value, a column, a condition or even a table name. If the variable isn't defined, the tool prompts for it each time. `&&name` prompts once and then keeps the value defined for the rest of the session. Character and date values need quotes, either around the variable in the statement (`'&job'`) or typed in by the user. Substitution is a client feature of SQL*Plus, SQLcl and SQL Developer; it isn't part of SQL. (The examples predefine the variables, because prompts can't be answered here.)
```sql
DEFINE dept = 60
DEFINE job = IT_PROG
DEFINE col = salary
SELECT last_name, &col FROM employees WHERE department_id = &dept AND job_id = '&job' ORDER BY &col DESC;
```
Output:
```
old   1: SELECT last_name, &col FROM employees WHERE department_id = &dept AND job_id = '&job' ORDER BY &col DESC
new   1: SELECT last_name, salary FROM employees WHERE department_id = 60 AND job_id = 'IT_PROG' ORDER BY salary DESC

LAST_NAME        SALARY
------------ ----------
Hunold             9000
Ernst              6000
```

#### 3.4 Use the DEFINE and VERIFY commands
`DEFINE name = value` creates a variable (always as CHAR text); `DEFINE name` shows it; `DEFINE` alone lists all; `UNDEFINE name` removes it. `SET VERIFY ON` (the default) makes the tool echo each line containing a substitution, before (`old`) and after (`new`) replacement; `SET VERIFY OFF` hides that. `SET DEFINE OFF` turns substitution off entirely (useful for literals containing `&`).
```sql
DEFINE min_sal = 12000
SET VERIFY ON
SELECT last_name FROM employees WHERE salary > &min_sal ORDER BY 1;
SET VERIFY OFF
SELECT COUNT(*) FROM employees WHERE salary > &min_sal;
DEFINE min_sal
SET DEFINE OFF
SELECT 'R&D' dept FROM dual;
```
Output:
```
old   1: SELECT last_name FROM employees WHERE salary > &min_sal ORDER BY 1
new   1: SELECT last_name FROM employees WHERE salary > 12000 ORDER BY 1

LAST_NAME
------------
Hartstein
King
Kochhar

  COUNT(*)
----------
         3

DEFINE MIN_SAL         = "12000" (CHAR)

DEP
---
R&D
```

## Explicitly not here
Functions are S05 onwards.
