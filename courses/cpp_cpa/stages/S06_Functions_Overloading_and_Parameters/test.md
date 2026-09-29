# S06_Functions_Overloading_and_Parameters - Test: Functions, overloading and parameters

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
void g(double) { cout << "double "; }
void g(int) { cout << "int "; }
// ---- main ----
    g(2.5f); g(true); g(3);
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
int f(int x) { return x; }
double f(int x) { return x * 1.0; }
// ---- main ----
    cout << f(1);
```
3. What is the output? If it does not compile, say so and why.
```cpp
void h(int a, int b = 2);
void h(int a, int b) { cout << a * b << endl; }
// ---- main ----
    h(4);
```
4. What is the output? If it does not compile, say so and why.
```cpp
void swapPtr(int *a, int *b) { int t = *a; *a = *b; *b = t; }
void swapVal(int a, int b) { int t = a; a = b; b = t; }
// ---- main ----
    int x = 1, y = 2;
    swapVal(x, y);
    cout << x << y;
    swapPtr(&x, &y);
    cout << x << y << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
int digits(int n) { return n < 10 ? 1 : 1 + digits(n / 10); }
// ---- main ----
    cout << digits(0) << digits(99) << digits(12345) << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
void k(long) { cout << "long"; }
void k(double) { cout << "double"; }
// ---- main ----
    k(1);
```
7. Which can distinguish two overloads of the same function? Choose every correct option.
   A. Number of parameters
   B. Types of parameters
   C. Return type only
   D. Parameter names only

## Answer key (for the tutor only)
1. Actual result (from running it):
```
double int int 
```
2. Actual result (from running it):
```
(does not compile: ambiguating new declaration of ‘double f(int)’)
```
3. Actual result (from running it):
```
8
```
4. Actual result (from running it):
```
1221
```
5. Actual result (from running it):
```
125
```
6. Actual result (from running it):
```
(does not compile: call of overloaded ‘k(int)’ is ambiguous)
```
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Functions_Overloading_and_Parameters` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Preprocessor_Directives.
