# S27_Relational_Databases - Test: Relational databases

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what a primary key is, and state the one rule it must always follow. [2 marks]
2. Explain what a foreign key is, and how it is used to link two tables. [3 marks]
3. Explain how using a relational database, rather than one large flat file, reduces data inconsistency. [3 marks]
4. Which best describes a relational database's advantage over storing all data in one large flat file? Choose every correct option.
   A. it reduces data redundancy and inconsistency by storing shared data once and linking to it
   B. it removes the need for any data types to be defined
   C. it means a primary key is no longer required
   D. it allows a table to have no records

## Answer key (for the tutor only)
1. [2] B1 a field (or combination of fields) whose value uniquely identifies each record in a table; B1 no two records may share the same primary key value (and it cannot be empty).
2. [3] B1 a field in one table that holds a value matching another table's primary key; B1 e.g. a StudentID field in a Results table matching the StudentID primary key in a Students table; B1 this links each record in the first table to the correct, related record in the second table, without repeating that record's other data.
3. [3] B1 shared data (e.g. a student's details) is stored once, in one table; B1 other tables link to it via a foreign key rather than repeating a copy of it; B1 so there is only one version of that data to update, removing the risk of duplicated copies disagreeing with each other.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S27_Relational_Databases` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 9 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S28_SQL.
