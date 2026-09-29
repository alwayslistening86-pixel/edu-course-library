# S07_Parameter_Passing_and_Recursion - Test: Passing arguments and recursion

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
void setZero(int *p) { *p = 0; }
// ---- main ----
    int a = 9;
    setZero(&a);
    cout << a << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
void twice(int &x) { x *= 2; }
// ---- main ----
    twice(5);
```
3. What is the output? If it does not compile, say so and why.
```cpp
void f(int a, int &b, int *c) { a++; b++; (*c)++; }
// ---- main ----
    int x = 1, y = 1, z = 1;
    f(x, y, &z);
    cout << x << y << z << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
int pw(int b, int e) { return e == 0 ? 1 : b * pw(b, e - 1); }
// ---- main ----
    cout << pw(3, 4) << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
void rev(int n) { if (n == 0) return; cout << n % 10; rev(n / 10); }
// ---- main ----
    rev(1234);
    cout << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
int len(const string &s) { return s.size(); }
// ---- main ----
    cout << len("hello") << endl;
```
7. Write a function that swaps two ints using pointers, and show it swapping 3 and 8.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
0
```
2. Actual result (from running it):
```
(does not compile: cannot bind non-const lvalue reference of type ‘int&’ to an rvalue of type ‘int’)
```
3. Actual result (from running it):
```
122
```
4. Actual result (from running it):
```
81
```
5. Actual result (from running it):
```
4321
```
6. Actual result (from running it):
```
5
```
7. The tutor runs or reads the learner's answer and checks: Signature with two int* parameters, dereferenced swap, called with addresses; prints 8 3.

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Parameter_Passing_and_Recursion` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Arrays_and_Vectors.
