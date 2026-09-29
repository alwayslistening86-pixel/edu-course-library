# S01_Relational_Concepts - Lesson: Relational databases, ERDs and SQL

## Goal
The learner explains tables, rows, columns, keys and relationships, maps ERD entities, attributes and relationships to SQL clauses, and describes how SQL is used to talk to an Oracle database.

## Syllabus items taught here
- 1.1 - Explain the theoretical and physical aspects of a relational database
- 1.2 - Relate clauses in SQL SELECT statements to the components of an ERD
- 1.3 - Explain the relationship between a database and SQL

## How to teach this
Show the course schema's four tables and ask the learner to draw the ERD: which columns are primary keys, which are foreign keys, and what the relationships' cardinalities are. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 1.1 Explain the theoretical and physical aspects of a relational database
**Theory (logical model):** a relational database stores data in **relations** (tables) of **tuples** (rows) and **attributes** (columns). Each row is identified by a **primary key** (unique, not null); a **foreign key** refers to a primary or unique key in another (or the same) table, enforcing **referential integrity**. Rows and columns have no inherent order. Normalisation removes redundancy (1NF atomic values; 2NF no partial dependency on part of a composite key; 3NF no transitive dependency). **Physical aspects:** the Oracle **database** is the set of files on disk (data files, control files, redo log files); an **instance** is the memory (SGA) and background processes that open it. Tables live in **tablespaces** made of data files; each user owns a **schema** of objects. Rows are located by **ROWID**, and indexes speed access.

The course schema (loaded into every example; the runs also narrow SQL*Plus's display of long dictionary name columns such as TABLE_NAME with `COLUMN ... FORMAT A20`, which changes only the display):
```sql
CREATE TABLE locations (location_id NUMBER(4) PRIMARY KEY, city VARCHAR2(20) NOT NULL, country_id CHAR(2));
CREATE TABLE departments (department_id NUMBER(4) PRIMARY KEY, department_name VARCHAR2(20) NOT NULL, manager_id NUMBER(6), location_id NUMBER(4) REFERENCES locations);
CREATE TABLE employees (
  employee_id NUMBER(6) PRIMARY KEY, first_name VARCHAR2(12), last_name VARCHAR2(12) NOT NULL,
  email VARCHAR2(12) UNIQUE, hire_date DATE NOT NULL, job_id VARCHAR2(10) NOT NULL,
  salary NUMBER(8,2) CHECK (salary > 0), commission_pct NUMBER(2,2),
  manager_id NUMBER(6) REFERENCES employees, department_id NUMBER(4) REFERENCES departments);
CREATE TABLE job_grades (grade_level CHAR(1) PRIMARY KEY, lowest_sal NUMBER(8), highest_sal NUMBER(8));
INSERT INTO locations VALUES (1700, 'Seattle', 'US');
INSERT INTO locations VALUES (1800, 'Toronto', 'CA');
INSERT INTO locations VALUES (2500, 'Oxford', 'UK');
INSERT INTO departments VALUES (10, 'Administration', 200, 1700);
INSERT INTO departments VALUES (20, 'Marketing', 201, 1800);
INSERT INTO departments VALUES (50, 'Shipping', 124, 1700);
INSERT INTO departments VALUES (60, 'IT', 103, 1700);
INSERT INTO departments VALUES (80, 'Sales', 149, 2500);
INSERT INTO departments VALUES (90, 'Executive', 100, 1700);
INSERT INTO departments VALUES (110, 'Accounting', NULL, 1700);
INSERT INTO employees VALUES (100, 'Steven', 'King', 'SKING', DATE '2003-06-17', 'AD_PRES', 24000, NULL, NULL, 90);
INSERT INTO employees VALUES (101, 'Neena', 'Kochhar', 'NKOCHHAR', DATE '2005-09-21', 'AD_VP', 17000, NULL, 100, 90);
INSERT INTO employees VALUES (103, 'Alexander', 'Hunold', 'AHUNOLD', DATE '2006-01-03', 'IT_PROG', 9000, NULL, 101, 60);
INSERT INTO employees VALUES (104, 'Bruce', 'Ernst', 'BERNST', DATE '2007-05-21', 'IT_PROG', 6000, NULL, 103, 60);
INSERT INTO employees VALUES (124, 'Kevin', 'Mourgos', 'KMOURGOS', DATE '2007-11-16', 'ST_MAN', 5800, NULL, 100, 50);
INSERT INTO employees VALUES (141, 'Trenna', 'Rajs', 'TRAJS', DATE '2003-10-17', 'ST_CLERK', 3500, NULL, 124, 50);
INSERT INTO employees VALUES (149, 'Eleni', 'Zlotkey', 'EZLOTKEY', DATE '2008-01-29', 'SA_MAN', 10500, .2, 100, 80);
INSERT INTO employees VALUES (174, 'Ellen', 'Abel', 'EABEL', DATE '2004-05-11', 'SA_REP', 11000, .3, 149, 80);
INSERT INTO employees VALUES (178, 'Kimberely', 'Grant', 'KGRANT', DATE '2007-05-24', 'SA_REP', 7000, .15, 149, NULL);
INSERT INTO employees VALUES (200, 'Jennifer', 'Whalen', 'JWHALEN', DATE '2003-09-17', 'AD_ASST', 4400, NULL, 101, 10);
INSERT INTO employees VALUES (201, 'Michael', 'Hartstein', 'MHARTSTE', DATE '2004-02-17', 'MK_MAN', 13000, NULL, 100, 20);
INSERT INTO job_grades VALUES ('A', 1000, 2999);
INSERT INTO job_grades VALUES ('B', 3000, 5999);
INSERT INTO job_grades VALUES ('C', 6000, 9999);
INSERT INTO job_grades VALUES ('D', 10000, 14999);
INSERT INTO job_grades VALUES ('E', 15000, 24999);
COMMIT;
```
```sql
COLUMN table_name FORMAT A20
SELECT table_name FROM user_tables ORDER BY table_name;
```
Output:
```
TABLE_NAME
--------------------
DEPARTMENTS
EMPLOYEES
JOB_GRADES
LOCATIONS
```

#### 1.2 Relate clauses in SQL SELECT statements to the components of an ERD
In an **ERD** (entity relationship diagram), an **entity** becomes a table (the FROM clause), **attributes** become columns (the SELECT list and WHERE conditions), a **unique identifier** becomes the primary key, and a **relationship** becomes a foreign key that you follow with a **join** (the JOIN ... ON clause). Relationship cardinality (one-to-many, many-to-many via an intersection table, one-to-one) and optionality (must/may: a solid or dashed line) tell you which join to use: an optional relationship (an employee *may* belong to a department) needs an **outer join** to keep rows without a match. A recursive relationship (an employee is managed by an employee) becomes a self-join.
```sql
SELECT e.last_name, d.department_name
FROM   employees e JOIN departments d ON e.department_id = d.department_id
WHERE  e.job_id LIKE 'SA%';
```
Output:
```
LAST_NAME    DEPARTMENT_NAME
------------ --------------------
Zlotkey      Sales
Abel         Sales
```
Grant has no department (the relationship is optional), so the inner join drops her.

#### 1.3 Explain the relationship between a database and SQL
**SQL** (Structured Query Language) is the ANSI/ISO standard language for relational databases, and the only way applications talk to the data in Oracle. It is declarative (you state *what* you want and the optimiser decides how). Statement categories: **DQL** SELECT; **DML** INSERT, UPDATE, DELETE, MERGE; **DDL** CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT; **DCL** GRANT, REVOKE; **TCL** COMMIT, ROLLBACK, SAVEPOINT. Tools such as SQL*Plus, SQL Developer, SQLcl and Live SQL send SQL to the server. SQL keywords and unquoted identifiers are case-insensitive (Oracle stores them in upper case); string literals are case-sensitive. SQL*Plus commands (DESCRIBE, DEFINE, SET) are tool commands, not SQL.
```sql
SET LINESIZE 60
DESCRIBE departments
SET LINESIZE 200
select DEPARTMENT_NAME from Departments where department_name = 'IT';
select department_name from departments where department_name = 'it';
```
Output:
```
 Name                          Null?    Type
 ----------------------------- -------- --------------------
 DEPARTMENT_ID                 NOT NULL NUMBER(4)
 DEPARTMENT_NAME               NOT NULL VARCHAR2(20)
 MANAGER_ID                             NUMBER(6)
 LOCATION_ID                            NUMBER(4)

DEPARTMENT_NAME
--------------------
IT

no rows selected
```
(The last query finds no rows, so SQL*Plus reports 'no rows selected'.)

## Explicitly not here
Writing SELECT statements properly starts in S02.
