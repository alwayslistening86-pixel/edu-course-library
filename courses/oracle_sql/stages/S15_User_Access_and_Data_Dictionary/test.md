# S15_User_Access_and_Data_Dictionary - Test: Privileges, roles and the data dictionary

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. User A grants SELECT on A.t to B WITH GRANT OPTION; B grants it to C. A then revokes it from B. What can C do? (choose one) Choose every correct option.
   A. C loses the privilege too
   B. C keeps the privilege
   C. The REVOKE fails while C holds it
   D. C keeps it until C logs off
2. User A grants CREATE TABLE to B WITH ADMIN OPTION; B grants it to C. A then revokes it from B. What can C do? (choose one) Choose every correct option.
   A. C keeps CREATE TABLE
   B. C loses CREATE TABLE
   C. The REVOKE fails
   D. `C's existing tables are dropped`
3. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
GRANT SELECT ON employees TO clerk, PUBLIC;
GRANT CREATE ANY TABLE TO clerk;
```
4. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT constraint_type, COUNT(*) FROM user_constraints WHERE table_name = 'EMPLOYEES' GROUP BY constraint_type ORDER BY 1;
```
5. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SET FEEDBACK ON
CREATE ROLE analyst_r;
GRANT SELECT ON job_grades TO analyst_r;
GRANT analyst_r TO clerk;
SELECT table_name, privilege FROM role_tab_privs WHERE role = 'ANALYST_R';
DROP ROLE analyst_r;
```
6. Which dictionary views describe only the objects you own? (choose two) Choose every correct option.
   A. `USER_TABLES`
   B. `ALL_TABLES`
   C. `USER_CONSTRAINTS`
   D. `DBA_OBJECTS`
7. Which are true of roles? (choose two) Choose every correct option.
   A. A role can be granted to another role
   B. A role belongs to the schema of its creator
   C. Changing a role's privileges affects every user who has the role
   D. `Object privileges can't be granted to roles`

## Answer key (for the tutor only)
1. Correct: A (exactly these options, no others)
2. Correct: A (exactly these options, no others)
3. Actual result (from running it):
```
Grant succeeded.
(error: ORA-01031: insufficient privileges)
```
4. Actual result (from running it):
```
C   COUNT(*)
- ----------
C          4
P          1
R          2
U          1
```
5. Actual result (from running it):
```
Role created.

Grant succeeded.

Grant succeeded.

TABLE_NAME           PRIVILEGE
-------------------- --------------------
JOB_GRADES           SELECT

1 row selected.

Role dropped.
```
6. Correct: A, C (exactly these options, no others)
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_User_Access_and_Data_Dictionary` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S16_Time_Zones_and_Intervals.
