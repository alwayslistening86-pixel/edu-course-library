# S15_Modules_and_Deployment - Practice: Modules, jars, runtime images and migration

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. Which directive lets another module call public methods of types in package com.x.api? (choose one) Choose every correct option.
   A. `exports com.x.api;`
   B. `opens com.x.api;`
   C. `requires com.x.api;`
   D. `uses com.x.api;`
2. Write module-info.java for a module com.acme.report that depends on java.sql (and passes that dependency on to its users), exports com.acme.report.api only to com.acme.web, and consumes the service com.acme.spi.Exporter.

## Answers (for the tutor; reveal only after a genuine attempt)
1. Correct: A (exactly these options, no others)
2. The tutor runs or reads the learner's answer and checks: module com.acme.report { requires transitive java.sql; exports com.acme.report.api to com.acme.web; uses com.acme.spi.Exporter; } plus requires for the module holding com.acme.spi

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
