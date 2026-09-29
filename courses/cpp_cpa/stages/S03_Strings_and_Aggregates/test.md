# S03_Strings_and_Aggregates - Test: Strings and aggregate types

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    string a = "abc", b = "abd";
    cout << (a < b) << (a == "abc") << " " << a + b << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    string s = "one\ttwo\\three";
    cout << s.size() << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
union U { int i; char c; };
// ---- main ----
    U u;
    u.i = 0x41;
    cout << u.c << " " << sizeof(U) << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
enum class Fruit { Apple, Pear };
// ---- main ----
    Fruit f = Fruit::Pear;
    cout << static_cast<int>(f) << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
enum class Fruit { Apple, Pear };
// ---- main ----
    int n = Fruit::Pear;
```
6. What is the output? If it does not compile, say so and why.
```cpp
struct P { int x; int y = 9; };
// ---- main ----
    P arr[2] = {{1}, {2, 3}};
    cout << arr[0].y << arr[1].y << endl;
```
7. What is the output? If it does not compile, say so and why.
```cpp
    string s = "hello";
    s.erase(1, 3);
    s.insert(1, "ELL");
    cout << s << " " << s.at(1) << endl;
```

## Answer key (for the tutor only)
1. Actual result (from running it):
```
11 abcabd
```
2. Actual result (from running it):
```
13
```
3. Actual result (from running it):
```
A 4
```
4. Actual result (from running it):
```
1
```
5. Actual result (from running it):
```
(does not compile: cannot convert ‘Fruit’ to ‘int’ in initialization)
```
6. Actual result (from running it):
```
93
```
7. Actual result (from running it):
```
hELLo E
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Strings_and_Aggregates` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Control_Flow.
