# S15_Modules_and_Deployment - Test: Modules, jars, runtime images and migration

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which directives belong in a service provider module? (choose two) Choose every correct option.
   A. provides com.pay.spi.Gateway with com.pay.stripe.StripeGateway;
   B. `uses com.pay.spi.Gateway;`
   C. `requires com.pay.spi;`
   D. `exports com.pay.stripe;`
2. A framework needs setAccessible(true) on private fields in package com.app.model at run time, and no other module needs compile-time access. Which is the minimal directive? (choose one) Choose every correct option.
   A. `opens com.app.model;`
   B. `exports com.app.model;`
   C. `requires transitive com.app.model;`
   D. `exports com.app.model to framework;`
3. Which commands run the main class com.shop.Main in module com.shop, compiled into the mods directory? (choose two) Choose every correct option.
   A. java -p mods -m com.shop/com.shop.Main
   B. java --module-path mods --module com.shop/com.shop.Main
   C. java -cp mods com.shop/com.shop.Main
   D. java -m mods com.shop.Main
4. The plain jar commons-text-1.10.0.jar (no Automatic-Module-Name) is placed on the module path. What is its module name? (choose one) Choose every correct option.
   A. `commons.text`
   B. `commons-text`
   C. `commons.text.1.10.0`
   D. It is in the unnamed module
5. Which are true? (choose three) Choose every correct option.
   A. Code on the class path is in the unnamed module
   B. A named module can require the unnamed module
   C. An automatic module exports all its packages
   D. jlink creates a custom runtime image
   E. Two modules may contain the same package
6. Which tool lists the modules and packages a jar depends on? (choose one) Choose every correct option.
   A. `jdeps`
   B. `jlink`
   C. `jpackage`
   D. `jshell`
7. Describe a top-down migration of an application made of your own app.jar plus two third-party jars, naming the steps and the kind of module each jar is at each stage.

## Answer key (for the tutor only)
1. Correct: A, C (exactly these options, no others)
2. Correct: A (exactly these options, no others)
3. Correct: A, B (exactly these options, no others)
4. Correct: A (exactly these options, no others)
5. Correct: A, C, D (exactly these options, no others)
6. Correct: A (exactly these options, no others)
7. The tutor runs or reads the learner's answer and checks: all jars moved to the module path; third-party jars become automatic modules (names from manifest or file name); app gets module-info.java requiring them; later libraries may become named modules; nothing left relies on the unnamed module

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_Modules_and_Deployment` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
