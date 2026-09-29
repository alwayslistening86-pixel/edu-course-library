# S02_Basic_Java_Elements - Lesson: Conventions, reserved words, comments, imports and java.lang

## Goal
The learner follows Java naming and layout conventions, recognises reserved words, writes both comment styles, imports classes and knows what java.lang provides automatically.

## Syllabus items taught here
- 3.1 - Identify the conventions to be followed in a Java program
- 3.2 - Use Java reserved words
- 3.3 - Use single-line and multi-line comments in Java programs
- 3.4 - Import other Java packages to make them accessible in your code
- 3.5 - Describe the java.lang package

## How to teach this
Show `class my_class { int X_VALUE; }` and ask what conventions it breaks, even though it compiles. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 3.1 Identify the conventions to be followed in a Java program
Conventions (not enforced by the compiler, but expected): classes and interfaces in **UpperCamelCase** (`BankAccount`); methods and variables in **lowerCamelCase** (`getBalance`, `totalCount`); constants in **UPPER_SNAKE_CASE** (`MAX_SIZE`); packages in lowercase (`com.example.shop`). Identifiers may use letters, digits, `_` and `$`, must not start with a digit, are case-sensitive, and cannot be reserved words. One public class per file, named after the file. Indent blocks consistently.
```java
int itemCount = 3;
final int MAX_ITEMS = 10;
int $cost = 5, _tax = 1;
System.out.println(itemCount + " of " + MAX_ITEMS + " costing " + ($cost + _tax));
```
Output:
```
3 of 10 costing 6
```

#### 3.2 Use Java reserved words
Reserved words can't be identifiers: e.g. `class public private static void int double boolean if else switch case default for while do break continue return new this super try catch finally throw throws import package final abstract extends implements interface`. `goto` and `const` are reserved but unused. `true`, `false` and `null` are literals, and also can't be identifiers. Java is case-sensitive, so `Class` or `INT` are legal (but poor) names.
```java
int class = 5;
```
Output:
```
(does not compile: not a statement)
```

#### 3.3 Use single-line and multi-line comments in Java programs
`//` comments to the end of the line; `/* ... */` spans lines (and cannot nest); `/** ... */` is a Javadoc comment used to generate documentation. Comments inside a string literal are just text.
```java
/** Javadoc for a helper. */
class Util { }
// ---- main ----
int x = 1; // set x
/* x = 2;
   x = 3; */
System.out.println(x + " // not a comment");
```
Output:
```
1 // not a comment
```

#### 3.4 Import other Java packages to make them accessible in your code
`import java.util.Scanner;` imports one class; `import java.util.*;` imports every class in the package (not sub-packages). Without an import you must use the fully qualified name, e.g. `java.util.ArrayList`. Imports go after any `package` statement and before the class. Importing doesn't copy code; it just lets you use the short name.
```java
import java.time.LocalDate;
// ---- main ----
LocalDate d = LocalDate.of(2024, 2, 28).plusDays(1);
java.time.DayOfWeek w = d.getDayOfWeek();
System.out.println(d + " " + w);
```
Output:
```
2024-02-29 THURSDAY
```

#### 3.5 Describe the java.lang package
`java.lang` is imported automatically into every class. It contains the fundamental classes: `Object` (the root of all classes), `String`, `StringBuilder`, `Math`, `System`, the wrapper classes (`Integer`, `Double`, `Boolean`, `Character`...), and the core exceptions (`Exception`, `RuntimeException`, `ArithmeticException`, `NullPointerException`...). `Scanner`, `Random` and `ArrayList` are in `java.util` and need importing.
```java
System.out.println(Math.max(3, 8) + " " + Integer.parseInt("42") + " " + Character.isDigit('7') + " " + String.valueOf(3.5));
```
Output:
```
8 42 true 3.5
```

## Explicitly not here
Using Math and Random in depth is S05.
