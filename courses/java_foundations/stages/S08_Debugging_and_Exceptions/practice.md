# S08_Debugging_and_Exceptions - Practice: Debugging and exception handling

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
try {
    String s = null;
    System.out.println(s.length());
} catch (NullPointerException e) {
    System.out.println("caught");
}
System.out.println("end");
```
2. Which are logic errors rather than syntax errors? Choose every correct option.
   A. `Using < where <= was needed in a loop bound`
   B. Forgetting a semicolon
   C. Averaging ints with integer division by mistake
   D. Misspelling System as system

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
caught
end
```
2. Correct: A, C (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
