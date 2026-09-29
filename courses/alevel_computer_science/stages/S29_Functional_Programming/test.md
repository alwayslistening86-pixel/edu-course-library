# S29_Functional_Programming - Test: Functional programming: concepts, higher-order functions and lists

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
from functools import reduce
nums = [5, 2, 8, 1]
print(reduce(lambda a, b: a + b, nums))
```
2. Explain what it means for a function to be a first-class object in a functional programming language, giving one example of this in use. [3 marks]
3. Explain what composition of functions means, and give the result of composing a squaring function then an increment-by-1 function, applied to the input 4. [3 marks]
4. Using the head/tail view of lists, explain how a recursive function summing all the elements of a list would work, stating its base case. [3 marks]
5. Explain what filter does, and give the result of filtering [12, 5, 8, 3, 20] to keep only values greater than 10. [2 marks]
6. Which higher-order function combines every element of a list into a single value by repeatedly applying a combining function? Choose every correct option.
   A. `reduce (fold)`
   B. `map`
   C. `filter`
   D. `compose`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
16
```
2. [3] B1 a function can be treated like any other value: stored in a variable, passed as an argument to another function, or returned as a result from a function; B1 example, e.g. passing a doubling function as the argument to map; B1 this is what makes higher-order functions (like map, filter, reduce) possible at all.
3. [3] B1 composition builds a new function by feeding one function's output directly in as the next function's input; B1 correct working: square(4) = 16, then increment(16) = 17; A1 result: 17.
4. [3] B1 base case: an empty list sums to 0; B1 general case: the sum of a non-empty list is its head plus the sum of its tail; B1 this recursively breaks the list down one element at a time until the empty-list base case is reached, then the sums are added back up as the recursion unwinds.
5. [2] B1 filter keeps only the elements for which a given predicate function returns True, discarding the rest, without an explicitly written loop; B1 result: [12, 20].
6. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S29_Functional_Programming` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
