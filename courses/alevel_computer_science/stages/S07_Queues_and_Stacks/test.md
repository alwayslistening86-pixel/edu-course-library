# S07_Queues_and_Stacks - Test: Queues and stacks

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Starting from an empty stack, trace: push(X); push(Y); push(Z); pop(); push(W); pop(). Give the sequence of values returned by pop(), and the final contents of the stack. [3 marks]
2. Explain the difference between a queue and a stack in terms of the order items are removed. [2 marks]
3. Explain what the peek (or top) operation does on a stack, and how it differs from pop. [2 marks]
4. A queue is used to manage print jobs sent to a printer. Which behaviour does this achieve? Choose every correct option.
   A. jobs are printed in the order they were sent (first sent, first printed)
   B. the most recently sent job is always printed first
   C. jobs are printed in a random order
   D. only the last job sent is ever printed

## Answer key (for the tutor only)
1. [3] M1 first pop() returns Z (stack was [X,Y,Z]); M1 second pop() returns W (stack was [X,Y,W] after push(W)); A1 final stack contents: [X, Y].
2. [2] B1 a queue is First-In-First-Out (FIFO): items are removed in the same order they were added; B1 a stack is Last-In-First-Out (LIFO): the most recently added item is removed first.
3. [2] B1 peek returns the value of the top item without removing it from the stack; B1 pop returns the top item and removes it, changing the stack's contents.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Queues_and_Stacks` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Graphs_Trees_Hash_Dict_Vectors.
