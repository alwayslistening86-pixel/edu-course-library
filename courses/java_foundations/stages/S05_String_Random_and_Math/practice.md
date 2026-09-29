# S05_String_Random_and_Math - Practice: The String, Random and Math classes

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
String s = "Programming";
System.out.println(s.substring(3, 7) + " " + s.indexOf('g') + " " + s.lastIndexOf('g') + " " + s.charAt(s.length() - 1));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.printf("%-6s|%4d|%.1f%n", "ab", 7, 2.25);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
gram 3 10 g
```
2. Actual result (from running it):
```
ab    |   7|2.3
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
