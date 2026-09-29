# S07_Data_Structures - Test: Data structures: arrays and records

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
students = [{"name": "Ben", "mark": 62}, {"name": "Amy", "mark": 78}]
print(students[1]["name"])
```
2. Explain the difference between an array and a record. [3 marks]
3. Given the array days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], state days[0] and days[4]. [2 marks]
4. Explain why a record (rather than several separate arrays) is a sensible way to store a single student's name, mark and form group. [2 marks]

## Answer key (for the tutor only)
1. Actual result (from running it):
```
Amy
```
2. [3] B1 an array stores multiple values, usually of the same type, each accessed by an index/position; B1 a record groups several related fields (possibly of different types) about one entity under one name; B1 an array of records combines both: many entities, each with several named fields.
3. [2] B1 days[0] is 'Mon'; B1 days[4] is 'Fri'.
4. [2] B1 keeps all the related data about one student together under a single name; B1 avoids the risk of separate arrays getting out of step (e.g. wrong mark matched to wrong student).

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Data_Structures` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Input_Output.
