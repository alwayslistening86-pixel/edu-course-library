# S02_Types_Literals_Conversions_Modifiers - Practice: Types, literals, conversions and modifiers

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    cout << 0x1F + 010 << " " << 'A' + 1 << " " << static_cast<char>('A' + 1) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    unsigned int u = 3;
    int s = -5;
    cout << (s < u) << " " << s + (int)u << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
39 66 B
```
2. Actual result (from running it):
```
0 -2
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
