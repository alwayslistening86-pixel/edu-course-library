# S11_Strings - Test: std::string

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    string s = "programming";
    cout << s.length() << " " << s.substr(3) << " " << s[0] << s.at(3) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    string s = "banana";
    cout << s.find("an") << " " << s.rfind("an") << " " << (s.find("z") == string::npos) << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    string s = "hello world";
    s.erase(5);
    s.insert(0, ">> ");
    s[3] = 'H';
    cout << s << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
    string a = "10", b = "9";
    cout << (a < b) << " " << (stoi(a) < stoi(b)) << " " << a + b << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
    string s = "x";
    string t = s + "y" + to_string(3 + 4);
    cout << t << " " << t.size() << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
    string s = "a" + "b";
    cout << s;
```
7. Which are true of std::string? Choose every correct option.
   A. It can be changed in place
   B. `== compares contents`
   C. Its size is fixed when it is created
   D. `at(i) checks the index`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
11 gramming pg
```
2. Actual result (from running it):
```
1 3 1
```
3. Actual result (from running it):
```
>> Hello
```
4. Actual result (from running it):
```
1 0 109
```
5. Actual result (from running it):
```
xy7 3
```
6. Actual result (from running it):
```
(does not compile: invalid operands of types ‘const char [2]’ and ‘const char [2]’ to binary ‘operator+’)
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Strings` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
