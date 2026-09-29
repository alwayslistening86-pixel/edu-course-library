# S05_Programming_Paradigms - Lesson: Programming paradigms: procedural and object-oriented programming

## Goal
The learner explains procedural and object-oriented programming, uses hierarchy charts, and writes/interprets simple object-oriented programs and class diagrams.

## Syllabus items taught here
- 4.1.2.1 - Programming paradigms, and procedural-oriented programming
- 4.1.2.3 - Object-oriented programming

## How to teach this
Ask the learner to describe a car two ways: as a list of steps to drive it (procedural), and as a 'thing' with its own properties (speed, fuel) and behaviours (accelerate, brake) bundled together (object-oriented). AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.1.2.1 Programming paradigms, and procedural-oriented programming
A **programming paradigm** is a fundamental style/approach to structuring a program. In **procedural-oriented programming**, a program is built as a structured sequence of procedures/functions that operate on data, designed top-down by breaking the problem into smaller sub-tasks; a **hierarchy chart** shows this breakdown as a tree, with the main task at the top and each level showing the sub-tasks called by the level above. Advantages of the structured approach: easier to design, test and maintain piece by piece, and sub-tasks can be reused.

#### 4.1.2.3 Object-oriented programming
**Object-oriented programming (OOP)** bundles data and the operations on that data together into **objects**. A **class** is a template/blueprint defining an object's data (**attributes**) and behaviour (**methods**); an **object** is a specific **instance** of a class (**instantiation** creates one). **Encapsulation** hides an object's internal data, exposing it only through its methods (protecting it from invalid direct changes). **Inheritance** lets a new (**sub-**) class reuse and extend an existing (**super-**) class's attributes/methods. **Aggregation** and **composition** both model a "has-a" relationship between objects (one class contains/uses another); composition implies the contained object cannot meaningfully exist independently of its owner, aggregation is a looser "has-a" link where it can. **Polymorphism** lets objects of different classes respond to the same method call in their own way; **overriding** is a subclass replacing/redefining a method it inherited. A **class diagram** shows classes, their attributes/methods, and the relationships (inheritance, aggregation, composition) between them.

## Explicitly not here
A-level's specific data structures (queues, stacks, trees, hash tables, dictionaries, vectors) start in S06.
