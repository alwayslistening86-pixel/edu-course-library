# Java: 1Z0-830 Java SE 21 Developer Professional (Oracle) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
50 items: about 6 from S01-S04, 16 from S05-S08, 3 from S09, 6 from S10, 6 from S11, 4 from S12, 4 from S13, 2 from S14 and 3 from S15. Mostly code-reading, with multiple-select items that state how many answers to choose, as Oracle does. Non-sequential order; 120 minutes, matching the real exam. No running of code until everything is answered.

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What is the output? If it does not compile, or throws, say so and why.
```java
int x = 7;
x += x++ * 2 - --x;
System.out.println(x);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
StringBuilder sb = new StringBuilder("abcdef");
sb.reverse().delete(1, 3).insert(2, "-");
System.out.println(sb + " " + sb.indexOf("-") + " " + """
    x""".length());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
record Temp(double c) implements Comparable<Temp> {
    Temp { if (c < -273.15) throw new IllegalArgumentException("too cold"); }
    public int compareTo(Temp o) { return Double.compare(c, o.c); }
}
// ---- main ----
TreeSet<Temp> ts = new TreeSet<>(List.of(new Temp(20), new Temp(-5), new Temp(20)));
System.out.println(ts.size() + " " + ts.first() + " " + ts.last().c());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
sealed interface Animal permits Cat, Dog { }
record Cat(String name, int lives) implements Animal { }
record Dog(String name) implements Animal { }
class Talk {
    static String of(Animal a) {
        return switch (a) {
            case Cat(var n, int l) when l < 9 -> n + " has used lives";
            case Cat c -> c.name() + " purrs";
            case Dog(String n) -> n + " barks";
        };
    }
}
// ---- main ----
System.out.println(Talk.of(new Cat("Tom", 9)) + "; " + Talk.of(new Cat("Kit", 3)) + "; " + Talk.of(new Dog("Rex")));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
Map<Character, Long> m = Stream.of("apple", "avocado", "banana", "blueberry", "cherry")
    .collect(Collectors.groupingBy(s -> s.charAt(0), TreeMap::new, Collectors.counting()));
System.out.println(m + " " + Stream.of(3, 1, 2).sorted(Comparator.reverseOrder()).map(String::valueOf).collect(Collectors.joining("-")));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
class Base { Base() { hello(); } void hello() { System.out.print("base "); } }
class Sub extends Base { String msg = "sub"; void hello() { System.out.print(msg + " "); } }
// ---- main ----
new Sub().hello();
System.out.println();
```
7. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
// ---- main ----
ZonedDateTime z = ZonedDateTime.of(2024, 10, 27, 0, 30, 0, 0, ZoneId.of("Europe/London"));
System.out.println(z.plusHours(1).toLocalTime() + " " + z.plusHours(2).toLocalTime() + " " + Duration.between(z, z.plusDays(1)).toHours());
```
8. What is the output? If it does not compile, or throws, say so and why.
```java
class T {
    static String f(Object o) { return "O"; }
    static String f(Number... n) { return "N..."; }
    static String f(Integer i, Integer j) { return "II"; }
}
// ---- main ----
System.out.println(T.f(1) + T.f(1, 2) + T.f(1, 2, 3) + T.f());
```

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
14
```
2. Actual result (from running it):
```
fc-ba 2 1
```
3. Actual result (from running it):
```
2 Temp[c=-5.0] 20.0
```
4. Actual result (from running it):
```
Tom purrs; Kit has used lives; Rex barks
```
5. Actual result (from running it):
```
{a=2, b=2, c=1} 3-2-1
```
6. Actual result (from running it):
```
null sub 
```
7. Actual result (from running it):
```
01:30 01:30 25
```
8. Actual result (from running it):
```
OIIN...N...
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 34 of 50 (68%) for a pass, and report the score per area.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest areas, offer targeted review, and retry with a fresh paper.
