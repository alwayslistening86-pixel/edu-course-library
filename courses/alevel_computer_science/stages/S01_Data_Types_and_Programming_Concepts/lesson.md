# S01_Data_Types_and_Programming_Concepts - Lesson: Data types and core programming concepts

## Goal
The learner uses AQA's full set of A-level data types, declares/assigns variables and constants, and uses definite/indefinite iteration and nested selection/iteration with meaningful identifiers.

## Syllabus items taught here
- 4.1.1.1 - Data types: integer, real, Boolean, character, string, date/time, pointer/reference, record, array; user-defined types
- 4.1.1.2 - Programming concepts: declaration, assignment, definite and indefinite iteration, nested selection/iteration, meaningful identifiers

## How to teach this
Ask the learner what type of value 'date of birth', 'a memory address' and 'a student record' each need -- these go beyond GCSE's five core types. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.1.1.1 Data types: integer, real, Boolean, character, string, date/time, pointer/reference, record, array; user-defined types
A-level extends GCSE's five core data types (**integer**, **real/float**, **Boolean**, **character**, **string**) with: **date/time** (a value representing a calendar date and/or time of day), **pointer/reference** (a value that stores the memory address of another piece of data, rather than the data itself), **record** (a grouping of related fields, possibly of different types, under one name) and **array** (an indexed collection of values, usually of the same type). Languages also let the programmer define **user-defined data types** built from these -- e.g. a `Point` record combining two reals for x and y, or an **enumerated type** naming a fixed set of values (e.g. `MONDAY, TUESDAY, ...`). Choosing the right type affects both what operations are valid and how memory is used.

#### 4.1.1.2 Programming concepts: declaration, assignment, definite and indefinite iteration, nested selection/iteration, meaningful identifiers
**Declaration** introduces a name (and often its type); **assignment** (`=`) gives it a value. **Definite (count-controlled) iteration** (`FOR`) repeats a known number of times; **indefinite (condition-controlled) iteration** (`WHILE`, condition tested first; or `REPEAT ... UNTIL`, condition tested after, so the body always runs at least once) repeats until a condition changes. **Nested selection** (an `IF` inside another `IF`) and **nested iteration** (a loop inside another loop) let more than one condition, or more than one dimension of repetition (e.g. rows and columns), be handled together. **Meaningful identifier names** (`total_score` rather than `x`) make code easier to read, maintain and debug, and reduce the chance of using the wrong variable.

## Explicitly not here
The individual arithmetic, relational and Boolean operators used inside expressions and conditions are S02.
