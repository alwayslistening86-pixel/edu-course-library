# S05_Loops - Test: Loops, break and continue

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    int c = 0;
    for (int i = 0; i < 10; i += 3) c++;
    cout << c << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int i = 0;
    while (i < 5) {
        i++;
        if (i == 2) continue;
        if (i == 4) break;
        cout << i;
    }
    cout << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (j == i) cout << i;
    cout << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    int x = 100;
    do { cout << "once "; } while (x < 0);
    cout << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    int total = 0;
    for (int v : {4, 5, 6}) total += v;
    cout << total << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    int i;
    for (i = 0; i < 5; i++);
    cout << i << endl;
```
7. Write a loop that prints the first 8 Fibonacci numbers on one line: 0 1 1 2 3 5 8 13.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
4
```
2. Actual result (from running it):
```
13
```
3. Actual result (from running it):
```
012
```
4. Actual result (from running it):
```
once 
```
5. Actual result (from running it):
```
15
```
6. Actual result (from running it):
```
5
```
7. The tutor runs or reads the learner's answer and checks: Correct loop and output; uses two running variables or an array.

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Loops` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Functions_and_Return.
