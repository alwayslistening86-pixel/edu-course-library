# S07_Preprocessor_Directives - Test: The preprocessor

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
#define DOUBLE(x) x + x
// ---- main ----
    cout << DOUBLE(3) * 2 << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
#define LEVEL 2
// ---- main ----
#if LEVEL > 3
    cout << "high";
#elif LEVEL == 2
    cout << "two";
#else
    cout << "low";
#endif
    cout << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
#define MIN(a, b) ((a) < (b) ? (a) : (b))
// ---- main ----
    int x = 1, y = 5;
    int m = MIN(x++, y);
    cout << m << " " << x << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
#define NAME "Ada"
#undef NAME
// ---- main ----
#ifndef NAME
    cout << "undefined now" << endl;
#endif
```
5. What is the output? If it does not compile, say so and why.
```cpp
#define AREA(w, h) ((w) * (h))
// ---- main ----
    cout << AREA(2 + 1, 4) << " " << 100 / AREA(5, 2) << endl;
```
6. When is macro text substituted? Choose every correct option.
   A. Before compilation, by the preprocessor
   B. At link time
   C. At run time
   D. When the function is first called

## Answer key (for the tutor only)
1. Actual result (from running it):
```
9
```
2. Actual result (from running it):
```
two
```
3. Actual result (from running it):
```
2 3
```
4. Actual result (from running it):
```
undefined now
```
5. Actual result (from running it):
```
12 10
```
6. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Preprocessor_Directives` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Pointers_and_Dynamic_Memory.
