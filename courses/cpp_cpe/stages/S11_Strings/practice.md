# S11_Strings - Practice: std::string

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    string s = "abc";
    s += "def";
    cout << s.size() << " " << s.substr(2, 3) << " " << s.find("d") << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    cout << (string("cat") < string("car")) << (string("Cat") < string("cat")) << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
6 cde 3
```
2. Actual result (from running it):
```
01
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
