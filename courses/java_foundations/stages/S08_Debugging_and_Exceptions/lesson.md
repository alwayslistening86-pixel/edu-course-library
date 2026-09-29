# S08_Debugging_and_Exceptions - Lesson: Debugging and exception handling

## Goal
The learner tells syntax errors from logic errors and runtime exceptions, and handles common exceptions with try and catch.

## Syllabus items taught here
- 10.1 - Identify syntax and logic errors
- 10.2 - Use exception handling
- 10.3 - Handle common exceptions thrown
- 10.4 - Use try and catch blocks

## How to teach this
Ask what the difference is between code that won't compile, code that crashes, and code that runs but gives the wrong answer. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 10.1 Identify syntax and logic errors
A **syntax (compile-time) error** breaks the language rules, so the compiler refuses and no .class file is made: a missing semicolon or brace, a misspelled keyword, a type mismatch, an undeclared variable. A **logic error** compiles and runs but gives the wrong result: an off-by-one loop bound, `=` where `+=` was meant, integer division where a decimal was needed. A **runtime error** (exception) compiles but fails while running. Debug logic errors by tracing values, adding print statements, or stepping through with a debugger.
```java
int total = 0
System.out.println(total);
```
Output:
```
(does not compile: ';' expected)
```
A logic error: this is meant to average 1, 2 and 4 (2.333...).
```java
int a = 1, b = 2, c = 4;
double avg = (a + b + c) / 3;
System.out.println(avg);
```
Output:
```
2.0
```

#### 10.2 Use exception handling
An **exception** is an object describing a problem at run time. When one is thrown and not handled, the program stops and prints a stack trace. Handling it lets the program recover. All exceptions extend `Throwable`; under `Exception`, **checked** exceptions (such as `IOException`) must be handled or declared with `throws`, while **unchecked** ones (subclasses of `RuntimeException`) need not be. You can throw one yourself with `throw new IllegalArgumentException("message")`.
```java
int[] data = {1, 2, 3};
System.out.println("before");
System.out.println(data[3]);
System.out.println("after");
```
Output:
```
before
(throws ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3)
```

#### 10.3 Handle common exceptions thrown
Common unchecked exceptions: `ArithmeticException` (integer divide by zero), `ArrayIndexOutOfBoundsException`, `StringIndexOutOfBoundsException`, `IndexOutOfBoundsException` (from ArrayList), `NullPointerException` (calling a method on null), `NumberFormatException` (`Integer.parseInt("abc")`), `ClassCastException`, and `InputMismatchException` (Scanner reading the wrong type). `getMessage()` returns the detail text.
```java
String[] tests = {"12", "x1", null};
for (String t : tests) {
    try {
        System.out.println(Integer.parseInt(t.trim()) * 2);
    } catch (NumberFormatException e) {
        System.out.println("bad number: " + e.getMessage());
    } catch (NullPointerException e) {
        System.out.println("null input");
    }
}
```
Output:
```
24
bad number: For input string: "x1"
null input
```

#### 10.4 Use try and catch blocks
`try { risky code } catch (ExceptionType e) { handler }`: if the try block throws, control jumps to the first catch whose type matches (a subclass matches its superclass), and the rest of the try block is skipped. Catch the more specific types first; putting `Exception` before `ArithmeticException` makes the second unreachable, a compile error. An optional `finally` block always runs. After handling, execution continues after the try statement.
```java
try {
    System.out.print("A");
    int x = 5 / 0;
    System.out.print("B");
} catch (ArithmeticException e) {
    System.out.print("C");
} finally {
    System.out.print("D");
}
System.out.println("E");
```
Output:
```
ACDE
```
```java
try {
    int x = 5 / 0;
} catch (Exception e) {
    System.out.println("general");
} catch (ArithmeticException e) {
    System.out.println("maths");
}
```
Output:
```
(does not compile: exception ArithmeticException has already been caught)
```

## Explicitly not here
Custom exceptions, multi-catch and try-with-resources belong to java_se21_developer.
