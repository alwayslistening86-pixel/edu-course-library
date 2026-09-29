# S09_Arrays_and_ArrayLists - Test: Arrays and ArrayLists

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
int[] nums = new int[3];
nums[1] = 4;
int sum = 0;
for (int n : nums) sum += n;
System.out.println(sum + " " + nums[2] + " " + nums.length);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
String[] words = new String[2];
System.out.println(words[0]);
System.out.println(words[0].length());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
ArrayList<Integer> list = new ArrayList<>(List.of(10, 20, 30, 40));
list.remove(1);
list.remove(Integer.valueOf(40));
list.set(0, list.get(0) + 1);
System.out.println(list + " " + list.size());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
ArrayList<String> xs = new ArrayList<>(List.of("a", "bb", "ccc", "dd"));
Iterator<String> it = xs.iterator();
while (it.hasNext()) { if (it.next().length() == 2) it.remove(); }
System.out.println(xs);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
ArrayList<int> xs = new ArrayList<>();
xs.add(1);
System.out.println(xs);
```
6. Which are true? Choose every correct option.
   A. An array's length is fixed when it is created
   B. An ArrayList reports its length with the length field
   C. An ArrayList can hold primitive values directly without wrappers
   D. Arrays.toString gives a readable listing of an array
7. Write code that creates an ArrayList<String> of three names, adds a fourth at the front, removes the last one, and prints each remaining name in upper case using an enhanced for loop.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
4 0 3
```
2. Actual result (from running it):
```
null
(throws NullPointerException: Cannot invoke "String.length()" because "words[0]" is null)
```
3. Actual result (from running it):
```
[11, 30] 2
```
4. Actual result (from running it):
```
[a, ccc]
```
5. Actual result (from running it):
```
(does not compile: unexpected type)
```
6. Correct: A, D (exactly these options, no others)
7. The tutor runs or reads the learner's answer and checks: uses add(0, ...), remove(size()-1) or remove by value, and an enhanced for loop printing toUpperCase(); runs and prints three names.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Arrays_and_ArrayLists` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Classes_and_Constructors.
