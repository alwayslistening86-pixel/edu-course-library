# S27_Data_Modelling_and_Normalisation - Lesson: Conceptual data models, relational databases and normalisation

## Goal
The learner uses conceptual data models and entity-relationship modelling, explains relational databases, and applies database design and normalisation techniques.

## Syllabus items taught here
- 4.10.1.1 - Conceptual data models and entity-relationship modelling
- 4.10.2.1 - Relational databases
- 4.10.3.1 - Database design and normalisation

## How to teach this
Ask the learner what could go wrong storing every order's customer address directly in the orders table, repeated on every single order that customer places. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.10.1.1 Conceptual data models and entity-relationship modelling
A **conceptual data model** represents the important things (**entities**) a system needs to store data about, and the **relationships** between them, independent of how it will actually be implemented in a particular database system. **Entity-relationship (ER) modelling** shows this visually: entities (e.g. Customer, Order) as boxes, with the **relationships** between them labelled by their **cardinality/degree** -- **one-to-one** (1:1, e.g. one Person has one Passport), **one-to-many** (1:M, e.g. one Customer places many Orders) or **many-to-many** (M:N, e.g. many Students take many Courses, usually requiring a linking entity to represent in a relational database).

#### 4.10.2.1 Relational databases
A **relational database** organises data into **tables** (relations), each with **rows** (records/tuples) and **columns** (fields/attributes). A **primary key** uniquely identifies each row in a table (no two rows share the same primary key value, and it cannot be blank/null); a **foreign key** is a field in one table that references another table's primary key, implementing a relationship between the two tables (e.g. an Orders table's `customer_id` foreign key referencing Customers' primary key `customer_id`). A many-to-many relationship (e.g. Students and Courses) is implemented using a **linking table** holding a foreign key to each side.

#### 4.10.3.1 Database design and normalisation
**Database design** involves identifying entities, attributes, keys and relationships (often starting from an ER model) and organising them into well-structured tables. **Normalisation** is a systematic process for reducing data **redundancy** (the same fact stored in more than one place) and avoiding **update anomalies** (e.g. updating a customer's address in one order row but forgetting another, leaving inconsistent data). Un-normalised data with repeating groups is progressively reorganised into **first normal form (1NF)** (no repeating groups; every field holds a single, atomic value), **second normal form (2NF)** (1NF, and every non-key attribute depends on the *whole* of the primary key, not just part of it -- relevant where the key is composite) and **third normal form (3NF)** (2NF, and no non-key attribute depends on another non-key attribute -- i.e. no transitive dependency; each non-key attribute depends only, and directly, on the key). Normalisation trades some query complexity (more tables to join) for far less redundancy and fewer update anomalies.

## Explicitly not here
Writing SQL to actually query a database, client-server databases and Big Data are S28.
