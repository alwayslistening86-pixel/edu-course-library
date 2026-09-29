# S12_Concurrency - Practice: Threads, executors, thread safety and parallel processing

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
Thread t = new Thread(() -> System.out.print("in thread "));
t.start();
t.join();
System.out.println(t.isAlive());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
import java.util.concurrent.*;
// ---- main ----
try (ExecutorService ex = Executors.newSingleThreadExecutor()) {
    Future<String> f = ex.submit(() -> "done");
    System.out.println(f.get());
}
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
in thread false
```
2. Actual result (from running it):
```
done
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
