# S02_Types_Literals_Conversions_Modifiers - Test: Types, literals, conversions and modifiers

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    cout << sizeof(char) << " " << sizeof('a' + 'b') << " " << sizeof(3.0f) << " " << sizeof(3.0) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    unsigned char c = 255;
    c++;
    cout << +c << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    int i = 7;
    double d = i / 2;
    double e = i / 2.0;
    cout << d << " " << e << " " << (int)e << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
int next() { static int v = 10; return v++; }
// ---- main ----
    next(); next();
    cout << next() << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    const int k = 5;
    k = 6;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    cout << 0b1010 << " " << 012 << " " << 0xa << " " << 10e-1 << endl;
```
7. Which are true? Choose every correct option.
   A. A const variable must be initialised
   B. A static local variable keeps its value between calls
   C. unsigned int arithmetic wraps around
   D. `sizeof(char) depends on the platform`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1 4 4 8
```
2. Actual result (from running it):
```
0
```
3. Actual result (from running it):
```
3 3.5 3
```
4. Actual result (from running it):
```
12
```
5. Actual result (from running it):
```
(does not compile: assignment of read-only variable ‘k’)
```
6. Actual result (from running it):
```
10 10 10 1
```
7. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Types_Literals_Conversions_Modifiers` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Strings_and_Aggregates.
