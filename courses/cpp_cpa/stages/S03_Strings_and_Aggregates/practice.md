# S03_Strings_and_Aggregates - Practice: Strings and aggregate types

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    string s = "C++";
    s += " rocks";
    cout << s.substr(4) << " " << s.size() << " " << s.find('+') << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
enum Level { LOW = 1, MID, HIGH = 10 };
// ---- main ----
    cout << LOW << MID << HIGH << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
rocks 9 1
```
2. Actual result (from running it):
```
1210
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
