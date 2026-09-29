# S26_TCPIP_Protocols_and_Addressing - Test: The TCP/IP stack, application protocols, IP addressing and the client-server model

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe the role of each of the four TCP/IP layers. [4 marks]
2. Explain the purpose of NAT, and why it is commonly used alongside a private IP address range. [3 marks]
3. Explain the purpose of DHCP, and one advantage of using it over manually configuring every device's IP address. [2 marks]
4. Explain the difference between JSON and XML as data formats for a web API, and one advantage of JSON. [3 marks]
5. Which best distinguishes thin-client from thick-client computing? Choose every correct option.
   A. a thin client relies on a central server for most processing; a thick client does most processing itself
   B. a thin client never needs any network connection at all
   C. a thick client cannot store any data locally
   D. a thin client always has more processing power than the server it connects to

## Answer key (for the tutor only)
1. [4] B1 application layer: protocols used directly by applications (e.g. HTTP, FTP); B1 transport layer: end-to-end delivery between programs (e.g. TCP), using ports; B1 network layer: routing packets between networks (e.g. IP), using IP addresses; B1 link layer: transmission over the local physical medium, using MAC addresses.
2. [3] B1 NAT lets many devices on a private network share one public IP address when communicating with the wider Internet; B1 it translates between the private addresses used internally and the single public address used externally, as traffic passes through the router; B1 this means a whole private network need not have its own large block of scarce/costly public IP addresses.
3. [2] B1 DHCP automatically assigns an IP address (and other network settings) to a device when it joins a network; B1 advantage, e.g. saves administrator time and avoids the risk of accidentally assigning the same address to two devices, which manual configuration risks at scale.
4. [3] B1 both are common formats for structuring data exchanged between client and server; B1 JSON is generally more compact and maps naturally onto typical programming-language data structures (lists, key-value pairs); B1 advantage of JSON, e.g. simpler/faster to read, write and parse than XML's more verbose tag-based structure.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S26_TCPIP_Protocols_and_Addressing` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S27_Data_Modelling_and_Normalisation.
