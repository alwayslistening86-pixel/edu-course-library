# S04_Databases_and_Software_Engineering_Foundations - Test: Databases and software engineering foundations

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A table Books(isbn, title, author_id, author_name, author_nationality) stores author details repeated on every book by that author. Identify the functional dependencies that show this table is not in 3NF, and state the transitive dependency responsible. [5 marks]
2. Explain the Isolation property of ACID transactions, and describe one problem that can occur if two transactions are not properly isolated. [4 marks]
3. Compare waterfall and Agile/Scrum development in terms of how each handles a significant requirements change discovered midway through the project. [4 marks]
4. Two transactions T1 and T2 each need exclusive locks on rows A and B. T1 locks A then requests B; T2 locks B then requests A. Explain what happens and name this situation. [3 marks]
5. Which statements about database normalisation are correct? Choose every correct option.
   A. 1NF requires every column to hold a single atomic value
   B. 2NF eliminates partial dependency on part of a composite key
   C. 3NF allows a non-key attribute to depend on another non-key attribute
   D. Normalisation reduces data redundancy and the anomalies redundancy causes

## Answer key (for the tutor only)
1. [5] B1 isbn -> title, author_id (isbn is the natural primary key and determines title and which author wrote it); B1 author_id -> author_name, author_nationality (author details depend on author_id, not directly on isbn); A1 this is a transitive dependency: isbn -> author_id -> author_name/author_nationality; A2 to fix it, split into Books(isbn, title, author_id) and Authors(author_id, author_name, author_nationality) with author_id as a foreign key in Books (1 mark for correct table split, 1 for correctly keeping author_id as the linking foreign key).
2. [4] B1 Isolation means concurrent transactions do not observe each other's uncommitted intermediate changes, behaving as if executed one after another; B1 a genuine problem named, e.g. a 'dirty read' (one transaction reads data another transaction has written but not yet committed, which may later be rolled back); B1 explains the consequence: the reading transaction may act on data that never actually existed in the committed database; B1 or an alternative correct problem such as a lost update (two transactions both read then write the same value, and one write overwrites the other without either seeing the other's change).
3. [4] B2 waterfall: because phases are sequential and requirements are fixed early, a significant change discovered mid-project typically requires reworking already-completed design/implementation documentation and is costly/disruptive to accommodate (B1 if named but not explained); B2 Agile/Scrum: because work happens in short sprints with a continuously reprioritised backlog, a requirements change can be incorporated into the next sprint's planning with comparatively little wasted work (B1 if named but not explained).
4. [3] B1 T1 holds A and waits for B (held by T2); T2 holds B and waits for A (held by T1); each waits forever for a lock the other will never release; B1 this situation is a deadlock; B1 the database management system must detect it (e.g. via a wait-for graph) and resolve it, typically by aborting/rolling back one of the transactions.
5. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Databases_and_Software_Engineering_Foundations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Programming_and_Software_Engineering.
