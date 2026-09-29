# S10_Collections_Generics_Annotations - Test: Arrays, collections, generics and annotations

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
List<Integer> list = new ArrayList<>(List.of(5, 1, 4));
list.add(1, 9);
list.remove(Integer.valueOf(1));
list.remove(0);
Collections.sort(list);
System.out.println(list + " " + list.reversed() + " " + list.getFirst());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
Deque<Integer> d = new ArrayDeque<>();
d.offer(1); d.push(2); d.offerFirst(3); d.add(4);
System.out.println(d.pop() + " " + d.pollLast() + " " + d.peekFirst() + " " + d);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
TreeMap<String, Integer> t = new TreeMap<>(Map.of("pear", 3, "apple", 5, "fig", 1));
System.out.println(t.firstKey() + " " + t.ceilingKey("b") + " " + t.headMap("fig") + " " + t.descendingMap());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
record Item(String name, int qty) { }
// ---- main ----
List<Item> items = new ArrayList<>(List.of(new Item("b", 2), new Item("a", 2), new Item("c", 1)));
items.sort(Comparator.comparingInt(Item::qty).reversed().thenComparing(Item::name));
System.out.println(items.stream().map(Item::name).toList());
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
List<Integer> fixed = Arrays.asList(3, 1, 2);
Collections.sort(fixed);
System.out.print(fixed + " ");
List<Integer> immutable = List.of(3, 1, 2);
Collections.sort(immutable);
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
class G {
    static <T extends Comparable<? super T>> T min(Collection<? extends T> c) {
        T best = null;
        for (T t : c) if (best == null || t.compareTo(best) < 0) best = t;
        return best;
    }
    static double total(List<? extends Number> ns) { return ns.stream().mapToDouble(Number::doubleValue).sum(); }
}
// ---- main ----
System.out.println(G.min(Set.of(4, 2, 9)) + " " + G.min(List.of("kiwi", "apple")) + " " + G.total(List.of(1, 2.5f)));
```
7. Given `List<? extends Number> nums`, which statements compile? (choose two) Choose every correct option.
   A. `Number n = nums.get(0);`
   B. `nums.add(Integer.valueOf(1));`
   C. `nums.add(null);`
   D. `Integer i = nums.get(0);`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
[4, 9] [9, 4] 4
```
2. Actual result (from running it):
```
3 4 2 [2, 1]
```
3. Actual result (from running it):
```
apple fig {apple=5} {pear=3, fig=1, apple=5}
```
4. Actual result (from running it):
```
[a, b, c]
```
5. Actual result (from running it):
```
[1, 2, 3] 
(throws UnsupportedOperationException)
```
6. Actual result (from running it):
```
2 apple 3.5
```
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Collections_Generics_Annotations` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Streams_and_Lambdas.
