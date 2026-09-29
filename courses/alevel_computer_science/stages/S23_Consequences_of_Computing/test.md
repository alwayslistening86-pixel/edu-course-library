# S23_Consequences_of_Computing - Test: Individual, social, legal and cultural issues and opportunities in computing

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what is meant by the claim that 'software and its algorithms embed moral and cultural values'. [3 marks]
2. Explain why the scale at which software can be deployed makes its ethical design especially important. [2 marks]
3. Discuss the ethical and legal issues raised by a company using a facial-recognition system in a public space without informing the people photographed. [6 marks]
4. Which best describes why legislation often struggles to keep pace with new computing technology? Choose every correct option.
   A. technology changes quickly, while creating and passing new law is typically a much slower process
   B. computing technology never raises any legal questions
   C. legislation is always written before the technology it applies to exists
   D. computer scientists are legally required to write new laws themselves

## Answer key (for the tutor only)
1. [3] B1 the choices made when designing an algorithm (what it optimises for, what data it is trained/tested on, what it treats as normal or acceptable) are not neutral; B1 these choices reflect the values (intentional or not) of the people who built it; B1 example, e.g. a recommendation algorithm optimised purely for engagement may end up favouring sensational content, or a facial-recognition system trained mostly on one demographic may perform worse on others.
2. [2] B1 a single flawed or biased algorithm, once deployed, can affect a very large number of people simultaneously; B1 this is different from a single human decision-maker's mistakes, which typically affect far fewer people at a time -- so errors in widely-deployed software have disproportionately large consequences.
3. [6] Level 2 (4-6): balanced discussion covering at least two of: consent and privacy (people were not asked and may not know they are being identified); legal issues (whether this complies with data protection law, and which jurisdiction's law applies); potential for bias/error in the system (misidentification, disproportionately affecting some groups); accountability if the system is misused or makes a harmful error; and a reasoned overall point. Level 1 (1-3): limited/one-sided discussion. 0: no relevant discussion.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S23_Consequences_of_Computing` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S24_Transmission_Topology_and_Network_Models.
