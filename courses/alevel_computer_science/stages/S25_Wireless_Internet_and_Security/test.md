# S25_Wireless_Internet_and_Security - Test: Wireless networking, the Internet and Internet security

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain how CSMA/CA with RTS/CTS reduces collisions on a wireless network, compared with not using RTS/CTS. [4 marks]
2. Explain the role of packet switching in how the Internet transmits data, including why packets carry a sequence number. [3 marks]
3. Explain the role of DNS, and what happens if a domain name cannot be resolved. [3 marks]
4. Explain the difference between symmetric and asymmetric encryption, and why asymmetric encryption is often used only to exchange a symmetric key rather than to encrypt an entire session. [4 marks]
5. Which malicious code type disguises itself as legitimate software to trick a user into installing it? Choose every correct option.
   A. a trojan
   B. a worm
   C. a firewall
   D. a digital certificate

## Answer key (for the tutor only)
1. [4] B1 without RTS/CTS, a device only listens to check the channel is clear before transmitting, which does not fully prevent two out-of-range-of-each-other devices ('hidden nodes') from transmitting simultaneously; B1 with RTS/CTS, the device first sends a short Request To Send; B1 the access point replies with Clear To Send, reserving the channel for that device; B1 this warns other devices (that can hear the CTS, even if not the original RTS) not to transmit, reducing hidden-node collisions.
2. [3] B1 a message is broken into small packets, each sent independently, potentially by different routes across the network; B1 packets carry a sequence number so they can be correctly reassembled into the original message at the destination, even if they arrive out of order; B1 this allows the network to route around congestion/failures, since each packet can take whatever path is currently available.
3. [3] B1 DNS is a distributed hierarchy of servers that translates human-readable domain names into the numeric IP addresses routers actually use; B1 a device queries DNS (often via its configured DNS server) to look up a domain name before it can connect to that server; B1 if the domain name cannot be resolved (e.g. it does not exist, or the DNS server cannot be reached), the connection fails, typically shown to the user as a 'server not found'-type error.
4. [4] B1 symmetric encryption uses the same secret key to encrypt and decrypt; B1 asymmetric encryption uses a mathematically linked public/private key pair, so the public key can be shared openly without compromising security; B1 asymmetric encryption is computationally slower than symmetric encryption; B1 so it is efficient to use it just once, to securely exchange a symmetric key, then use faster symmetric encryption for the rest of the session's data.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S25_Wireless_Internet_and_Security` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S26_TCPIP_Protocols_and_Addressing.
