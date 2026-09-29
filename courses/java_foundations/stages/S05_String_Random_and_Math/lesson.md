# S05_String_Random_and_Math - Lesson: The String, Random and Math classes

## Goal
The learner uses the core String methods, formats output with printf/String.format and escape sequences, generates random numbers in a range with Random, and uses the Math class.

## Syllabus items taught here
- 6.1 - Develop code that uses methods from the String class
- 6.2 - Format Strings using escape sequences, including %d, %n and %s
- 7.1 - Use the Random class
- 7.2 - Use the Math class

## How to teach this
Ask what `"hello".toUpperCase()` does to the original string, then prove that Strings are immutable. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 6.1 Develop code that uses methods from the String class
Key methods: `length()`, `charAt(i)` (0-based), `indexOf(s)` (-1 if absent), `substring(begin)` and `substring(begin, end)` (end exclusive), `toUpperCase()`, `toLowerCase()`, `trim()`, `replace(a, b)`, `contains(s)`, `startsWith(s)`, `endsWith(s)`, `isEmpty()`, `concat(s)`. Strings are **immutable**: methods return new Strings. A bad index throws `StringIndexOutOfBoundsException`.
```java
String s = "  Java Foundations ";
String t = s.trim();
System.out.println(t.length() + " " + t.charAt(0) + " " + t.indexOf("F") + " " + t.substring(5, 9) + " " + t.substring(12));
System.out.println(t.toUpperCase() + " " + t.replace('a', '@') + " " + t.contains("Found") + " " + t.endsWith("s") + " " + s.length());
String u = "abc";
u.toUpperCase();
System.out.println(u);
```
Output:
```
16 J 5 Foun ions
JAVA FOUNDATIONS J@v@ Found@tions true true 19
abc
```

#### 6.2 Format Strings using escape sequences, including %d, %n and %s
**Escape sequences** go inside string literals: `\n` newline, `\t` tab, `\"` double quote, `\'` single quote, `\\` backslash. **Format specifiers** go in `System.out.printf(format, args...)` or `String.format(...)`: `%d` integer, `%s` string (any value), `%f` floating-point (`%.2f` two decimal places), `%n` platform newline, `%5d` width 5 right-aligned, `%-5s` left-aligned. (Oracle's objective calls `%d`, `%n` and `%s` 'escape sequences'; strictly they are format specifiers.)
```java
System.out.println("Tab:\tend \"quoted\" back\\slash");
System.out.printf("%s is %d years old%n", "Ann", 30);
System.out.printf("[%5d][%-5s][%.2f]%n", 42, "ab", 3.14159);
String line = String.format("%s scored %d%%", "Bo", 95);
System.out.println(line);
```
Output:
```
Tab:	end "quoted" back\slash
Ann is 30 years old
[   42][ab   ][3.14]
Bo scored 95%
```

#### 7.1 Use the Random class
`java.util.Random`: `new Random()` (random seed) or `new Random(seed)` (repeatable sequence, handy for testing). `nextInt()` any int; `nextInt(n)` 0 to n-1; `nextDouble()` 0.0 to just under 1.0; `nextBoolean()`. For a range min..max inclusive: `min + r.nextInt(max - min + 1)`.
```java
Random r = new Random(42);
int die = 1 + r.nextInt(6);
int card = r.nextInt(52);
boolean coin = r.nextBoolean();
System.out.println(die + " " + card + " " + coin);
Random r2 = new Random(42);
System.out.println(1 + r2.nextInt(6));
```
Output:
```
3 7 true
3
```
The point is not the particular numbers but that the same seed gives the same sequence (both dice above show the same value), and that `1 + nextInt(6)` can only be 1 to 6.

#### 7.2 Use the Math class
`Math` is in java.lang, and all its methods are static: `Math.abs`, `Math.max`, `Math.min`, `Math.pow(a, b)` (a double), `Math.sqrt` (a double), `Math.round` (nearest; .5 rounds up, and a double returns a long), `Math.ceil` and `Math.floor` (doubles), `Math.random()` (0.0 to just under 1.0), and the constant `Math.PI`.
```java
System.out.println(Math.abs(-7) + " " + Math.max(3, 9) + " " + Math.pow(2, 10) + " " + Math.sqrt(49) + " " + Math.round(2.5) + " " + Math.round(-2.5) + " " + Math.ceil(4.1) + " " + Math.floor(-4.1));
int roll = (int) (Math.random() * 6) + 1;
System.out.println(roll >= 1 && roll <= 6);
System.out.printf("%.4f%n", Math.PI);
```
Output:
```
7 9 1024.0 7.0 3 -2 5.0 -5.0
true
3.1416
```

## Explicitly not here
Comparing Strings (equals, compareTo) is S06.
