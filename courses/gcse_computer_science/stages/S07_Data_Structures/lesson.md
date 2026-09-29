# S07_Data_Structures - Lesson: Data structures: arrays and records

## Goal
The learner understands the concept of a data structure and uses arrays (or an equivalent list structure) and records (or an equivalent) in the design of solutions.

## Syllabus items taught here
- 3.2.6 - Data structures: arrays and records

## How to teach this
Ask the learner how they'd store the names of every student in a class in one place, and then how they'd store one student's name, age and form group together. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.2.6 Data structures: arrays and records
A **data structure** organises a collection of related data so it can be used efficiently. An **array** (Python's list can be used to represent it) stores multiple values of (usually) the same type under one name, each accessed by its **index** (position); most languages, including Python's lists, index from 0. *Example:* `scores = [56, 72, 81, 49]`; `scores[0]` is 56, `scores[2]` is 81; a two-dimensional array (a grid, e.g. `grid[row][col]`) extends the idea to rows and columns. A **record** groups several related fields, possibly of different types, about a single entity under one name (Python's dictionary is commonly used to represent one, e.g. `student = {"name": "Amara", "age": 15, "form": "10B"}`); an array of records (a list of dictionaries) is a common way to store many entities, each with several fields, e.g. a whole class's data.

## Explicitly not here
Reading values in and printing values out is S08.
