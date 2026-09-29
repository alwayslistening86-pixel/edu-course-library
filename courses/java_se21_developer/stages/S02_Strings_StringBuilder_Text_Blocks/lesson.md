# S02_Strings_StringBuilder_Text_Blocks - Lesson: String, StringBuilder and text blocks

## Goal
The learner predicts the behaviour of String, StringBuilder and text-block code, including immutability, the string pool, method chaining and incidental whitespace.

## Syllabus items taught here
- 1.2 - Manipulate text, including text blocks, using the String and StringBuilder classes

## How to teach this
Ask what `sb.append("a").reverse().insert(0, 1)` leaves in `sb`, and whether a String method could ever do the same. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 1.2 Manipulate text, including text blocks, using the String and StringBuilder classes
**String** is immutable; every 'modifying' method returns a new String. Literals and compile-time constant expressions are pooled; runtime concatenation isn't (unless `intern()`). Know: `length charAt indexOf lastIndexOf substring(begin, end)` (end exclusive) `strip stripLeading stripTrailing trim` (strip is Unicode-aware) `isBlank isEmpty repeat replace contains startsWith endsWith toUpperCase equalsIgnoreCase compareTo split join chars lines indent translateEscapes formatted`.
```java
String s = "  Java 21  ";
String t = s.strip();
System.out.println("[" + t + "] " + t.substring(2) + "|" + t.substring(1, 3) + " " + t.indexOf('a', 2) + " " + "ab".repeat(3) + " " + "   ".isBlank() + " " + "".isEmpty());
System.out.println(String.join("-", "a", "b", "c") + " " + Arrays.toString("x,y,,z,,".split(",")) + " " + "%s=%03d".formatted("id", 7) + " " + "Hello".chars().filter(Character::isUpperCase).count());
String p = "hello", q = "hel" + "lo", r = "hel";
String w = r + "lo";
final String f = "hel";
String x = f + "lo";
System.out.println((p == q) + " " + (p == w) + " " + (p == w.intern()) + " " + (p == x));
```
Output:
```
[Java 21] va 21|av 3 ababab true true
a-b-c [x, y, , z] id=007 1
true false true true
```
**StringBuilder** is a mutable sequence: `append insert delete deleteCharAt replace reverse setCharAt setLength charAt indexOf length`. Most methods return the same builder (`this`), so calls chain and all affect one object. `StringBuilder` doesn't override `equals`, so compare via `toString()` or `compareTo`. `substring` returns a String and leaves the builder unchanged.
```java
StringBuilder sb = new StringBuilder("abc");
StringBuilder same = sb.append("def").insert(0, "-").reverse();
sb.delete(1, 3).deleteCharAt(0);
sb.replace(0, 1, "XY");
String sub = sb.substring(1);
System.out.println(sb + " " + (sb == same) + " " + sub + " " + sb.length() + " " + new StringBuilder("a").equals(new StringBuilder("a")) + " " + new StringBuilder("a").compareTo(new StringBuilder("a")));
StringBuilder t = new StringBuilder("12345");
t.setLength(3);
t.setCharAt(0, '9');
System.out.println(t + " " + t.indexOf("3"));
```
Output:
```
XYba- true Yba- 5 false 0
923 2
```
**Text blocks** (`"""` then a newline) keep line breaks. **Incidental** indentation is removed: the common leading whitespace of the content lines and the closing delimiter line. Trailing spaces are stripped unless escaped (`\s`). `\` at a line end joins lines. A closing `"""` on the last content line means no trailing newline. Quotes needn't be escaped.
```java
String a = """
    first
      second\s
    third \
    joined
    """;
String b = """
    x
    y""";
System.out.print(a);
System.out.println(b.length() + " " + a.lines().count() + " [" + a.lines().toList().get(1) + "]");
String c = """
        indented
    """;
System.out.print(c.replace(' ', '.'));
```
Output:
```
first
  second 
third joined
3 3 [  second ]
....indented
```

## Explicitly not here
Formatting numbers and dates for a locale is S14.
