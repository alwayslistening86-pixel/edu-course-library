# S13_IO_and_NIO2 - Practice: I/O streams, serialization and java.nio.file

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Path p = Path.of("/a/b/c/d.txt");
System.out.println(p.getNameCount() + " " + p.subpath(1, 3) + " " + p.getParent().getFileName() + " " + p.getRoot());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Files.writeString(Path.of("x.txt"), "one\ntwo\n");
System.out.println(Files.readAllLines(Path.of("x.txt")).size() + " " + Files.size(Path.of("x.txt")));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
4 b/c c /
```
2. Actual result (from running it):
```
2 8
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
