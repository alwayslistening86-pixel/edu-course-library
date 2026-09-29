# S15_Modules_and_Deployment - Lesson: Modules, jars, runtime images and migration

## Goal
The learner writes module-info.java declarations (requires, requires transitive, exports, exports ... to, opens, uses, provides ... with), compiles and runs modular code, builds modular and non-modular jars and a jlink runtime image, uses ServiceLoader, and plans a migration with unnamed and automatic modules.

## Syllabus items taught here
- 7.1 - Define modules and expose module content, including by reflection; declare module dependencies; define services, providers and consumers
- 7.2 - Compile Java code; create modular and non-modular jars and runtime images; migrate to modules using unnamed and automatic modules

## How to teach this
Ask what the difference is between `exports` and `opens`, and which one reflection needs to read a private field. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 7.1 Define modules and expose module content, including by reflection; declare module dependencies; define services, providers and consumers
A **module** is a named set of packages with a `module-info.java` at the root of its source tree. Directives:
- `requires M;` depends on module M (`java.base` is implicit). `requires transitive M;` also gives M to anyone who requires this module. `requires static M;` is needed at compile time only.
- `exports p;` makes the **public** types of package p accessible to other modules (compile time and run time); `exports p to M1, M2;` is a qualified export. Non-exported packages are encapsulated even if their classes are public.
- `opens p;` (or `opens p to M;`, or `open module X {}` for every package) allows **deep reflection** at run time, including on private members (`setAccessible(true)`), but gives no compile-time access. Frameworks that use reflection need `opens`.
- **Services:** an API module exports a service interface; a provider module declares `provides api.Service with impl.Provider;` (the provider class needs a public no-arg constructor or a public static `provider()` method, and its package needn't be exported); a consumer declares `uses api.Service;` and finds implementations with `ServiceLoader.load(Service.class)`. The consumer doesn't require the provider module; it only has to be on the module path.
Rules: a module graph can't have cycles, and two modules may not contain the same package (a split package).

A worked example with three modules, all compiled and run for real on JDK 21 while this course was written:
```java
// src/com.shop.api/module-info.java
module com.shop.api {
    exports com.shop.api;
}
// src/com.shop.api/com/shop/api/PriceService.java
package com.shop.api;
public interface PriceService {
    String name();
    int price(int base);
}
// src/com.shop.impl/module-info.java
module com.shop.impl {
    requires com.shop.api;
    provides com.shop.api.PriceService with com.shop.impl.HalfPrice;
    opens com.shop.impl to com.shop.app;
}
// src/com.shop.impl/com/shop/impl/HalfPrice.java
package com.shop.impl;
import com.shop.api.PriceService;
public class HalfPrice implements PriceService {
    private String secret = "hidden";
    public String name() { return "half"; }
    public int price(int base) { return base / 2; }
}
// src/com.shop.app/module-info.java
module com.shop.app {
    requires com.shop.api;
    uses com.shop.api.PriceService;
}
// src/com.shop.app/com/shop/app/Main.java
package com.shop.app;
import com.shop.api.PriceService;
import java.lang.reflect.Field;
import java.util.ServiceLoader;
public class Main {
    public static void main(String[] args) throws Exception {
        for (PriceService s : ServiceLoader.load(PriceService.class)) {
            System.out.println(s.name() + " -> " + s.price(80) + " from " + s.getClass().getModule().getName());
            Field f = s.getClass().getDeclaredField("secret");
            f.setAccessible(true);
            System.out.println("reflected: " + f.get(s));
        }
    }
}
```
Running it prints:
```
half -> 40 from com.shop.impl
reflected: hidden
```
With the `opens` line removed from com.shop.impl, the service still loads, but the reflection fails at run time:
```
half -> 40 from com.shop.impl
Exception in thread "main" java.lang.reflect.InaccessibleObjectException: Unable to make field private java.lang.String com.shop.impl.HalfPrice.secret accessible: module com.shop.impl does not "opens com.shop.impl" to module com.shop.app
```

#### 7.2 Compile Java code; create modular and non-modular jars and runtime images; migrate to modules using unnamed and automatic modules
**Compiling and running.** Non-modular: `javac -d out src/.../*.java`, then `java -cp out pkg.Main` (or `-classpath`, `--class-path`). Modular: `javac -d out --module-source-path src $(find src -name "*.java")` (or `-p`/`--module-path` for already-compiled modules), then `java --module-path out --module com.shop.app/com.shop.app.Main` (short forms `-p` and `-m`).

**Jars.** `jar --create --file app.jar -C out .` (short `jar -cf`); `--main-class pkg.Main` records the entry point, so `java -jar app.jar` works for a plain jar and `java -p mods -m com.shop.app` works for a modular one. A **modular jar** is simply a jar with `module-info.class` at its root. For the example above:
```
jar --create --file mods/com.shop.api.jar -C out/com.shop.api .
jar --create --file mods/com.shop.impl.jar -C out/com.shop.impl .
jar --create --file mods/com.shop.app.jar --main-class com.shop.app.Main -C out/com.shop.app .
java -p mods -m com.shop.app
```
That prints the same two lines as before. **Inspecting:** `jar --describe-module --file mods/com.shop.impl.jar` printed:
```
com.shop.impl jar:file:///.../mods/com.shop.impl.jar!/module-info.class
requires com.shop.api
requires java.base mandated
provides com.shop.api.PriceService with com.shop.impl.HalfPrice
qualified opens com.shop.impl to com.shop.app
```
Also `java --describe-module` (`-d`) with `-p`, `java --list-modules`, `java --show-module-resolution`, and `jdeps` (`jdeps -s`, `--jdk-internals`) to list dependencies. `jdeps --module-path mods -s mods/com.shop.app.jar` printed `com.shop.app -> com.shop.api` and `com.shop.app -> java.base`.

**Runtime images.** `jlink --module-path mods --add-modules com.shop.app,com.shop.impl --launcher shop=com.shop.app --output image` builds a self-contained runtime holding only the modules needed (the service provider has to be added explicitly, since nothing `requires` it; `--bind-services` is the alternative). `image/bin/java --list-modules` printed `com.shop.api`, `com.shop.app`, `com.shop.impl` and `java.base@21.0.10`, and `image/bin/shop` ran the program. (`jpackage` goes further and builds a native installer.)

**Migration.**
- Everything on the **class path** belongs to the single **unnamed module**. It reads every module and exports all its packages, but named modules can't `requires` it.
- A plain (non-modular) jar placed on the **module path** becomes an **automatic module**. Its name comes from `Automatic-Module-Name` in the manifest, or else from the file name: the version is dropped and non-alphanumeric characters become dots. For example, `string-utils-2.1.jar` became `string.utils@2.1 automatic`. An automatic module exports and opens all its packages and reads all other modules, including the unnamed one.
- **Bottom-up migration** modularises the lowest-level libraries first, leaving the rest on the class path.
- **Top-down migration** puts every jar on the module path (so third-party jars become automatic modules), then modularises your own code from the application down.
- A small non-modular program shows where its classes live: calling `getModule()` printed `unnamed module @...`, and `isNamed()` was false.

## Explicitly not here
This is the last stage; the cumulative exam follows.
