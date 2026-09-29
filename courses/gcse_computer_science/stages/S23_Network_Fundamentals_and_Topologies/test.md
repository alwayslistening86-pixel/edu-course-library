# S23_Network_Fundamentals_and_Topologies - Test: Network fundamentals and topologies

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe the difference between a LAN and a WAN. [2 marks]
2. Explain one advantage and one disadvantage of a wireless network compared with a wired network. [4 marks]
3. Describe a star network topology and explain one advantage it has over a bus topology. [3 marks]
4. A small office wants to install a network as cheaply as possible and does not mind if a single cable fault affects every computer. Recommend and justify a suitable topology. [3 marks]
5. Which best describes a Personal Area Network (PAN)? Choose every correct option.
   A. a network connecting devices over a very short range around one person
   B. a network covering a whole city
   C. a network that must always be wired
   D. a network that connects multiple LANs across countries

## Answer key (for the tutor only)
1. [2] B1 a LAN covers a small area (e.g. one site/building), typically owned/managed by a single organisation; B1 a WAN covers a large geographical area, often connecting multiple LANs, typically using leased third-party infrastructure.
2. [4] B1 advantage, e.g. more flexible -- devices can move/connect without needing a cable to a socket; B1 explained/expanded; B1 disadvantage, e.g. can be less reliable (interference/walls) or less secure (signal can potentially be intercepted); B1 explained/expanded.
3. [3] B1 every device connects individually to a central device (e.g. a switch); B1 advantage, e.g. if one device/cable fails only that device is affected (the rest of the network keeps working); B1 explained/contrasted with bus, where a single cable failure takes the whole network down.
4. [3] B1 bus topology; B1 needs less cabling, so it is cheaper to install; B1 the stated trade-off (a single cable fault taking down the whole network) is explicitly acceptable to this office, matching bus's main weakness.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S23_Network_Fundamentals_and_Topologies` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S24_Protocols_and_Network_Security.
