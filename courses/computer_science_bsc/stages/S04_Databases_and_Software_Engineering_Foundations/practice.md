# S04_Databases_and_Software_Engineering_Foundations - Practice: Databases and software engineering foundations

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. A table Orders(order_id, customer_name, customer_address, product, quantity) stores one row per order line, with customer_name and customer_address repeated for every order the same customer places. Name the anomaly this risks if a customer moves house, and explain it. [3 marks]
2. State whether a Student-to-Course relationship (students can take many courses, courses can have many students) is 1:1, 1:M or M:N, and state how it is implemented in a relational database. [2 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. [3] B1 update anomaly; B1 the customer's address is stored redundantly in every order row; B1 if only some rows are updated with the new address, the data becomes inconsistent (the same customer appears to have two different addresses).
2. [2] B1 M:N (many-to-many); B1 implemented via a junction/associative table (e.g. Enrolment) holding foreign keys to both Student and Course.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
