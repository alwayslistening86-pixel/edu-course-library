# S08_Graphs_Trees_Hash_Dict_Vectors - Test: Graphs, trees, hash tables, dictionaries and vectors

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a graph and a tree. [2 marks]
2. Explain how a hash table achieves fast lookup, and what a collision is. [3 marks]
3. Explain the difference between a dictionary and an array as ways of storing data. [2 marks]
4. Explain one advantage a vector has over a fixed-size array. [2 marks]
5. Which structure is best suited to representing a company's organisational chart, where each employee (except the top) has exactly one manager? Choose every correct option.
   A. a tree
   B. a hash table
   C. a queue
   D. a stack

## Answer key (for the tutor only)
1. [2] B1 a tree is a special kind of graph: connected, with no cycles, and exactly one path between the root and any other node; B1 a general graph can have cycles, disconnected parts, and more than one path between two nodes.
2. [3] B1 a hash function converts a key into an array index, so the value can be accessed almost directly rather than by searching; B1 this gives close-to-constant-time (O(1)) average lookup/insertion/deletion; B1 a collision is when two different keys hash to the same index, which must then be resolved (e.g. by chaining or probing).
3. [2] B1 an array is indexed by numeric position; B1 a dictionary is indexed by a (often more meaningful) key, mapping each unique key to a value.
4. [2] B1 a vector can grow or shrink dynamically at runtime as items are added/removed; B1 a fixed-size array's size must be decided in advance and cannot change, which can waste memory or run out of room.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Graphs_Trees_Hash_Dict_Vectors` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Graph_Tree_Traversal_and_RPN.
