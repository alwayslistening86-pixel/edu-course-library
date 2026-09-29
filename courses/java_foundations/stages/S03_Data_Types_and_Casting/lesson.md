# S03_Data_Types_and_Casting - Lesson: Variables, data types, casting and String variables

## Goal
The learner declares and initialises variables of every primitive type and String, uses final, and predicts automatic promotion and manual casting.

## Syllabus items taught here
- 4.1 - Declare and initialize variables, including a variable using final
- 4.2 - Cast a value from one data type to another, including automatic and manual promotion
- 4.3 - Declare and initialize a String variable

## How to teach this
Ask why `int x = 3.0;` fails but `double d = 3;` works. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 4.1 Declare and initialize variables, including a variable using final
The eight primitives: `byte` (8-bit), `short` (16), `int` (32, default for whole-number literals), `long` (64, literal suffix `L`), `float` (32, suffix `f`), `double` (64, default for decimals), `char` (a 16-bit Unicode character in single quotes), `boolean` (`true`/`false`). Declare then assign, or both at once; several per line with commas. A local variable must be assigned before use. `final` makes a variable assignable only once.
```java
int a = 5, b;
b = a * 2;
long big = 3_000_000_000L;
float f = 1.5f;
char c = 'J';
boolean ok = true;
final double RATE = 0.2;
System.out.println(a + " " + b + " " + big + " " + f + " " + c + " " + ok + " " + RATE);
```
Output:
```
5 10 3000000000 1.5 J true 0.2
```
Reassigning a final variable is a compile error:
```java
final int LIMIT = 3;
LIMIT = 4;
```
Output:
```
(does not compile: cannot assign a value to final variable LIMIT)
```

#### 4.2 Cast a value from one data type to another, including automatic and manual promotion
**Automatic (widening) promotion** happens when no data can be lost: `byte → short → int → long → float → double`, and `char → int`. In expressions, `byte`, `short` and `char` are promoted to `int`, and mixed types are promoted to the wider one. **Manual (narrowing) casting** needs `(type)`: `(int) 9.99` truncates to 9; values too big wrap around.
```java
int i = 'A';
double d = 7;
int t = (int) 9.99;
byte small = (byte) 130;
System.out.println(i + " " + d + " " + t + " " + small + " " + 7 / 2 + " " + 7 / 2.0 + " " + (double) 7 / 2);
```
Output:
```
65 7.0 9 -126 3 3.5 3.5
```
Narrowing without a cast doesn't compile:
```java
double price = 4.5;
int whole = price;
```
Output:
```
(does not compile: incompatible types: possible lossy conversion from double to int)
```

#### 4.3 Declare and initialize a String variable
`String` is a class, not a primitive, but it has literal syntax: `String s = "Hi";`. Also `new String("Hi")`. A String can be `null` (no object) or empty `""`. `+` concatenates, and anything concatenated with a String becomes text: evaluation is left to right, so numbers before the first String are added first.
```java
String name = "Ada";
String empty = "";
String none = null;
System.out.println(name + " " + empty.length() + " " + none);
System.out.println(1 + 2 + "3" + 4 + 5);
```
Output:
```
Ada 0 null
3345
```

## Explicitly not here
String methods are S05; comparing Strings is S06.
