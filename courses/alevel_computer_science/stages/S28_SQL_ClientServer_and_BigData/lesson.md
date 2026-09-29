# S28_SQL_ClientServer_and_BigData - Lesson: SQL, client-server databases and Big Data

## Goal
The learner writes SQL to query/update relational databases, explains client-server database architecture, and describes Big Data's defining characteristics and processing needs.

## Syllabus items taught here
- 4.10.4.1 - Structured Query Language (SQL)
- 4.10.5.1 - Client-server databases
- 4.11.1.1 - Big Data: volume, velocity and variety; distributed processing

## How to teach this
Ask the learner how they would find, from a table of thousands of orders, only the ones placed in the last week by a particular customer -- without reading every row by eye. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.10.4.1 Structured Query Language (SQL)
**Structured Query Language (SQL)** manipulates and queries relational databases. `SELECT columns FROM table WHERE condition` retrieves matching rows (a specific list of columns, or `*` for all); `ORDER BY column` sorts results; joining tables (e.g. `SELECT a.name, b.total FROM Customers a JOIN Orders b ON a.customer_id = b.customer_id`) combines matching rows across tables via their key relationship. `INSERT INTO table (columns) VALUES (values)` adds a new row; `UPDATE table SET column = value WHERE condition` modifies matching existing rows; `DELETE FROM table WHERE condition` removes matching rows (omitting `WHERE` from `UPDATE`/`DELETE` affects every row -- a common, serious mistake).

#### 4.10.5.1 Client-server databases
A **client-server database** runs the database management system on a central server, which client applications connect to (often over a network) to run queries and updates, rather than each client holding its own private copy of the data. This centralises data (one consistent, up-to-date version, rather than out-of-sync copies), simplifies backup/security/access control, and lets many clients share the same data concurrently -- at the cost of clients depending on network connectivity to the server, and the server needing to handle potentially many simultaneous requests correctly (e.g. two clients trying to update the same row at once).

#### 4.11.1.1 Big Data: volume, velocity and variety; distributed processing
**Big Data** describes datasets too large, fast-changing, or varied for traditional single-machine database approaches to handle well, often characterised by three properties: **volume** (the sheer size of the data), **velocity** (how fast new data arrives and must be processed, sometimes in real time) and **variety** (a mix of structured, semi-structured and unstructured data, e.g. structured sales records alongside unstructured social media text). Because a single machine cannot realistically store or process Big Data alone, it is typically handled by **distributed processing** across many servers working together; the **functional programming paradigm** (S29) suits this well, because pure functions (that don't rely on or change shared, mutable state) can safely be run on different chunks of data across different machines in parallel, without one machine's work interfering with another's. Big Data is represented and modelled in various ways beyond the traditional relational model, including **fact-based** models (storing individual discrete facts/observations, well suited to append-only, rapidly-arriving data) and **graph schema** approaches (modelling data as richly interconnected nodes/relationships, well suited to highly-connected data like social networks).

## Explicitly not here
This is the last databases/Big-Data stage; S29 covers functional programming.
