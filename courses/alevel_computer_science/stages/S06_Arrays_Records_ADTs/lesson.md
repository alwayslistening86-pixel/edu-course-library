# S06_Arrays_Records_ADTs - Lesson: Arrays, records/files and abstract data types

## Goal
The learner uses single- and multi-dimensional arrays and records/files, and explains the concept of an abstract data type.

## Syllabus items taught here
- 4.2.1.1 - Data structures, arrays (single- and multi-dimensional) and records/files
- 4.2.1.4 - Abstract data types

## How to teach this
Ask the learner how they would store a whole seating plan (rows and columns of seats) in one structure, rather than a single row. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.2.1.1 Data structures, arrays (single- and multi-dimensional) and records/files
A **single-dimensional array** stores multiple values (usually of the same type) under one name, indexed by position (from 0 in most languages, including Python lists). A **multi-dimensional array** (e.g. a 2D array/grid, `grid[row][col]`) extends this to more than one index, useful for tables, grids or matrices. A **record** groups several related fields (possibly of different types) about one entity under one name (a Python dictionary, or a list of dictionaries for many records); a **file** stores data (often many records) persistently on secondary storage, to be read/written by a program across separate runs.

#### 4.2.1.4 Abstract data types
An **abstract data type (ADT)** is a data type defined by its behaviour (the operations that can be performed on it, and what they do) rather than by how it is implemented internally. A **stack** and a **queue** (S07) are both classic ADTs: the specification (push/pop for a stack; add/remove for a queue) is fixed, but the underlying implementation (e.g. built from an array or from a linked structure) is hidden from -- and can change without affecting -- the code that uses it. Thinking in terms of ADTs is a form of abstraction: the programmer using a stack does not need to know how it is implemented, only what operations it supports.

## Explicitly not here
Two specific ADTs, queues and stacks, are covered fully in S07.
