# S10_Collections_Generics_Annotations - Practice: Arrays, collections, generics and annotations

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
Map<String, Integer> m = new HashMap<>();
m.put("a", 1);
System.out.println(m.put("a", 2) + " " + m.putIfAbsent("a", 3) + " " + m.merge("a", 10, Integer::sum) + " " + m);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
List<? super Integer> sink = new ArrayList<Number>();
sink.add(5);
Object o = sink.get(0);
Integer i = sink.get(0);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
1 2 12 {a=12}
```
2. Actual result (from running it):
```
(does not compile: incompatible types: CAP#1 cannot be converted to Integer)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
