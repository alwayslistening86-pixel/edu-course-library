# S04_Control_Flow - Test: Control flow

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    int i = 10;
    while (i-- > 7) cout << i;
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int n = 0;
    do n++; while (n < 0);
    cout << n << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
            if (j == 1) break;
            cout << i << j << " ";
        }
    cout << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    int v = 5;
    switch (v % 3) {
        case 0: cout << "zero"; break;
        case 2: cout << "two";
        default: cout << "+def";
    }
    cout << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
int sign(int x) { return x > 0 ? 1 : x < 0 ? -1 : 0; }
// ---- main ----
    cout << sign(-4) << sign(0) << sign(9) << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    int k = 1;
loop:
    k *= 2;
    if (k < 20) goto loop;
    cout << k << endl;
```
7. Which statements can switch on? Choose every correct option.
   A. An int
   B. A char
   C. An enum value
   D. A std::string

## Answer key (for the tutor only)
1. Actual result (from running it):
```
987
```
2. Actual result (from running it):
```
1
```
3. Actual result (from running it):
```
00 10 20 
```
4. Actual result (from running it):
```
two+def
```
5. Actual result (from running it):
```
-101
```
6. Actual result (from running it):
```
32
```
7. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Control_Flow` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Exceptions.
