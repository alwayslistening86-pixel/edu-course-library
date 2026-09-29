# S10_Structures - Test: Structures

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
struct Pt { int x, y; };
// ---- main ----
    Pt a{1, 2}, b = a;
    b.x = 5;
    cout << a.x << a.y << b.x << b.y << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
struct Rec { string name; int score = 0; };
// ---- main ----
    vector<Rec> v = {{"A", 5}, {"B"}};
    v[1].score += 3;
    cout << v[0].score + v[1].score << " " << v.size() << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
struct T { int n; };
// ---- main ----
    vector<T> v = {{1}, {2}, {3}};
    for (auto t : v) t.n = 0;
    cout << v[0].n;
    for (auto &t : v) t.n = 0;
    cout << v[0].n << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
struct A { int x; }
int k;
// ---- main ----
    cout << 1;
```
5. What is the output? If it does not compile, say so and why.
```cpp
struct Book { string title; double price; };
// ---- main ----
    Book b{"C++", 20};
    Book *p = &b;
    p->price *= 1.5;
    cout << b.title << " " << (*p).price << endl;
```
6. Define a struct Employee (name, salary) and write code that finds and prints the name of the highest-paid employee in a vector of three employees.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1252
```
2. Actual result (from running it):
```
8 2
```
3. Actual result (from running it):
```
10
```
4. Actual result (from running it):
```
(does not compile: expected ‘;’ after struct definition)
```
5. Actual result (from running it):
```
C++ 30
```
6. The tutor runs or reads the learner's answer and checks: Correct struct, vector initialisation, loop comparing salary fields, prints the right name.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Structures` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Strings.
