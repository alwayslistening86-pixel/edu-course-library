# S08_Arrays_and_Vectors - Test: Arrays and vectors

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    int m[3][2] = {{1, 2}, {3, 4}, {5, 6}};
    cout << m[2][1] << m[1][0] << " " << sizeof(m) / sizeof(m[0]) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    vector<int> v(3, 5);
    v[0] = 1;
    v.push_back(9);
    int s = 0;
    for (int x : v) s += x;
    cout << v.size() << " " << s << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    vector<int> v = {1, 2, 3};
    try { cout << v.at(3); } catch (const out_of_range &) { cout << "caught"; }
    cout << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    vector<int> v = {4, 5, 6};
    int *p = v.data();
    *(p + 1) = 50;
    cout << v[1] << " " << p[2] << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    vector<vector<int>> g = {{1}, {2, 3}, {4, 5, 6}};
    cout << g.size() << " " << g[2].size() << " " << g[1][1] << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    int a[] = {1, 2, 3, 4, 5};
    int total = 0;
    for (int i = 0; i < 5; i += 2) total += a[i];
    cout << total << endl;
```
7. Which are true? Choose every correct option.
   A. An array's size cannot change after declaration
   B. v.at(i) checks the index and throws if it is invalid
   C. `v[i] checks the index`
   D. v.data() returns a pointer to the first element

## Answer key (for the tutor only)
1. Actual result (from running it):
```
63 3
```
2. Actual result (from running it):
```
4 20
```
3. Actual result (from running it):
```
caught
```
4. Actual result (from running it):
```
50 6
```
5. Actual result (from running it):
```
3 3 3
```
6. Actual result (from running it):
```
9
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Arrays_and_Vectors` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Pointers_Casts_and_Dynamic_Memory.
