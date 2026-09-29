# S08_Graphs_Trees_Hash_Dict_Vectors - Lesson: Graphs, trees, hash tables, dictionaries and vectors

## Goal
The learner explains graphs, trees, hash tables, dictionaries and vectors as data structures, and how each stores/organises data.

## Syllabus items taught here
- 4.2.4.1 - Graphs
- 4.2.5.1 - Trees
- 4.2.6.1 - Hash tables
- 4.2.7.1 - Dictionaries
- 4.2.8.1 - Vectors

## How to teach this
Ask the learner how a map app might store which towns connect to which by road (a graph), versus how a family tree branches from one ancestor (a tree). AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.2.4.1 Graphs
A **graph** is a set of **nodes (vertices)** connected by **edges**; edges can be **directed** (one-way, e.g. a one-way street) or **undirected** (two-way), and can be **weighted** (each edge has an associated value, e.g. a distance or cost) or unweighted. Graphs model networks: road maps, social networks, computer networks, dependency relationships.

#### 4.2.5.1 Trees
A **tree** is a connected, undirected graph with no cycles: one node is the **root**, and every other node has exactly one **parent**, possibly with several **children**; a node with no children is a **leaf**. A **binary tree** restricts each node to at most two children. Trees model hierarchical data: file systems, organisation charts, decision structures, and (as a binary search tree) efficiently searchable ordered data (S10).

#### 4.2.6.1 Hash tables
A **hash table** stores key-value pairs by applying a **hash function** to a key to compute an index into an underlying array, giving very fast (close to constant-time, O(1)) lookup, insertion and deletion on average. A **collision** occurs when two different keys hash to the same index; common resolutions include chaining (storing a small list at that index) or probing (finding the next free slot).

#### 4.2.7.1 Dictionaries
A **dictionary** (associative array/map) stores **key-value pairs**, where each unique key maps to a value, and a value is looked up by its key rather than by numeric position (unlike an array). Many languages' built-in dictionaries (e.g. Python's `dict`) are implemented internally using a hash table for fast lookup. *Example:* `ages = {"Amy": 15, "Ben": 16}`; `ages["Amy"]` is 15.

#### 4.2.8.1 Vectors
A **vector** is a one-dimensional, ordered, indexed collection of values -- similar to a single-dimensional array, but in many languages a vector can **grow or shrink dynamically** at runtime (unlike a fixed-size array), automatically managing its own underlying storage as items are added or removed.

## Explicitly not here
How to traverse graphs and trees (specific algorithms) is S09; searching and sorting algorithms over these structures are S10-S11.
