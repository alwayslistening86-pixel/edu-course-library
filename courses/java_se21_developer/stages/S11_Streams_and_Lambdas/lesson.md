# S11_Streams_and_Lambdas - Lesson: Lambdas and streams

## Goal
The learner writes lambdas and method references for the functional interfaces, builds stream pipelines (sources, intermediate and terminal operations, primitive streams, Optional), and reduces, groups, partitions, joins and concatenates results, sequentially and in parallel.

## Syllabus items taught here
- 6.1 - Use object and primitive streams, with lambda expressions implementing functional interfaces, to create, filter, transform, process and sort data
- 6.2 - Perform decomposition, concatenation and reduction, and grouping and partitioning, on sequential and parallel streams

## How to teach this
Ask what `Stream.of(1, 2, 3).peek(System.out::print).map(x -> x * 2);` prints on its own, and why. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 6.1 Use object and primitive streams, with lambda expressions implementing functional interfaces, to create, filter, transform, process and sort data
**Lambdas:** `(params) -> expression` or `-> { statements; return ...; }`; parameter types are optional (all or none), parentheses optional for exactly one untyped parameter; the lambda's type comes from the target functional interface. **Method references:** static `Integer::parseInt`, bound `str::startsWith`, unbound `String::length` (first argument becomes the receiver), constructor `ArrayList::new`.

**Streams:** a pipeline is a source (`collection.stream()`, `Stream.of`, `Arrays.stream`, `Stream.iterate`, `Stream.generate`, `IntStream.range`/`rangeClosed`), zero or more **lazy** intermediate operations (`filter map flatMap distinct sorted peek limit skip takeWhile dropWhile mapToInt mapToObj boxed`), and one **terminal** operation (`forEach collect toList reduce count min max findFirst findAny anyMatch allMatch noneMatch toArray`). Nothing runs until the terminal operation, elements flow one at a time, and a stream can be used only once (`IllegalStateException`).
```java
List<String> words = List.of("delta", "alpha", "charlie", "bravo", "alpha", "echo");
List<String> out = words.stream().filter(w -> w.length() == 5).distinct().sorted(Comparator.reverseOrder()).map(String::toUpperCase).toList();
System.out.println(out);
Stream.of(3, 1, 2).peek(x -> System.out.print("p" + x + " ")).filter(x -> x > 1).map(x -> x * 10).forEach(x -> System.out.print("f" + x + " "));
System.out.println();
Stream.of("a", "b").peek(System.out::print).map(String::toUpperCase);
System.out.println("<- nothing printed: no terminal operation");
System.out.println(Stream.iterate(1, n -> n < 100, n -> n * 3).toList() + " " + IntStream.rangeClosed(1, 5).takeWhile(n -> n < 4).sum() + " " + Stream.of(List.of(1, 2), List.of(3)).flatMap(List::stream).map(n -> n * n).toList());
Stream<String> once = words.stream();
once.count();
once.count();
```
Output:
```
[DELTA, BRAVO, ALPHA]
p3 f30 p1 p2 f20 
<- nothing printed: no terminal operation
[1, 3, 9, 27, 81] 6 [1, 4, 9]
(throws IllegalStateException: stream has already been operated upon or closed)
```
**Primitive streams** (`IntStream`, `LongStream`, `DoubleStream`) avoid boxing and add `sum`, `average` (an `OptionalDouble`), `summaryStatistics`, `range`. Convert with `mapToInt`/`mapToObj`/`boxed`/`asDoubleStream`. **Optional** results: `findFirst`, `min`, `max`, `reduce(op)`: use `orElse`, `orElseGet`, `orElseThrow`, `ifPresent`, `map`, `isPresent`; `Optional.get()` on empty throws `NoSuchElementException`.
```java
int[] scores = {72, 91, 58, 84};
IntSummaryStatistics st = Arrays.stream(scores).summaryStatistics();
OptionalDouble avg = IntStream.of().average();
Optional<String> longest = Stream.of("kiwi", "banana", "fig").max(Comparator.comparingInt(String::length));
Optional<String> none = Stream.of("kiwi").filter(s -> s.startsWith("z")).findFirst();
System.out.println(st.getMax() + " " + st.getAverage() + " " + avg.isPresent() + " " + longest.map(String::length).orElse(0) + " " + none.orElse("none") + " " + IntStream.range(0, 4).mapToObj(i -> "x" + i).toList() + " " + Stream.of("1", "2").mapToInt(Integer::parseInt).sum());
none.get();
```
Output:
```
91 76.25 false 6 none [x0, x1, x2, x3] 3
(throws NoSuchElementException: No value present)
```

#### 6.2 Perform decomposition, concatenation and reduction, and grouping and partitioning, on sequential and parallel streams
**Reduction:** `reduce(identity, accumulator)` returns a value; `reduce(accumulator)` returns an Optional; `reduce(identity, accumulator, combiner)` allows a different result type (the combiner merges partial results in parallel). The identity must be a true identity for correct parallel results. **Collectors:** `toList`, `toSet`, `toMap(k, v)` (throws `IllegalStateException` on duplicate keys unless given a merge function), `joining(sep, prefix, suffix)`, `counting`, `summingInt`, `averagingInt`, `mapping`, `groupingBy(classifier[, mapFactory][, downstream])` (a Map of lists by default), `partitioningBy(predicate[, downstream])` (always both keys, true and false), `teeing`. **Concatenation:** `Stream.concat(a, b)`. **Decomposition** splits the work: `flatMap` breaks elements into sub-streams, and parallel streams split the source across threads.
```java
record City(String name, String country, int pop) { }
// ---- main ----
List<City> cs = List.of(new City("Leeds", "UK", 8), new City("Lyon", "FR", 5), new City("York", "UK", 2), new City("Paris", "FR", 21), new City("Nice", "FR", 3));
Map<String, List<String>> byCountry = cs.stream().collect(Collectors.groupingBy(City::country, TreeMap::new, Collectors.mapping(City::name, Collectors.toList())));
Map<Boolean, Long> big = cs.stream().collect(Collectors.partitioningBy(c -> c.pop() > 4, Collectors.counting()));
Map<String, Integer> popBy = cs.stream().collect(Collectors.toMap(City::country, City::pop, Integer::sum, TreeMap::new));
String joined = cs.stream().map(City::name).sorted().collect(Collectors.joining(", ", "[", "]"));
int total = cs.stream().reduce(0, (acc, c) -> acc + c.pop(), Integer::sum);
Optional<Integer> product = Stream.of(2, 3, 4).reduce((a, b) -> a * b);
System.out.println(byCountry + " " + big + " " + popBy + " " + joined + " " + total + " " + product.get());
System.out.println(Stream.concat(Stream.of("a", "b"), Stream.of("c")).collect(Collectors.joining()) + " " + Stream.of(1, 2, 3, 4).collect(Collectors.teeing(Collectors.counting(), Collectors.summingInt(x -> x), (n, s) -> s + "/" + n)) + " " + Map.of(false, 0).size());
Stream.of("a", "bb", "cc").collect(Collectors.toMap(String::length, s -> s));
```
Output:
```
{FR=[Lyon, Paris, Nice], UK=[Leeds, York]} {false=2, true=3} {FR=29, UK=10} [Leeds, Lyon, Nice, Paris, York] 39 24
abc 10/4 1
(throws IllegalStateException: Duplicate key 2 (attempted merging values bb and cc))
```
**Parallel streams** (`parallelStream()` or `.parallel()`) split the source and combine results on the common fork-join pool. Results of `sum`, `collect` and `reduce` with a proper identity match the sequential ones; `forEach` order is unpredictable (use `forEachOrdered`); `findAny` may return any element; a wrong identity or a stateful lambda gives wrong answers.
```java
int seq = IntStream.rangeClosed(1, 1000).sum();
int par = IntStream.rangeClosed(1, 1000).parallel().sum();
int badIdentity = List.of(1, 2, 3, 4, 5, 6, 7, 8).parallelStream().reduce(10, Integer::sum);
int goodIdentity = List.of(1, 2, 3, 4, 5, 6, 7, 8).parallelStream().reduce(0, Integer::sum) + 10;
StringBuilder ordered = new StringBuilder();
List.of(1, 2, 3, 4, 5).parallelStream().map(x -> x * 2).forEachOrdered(ordered::append);
System.out.println(seq + " " + par + " " + (badIdentity > goodIdentity) + " " + goodIdentity + " " + ordered + " " + List.of(1, 2, 3).parallelStream().isParallel());
```
Output:
```
500500 500500 true 46 246810 true
```
(The bad-identity total is larger than 46 because 10 is added once per chunk; the exact value depends on how the stream was split.)

## Explicitly not here
Parallel processing with executors and concurrent collections is S12.
