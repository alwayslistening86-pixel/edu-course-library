# S28_SQL - Test: Structured query language (SQL)

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Write a SQL statement to select the name and form of every student, ordered alphabetically by name (A to Z). [3 marks]
2. Write a SQL statement to insert a new student, id 7, name 'Grace', mark 58, form '10B', into the Students table. [2 marks]
3. Write a SQL statement to change Chen's mark to 74. [2 marks]
4. Explain why it would be dangerous to run DELETE FROM Students; with no WHERE clause. [2 marks]
5. Given the Students table (Amara 82 10A, Ben 45 10B, Chen 67 10A, Diya 90 10C, Ewan 38 10B), state exactly what this query returns, in order: SELECT name FROM Students WHERE form = '10A' ORDER BY mark ASC; [2 marks]

## Answer key (for the tutor only)
1. [3] M1 correct SELECT with the two named fields; M1 correct FROM Students; A1 ORDER BY name ASC (or ORDER BY name, since ascending is the default) -- e.g. SELECT name, form FROM Students ORDER BY name ASC;
2. [2] B1 correct INSERT INTO Students (...) structure naming all four fields; B1 correct VALUES (7, 'Grace', 58, '10B');
3. [2] B1 correct UPDATE Students SET mark = 74 structure; B1 correct WHERE name = 'Chen'; (so only Chen's record is changed).
4. [2] B1 with no WHERE clause the condition applies to every record; B1 so every single record in the Students table would be deleted, not just an intended one.
5. [2] B1 filters to form 10A: Amara and Chen; B1 ascending by mark: Chen, then Amara.

## Grading
Apply `rubric.json`'s `stage_rubrics.S28_SQL` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S29_Ethical_Legal_Environmental_Impacts.
