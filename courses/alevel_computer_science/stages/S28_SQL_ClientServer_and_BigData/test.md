# S28_SQL_ClientServer_and_BigData - Test: SQL, client-server databases and Big Data

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Given a Students table (student_id, name, grade) and an Attendance table (student_id, present_days), write SQL that returns each student's name and present_days, for students with fewer than 100 present days. [3 marks]
2. Explain what UPDATE Orders SET status = 'shipped'; (with no WHERE clause) would do, and why this is a common serious mistake. [2 marks]
3. Explain one advantage of a client-server database architecture over each client holding its own private copy of the data. [2 marks]
4. Explain what is meant by the 'three Vs' of Big Data, and why a single machine typically cannot handle it alone. [4 marks]
5. Why does the functional programming paradigm suit distributed processing of Big Data particularly well? Choose every correct option.
   A. pure functions do not rely on or change shared, mutable state, so they can safely run on different machines in parallel
   B. functional programs can only ever run on a single machine
   C. functional programming requires all data to fit in one machine's memory
   D. functional programming cannot process unstructured data at all

## Answer key (for the tutor only)
1. [3] M1 correct SELECT s.name, a.present_days; M1 FROM Students s JOIN Attendance a ON s.student_id = a.student_id; A1 WHERE a.present_days < 100;
2. [2] B1 it would set the status column to 'shipped' on every single row of the Orders table, not just the one(s) intended; B1 this is a common mistake because a missing WHERE clause is easy to overlook, and its effect (silently overwriting all rows) can be hard to reverse.
3. [2] B1 centralises the data into one consistent, up-to-date version, rather than risking clients' copies going out of sync with each other; B1 simplifies backup, security and access control, since these only need managing in one place (the server), and many clients can share the same live data concurrently.
4. [4] B1 volume: the sheer size of the data; B1 velocity: how fast new data arrives and must be processed; B1 variety: a mix of structured, semi-structured and unstructured data types; B1 a single machine has limited storage/processing capacity, so Big Data is typically processed by distributing the work across many servers working together.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S28_SQL_ClientServer_and_BigData` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S29_Functional_Programming.
