# S08_Pointers_and_Dynamic_Memory - Test: Pointers and dynamic memory

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    double d[3] = {1.5, 2.5, 3.5};
    double *p = d;
    p += 2;
    cout << *p << " " << p - d << " " << (p > d) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
struct S { int v; };
// ---- main ----
    S s{3};
    S *ps = &s;
    (*ps).v += 1;
    ps->v *= 2;
    cout << s.v << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    int x = 1, y = 2;
    const int *p = &x;
    p = &y;
    *p = 5;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    int *p = new int[3]{1, 2, 3};
    int *q = p;
    q[2] = 30;
    cout << p[2] << endl;
    delete[] p;
```
5. What is the output? If it does not compile, say so and why.
```cpp
int twice(int n) { return 2 * n; }
int thrice(int n) { return 3 * n; }
// ---- main ----
    int (*ops[])(int) = {twice, thrice};
    cout << ops[0](5) + ops[1](5) << endl;
```
6. Which cause a memory leak? Choose every correct option.
   A. `int *p = new int; p = new int; delete p;`
   B. `int *p = new int[5]; delete[] p;`
   C. `{ int *p = new int(1); }`
   D. `int *p = nullptr; delete p;`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3.5 2 1
```
2. Actual result (from running it):
```
8
```
3. Actual result (from running it):
```
(does not compile: assignment of read-only location ‘* p’)
```
4. Actual result (from running it):
```
30
```
5. Actual result (from running it):
```
25
```
6. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Pointers_and_Dynamic_Memory` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_OOP_Principles_and_Class_Definitions.
