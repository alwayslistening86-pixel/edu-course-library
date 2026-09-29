# S27_Data_Modelling_and_Normalisation - Test: Conceptual data models, relational databases and normalisation

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a primary key and a foreign key, using a Customers/Orders example. [3 marks]
2. A Students table and a Courses table have a many-to-many relationship (each student takes several courses; each course has several students). Explain how this is implemented in a relational database. [3 marks]
3. Explain what an update anomaly is, giving an example based on a single un-normalised table storing each order together with its customer's full address. [3 marks]
4. Explain, in general terms, what third normal form (3NF) requires beyond second normal form (2NF). [2 marks]
5. Which best describes the purpose of normalisation? Choose every correct option.
   A. reducing data redundancy and avoiding update anomalies by systematically reorganising tables
   B. making every table in a database as large as possible
   C. removing the need for any primary keys
   D. converting a relational database into a spreadsheet

## Answer key (for the tutor only)
1. [3] B1 a primary key uniquely identifies each row in its own table (e.g. customer_id in Customers); B1 a foreign key is a field in one table referencing another table's primary key (e.g. customer_id in Orders, referencing Customers); B1 this foreign key implements the relationship between an order and the customer who placed it.
2. [3] B1 a many-to-many relationship cannot be implemented directly with a single foreign key on either side; B1 a linking table is created, with a foreign key referencing Students' primary key and a foreign key referencing Courses' primary key; B1 each row in the linking table represents one student-course enrolment.
3. [3] B1 an update anomaly is when the same fact is stored redundantly in multiple places, and an update to one copy is made while another copy is missed, leaving inconsistent data; B1 example: if a customer's address is repeated on every one of their orders and they move house, every single order row needs updating; B1 if even one row is missed, the database then holds two different addresses for the same customer, an inconsistency.
4. [2] B1 3NF requires the table to already be in 2NF (every non-key attribute depends on the whole of the primary key); B1 3NF additionally requires no non-key attribute to depend on another non-key attribute (no transitive dependency) -- every non-key attribute must depend only, and directly, on the key.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S27_Data_Modelling_and_Normalisation` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S28_SQL_ClientServer_and_BigData.
