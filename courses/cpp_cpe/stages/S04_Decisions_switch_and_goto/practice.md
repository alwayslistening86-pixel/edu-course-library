# S04_Decisions_switch_and_goto - Practice: if, switch and goto

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    int n = 3;
    switch (n) {
        case 1: cout << "a";
        case 3: cout << "b";
        case 4: cout << "c"; break;
        default: cout << "d";
    }
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int t = 15;
    if (t > 20) cout << "hot";
    else if (t > 10) cout << "warm";
    else cout << "cold";
    cout << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
bc
```
2. Actual result (from running it):
```
warm
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
