# S05_Programming_Paradigms - Test: Programming paradigms: procedural and object-oriented programming

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a class and an object. [2 marks]
2. Explain the difference between inheritance and composition, with one example of each. [4 marks]
3. Explain what method overriding means, using the Animal/Dog example where Dog redefines speak(). [2 marks]
4. Explain one advantage of the structured (procedural) top-down approach to program design. [2 marks]
5. Which best describes polymorphism? Choose every correct option.
   A. objects of different classes can respond to the same method call, each in its own way
   B. a class can only ever have one object instantiated from it
   C. a subclass cannot access any of its superclass's methods
   D. every attribute in a class must be public

## Answer key (for the tutor only)
1. [2] B1 a class is a template/blueprint defining attributes and methods; B1 an object is a specific instance of a class, created by instantiation.
2. [4] B1 inheritance: a subclass reuses/extends a superclass's attributes and methods (an 'is-a' relationship); B1 example, e.g. a Car class inheriting from a Vehicle class; B1 composition: a class contains another object as part of itself, which cannot meaningfully exist independently (a 'has-a' relationship); B1 example, e.g. a Car containing an Engine object.
3. [2] B1 a subclass (Dog) provides its own version of a method it inherited from its superclass (Animal); B1 calling speak() on a Dog object runs Dog's version, not Animal's -- this is polymorphism in action.
4. [2] B1 breaking a problem into smaller sub-tasks (shown in a hierarchy chart) makes each part easier to design, code and test independently; B1 sub-tasks (procedures/functions) can potentially be reused elsewhere in the program.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Programming_Paradigms` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Arrays_Records_ADTs.
