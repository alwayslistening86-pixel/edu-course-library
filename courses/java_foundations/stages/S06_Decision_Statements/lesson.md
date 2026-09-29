# S06_Decision_Statements - Lesson: Decision statements and comparing values

## Goal
The learner writes if, if-else and else-if chains and switch statements (including fall-through), and chooses correctly between ==, equals and compareTo.

## Syllabus items taught here
- 8.1 - Use the decision-making statements if-then and if-then-else
- 8.2 - Use the switch statement
- 8.3 - Compare how == differs between primitives and objects
- 8.4 - Compare two String objects using the compareTo and equals methods

## How to teach this
Show two Strings that print identically but where `==` gives false, and ask why. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 8.1 Use the decision-making statements if-then and if-then-else
`if (condition) statement` runs the statement only when the condition is true; `else` gives the alternative; chains of `else if` test in order and stop at the first true one. The condition must be a boolean. Without braces only the next single statement belongs to the if, and an `else` pairs with the nearest unmatched `if` (the 'dangling else').
```java
int score = 72;
if (score >= 80) System.out.println("A");
else if (score >= 70) System.out.println("B");
else if (score >= 60) System.out.println("C");
else System.out.println("F");
int x = 5;
if (x > 10)
    System.out.println("big");
    System.out.println("always printed");
if (x > 0) if (x > 100) System.out.println("huge"); else System.out.println("pos, not huge");
```
Output:
```
B
always printed
pos, not huge
```

#### 8.2 Use the switch statement
`switch (expr) { case value: ... break; default: ... }` works on `int` (and byte, short, char), `String`, enums and wrapper types, not on long, float, double or boolean. Case labels must be compile-time constants and unique. Without `break`, execution **falls through** into the next case. `default` runs when nothing matches, wherever it is placed.
```java
String day = "SAT";
switch (day) {
    case "SAT":
    case "SUN":
        System.out.println("weekend");
        break;
    default:
        System.out.println("weekday");
}
int n = 2;
switch (n) {
    case 1: System.out.print("one ");
    case 2: System.out.print("two ");
    case 3: System.out.print("three ");
    default: System.out.print("other ");
}
System.out.println();
```
Output:
```
weekend
two three other 
```

#### 8.3 Compare how == differs between primitives and objects
For **primitives**, `==` compares values. For **objects** (reference types), `==` compares **references**: whether two variables point to the same object. String literals with the same text share one pooled object, so `==` may happen to be true for them, but a String made with `new` or built at runtime is a different object.
```java
int a = 1000, b = 1000;
String s1 = "hi";
String s2 = "hi";
String s3 = new String("hi");
String s4 = "h";
s4 = s4 + "i";
System.out.println((a == b) + " " + (s1 == s2) + " " + (s1 == s3) + " " + (s1 == s4));
```
Output:
```
true true false false
```

#### 8.4 Compare two String objects using the compareTo and equals methods
`s1.equals(s2)` compares the characters (use this for String equality); `equalsIgnoreCase` ignores case. `s1.compareTo(s2)` compares lexicographically (by Unicode value): negative if s1 comes first, 0 if equal, positive if s1 comes after. Uppercase letters sort before lowercase. When one String is a prefix of the other, the result is the difference in lengths.
```java
String a = "apple", b = new String("apple"), c = "Apple";
System.out.println(a.equals(b) + " " + a.equals(c) + " " + a.equalsIgnoreCase(c));
System.out.println("apple".compareTo("banana") + " " + "cat".compareTo("car") + " " + "Zoo".compareTo("apple") + " " + "abc".compareTo("abcde") + " " + a.compareTo(b));
```
Output:
```
true false true
-1 2 -7 -2 0
```

## Explicitly not here
Arrow-form switch and switch expressions are Java 14+ and belong to java_se21_developer.
