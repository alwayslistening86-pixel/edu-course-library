# S14_Views_Indexes_Synonyms_Sequences - Lesson: Views, indexes, synonyms and sequences

## Goal
The learner creates, replaces and drops simple and complex views (with CHECK OPTION and READ ONLY) and knows when DML through a view works; creates and manages indexes, private synonyms and sequences (including NEXTVAL/CURRVAL rules and gaps) and identity columns.

## Syllabus items taught here
- 13.1 - Manage views
- 11.1 - Manage indexes
- 11.2 - Manage synonyms
- 11.3 - Manage sequences

## How to teach this
Ask whether you can UPDATE through a view that contains GROUP BY, and what WITH CHECK OPTION prevents. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 13.1 Manage views
A **view** is a stored query (a logical table with no data of its own): `CREATE [OR REPLACE] [FORCE | NOFORCE] VIEW v [(aliases)] AS subquery [WITH CHECK OPTION [CONSTRAINT c]] [WITH READ ONLY]`. Views simplify queries, restrict access to rows and columns, and give data independence. DML works through a **simple** view (one table, no group functions, GROUP BY, DISTINCT, ROWNUM or expressions on the changed columns); you can't insert through a view that omits a NOT NULL column without a default. `WITH CHECK OPTION` rejects inserts and updates whose rows the view couldn't then see (ORA-01402); `WITH READ ONLY` blocks all DML. `OR REPLACE` changes a view without dropping it (so grants survive); `FORCE` creates a view even if its base table doesn't exist yet (invalid until it does). `DROP VIEW v` doesn't affect the data.
```sql
SET FEEDBACK ON
CREATE VIEW it_staff AS SELECT employee_id, last_name, salary, department_id FROM employees WHERE department_id = 60 WITH CHECK OPTION;
UPDATE it_staff SET salary = salary + 500;
SELECT * FROM it_staff ORDER BY employee_id;
CREATE OR REPLACE VIEW dept_stats (dept, headcount, avg_pay) AS SELECT department_id, COUNT(*), ROUND(AVG(salary)) FROM employees GROUP BY department_id;
SELECT * FROM dept_stats WHERE headcount > 1 ORDER BY dept;
CREATE FORCE VIEW later_v AS SELECT * FROM not_there_yet;
SELECT object_name, status FROM user_objects WHERE object_type = 'VIEW' ORDER BY 1;
UPDATE it_staff SET department_id = 90 WHERE employee_id = 104;
```
Output:
```
View created.

2 rows updated.

EMPLOYEE_ID LAST_NAME        SALARY DEPARTMENT_ID
----------- ------------ ---------- -------------
        103 Hunold             9500            60
        104 Ernst              6500            60

2 rows selected.

View created.

      DEPT  HEADCOUNT    AVG_PAY
---------- ---------- ----------
        50          2       4650
        60          2       8000
        80          2      10750
        90          2      20500

4 rows selected.

Warning: View created with compilation errors.

OBJECT_NAME          STATUS
-------------------- -------
DEPT_STATS           VALID
IT_STAFF             VALID
LATER_V              INVALID

3 rows selected.
(error: ORA-01402: view WITH CHECK OPTION where-clause violation)
```
```sql
CREATE VIEW dept_stats AS SELECT department_id, COUNT(*) n FROM employees GROUP BY department_id;
UPDATE dept_stats SET n = 5;
```
Output:
```
View created.
(error: ORA-01732: data manipulation operation not legal on this view)
```

#### 11.1 Manage indexes
An **index** speeds up retrieval through a pointer structure (B-tree by default) at the cost of slower DML and storage. Oracle creates a **unique index** automatically for PRIMARY KEY and UNIQUE constraints (dropping the constraint drops that index). Create one manually with `CREATE [UNIQUE] INDEX i ON t (col [, col...])` (composite), or on an expression (**function-based**: `ON t (UPPER(last_name))`, used when queries filter on that exact expression). `ALTER INDEX i INVISIBLE` hides it from the optimiser without dropping it; you can't index the same column list twice (ORA-01408) unless the indexes differ in type or visibility; `DROP INDEX i`. Indexes help queries that return few rows of large tables on indexed columns; `IS NULL` conditions can't use a single-column B-tree index.
```sql
SET FEEDBACK ON
CREATE INDEX emp_name_ix ON employees (last_name, first_name);
CREATE INDEX emp_upper_ix ON employees (UPPER(last_name));
ALTER INDEX emp_name_ix INVISIBLE;
SELECT index_name, uniqueness, visibility FROM user_indexes WHERE table_name = 'EMPLOYEES' ORDER BY index_name;
CREATE INDEX emp_name_ix2 ON employees (last_name, first_name);
```
Output:
```
Index created.

Index created.

Index altered.

INDEX_NAME           UNIQUENES VISIBILIT
-------------------- --------- ---------
EMP_NAME_IX          NONUNIQUE INVISIBLE
EMP_UPPER_IX         NONUNIQUE VISIBLE
SYS_Cnnnnnn         UNIQUE    VISIBLE
SYS_Cnnnnnn         UNIQUE    VISIBLE

4 rows selected.
(error: ORA-01408: such column list already indexed)
```
(The SYS_ names are the indexes Oracle made for the primary key and the UNIQUE email constraint.)

#### 11.2 Manage synonyms
A **synonym** is an alias for an object (table, view, sequence, procedure, another synonym): `CREATE [OR REPLACE] [PUBLIC] SYNONYM s FOR [schema.]object`. A private synonym belongs to your schema; a public one is visible to every user (needs the CREATE PUBLIC SYNONYM privilege). Synonyms don't grant privileges; the user still needs rights on the object. A private synonym takes precedence over a public one of the same name. `DROP [PUBLIC] SYNONYM s`. A synonym can exist for an object that doesn't (yet) exist.
```sql
SET FEEDBACK ON
CREATE SYNONYM emps FOR employees;
SELECT COUNT(*) FROM emps;
CREATE SYNONYM ghost FOR missing_table;
SELECT synonym_name, table_name FROM user_synonyms ORDER BY 1;
CREATE PUBLIC SYNONYM all_emps FOR employees;
```
Output:
```
Synonym created.

  COUNT(*)
----------
        11

1 row selected.

Synonym created.

SYNONYM_NAME     TABLE_NAME
---------------- --------------------
EMPS             EMPLOYEES
GHOST            MISSING_TABLE

2 rows selected.
(error: ORA-01031: insufficient privileges)
```

#### 11.3 Manage sequences
A **sequence** generates unique integers: `CREATE SEQUENCE s [START WITH n] [INCREMENT BY n] [MAXVALUE n | NOMAXVALUE] [MINVALUE n] [CYCLE | NOCYCLE] [CACHE n | NOCACHE]`. `s.NEXTVAL` returns the next value; `s.CURRVAL` returns the value NEXTVAL last gave **this session** (ORA-08002 if NEXTVAL hasn't been used yet). NEXTVAL in a statement is evaluated once per row, even if it appears twice. Values are never reused after a rollback, and a cache is lost on shutdown, so **gaps** are normal. You can't use NEXTVAL in a view, with DISTINCT, GROUP BY, ORDER BY or in a subquery of a SELECT. `ALTER SEQUENCE` can change everything except START WITH (restart in newer releases with RESTART). A column can default to `s.NEXTVAL`, or be an **identity column**: `id NUMBER GENERATED [ALWAYS | BY DEFAULT [ON NULL]] AS IDENTITY` (ALWAYS rejects explicit values).
```sql
SET FEEDBACK ON
CREATE SEQUENCE ticket_seq START WITH 100 INCREMENT BY 10 MAXVALUE 130 NOCYCLE NOCACHE;
CREATE TABLE tickets (id NUMBER DEFAULT ticket_seq.NEXTVAL, label VARCHAR2(10));
INSERT INTO tickets (label) VALUES ('a');
INSERT INTO tickets VALUES (ticket_seq.NEXTVAL, 'b');
ROLLBACK;
INSERT INTO tickets (label) VALUES ('c');
SELECT id, label, ticket_seq.CURRVAL cur FROM tickets;
INSERT INTO tickets (label) VALUES ('d');
```
Output:
```
Sequence created.

Table created.

1 row created.

1 row created.

Rollback complete.

1 row created.

        ID LABEL             CUR
---------- ---------- ----------
       120 c                 120

1 row selected.

1 row created.
```
```sql
SET FEEDBACK ON
CREATE SEQUENCE s1;
SELECT s1.CURRVAL FROM dual;
```
Output:
```
Sequence created.
(error: ORA-08002: Sequence S1.CURRVAL is not yet defined in this session.)
```
```sql
SET FEEDBACK ON
CREATE TABLE orders (order_id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1), item VARCHAR2(10));
INSERT INTO orders (item) VALUES ('pen');
INSERT INTO orders (item) VALUES ('ink');
SELECT * FROM orders;
INSERT INTO orders (order_id, item) VALUES (99, 'nib');
```
Output:
```
Table created.

1 row created.

1 row created.

  ORDER_ID ITEM
---------- ----------
         1 pen
         2 ink

2 rows selected.
(error: ORA-32795: cannot insert into a generated always identity column)
```

## Explicitly not here
Privileges on these objects are S15.
