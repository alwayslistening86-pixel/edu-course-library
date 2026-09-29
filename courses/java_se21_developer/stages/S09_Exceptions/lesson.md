# S09_Exceptions - Lesson: Exception handling

## Goal
The learner traces try/catch/finally flow exactly, uses multi-catch and try-with-resources (including close order and suppressed exceptions), and writes checked and unchecked custom exceptions while obeying the catch-or-declare rule.

## Syllabus items taught here
- 4.1 - Handle exceptions using try/catch/finally, try-with-resources and multi-catch blocks, including custom exceptions

## How to teach this
Ask what a method returns when both its try block and its finally block contain a return statement. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 4.1 Handle exceptions using try/catch/finally, try-with-resources and multi-catch blocks, including custom exceptions
**Hierarchy:** `Throwable` has subclasses `Error` (serious, don't catch) and `Exception`. `RuntimeException` and its subclasses are **unchecked**; other `Exception`s are **checked** and must be caught or declared (`throws`). Catch blocks are tried in order; a catch for a subtype after its supertype is unreachable (compile error); catching a checked exception that the try block can't throw is also a compile error (except `Exception`/`Throwable`).

**finally** always runs after try/catch (unless the JVM exits). If finally executes `return` or throws, that replaces whatever the try or catch was doing. A return value that is a primitive is fixed when the `return` in try runs, even if finally changes the variable.
```java
class Flow {
    static int f() {
        int x = 1;
        try { return x; } finally { x = 99; System.out.print("fin "); }
    }
    @SuppressWarnings("finally")
    static String g() {
        try { throw new IllegalStateException("lost"); } finally { return "finally wins"; }
    }
}
// ---- main ----
System.out.println(Flow.f() + " " + Flow.g());
try {
    System.out.print("a ");
    Object o = List.of(1).get(3);
} catch (IllegalArgumentException | IndexOutOfBoundsException e) {
    System.out.print("multi:" + e.getClass().getSimpleName() + " ");
} finally {
    System.out.println("done");
}
```
Output:
```
fin 1 finally wins
a multi:IndexOutOfBoundsException done
```
In a **multi-catch** (`catch (A | B e)`), the types can't be subclasses of each other, and `e` is implicitly final.
```java
try { Integer.parseInt("x"); }
catch (NumberFormatException | IllegalArgumentException e) { System.out.println("x"); }
```
Output:
```
(does not compile: Alternatives in a multi-catch statement cannot be related by subclassing)
```
**try-with-resources:** resources (anything `AutoCloseable`) declared in the parentheses, or effectively final variables named there, are closed automatically in **reverse order of creation**, **before** any catch or finally block runs. If the body throws and `close()` also throws, the close exception is **suppressed** (attached via `getSuppressed()`) and the body's exception propagates. Resources declared in the header are out of scope in catch and finally.
```java
class Res implements AutoCloseable {
    final String n;
    Res(String n) { this.n = n; System.out.print("open " + n + " "); }
    public void close() throws Exception { System.out.print("close " + n + " "); if (n.equals("B")) throw new Exception("close " + n + " failed"); }
}
// ---- main ----
Res pre = new Res("P");
try (pre; Res a = new Res("A"); Res b = new Res("B")) {
    System.out.print("body ");
    throw new RuntimeException("body failed");
} catch (Exception e) {
    System.out.println("\ncaught: " + e.getMessage() + " suppressed: " + e.getSuppressed()[0].getMessage());
} finally {
    System.out.println("finally");
}
```
Output:
```
open P open A open B body close B close A close P 
caught: body failed suppressed: close B failed
finally
```
**Custom exceptions:** extend `Exception` for checked or `RuntimeException` for unchecked; provide constructors that pass a message and optionally a **cause** to `super`. Chaining keeps the original. An overriding method may throw fewer or narrower checked exceptions, never broader or new ones.
```java
class InsufficientFunds extends Exception {
    InsufficientFunds(String msg, Throwable cause) { super(msg, cause); }
}
class Bank {
    static void withdraw(int bal, int amt) throws InsufficientFunds {
        try {
            if (amt > bal) throw new ArithmeticException("short by " + (amt - bal));
        } catch (ArithmeticException e) {
            throw new InsufficientFunds("cannot withdraw " + amt, e);
        }
    }
}
// ---- main ----
try { Bank.withdraw(50, 80); }
catch (InsufficientFunds e) { System.out.println(e.getMessage() + " <- " + e.getCause().getMessage()); }
```
Output:
```
cannot withdraw 80 <- short by 30
```
```java
class Bank {
    static void withdraw() throws Exception { }
}
class Teller {
    static void serve() { Bank.withdraw(); }
}
// ---- main ----
Teller.serve();
```
Output:
```
(does not compile: unreported exception Exception; must be caught or declared to be thrown)
```

## Explicitly not here
Exceptions from I/O and concurrency are met in S12 and S13.
