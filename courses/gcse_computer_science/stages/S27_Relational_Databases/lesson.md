# S27_Relational_Databases - Lesson: Relational databases

## Goal
The learner explains the concept of a database and of a relational database, uses the terms table, record, field, data type, primary key and foreign key, and explains how relational databases reduce data inconsistency and redundancy.

## Syllabus items taught here
- 3.7.1 - Relational databases: tables, records, fields, primary and foreign keys

## How to teach this
Ask the learner what could go wrong if a school stored every teacher's name separately, retyped in every single class list, rather than looking it up from one shared staff list. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.7.1 Relational databases: tables, records, fields, primary and foreign keys
A **database** is an organised collection of structured data, held so it can be efficiently entered, stored, updated and retrieved. A **relational database** organises data into multiple related **tables** rather than one large flat file, with tables linked together through shared fields. A **table** is a named collection of records about one type of entity (e.g. a Students table); a **record** is one row of a table, representing a single item/instance (e.g. one student); a **field** is one column of a table, representing one category of data held about every record (e.g. name, mark, form); a **data type** restricts what kind of value a field can hold (e.g. integer, text, date), which helps keep the data consistent and valid. A **primary key** is a field (or combination of fields) whose value uniquely identifies each record in a table -- no two records may share the same primary key value, and it cannot be left empty; a **foreign key** is a field in one table that holds the value of another table's primary key, creating a link between the two tables (e.g. a Results table might have a StudentID foreign key linking each result back to the correct student in the Students table). By storing shared data once, in one table, and linking to it via foreign keys rather than repeating it everywhere it's needed, relational databases reduce **data redundancy** (the same data being needlessly duplicated across many records) and **data inconsistency** (duplicated copies of the same fact getting out of sync and disagreeing with each other, e.g. a student's name spelled two different ways in two different tables).

## Explicitly not here
Actually writing the queries that read and change this data is S28.
