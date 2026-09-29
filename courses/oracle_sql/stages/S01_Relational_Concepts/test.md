# S01_Relational_Concepts - Test: Relational databases, ERDs and SQL

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which statements about primary keys are true? (choose two) Choose every correct option.
   A. A primary key value must be unique
   B. A primary key column may contain one NULL
   C. A table can have several primary keys
   D. A primary key can span several columns
2. Which are physical structures of an Oracle database rather than logical ones? (choose two) Choose every correct option.
   A. Data files
   B. `Tables`
   C. Redo log files
   D. `Views`
3. An ERD shows DEPARTMENT to EMPLOYEE as one-to-many, with employees optionally assigned. Which join lists every employee, including those with no department? (choose one) Choose every correct option.
   A. employees LEFT OUTER JOIN departments
   B. employees INNER JOIN departments
   C. employees CROSS JOIN departments
   D. employees NATURAL JOIN departments
4. Which are true of SQL? (choose two) Choose every correct option.
   A. It is declarative: you state what you want, not how to get it
   B. Unquoted identifiers are case-sensitive
   C. String literals are case-sensitive
   D. DESCRIBE is a SQL statement
5. Which statement category do GRANT and REVOKE belong to? (choose one) Choose every correct option.
   A. `DCL`
   B. `DDL`
   C. `DML`
   D. `TCL`
6. What does this return in Oracle? (If it fails, give the error and why.)
```sql
SELECT d.department_name, l.city FROM departments d JOIN locations l ON d.location_id = l.location_id WHERE l.country_id <> 'US' ORDER BY 1;
```
7. What does a foreign key enforce? (choose one) Choose every correct option.
   A. Referential integrity: each value matches a parent key or is NULL
   B. Uniqueness of each value
   C. That the column is never NULL
   D. That values fall within a range

## Answer key (for the tutor only)
1. Correct: A, D (exactly these options, no others)
2. Correct: A, C (exactly these options, no others)
3. Correct: A (exactly these options, no others)
4. Correct: A, C (exactly these options, no others)
5. Correct: A (exactly these options, no others)
6. Actual result (from running it):
```
DEPARTMENT_NAME      CITY
-------------------- --------------------
Marketing            Toronto
Sales                Oxford
```
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Relational_Concepts` exactly. 7 items; a pass needs at least 5 fully correct (63%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Basic_SELECT.
