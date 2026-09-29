# S11_Streams_and_Lambdas - Practice: Lambdas and streams

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println(Stream.of("b", "a", "c").sorted().map(String::toUpperCase).reduce("", String::concat));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
Map<Integer, List<String>> byLen = Stream.of("aa", "b", "cc", "ddd").collect(Collectors.groupingBy(String::length));
System.out.println(byLen);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
ABC
```
2. Actual result (from running it):
```
{1=[b], 2=[aa, cc], 3=[ddd]}
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
