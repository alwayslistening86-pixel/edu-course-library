# S02_Strings_StringBuilder_Text_Blocks - Test: String, StringBuilder and text blocks

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
String s = "certification";
System.out.println(s.substring(4, 8) + " " + s.indexOf("i", 5) + " " + s.lastIndexOf('i') + " " + s.replace("i", "") .length() + " " + s.charAt(s.length() / 2));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
String a = "Java";
String b = a.concat("21");
a.toUpperCase();
String c = "Java21";
System.out.println(a + " " + (b == c) + " " + b.equals(c) + " " + (b.intern() == c));
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
StringBuilder sb = new StringBuilder("0123456789");
sb.delete(2, 5).replace(0, 2, "AB").deleteCharAt(sb.length() - 1).setLength(5);
System.out.println(sb);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
StringBuilder sb = new StringBuilder("0123456789");
sb.delete(2, 5).replace(0, 2, "AB").deleteCharAt(sb.length() - 1);
String s2 = sb.substring(3);
System.out.println(sb + " " + s2 + " " + sb.indexOf("8"));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
String text = """
    <p>
      "hi"\
     there
    </p>""";
System.out.println(text.lines().count() + " " + text.lines().toList().get(1).strip());
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println(" x ".strip().length() + " " + "\t".isBlank() + " " + "a,b,,".split(",").length + " " + String.join("/", List.of("p", "q")) + " " + "ab".compareTo("abc") + " " + "b".repeat(0).isEmpty());
```
7. Which are true? (choose two) Choose every correct option.
   A. StringBuilder.equals compares contents
   B. String.strip removes Unicode whitespace from both ends
   C. A text block's closing delimiter position can change the indentation kept
   D. sb.append returns a new StringBuilder

## Answer key (for the tutor only)
1. Actual result (from running it):
```
ific 6 10 10 i
```
2. Actual result (from running it):
```
Java false true true
```
3. Actual result (from running it):
```
AB567
```
4. Actual result (from running it):
```
AB5678 678 5
```
5. Actual result (from running it):
```
3 "hi" there
```
6. Actual result (from running it):
```
1 true 2 p/q -1 true
```
7. Correct: B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Strings_StringBuilder_Text_Blocks` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Date_Time_API.
