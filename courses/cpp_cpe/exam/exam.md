# C++: CPE-20-01 C++ Certified Entry-Level Programmer (C++ Institute) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
30 items in CPE's real proportions: 9 from S01-S03, 8 from S04-S07, 7 from S08-S09 and 6 from S10-S11. Mix single-choice, multiple-choice, gap-fill ('complete this line so that it prints ...') and code-output items, in non-sequential order. 45 minutes, matching the real exam. No compiling until everything is answered.

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What is the output? If it does not compile, say so and why.
```cpp
    int a = 9, b = 4;
    cout << a / b * b + a % b << " " << (a > b && b > 5) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    for (int i = 5; i > 0; i -= 2) {
        if (i == 3) continue;
        cout << i;
    }
    cout << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
void f(int &r, int v) { r += v; v = 0; }
// ---- main ----
    int x = 1, y = 2;
    f(x, y);
    cout << x << y << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    vector<int> v = {1, 2, 3};
    int *p = v.data();
    cout << *(p + v.size() - 1) << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
struct S { int a; string b; };
// ---- main ----
    vector<S> v{{1, "x"}, {2, "yy"}};
    cout << v[1].b.size() + v[0].a << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    string s = "C++ exam";
    cout << s.substr(s.find(' ') + 1) << " " << (s < "C++") << endl;
```
7. What is the output? If it does not compile, say so and why.
```cpp
    int *p = new int[3]{7, 8, 9};
    int s = 0;
    for (int i = 0; i < 3; i++) s += *(p + i);
    delete[] p;
    cout << s << endl;
```
8. What is the output? If it does not compile, say so and why.
```cpp
    cout << setw(4) << setfill('.') << 42 << "|" << 3 << endl;
```

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
9 0
```
2. Actual result (from running it):
```
51
```
3. Actual result (from running it):
```
32
```
4. Actual result (from running it):
```
3
```
5. Actual result (from running it):
```
3
```
6. Actual result (from running it):
```
exam 0
```
7. Actual result (from running it):
```
24
```
8. Actual result (from running it):
```
..42|3
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 21 of 30 (70%) for a pass, and report the score per block.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete, and it now satisfies the prerequisite for CPA.
- **Not yet:** leave `exam_status: "available"`, name the weakest block, offer targeted review, and retry with a fresh paper.
