# S03_Console_Input_and_Output - Test: Console input and output

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    cout << "[" << setw(3) << 12345 << "]" << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    cout << setfill('0') << setw(3) << 7 << " " << 7 << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    cout << left << setw(5) << "ab" << "|" << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    cout << true << " " << boolalpha << true << " " << (1 > 2) << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    cout << "a" << endl << "b\n" << "c" << '\n';
```
6. Which are true? Choose every correct option.
   A. setw affects only the next output item
   B. cerr is the standard error stream
   C. `cin >> x skips leading whitespace`
   D. endl does not flush the stream

## Answer key (for the tutor only)
1. Actual result (from running it):
```
[12345]
```
2. Actual result (from running it):
```
007 7
```
3. Actual result (from running it):
```
ab   |
```
4. Actual result (from running it):
```
1 true false
```
5. Actual result (from running it):
```
a
b
c
```
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Console_Input_and_Output` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Decisions_switch_and_goto.
