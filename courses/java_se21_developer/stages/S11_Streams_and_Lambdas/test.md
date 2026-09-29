# S11_Streams_and_Lambdas - Test: Lambdas and streams

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
List<Integer> n = List.of(4, 8, 15, 16, 23, 42);
System.out.println(n.stream().filter(x -> x % 2 == 0).mapToInt(Integer::intValue).sum() + " " + n.stream().skip(2).limit(3).toList() + " " + n.stream().anyMatch(x -> x > 40) + " " + n.stream().dropWhile(x -> x < 16).count());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
Stream.of("x", "y", "z").filter(s -> { System.out.print("f" + s + " "); return !s.equals("y"); }).map(s -> { System.out.print("m" + s + " "); return s; }).findFirst();
System.out.println();
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
Optional<String> o = Stream.of("pear", "fig").filter(s -> s.length() > 4).findAny();
System.out.println(o.isPresent() + " " + o.orElse("none") + " " + o.map(String::length).orElseGet(() -> -1) + " " + Optional.of("a").or(() -> Optional.of("b")).get());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
Map<Boolean, List<Integer>> parts = IntStream.rangeClosed(1, 6).boxed().collect(Collectors.partitioningBy(i -> i > 4));
Map<Boolean, Long> none = Stream.<Integer>empty().collect(Collectors.partitioningBy(i -> i > 4, Collectors.counting()));
System.out.println(parts + " " + none);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
String s = Stream.of("c", "a", "b").collect(Collectors.joining("|", "<", ">"));
int sumLen = Stream.of("aa", "bbb").reduce(0, (acc, w) -> acc + w.length(), Integer::sum);
double avg = Stream.of(1, 2, 3, 4).collect(Collectors.averagingInt(x -> x));
System.out.println(s + " " + sumLen + " " + avg + " " + Stream.concat(Stream.of(1), Stream.of(2, 3)).map(String::valueOf).collect(Collectors.joining()));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
var st = Stream.of(1, 2, 3);
var mapped = st.map(x -> x * 2);
System.out.println(st.count());
```
7. Which are terminal operations? (choose three) Choose every correct option.
   A. `peek`
   B. `collect`
   C. `sorted`
   D. `forEachOrdered`
   E. `anyMatch`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
70 [15, 16, 23] true 3
```
2. Actual result (from running it):
```
fx mx 
```
3. Actual result (from running it):
```
false none -1 a
```
4. Actual result (from running it):
```
{false=[1, 2, 3, 4], true=[5, 6]} {false=0, true=0}
```
5. Actual result (from running it):
```
<c|a|b> 5 2.5 123
```
6. Actual result (from running it):
```
(throws IllegalStateException: stream has already been operated upon or closed)
```
7. Correct: B, D, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Streams_and_Lambdas` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Concurrency.
