# S13_DDL_Tables_and_Constraints - Lesson: Tables, data types, constraints, temporary and external tables

## Goal
The learner creates tables (directly and with CTAS) using the right data types and defaults, alters, renames, truncates, drops and restores them, drops or sets columns UNUSED, creates global and private temporary tables and external tables, and defines, names, enables, disables and drops every kind of constraint.

## Syllabus items taught here
- 12.1 - Describe and work with tables
- 12.2 - Describe and work with columns and data types
- 12.3 - Create tables
- 12.4 - Drop columns and set columns UNUSED
- 12.5 - Truncate tables
- 12.6 - Create and use temporary tables
- 12.7 - Create and use external tables
- 12.8 - Manage constraints

## How to teach this
Ask which constraints CREATE TABLE ... AS SELECT copies from the source table. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 12.1 Describe and work with tables
Table names (and other identifiers) start with a letter, are up to 128 bytes (30 before 12.2), may contain letters, digits, `_`, `$` and `#`, mustn't be reserved words, and must be unique among the objects in the schema's namespace. Quoted identifiers are case-sensitive. `DESCRIBE`, `ALTER TABLE ... RENAME TO` or `RENAME old TO new`, `ALTER TABLE ... READ ONLY` / `READ WRITE`, `COMMENT ON TABLE`. `DROP TABLE t` moves it to the **recycle bin** (restore with `FLASHBACK TABLE t TO BEFORE DROP`), unless you add `PURGE`. Dropping a table also drops its indexes and constraints; views on it become invalid. DDL commits implicitly and can't be rolled back.
```sql
SET FEEDBACK ON
CREATE TABLE notes (id NUMBER, body VARCHAR2(50));
INSERT INTO notes VALUES (1, 'keep me');
ALTER TABLE notes READ ONLY;
INSERT INTO notes VALUES (2, 'rejected');
```
Output:
```
Table created.

1 row created.

Table altered.
(error: ORA-12081: update operation not allowed on table "YOUR_SCHEMA"."NOTES")
```
```sql
SET FEEDBACK ON
CREATE TABLE notes (id NUMBER, body VARCHAR2(50));
INSERT INTO notes VALUES (1, 'keep me');
RENAME notes TO memos;
DROP TABLE memos;
SELECT COUNT(*) FROM memos;
```
Output:
```
Table created.

1 row created.

Table renamed.

Table dropped.
(error: ORA-00942: table or view "YOUR_SCHEMA"."MEMOS" does not exist)
```
```sql
SET FEEDBACK ON
CREATE TABLE memos (id NUMBER);
INSERT INTO memos VALUES (1);
DROP TABLE memos;
FLASHBACK TABLE memos TO BEFORE DROP;
SELECT COUNT(*) FROM memos;
```
Output:
```
Table created.

1 row created.

Table dropped.

Flashback complete.

  COUNT(*)
----------
         1

1 row selected.
```

#### 12.2 Describe and work with columns and data types
Key types: `VARCHAR2(n)` (variable-length text, size required), `CHAR(n)` (fixed-length, blank-padded, default 1), `NUMBER(p, s)` (p digits in all, s after the point; a negative s rounds to the left; too many digits before the point raises ORA-01438), `DATE`, `TIMESTAMP` (fractional seconds), `TIMESTAMP WITH [LOCAL] TIME ZONE`, `INTERVAL` types, `CLOB`/`NCLOB`/`BLOB` (large objects), `RAW`, `BFILE`, `ROWID`. `LONG` is legacy (one per table, not in CTAS, GROUP BY or constraints). `ALTER TABLE t ADD (col type)`, `MODIFY (col newtype | DEFAULT x | NOT NULL)` (you can shorten or change the type only if existing data fits or the column is empty), `RENAME COLUMN a TO b`.
```sql
SET FEEDBACK ON
CREATE TABLE amounts (n1 NUMBER(5, 2), n2 NUMBER(5, -2), c CHAR(5), v VARCHAR2(5));
INSERT INTO amounts VALUES (123.456, 12345, 'ab', 'ab');
SELECT n1, n2, LENGTH(c) lc, LENGTH(v) lv, '[' || c || ']' padded FROM amounts;
ALTER TABLE amounts ADD (created DATE DEFAULT DATE '2024-01-01');
ALTER TABLE amounts RENAME COLUMN v TO label;
SELECT label, created FROM amounts;
INSERT INTO amounts (n1) VALUES (1234.5);
```
Output:
```
Table created.

1 row created.

        N1         N2         LC         LV PADDED
---------- ---------- ---------- ---------- -------
    123.46      12300          5          2 [ab   ]

1 row selected.

Table altered.

Table altered.

LABEL CREATED
----- ------------------
ab    01-JAN-24

1 row selected.
(error: ORA-01438: value 1234.5 greater than specified precision (5, 2) for column)
```

#### 12.3 Create tables
`CREATE TABLE [schema.]t (col type [DEFAULT expr] [column constraint], ..., [table constraints])` (you need the CREATE TABLE privilege and quota). **CTAS**, `CREATE TABLE t [(new names)] AS SELECT ...`, creates and fills a table in one step; column types and **NOT NULL** constraints come from the query, but no other constraints are copied; expressions need aliases. `WHERE 1 = 0` copies just the structure. A DEFAULT may use SYSDATE, USER or a sequence's NEXTVAL, but not another column; `DEFAULT ON NULL` also replaces explicit NULLs.
```sql
SET FEEDBACK ON
CREATE TABLE dept_summary AS
  SELECT department_id dept, COUNT(*) staff, SUM(salary) payroll FROM employees WHERE department_id IS NOT NULL GROUP BY department_id;
SELECT column_name, data_type, nullable FROM user_tab_columns WHERE table_name = 'DEPT_SUMMARY' ORDER BY column_id;
CREATE TABLE emp_copy AS SELECT employee_id, last_name, hire_date FROM employees WHERE 1 = 0;
SELECT constraint_type, COUNT(*) FROM user_constraints WHERE table_name = 'EMP_COPY' GROUP BY constraint_type;
CREATE TABLE tasks (id NUMBER, status VARCHAR2(10) DEFAULT ON NULL 'open', due DATE DEFAULT DATE '2030-01-01');
INSERT INTO tasks (id, status) VALUES (1, NULL);
SELECT * FROM tasks;
CREATE TABLE bad AS SELECT salary * 12 FROM employees;
```
Output:
```
Table created.

COLUMN_NAME      DATA_TYPE    N
---------------- ------------ -
DEPT             NUMBER       Y
STAFF            NUMBER       Y
PAYROLL          NUMBER       Y

3 rows selected.

Table created.

C   COUNT(*)
- ----------
C          2

1 row selected.

Table created.

1 row created.

        ID STATUS     DUE
---------- ---------- ------------------
         1 open       01-JAN-30

1 row selected.
(error: ORA-00998: must name this expression with a column alias)
```

#### 12.4 Drop columns and set columns UNUSED
`ALTER TABLE t DROP COLUMN c` (or `DROP (c1, c2)`) removes a column and its data immediately; you can't drop a table's last column, and a column referenced by other tables' foreign keys needs `CASCADE CONSTRAINTS`. `ALTER TABLE t SET UNUSED (c)` (or `SET UNUSED COLUMN c`) marks a column unused instantly: it disappears from queries and DESCRIBE, can't be recovered, and its name can be reused; the space is reclaimed later with `ALTER TABLE t DROP UNUSED COLUMNS`. `USER_UNUSED_COL_TABS` lists tables with unused columns.
```sql
SET FEEDBACK ON
CREATE TABLE wide (a NUMBER, b NUMBER, c NUMBER, d NUMBER);
INSERT INTO wide VALUES (1, 2, 3, 4);
ALTER TABLE wide DROP COLUMN b;
ALTER TABLE wide SET UNUSED (c);
SELECT * FROM wide;
SELECT table_name, count FROM user_unused_col_tabs;
ALTER TABLE wide ADD (c VARCHAR2(5) DEFAULT 'new');
ALTER TABLE wide DROP UNUSED COLUMNS;
SELECT * FROM wide;
ALTER TABLE wide DROP (a, c, d);
```
Output:
```
Table created.

1 row created.

Table altered.

Table altered.

         A          D
---------- ----------
         1          4

1 row selected.

TABLE_NAME                COUNT
-------------------- ----------
WIDE                          1

1 row selected.

Table altered.

Table altered.

         A          D C
---------- ---------- -----
         1          4 new

1 row selected.
(error: ORA-12983: cannot drop all columns in a table)
```

#### 12.5 Truncate tables
`TRUNCATE TABLE t` removes **all** rows quickly, releases storage (unless `REUSE STORAGE`), resets the high-water mark, fires no DELETE triggers, and is **DDL**, so it commits and can't be rolled back. It fails if an enabled foreign key from another table refers to it (unless `TRUNCATE ... CASCADE` with ON DELETE CASCADE keys). `DELETE` without WHERE removes all rows as DML: slower, but it can be rolled back.
```sql
SET FEEDBACK ON
CREATE TABLE scratch AS SELECT employee_id FROM employees;
DELETE FROM scratch;
ROLLBACK;
SELECT COUNT(*) after_delete_rollback FROM scratch;
TRUNCATE TABLE scratch;
ROLLBACK;
SELECT COUNT(*) after_truncate_rollback FROM scratch;
TRUNCATE TABLE departments;
```
Output:
```
Table created.

11 rows deleted.

Rollback complete.

AFTER_DELETE_ROLLBACK
---------------------
                   11

1 row selected.

Table truncated.

Rollback complete.

AFTER_TRUNCATE_ROLLBACK
-----------------------
                      0

1 row selected.
(error: ORA-02266: unique/primary keys in table referenced by enabled foreign keys)
```

#### 12.6 Create and use temporary tables
A **global temporary table** has a permanent definition, but its rows are private to each session and temporary: `CREATE GLOBAL TEMPORARY TABLE t (...) ON COMMIT DELETE ROWS` (rows last until the transaction ends; the default) or `ON COMMIT PRESERVE ROWS` (until the session ends). A **private temporary table** (18c+) exists only in the session's memory, and its name must start with the prefix `ORA$PTT_`: `CREATE PRIVATE TEMPORARY TABLE ora$ptt_x (...) ON COMMIT DROP DEFINITION` (the default, dropped at transaction end) or `ON COMMIT PRESERVE DEFINITION` (dropped at session end).
```sql
SET FEEDBACK ON
CREATE GLOBAL TEMPORARY TABLE cart (item VARCHAR2(10)) ON COMMIT DELETE ROWS;
CREATE GLOBAL TEMPORARY TABLE basket (item VARCHAR2(10)) ON COMMIT PRESERVE ROWS;
INSERT INTO cart VALUES ('apple');
INSERT INTO basket VALUES ('pear');
COMMIT;
SELECT (SELECT COUNT(*) FROM cart) cart_rows, (SELECT COUNT(*) FROM basket) basket_rows FROM dual;
CREATE PRIVATE TEMPORARY TABLE ora$ptt_calc (n NUMBER) ON COMMIT PRESERVE DEFINITION;
INSERT INTO ora$ptt_calc VALUES (42);
SELECT n FROM ora$ptt_calc;
CREATE PRIVATE TEMPORARY TABLE calc (n NUMBER);
```
Output:
```
Table created.

Table created.

1 row created.

1 row created.

Commit complete.

 CART_ROWS BASKET_ROWS
---------- -----------
         0           1

1 row selected.

Table created.

1 row created.

         N
----------
        42

1 row selected.
(error: ORA-00903: invalid table name)
```

#### 12.7 Create and use external tables
An **external table** is a read-only table whose data stays in an operating-system file, read through an access driver (`ORACLE_LOADER` for text files, `ORACLE_DATAPUMP` for Data Pump files). It needs a **directory object** (created by a DBA: `CREATE DIRECTORY ext_dir AS '/path'`, then `GRANT READ ON DIRECTORY ext_dir TO user`). You can query and join it, but no DML or indexes. This example reads a three-line CSV file, `products.csv`, from the directory object `ext_dir`.
```sql
SET FEEDBACK ON
CREATE TABLE products_ext (id NUMBER, name VARCHAR2(20), price NUMBER(6, 2))
ORGANIZATION EXTERNAL (
  TYPE ORACLE_LOADER
  DEFAULT DIRECTORY ext_dir
  ACCESS PARAMETERS (RECORDS DELIMITED BY NEWLINE NOLOGFILE NOBADFILE FIELDS TERMINATED BY ',')
  LOCATION ('products.csv'))
REJECT LIMIT UNLIMITED;
SELECT * FROM products_ext WHERE price < 10 ORDER BY id;
DELETE FROM products_ext;
```
Output:
```
Table created.

        ID NAME                      PRICE
---------- -------------------- ----------
         1 Widget                      4.5
         3 Doohickey                   .99

2 rows selected.
(error: ORA-30657: operation not supported on external organized table)
```

#### 12.8 Manage constraints
Constraints: `NOT NULL` (column level only), `UNIQUE` (NULLs allowed, and several NULLs don't clash), `PRIMARY KEY` (unique + not null, one per table), `FOREIGN KEY ... REFERENCES parent(col) [ON DELETE CASCADE | ON DELETE SET NULL]`, `CHECK (condition)` (can't use SYSDATE, sequences or subqueries). Define them inline (column level) or out of line (table level: required for composite keys); name them with `CONSTRAINT name`, or Oracle generates `SYS_Cn`. PRIMARY KEY and UNIQUE create an index automatically. Manage with `ALTER TABLE t ADD CONSTRAINT ...`, `MODIFY col NOT NULL`, `DISABLE`/`ENABLE [NOVALIDATE] CONSTRAINT`, `DROP CONSTRAINT name [CASCADE]`, `DROP PRIMARY KEY CASCADE`. Enabling fails if existing rows violate the constraint (unless NOVALIDATE).
```sql
SET FEEDBACK ON
CREATE TABLE teams (team_id NUMBER CONSTRAINT teams_pk PRIMARY KEY, name VARCHAR2(20) NOT NULL UNIQUE);
CREATE TABLE players (
  player_id NUMBER,
  team_id NUMBER CONSTRAINT players_team_fk REFERENCES teams ON DELETE SET NULL,
  shirt NUMBER(2) CHECK (shirt BETWEEN 1 AND 99),
  nick VARCHAR2(10),
  CONSTRAINT players_pk PRIMARY KEY (player_id),
  CONSTRAINT players_nick_uk UNIQUE (nick));
INSERT INTO teams VALUES (1, 'Reds');
INSERT INTO players VALUES (10, 1, 7, NULL);
INSERT INTO players VALUES (11, 1, 9, NULL);
DELETE FROM teams WHERE team_id = 1;
SELECT player_id, team_id FROM players ORDER BY 1;
SELECT constraint_name, constraint_type FROM user_constraints WHERE table_name = 'PLAYERS' AND constraint_name NOT LIKE 'SYS%' ORDER BY 1;
ALTER TABLE players DISABLE CONSTRAINT players_nick_uk;
INSERT INTO players VALUES (12, NULL, 10, 'Ace');
INSERT INTO players VALUES (13, NULL, 11, 'Ace');
ALTER TABLE players ENABLE CONSTRAINT players_nick_uk;
```
Output:
```
Table created.

Table created.

1 row created.

1 row created.

1 row created.

1 row deleted.

 PLAYER_ID    TEAM_ID
---------- ----------
        10 (null)
        11 (null)

2 rows selected.

CONSTRAINT_NAME      C
-------------------- -
PLAYERS_NICK_UK      U
PLAYERS_PK           P
PLAYERS_TEAM_FK      R

3 rows selected.

Table altered.

1 row created.

1 row created.
(error: ORA-02299: cannot validate (YOUR_SCHEMA.PLAYERS_NICK_UK) - duplicate keys found)
```
```sql
CREATE TABLE t2 (a NUMBER, b NUMBER, NOT NULL (a));
```
Output:
```
(error: ORA-03050: invalid identifier: "NOT" is a reserved word)
```
NOT NULL can only be declared at column level. (Older releases report this as ORA-00904 invalid identifier; the reason is the same.)

## Explicitly not here
Indexes, views, sequences and synonyms are S14.
