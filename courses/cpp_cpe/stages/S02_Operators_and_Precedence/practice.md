# S02_Operators_and_Precedence - Practice: Operators, precedence and short-circuiting

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    int a = 10;
    a -= 3;
    a %= 4;
    cout << a << " " << (5 & 3) << " " << (5 | 3) << " " << (1 << 3) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int i = 3;
    int j = i++ * 2;
    int k = ++i * 2;
    cout << i << " " << j << " " << k << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
3 1 7 8
```
2. Actual result (from running it):
```
5 6 10
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
