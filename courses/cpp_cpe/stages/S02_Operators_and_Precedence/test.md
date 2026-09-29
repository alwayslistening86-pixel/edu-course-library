# S02_Operators_and_Precedence - Test: Operators, precedence and short-circuiting

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    cout << 17 / 5 << " " << 17 % 5 << " " << -17 / 5 << " " << 17.0 / 5 << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    cout << 2 + 3 * 4 - 6 / 2 << " " << (2 + 3) * (4 - 6) / 2 << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    int x = 12;
    cout << (x >> 2) << " " << (x ^ 5) << " " << (~x & 0xF) << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    int a = 0, b = 0;
    if (a++ || b++) {}
    if (a++ && b++) {}
    cout << a << b << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    int a = 5, b = 3;
    cout << (a > b == 1) << (a & 1 == 1) << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    int n = 4;
    n *= 2 + 1;
    cout << n << endl;
```
7. Which operators are right-associative? Choose every correct option.
   A. `=`
   B. `+`
   C. `?:`
   D. `&&`
   E. `-=`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3 2 -3 3.4
```
2. Actual result (from running it):
```
11 -5
```
3. Actual result (from running it):
```
3 9 3
```
4. Actual result (from running it):
```
22
```
5. Actual result (from running it):
```
11
```
6. Actual result (from running it):
```
12
```
7. Correct: A, C, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Operators_and_Precedence` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Console_Input_and_Output.
