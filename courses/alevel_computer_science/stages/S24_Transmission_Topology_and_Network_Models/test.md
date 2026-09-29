# S24_Transmission_Topology_and_Network_Models - Test: Data transmission, network topologies and peer-to-peer/client-server networking

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between synchronous and asynchronous data transmission, and the purpose of start and stop bits. [4 marks]
2. Explain one advantage and one disadvantage of a star topology compared with a bus topology. [2 marks]
3. Explain the key difference between peer-to-peer and client-server networking, and give one situation each suits well. [4 marks]
4. Why is serial transmission generally preferred over parallel transmission for long-distance, high-speed communication? Choose every correct option.
   A. parallel transmission suffers skew and crosstalk between wires, which worsen with distance/speed
   B. serial transmission cannot be used over any distance greater than one metre
   C. parallel transmission requires no additional wires compared with serial
   D. serial transmission cannot represent more than 8 bits in total

## Answer key (for the tutor only)
1. [4] B1 synchronous transmission uses a shared clock signal to keep sender and receiver in step, sending a continuous stream; B1 asynchronous transmission has no shared clock; B1 each unit of data is individually framed with a start bit, signalling the start of new data so the receiver can synchronise just for that unit; B1 and one or more stop bits, signalling the end of that unit.
2. [2] B1 advantage, e.g. one failed cable only affects the single device on it, not the whole network (unlike a shared bus line); B1 disadvantage, e.g. the central device (e.g. switch) is a single point of failure for the entire star network, and more cabling is needed than a bus.
3. [4] B1 peer-to-peer: devices act as equals, sharing resources directly with no central server; B1 suited example, e.g. small-scale decentralised file sharing between a handful of home devices; B1 client-server: dedicated servers provide resources/services that client devices request; B1 suited example, e.g. a school or business network needing centralised management, security and backup.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S24_Transmission_Topology_and_Network_Models` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S25_Wireless_Internet_and_Security.
