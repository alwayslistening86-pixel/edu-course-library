# S06_Arrays_Records_ADTs - Test: Arrays, records/files and abstract data types

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
seats = [["A1", "A2"], ["B1", "B2"]]
for row in seats:
    print(row)
```
2. Given the 2D array table = [[10, 20], [30, 40], [50, 60]], state table[2][1] and table[0][0]. [2 marks]
3. Explain the difference between a record and a file. [2 marks]
4. Explain why defining a data structure as an abstract data type is useful when writing large programs. [3 marks]

## Answer key (for the tutor only)
1. Actual result (from running it):
```
['A1', 'A2']
['B1', 'B2']
```
2. [2] B1 table[2][1] is 60; B1 table[0][0] is 10.
3. [2] B1 a record groups related fields about one entity under one name, held in memory while the program runs; B1 a file stores data (often many records) persistently on secondary storage, so it survives after the program ends.
4. [3] B1 code that uses the ADT only needs to know its operations (the interface), not its internal implementation; B1 this hides unnecessary detail (abstraction), making the code using it simpler to write and understand; B1 the internal implementation can later be changed/optimised without needing to change the code that uses the ADT.

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Arrays_Records_ADTs` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Queues_and_Stacks.
