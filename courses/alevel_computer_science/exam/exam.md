# A-level Computer Science (AQA 7517) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
Paper 1 covers programming, data structures, algorithms and theory of computation (S01-S15): multiple-choice, short-answer and longer questions, including writing/adapting short Python routines (as a stand-in for AQA's on-screen skeleton-program task) and tracing algorithms/finite state machines/Turing machines in AQA pseudo-code. Paper 2 covers data representation, computer systems, computer organisation and architecture, the consequences of computing, networking, databases and functional programming (S16-S29): multiple-choice, short-answer, longer-answer and extended-response questions, plus SQL questions. Questions are original; write fresh ones rather than reusing stage tests. The ready-made questions below are a starter bank; the tutor writes the rest, kept to each paper's real content split.

## 11 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Paper 1] Trace a binary search for the value 26 in the sorted list [3, 8, 15, 21, 26, 34, 40, 55] (indices 0-7). Show each middle index checked and state the number of comparisons. [4 marks]
2. What does this print? (If it raises an error, name it.)
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```
3. [Paper 1] A stack is used to reverse the order of the characters in "CODE". Describe the sequence of pushes and pops needed, and state the final output. [3 marks]
4. [Paper 1] Give the Big-O time complexity of linear search and of binary search on a sorted list of n items, and explain why binary search scales better as n grows large. [3 marks]
5. Which finite state machine feature distinguishes a Moore machine from a Mealy machine? Choose every correct option.
   A. a Moore machine's output depends only on the current state; a Mealy machine's output depends on the current state and input
   B. a Moore machine has no accepting states
   C. a Mealy machine cannot have more than two states
   D. a Moore machine cannot process input strings
6. [Paper 2] Represent -58 in 8-bit two's complement, showing your working. [3 marks]
7. [Paper 2] Explain the purpose of the program counter and the memory address register in the fetch-execute cycle. [3 marks]
8. In relational database normalisation, a table in second normal form (2NF) but not yet in third normal form (3NF) contains which kind of dependency? Choose every correct option.
   A. a transitive dependency (a non-key attribute depends on another non-key attribute)
   B. a partial dependency on part of a composite primary key
   C. a repeating group of values in one column
   D. no dependency at all between its attributes
9. [Paper 2] Given a Students table (student_id, name, course_id) and a Courses table (course_id, course_name), write SQL to list each student's name and the name of the course they are on, ordered by student name. [3 marks]
10. [Paper 2] A function `double_all` uses `map` to double every number in a list in a functional language. Explain what `map` does in general, and give the result of applying it with a doubling function to [3, 7, 2]. [3 marks]
11. [Paper 2] Discuss the ethical and social issues raised by an algorithm used to screen job applications automatically. [6 marks]

## Answer key for the ready-made items (tutor only)
1. [4] M1 middle (0+7)//2=3, list[3]=21 < 26, search right half (4-7); M1 middle (4+7)//2=5, list[5]=34 > 26, search left half (4-4); M1 middle (4+4)//2=4, list[4]=26, found; A1 3 comparisons.
2. Actual result (from running it):
```
120
```
3. [3] B1 push C, O, D, E onto the stack in that order; B1 pop repeatedly (LIFO), which reverses the order; B1 output: EDOC.
4. [3] B1 linear search: O(n); B1 binary search: O(log n); B1 because each comparison in binary search halves the remaining search space, so the number of comparisons grows only logarithmically with n, while linear search's grows directly with n.
5. Correct: A (exactly these options, no others)
6. [3] M1 58 in binary: 00111010; M1 invert the bits: 11000101; A1 add 1: 11000110.
7. [3] B1 the program counter (PC) holds the address of the next instruction to be fetched; B1 the memory address register (MAR) holds the address currently being accessed in memory; B1 the PC's value is copied to the MAR at the start of fetch, then the PC is incremented ready for the next instruction.
8. Correct: A (exactly these options, no others)
9. [3] M1 correct SELECT students.name, courses.course_name; M1 FROM Students JOIN Courses ON students.course_id = courses.course_id; A1 ORDER BY students.name;
10. [3] B1 map applies a given function to every element of a list, producing a new list of the results, without a manually written loop; B1 the original list is unchanged (no mutation) in a purely functional style; B1 result: [6, 14, 4].
11. [6] Level 2 (4-6): balanced discussion covering at least two of: bias embedded in training data leading to unfair discrimination; lack of transparency/explainability in automated decisions; accountability when an algorithm makes a wrong or unfair decision; the scale at which one flawed algorithm can affect many applicants; and a reasoned overall point. Level 1 (1-3): limited/one-sided discussion. 0: no relevant discussion.

## Grading
Mark short answers and multiple-choice against the mark schemes; mark calculations, conversions and traces with method shown (a correct final answer with no valid method shown earns only what the mark scheme allows for a bare answer); mark the extended-response ethics/impact question by levels. A pass needs at least 50% of the 200 marks overall and at least 40% on each paper. Report the total, the percentage per paper and the weakest topic areas. AQA's grade boundaries change every series, so the course does not claim a predicted grade.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete (the NEA is out of scope; see the notice).
- **Not yet:** leave `exam_status: "available"`, name the weakest topic areas, offer targeted review, and retry with fresh papers.
