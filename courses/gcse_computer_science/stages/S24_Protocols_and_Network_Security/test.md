# S24_Protocols_and_Network_Security - Test: Protocols, network security and the TCP/IP model

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the main difference between TCP and UDP, and give a situation better suited to each. [4 marks]
2. Explain the purpose of a firewall and of MAC address filtering, and state one difference between them. [4 marks]
3. Explain why HTTPS is more suitable than HTTP for a website where users log in with a password. [2 marks]
4. State which layer of the TCP/IP model HTTP operates at, and which layer IP operates at. [2 marks]
5. Which network security method blocks any device not on an approved list from connecting, based on a unique hardware identifier? Choose every correct option.
   A. MAC address filtering
   B. `encryption`
   C. a firewall
   D. `authentication`

## Answer key (for the tutor only)
1. [4] B1 TCP guarantees reliable, ordered delivery (resending lost packets); B1 e.g. suited to downloading a file, where every byte must arrive correctly; B1 UDP is faster but does not guarantee delivery/order; B1 e.g. suited to a live video call, where a skipped frame matters less than a delay.
2. [4] B1 a firewall monitors/controls incoming and outgoing traffic against a set of rules, blocking suspicious/unauthorised traffic; B1 MAC address filtering only allows devices on an approved list of MAC addresses to connect at all; B1 both restrict who/what can access the network; B1 difference, e.g. a firewall inspects traffic content/rules generally, while MAC filtering checks a specific device identifier before any connection is allowed.
3. [2] B1 HTTPS encrypts the data sent between the browser and the server; B1 so a password intercepted in transit could not be read/used by an attacker, unlike over plain HTTP.
4. [2] B1 HTTP: application layer; B1 IP: internet layer.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S24_Protocols_and_Network_Security` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S25_Cyber_Security_Threats.
