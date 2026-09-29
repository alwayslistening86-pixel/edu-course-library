# S09_Pointers_Casts_and_Dynamic_Memory - Practice: Pointers, casts and dynamic memory

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    int x = 3;
    int *p = &x;
    *p *= 5;
    cout << x << " " << (*p == x) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int *arr = new int[4];
    for (int i = 0; i < 4; i++) arr[i] = i * 10;
    cout << arr[3] << endl;
    delete[] arr;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
15 1
```
2. Actual result (from running it):
```
30
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
