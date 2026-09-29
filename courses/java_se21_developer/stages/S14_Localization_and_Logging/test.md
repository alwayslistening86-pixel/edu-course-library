# S14_Localization_and_Logging - Test: Localization and the Logging API

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
import java.text.*;
// ---- main ----
NumberFormat nf = NumberFormat.getInstance(Locale.US);
nf.setMaximumFractionDigits(1);
System.out.println(nf.format(1234.56) + " " + nf.format(0.25) + " " + nf.format(0.35) + " " + nf.parse("42.9kg"));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Files.writeString(Path.of("Lbl.properties"), "ok=OK\nhelp=Help\n");
Files.writeString(Path.of("Lbl_es.properties"), "ok=Vale\n");
Files.writeString(Path.of("Lbl_es_MX.properties"), "ok=Sale\n");
ResourceBundle mx = ResourceBundle.getBundle("Lbl", Locale.of("es", "MX"));
ResourceBundle es = ResourceBundle.getBundle("Lbl", Locale.of("es", "ES"));
System.out.println(mx.getString("ok") + " " + mx.getString("help") + " " + es.getString("ok") + " " + es.getLocale());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
import java.time.*;
import java.time.format.*;
// ---- main ----
LocalDate d = LocalDate.of(2025, 12, 25);
System.out.println(d.format(DateTimeFormatter.ofLocalizedDate(FormatStyle.MEDIUM).withLocale(Locale.UK)) + " | " + d.format(DateTimeFormatter.ofPattern("EEE d MMM", Locale.FRANCE)));
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
import java.util.logging.*;
// ---- main ----
Logger log = Logger.getLogger("t");
log.setUseParentHandlers(false);
StreamHandler h = new StreamHandler(System.out, new SimpleFormatter() { public String format(LogRecord r) { return r.getLevel() + ":" + r.getMessage() + " "; } });
log.addHandler(h);
log.setLevel(Level.WARNING);
log.info("a"); log.warning("b"); log.severe("c"); log.config("d");
h.flush();
System.out.println();
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
Locale l = Locale.forLanguageTag("fr-CA");
System.out.println(l + " " + l.getLanguage() + " " + l.getCountry() + " " + l.getDisplayLanguage(Locale.ENGLISH) + " " + Locale.of("EN", "gb"));
```
6. The default locale is en_US. `getBundle("Msg", Locale.ITALY)` is called and only Msg.properties and Msg_en.properties exist. Which bundle is returned? (choose one) Choose every correct option.
   A. `Msg.properties`
   B. `Msg_en.properties`
   C. A MissingResourceException is thrown
   D. An empty bundle
7. Which are true of java.util.logging defaults? (choose two) Choose every correct option.
   A. The root logger's ConsoleHandler writes to System.err
   B. The default level is INFO
   C. FINE messages are shown by default
   D. Every logger must have a handler of its own

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1,234.6 0.2 0.3 42.9
```
2. Actual result (from running it):
```
Sale Help Vale es
```
3. Actual result (from running it):
```
25 Dec 2025 | jeu. 25 déc.
```
4. Actual result (from running it):
```
WARNING:b SEVERE:c 
```
5. Actual result (from running it):
```
fr_CA fr CA French en_GB
```
6. Correct: B (exactly these options, no others)
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S14_Localization_and_Logging` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S15_Modules_and_Deployment.
