# S09_Arrays_and_ArrayLists - Practice: Arrays and ArrayLists

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
int[] a = {2, 4, 6};
int[] b = a;
b[0] = 10;
System.out.println(a[0] + " " + a.length);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
ArrayList<String> xs = new ArrayList<>();
xs.add("x"); xs.add("y"); xs.add(1, "z");
System.out.println(xs + " " + xs.indexOf("y"));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
10 3
```
2. Actual result (from running it):
```
[x, z, y] 2
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
