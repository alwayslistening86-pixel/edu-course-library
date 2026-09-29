# S14_Localization_and_Logging - Lesson: Localization and the Logging API

## Goal
The learner creates and uses Locales, loads resource bundles with the correct fallback order, formats and parses messages, numbers, currency, percentages, dates and times for a locale, and uses the java.util.logging basics: loggers, levels, handlers and formatters.

## Syllabus items taught here
- 10.1 - Implement localization using locales and resource bundles; parse and format messages, dates, times and numbers, including currency and percentage values
- 11.1 - Understand the basics of the Java Logging API

## How to teach this
Ask which bundle file is used for `Locale.GERMAN` when only `Msgs.properties` and `Msgs_fr.properties` exist and the default locale is en_US. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 10.1 Implement localization using locales and resource bundles; parse and format messages, dates, times and numbers, including currency and percentage values
**Locale:** `Locale.UK`, `Locale.FRENCH`, `Locale.of("fr", "CA")` (Java 19+; the constructors are deprecated), `Locale.forLanguageTag("en-GB")`, `new Locale.Builder().setLanguage("es").setRegion("MX").build()`. Language codes are lowercase, country codes uppercase (`en_GB`). `Locale.getDefault()` and `Locale.setDefault(...)` (optionally per `Locale.Category.FORMAT` or `DISPLAY`). The examples here pass explicit locales so they don't depend on the machine; this runner's default is en_US.

**Resource bundles:** `ResourceBundle.getBundle("Msgs", locale)` looks for property files (or `ListResourceBundle` classes) in this order: requested language and country, requested language, **default locale** country and language, default language, then the base bundle `Msgs`. Once a bundle is chosen, missing keys are looked up in its **parents** (e.g. `Msgs_fr_CA` → `Msgs_fr` → `Msgs`), never in the default locale's bundles. A missing key throws `MissingResourceException`. `MessageFormat.format("Hello {0}, you have {1} messages", name, n)` fills placeholders.
```java
import java.nio.file.*;
import java.text.MessageFormat;
// ---- main ----
Files.writeString(Path.of("Msgs.properties"), "hello=Hello {0}\nbye=Goodbye\ncolour=colour\n");
Files.writeString(Path.of("Msgs_fr.properties"), "hello=Bonjour {0}\nbye=Au revoir\n");
Files.writeString(Path.of("Msgs_fr_CA.properties"), "hello=Allo {0}\n");
Files.writeString(Path.of("Msgs_en_US.properties"), "colour=color\n");
ResourceBundle ca = ResourceBundle.getBundle("Msgs", Locale.of("fr", "CA"));
ResourceBundle de = ResourceBundle.getBundle("Msgs", Locale.GERMAN);
System.out.println(MessageFormat.format(ca.getString("hello"), "Luc") + " | " + ca.getString("bye") + " | " + ca.getString("colour"));
System.out.println(de.getLocale() + " " + de.getString("colour") + " " + MessageFormat.format("{0} has {1} items, {0}!", "Kim", 3));
ca.getString("missing");
```
Output:
```
Allo Luc | Au revoir | colour
en_US color Kim has 3 items, Kim!
(throws MissingResourceException: Can't find resource for bundle java.util.PropertyResourceBundle, key missing)
```
**Numbers:** `NumberFormat.getInstance(locale)`, `getIntegerInstance` (rounds half-even), `getCurrencyInstance`, `getPercentInstance` (multiplies by 100), `getCompactNumberInstance(locale, Style.SHORT/LONG)`. `format` turns numbers into text; `parse` turns text into a `Number`, reading as far as it can and throwing `ParseException` only if nothing at the start parses. Some locales use a non-breaking space (U+00A0) as a separator; the example shows it as `_`. `DecimalFormat` patterns: `#` optional digit, `0` forced digit.
```java
import java.text.*;
// ---- main ----
double v = 1234567.891;
System.out.println(NumberFormat.getInstance(Locale.US).format(v) + " | " + NumberFormat.getInstance(Locale.GERMANY).format(v) + " | " + NumberFormat.getCurrencyInstance(Locale.UK).format(v) + " | " + NumberFormat.getCurrencyInstance(Locale.FRANCE).format(v).replace(' ', '_').replace(' ', '_'));
System.out.println(NumberFormat.getPercentInstance(Locale.US).format(0.256) + " " + NumberFormat.getIntegerInstance(Locale.US).format(2.5) + " " + NumberFormat.getIntegerInstance(Locale.US).format(3.5) + " " + NumberFormat.getCompactNumberInstance(Locale.US, NumberFormat.Style.SHORT).format(2_400_000) + " " + NumberFormat.getCompactNumberInstance(Locale.US, NumberFormat.Style.LONG).format(2_400_000) + " " + new DecimalFormat("#,##0.00").format(5.5) + " " + new DecimalFormat("000.#").format(7.25));
System.out.println(NumberFormat.getInstance(Locale.GERMANY).parse("1.234,5") + " " + NumberFormat.getInstance(Locale.US).parse("1.234,5") + " " + NumberFormat.getCurrencyInstance(Locale.US).parse("$12.50xyz"));
NumberFormat.getCurrencyInstance(Locale.US).parse("12.50");
```
Output:
```
1,234,567.891 | 1.234.567,891 | £1,234,567.89 | 1_234_567,89_€
26% 2 4 2M 2 million 5.50 007.2
1234.5 1.234 12.5
(throws ParseException: Unparseable number: "12.50")
```
**Dates and times:** `DateTimeFormatter.ofLocalizedDate(FormatStyle.SHORT/MEDIUM/LONG/FULL)` (and `ofLocalizedDateTime`, `ofLocalizedTime`) with `.withLocale(locale)`, or `ofPattern(pattern, locale)` for localised month and day names.
```java
import java.time.*;
import java.time.format.*;
// ---- main ----
LocalDate d = LocalDate.of(2024, 7, 4);
for (Locale l : List.of(Locale.US, Locale.UK, Locale.GERMANY))
    System.out.println(l + ": " + d.format(DateTimeFormatter.ofLocalizedDate(FormatStyle.SHORT).withLocale(l)) + " | " + d.format(DateTimeFormatter.ofLocalizedDate(FormatStyle.LONG).withLocale(l)) + " | " + d.format(DateTimeFormatter.ofPattern("EEEE d MMMM", l)));
```
Output:
```
en_US: 7/4/24 | July 4, 2024 | Thursday 4 July
en_GB: 04/07/2024 | 4 July 2024 | Thursday 4 July
de_DE: 04.07.24 | 4. Juli 2024 | Donnerstag 4 Juli
```

#### 11.1 Understand the basics of the Java Logging API
**java.util.logging:** get a logger with `Logger.getLogger("name")` (usually the class name); loggers form a dot-separated hierarchy under the root logger and pass records up to their parents' handlers. **Levels**, highest first: SEVERE, WARNING, INFO, CONFIG, FINE, FINER, FINEST (plus OFF and ALL). A record is published only if its level is at or above **both** the logger's level and the handler's level; the defaults are INFO for both, with a `ConsoleHandler` on the root that writes to **System.err**. Methods: `severe`, `warning`, `info`, `config`, `fine`..., `log(Level, msg)`, `log(Level, "x={0}", param)`, `log(Level, msg, throwable)`, and `Supplier<String>` overloads that build the message only if it will be logged. **Handlers** (`ConsoleHandler`, `FileHandler`, `StreamHandler`) send records somewhere; **formatters** (`SimpleFormatter`, `XMLFormatter` or your own) shape them. Configure in code or with a `logging.properties` file.
```java
import java.util.logging.*;
// ---- main ----
Logger log = Logger.getLogger("shop.orders");
log.setUseParentHandlers(false);
Handler h = new StreamHandler(System.out, new java.util.logging.Formatter() {
    public String format(LogRecord r) { return r.getLevel() + " [" + r.getLoggerName() + "] " + formatMessage(r) + "\n"; }
});
log.addHandler(h);
log.info("service started");
log.fine("not shown: logger level is inherited INFO");
log.setLevel(Level.FINE);
log.fine("still not shown: the handler's level is INFO");
h.setLevel(Level.ALL);
log.fine("now shown");
log.log(Level.WARNING, "order {0} is late by {1} days", new Object[]{"A17", 3});
log.finest(() -> { System.out.println("supplier never runs"); return "x"; });
h.flush();
System.out.println(log.getParent().getName().isEmpty() + " " + Logger.getLogger("shop").getLevel() + " " + Level.SEVERE.intValue() + " " + Level.INFO.intValue());
```
Output:
```
INFO [shop.orders] service started
FINE [shop.orders] now shown
WARNING [shop.orders] order A17 is late by 3 days
true null 1000 800
```

## Explicitly not here
Modules and packaging are S15.
