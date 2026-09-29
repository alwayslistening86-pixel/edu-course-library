# S04_Decisions_switch_and_goto - Test: if, switch and goto

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    int x = 0;
    if (x = 5) cout << "true " << x;
    else cout << "false";
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int a = 1, b = 2;
    if (a > 5)
        if (b > 1) cout << "X";
    else cout << "Y";
    cout << "|" << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    char c = 'x';
    switch (c) {
        case 'a': case 'e': case 'i': cout << "vowel"; break;
        default: cout << "consonant";
    }
    cout << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    string s = "go";
    switch (s) { case "go": cout << 1; }
```
5. What is the output? If it does not compile, say so and why.
```cpp
    int k = 0;
start:
    k += 2;
    if (k < 7) goto start;
    cout << k << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    for (int v : {1, 2, 3}) {
        switch (v % 2) {
            case 0: cout << "e";
            default: cout << "*";
        }
    }
    cout << endl;
```
7. Which types can a switch expression have? Choose every correct option.
   A. `int`
   B. `char`
   C. `std::string`
   D. `double`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
true 5
```
2. Actual result (from running it):
```
|
```
3. Actual result (from running it):
```
consonant
```
4. Actual result (from running it):
```
(does not compile: switch quantity not an integer)
```
5. Actual result (from running it):
```
8
```
6. Actual result (from running it):
```
*e**
```
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Decisions_switch_and_goto` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Loops.
