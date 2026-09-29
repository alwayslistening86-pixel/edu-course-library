# S28_SQL - Lesson: Structured query language (SQL)

## Goal
The learner uses SQL to retrieve data with SELECT, FROM, WHERE and ORDER BY ... ASC|DESC, and to insert, edit and delete data.

## Syllabus items taught here
- 3.7.2 - Structured query language (SQL): SELECT/FROM/WHERE/ORDER BY, INSERT, UPDATE, DELETE

## How to teach this
Show the learner a small table of students and marks, and ask them, in plain English first, to 'get the names and marks of everyone who scored 50 or more, highest first' -- then translate that into SQL. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.7.2 Structured query language (SQL): SELECT/FROM/WHERE/ORDER BY, INSERT, UPDATE, DELETE
**SQL (Structured Query Language)** is used to retrieve and change data in a relational database. To retrieve data: `SELECT` names which field(s) to return, `FROM` names the table, `WHERE` filters which records are returned by a condition, and `ORDER BY field ASC|DESC` sorts the returned records by a field, ascending (`ASC`, the default, smallest/earliest first) or descending (`DESC`, largest/latest first). *Worked example*, given a `Students` table (id, name, mark, form) containing (1,'Amara',82,'10A'), (2,'Ben',45,'10B'), (3,'Chen',67,'10A'), (4,'Diya',90,'10C'), (5,'Ewan',38,'10B'):
```
SELECT name, mark FROM Students WHERE mark >= 50 ORDER BY mark DESC;
```
returns, in order: Diya (90), Amara (82), Chen (67) -- Ben and Ewan are excluded (both under 50), and the remaining three are sorted from highest mark to lowest. To change data: `INSERT INTO table (field1, field2, ...) VALUES (value1, value2, ...)` adds a new record, e.g. `INSERT INTO Students (id, name, mark, form) VALUES (6, 'Farah', 71, '10C');` adds Farah as a new sixth record; `UPDATE table SET field = value WHERE condition` edits existing matching record(s), e.g. `UPDATE Students SET mark = 95 WHERE name = 'Ben';` changes Ben's mark to 95 (only Ben's record, because of the WHERE clause); `DELETE FROM table WHERE condition` removes matching record(s), e.g. `DELETE FROM Students WHERE mark < 40;` removes Ewan's record (mark 38), leaving everyone else. A `WHERE` clause is essential on `UPDATE` and `DELETE`: leaving it out would change or delete every record in the table, not just the intended one(s).

## Explicitly not here
This is the last databases stage; S29 covers the wider ethical, legal and environmental impacts of digital technology.
