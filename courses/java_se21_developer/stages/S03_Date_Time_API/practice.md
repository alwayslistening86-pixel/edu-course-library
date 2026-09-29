# S03_Date_Time_API - Practice: The Date-Time API and daylight saving time

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
LocalDate d = LocalDate.of(2024, 3, 31);
System.out.println(d.minusMonths(1) + " " + d.plusDays(1).getMonth() + " " + Period.between(d, LocalDate.of(2024, 5, 1)));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
LocalTime t = LocalTime.of(10, 0);
t.plusHours(2);
System.out.println(t + " " + Duration.ofMinutes(125) + " " + t.minus(Duration.ofMinutes(61)));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
2024-02-29 APRIL P1M1D
```
2. Actual result (from running it):
```
10:00 PT2H5M 08:59
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
