# S01_Operators_and_Expressions - Test: Operators and expressions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    cout << 7 + 3 * 2 % 4 << " " << (7 + 3) * 2 % 4 << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int i = 5;
    int j = i--;
    int k = --i;
    cout << i << j << k << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    unsigned x = 0xF0;
    cout << (x >> 4) << " " << (x & 0x3C) << " " << (~0u == 0xFFFFFFFF) << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    int a = 1, b = 2, c = 3;
    cout << (a < b ? b < c ? 'x' : 'y' : 'z') << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    int n = 0;
    bool r = (n != 0) && (10 / n > 1);
    cout << r << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    cout << (1 << 2 + 1) << " " << ((1 << 2) + 1) << endl;
```
7. Which operators take exactly three operands? Choose every correct option.
   A. `?:`
   B. `+`
   C. `&&`
   D. `sizeof`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
9 0
```
2. Actual result (from running it):
```
353
```
3. Actual result (from running it):
```
15 48 1
```
4. Actual result (from running it):
```
x
```
5. Actual result (from running it):
```
0
```
6. Actual result (from running it):
```
8 5
```
7. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Operators_and_Expressions` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Types_Literals_Conversions_Modifiers.
