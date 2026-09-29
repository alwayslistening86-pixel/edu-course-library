# S15_User_Access_and_Data_Dictionary - Lesson: Privileges, roles and the data dictionary

## Goal
The learner distinguishes system and object privileges, grants and revokes object privileges (WITH GRANT OPTION, PUBLIC, column-level), creates and grants roles, and queries the USER_, ALL_ and DBA_ data dictionary views to inspect objects, columns, constraints, privileges and comments.

## Syllabus items taught here
- 14.1 - Differentiate system privileges from object privileges
- 14.2 - Grant privileges on tables
- 14.3 - Distinguish between granting privileges and roles
- 15.1 - Use data dictionary views

## How to teach this
Ask what the difference is between WITH ADMIN OPTION and WITH GRANT OPTION, and what happens to third-party grants when each is revoked. Have the learner predict the result of every example before running it, and run SQL for real against an Oracle database (Oracle Database Free or Oracle Live SQL) loaded with the course's small HR-style schema, listed in the first lesson.

#### 14.1 Differentiate system privileges from object privileges
**System privileges** allow actions across the database or a schema: CREATE SESSION, CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE SYNONYM, CREATE PROCEDURE, and ANY-variants such as SELECT ANY TABLE (DBA territory); `CREATE USER u IDENTIFIED BY pw` is itself done by a privileged user. They are granted `WITH ADMIN OPTION` to let the grantee pass them on; revoking a system privilege does **not** cascade to users the grantee gave it to. **Object privileges** allow actions on a specific object: SELECT, INSERT, UPDATE, DELETE, ALTER, INDEX, REFERENCES (tables); SELECT (views, sequences); EXECUTE (procedures). The owner has all of them automatically. `SESSION_PRIVS` lists what's active for you.
```sql
SELECT privilege FROM session_privs ORDER BY 1;
```
Output:
```
PRIVILEGE
--------------------
CREATE PROCEDURE
CREATE ROLE
CREATE SEQUENCE
CREATE SESSION
CREATE SYNONYM
CREATE TABLE
CREATE TYPE
CREATE VIEW

8 rows selected.
```

#### 14.2 Grant privileges on tables
`GRANT {privs | ALL} ON object TO {user | role | PUBLIC} [WITH GRANT OPTION]`. UPDATE, INSERT and REFERENCES can be limited to columns: `GRANT UPDATE (salary) ON employees TO clerk`. The grantee must qualify the name (`owner.employees`) unless there's a synonym. `REVOKE privs ON object FROM user`: revoking an object privilege **cascades** to anyone the grantee passed it to WITH GRANT OPTION. You can't grant privileges on objects you don't own unless you hold them WITH GRANT OPTION. `USER_TAB_PRIVS_MADE` and `USER_COL_PRIVS_MADE` show what you have granted.
```sql
SET FEEDBACK ON
GRANT SELECT, INSERT ON departments TO clerk;
GRANT UPDATE (salary, commission_pct) ON employees TO clerk WITH GRANT OPTION;
GRANT SELECT ON locations TO PUBLIC;
SELECT grantee, table_name, privilege, grantable FROM user_tab_privs_made WHERE table_name <> USER ORDER BY 1, 2, 3;
SELECT grantee, table_name, column_name, privilege FROM user_col_privs_made ORDER BY 3;
REVOKE INSERT ON departments FROM clerk;
REVOKE UPDATE (salary) ON employees FROM clerk;
```
Output:
```
Grant succeeded.

Grant succeeded.

Grant succeeded.

GRANTEE      TABLE_NAME           PRIVILEGE            GRA
------------ -------------------- -------------------- ---
CLERK        DEPARTMENTS          INSERT               NO
CLERK        DEPARTMENTS          SELECT               NO
PUBLIC       LOCATIONS            SELECT               NO

3 rows selected.

GRANTEE      TABLE_NAME           COLUMN_NAME      PRIVILEGE
------------ -------------------- ---------------- --------------------
CLERK        EMPLOYEES            COMMISSION_PCT   UPDATE
CLERK        EMPLOYEES            SALARY           UPDATE

2 rows selected.

Revoke succeeded.
(error: ORA-01750: UPDATE/REFERENCES may only be REVOKEd from the whole table, not by column)
```
(Column-level UPDATE can only be revoked from the whole table, so that last statement fails.)

#### 14.3 Distinguish between granting privileges and roles
A **role** is a named group of privileges (system, object or other roles) that makes administration easier: `CREATE ROLE r`, `GRANT privs TO r`, `GRANT r TO user [WITH ADMIN OPTION]`, `SET ROLE`, `REVOKE r FROM user`, `DROP ROLE r`. Granting a **privilege** gives one right directly; granting a **role** gives the whole bundle, and changes to the role reach every grantee at once. Roles aren't owned by a schema. Predefined roles include CONNECT, RESOURCE and DBA. Privileges received through a role can't be used inside definer's-rights stored procedures, or to create a view on another user's table.
```sql
SET FEEDBACK ON
CREATE ROLE manager_r;
GRANT SELECT, UPDATE ON employees TO manager_r;
GRANT SELECT ON departments TO manager_r;
GRANT manager_r TO clerk;
SELECT role, table_name, privilege FROM role_tab_privs WHERE role = 'MANAGER_R' ORDER BY 2, 3;
SELECT granted_role, admin_option FROM user_role_privs WHERE granted_role = 'MANAGER_R';
DROP ROLE manager_r;
```
Output:
```
Role created.

Grant succeeded.

Grant succeeded.

Grant succeeded.

ROLE             TABLE_NAME           PRIVILEGE
---------------- -------------------- --------------------
MANAGER_R        DEPARTMENTS          SELECT
MANAGER_R        EMPLOYEES            SELECT
MANAGER_R        EMPLOYEES            UPDATE

3 rows selected.

GRANTED_ROLE     ADM
---------------- ---
MANAGER_R        YES

1 row selected.

Role dropped.
```
(Creating a role grants it to its creator WITH ADMIN OPTION, which is why the creating user appears to hold it.)

#### 15.1 Use data dictionary views
The **data dictionary** is a read-only set of tables and views, owned by SYS, describing the database. Prefixes: `USER_` (objects you own; no OWNER column), `ALL_` (objects you can access), `DBA_` (everything; needs privileges), `V$` (dynamic performance views). `DICTIONARY` (synonym `DICT`) lists them all with comments. Common views: USER_OBJECTS, USER_TABLES, USER_TAB_COLUMNS, USER_CONSTRAINTS (types P, U, R, C, where NOT NULL shows as C) and USER_CONS_COLUMNS, USER_VIEWS, USER_SEQUENCES, USER_SYNONYMS, USER_INDEXES, USER_IND_COLUMNS, USER_TAB_COMMENTS, USER_COL_COMMENTS. Names are stored in **upper case**, so filter with `'EMPLOYEES'`. `COMMENT ON TABLE t IS '...'` / `COMMENT ON COLUMN t.c IS '...'` adds documentation.
```sql
SET FEEDBACK ON
COMMENT ON TABLE employees IS 'Staff of the demo company';
SELECT table_name, comments FROM user_tab_comments WHERE table_name = 'EMPLOYEES';
SELECT object_type, COUNT(*) FROM user_objects GROUP BY object_type ORDER BY 1;
SELECT c.constraint_type, cc.column_name, c.r_constraint_name FROM user_constraints c JOIN user_cons_columns cc ON c.constraint_name = cc.constraint_name
WHERE c.table_name = 'EMPLOYEES' AND c.constraint_type IN ('P', 'R', 'U') ORDER BY 1, 2;
SELECT column_name, data_type, data_length, nullable FROM user_tab_columns WHERE table_name = 'DEPARTMENTS' ORDER BY column_id;
SELECT COUNT(*) FROM user_tables WHERE table_name = 'employees';
```
Output:
```
Comment created.

TABLE_NAME           COMMENTS
-------------------- ----------------------------------------
EMPLOYEES            Staff of the demo company

1 row selected.

OBJECT_TYPE    COUNT(*)
------------ ----------
INDEX                 5
TABLE                 4

2 rows selected.

C COLUMN_NAME      R_CONSTRAINT_NAME
- ---------------- --------------------
P EMPLOYEE_ID      (null)
R DEPARTMENT_ID    SYS_Cnnnnnn
R MANAGER_ID       SYS_Cnnnnnn
U EMAIL            (null)

4 rows selected.

COLUMN_NAME      DATA_TYPE    DATA_LENGTH N
---------------- ------------ ----------- -
DEPARTMENT_ID    NUMBER                22 N
DEPARTMENT_NAME  VARCHAR2              20 N
MANAGER_ID       NUMBER                22 Y
LOCATION_ID      NUMBER                22 Y

4 rows selected.

  COUNT(*)
----------
         0

1 row selected.
```

## Explicitly not here
Time zones are S16.
