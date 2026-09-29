# S06_Functions_and_Return - Test: Functions and return

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
double avg(int a, int b) { return (a + b) / 2; }
// ---- main ----
    cout << avg(3, 4) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
int sq(int x) { return x * x; }
// ---- main ----
    cout << sq(2.9) << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
void f() { return 1; }
// ---- main ----
    f();
```
4. What is the output? If it does not compile, say so and why.
```cpp
int g(int a, int b) { return a - b; }
// ---- main ----
    cout << g(5) << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
int area(int, int);
int area(int w, int h) { return w * h; }
// ---- main ----
    cout << area(3, 4) << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
void show(int n) {
    if (n < 0) { cout << "neg"; return; }
    cout << "ok";
}
// ---- main ----
    show(-1); show(1);
    cout << endl;
```
7. Which are true? Choose every correct option.
   A. A prototype allows a call before the definition
   B. A void function may use return; to exit early
   C. `main must always end with return 0;`
   D. A function's return value can be ignored by the caller

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3
```
2. Actual result (from running it):
```
4
```
3. Actual result (from running it):
```
(does not compile: return-statement with a value, in function returning ‘void’ [-fpermissive])
```
4. Actual result (from running it):
```
(does not compile: too few arguments to function ‘int g(int, int)’)
```
5. Actual result (from running it):
```
12
```
6. Actual result (from running it):
```
negok
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Functions_and_Return` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Parameter_Passing_and_Recursion.
