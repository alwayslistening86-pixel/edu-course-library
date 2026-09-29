# S10_Computer_Networks_and_Cybersecurity - Test: Computer networks and cybersecurity

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. An IP address 10.0.5.200 uses subnet mask 255.255.255.224 (/27). State the block size, the network address of the subnet containing this host, and the number of usable host addresses. [6 marks]
2. Explain, step by step, the TCP three-way handshake, and state why UDP does not use an equivalent handshake. [5 marks]
3. Explain why TLS/HTTPS uses asymmetric encryption only briefly at the start of a connection and switches to symmetric encryption for the actual data transfer, rather than using asymmetric encryption throughout. [4 marks]
4. A login form builds its SQL query as: "SELECT * FROM users WHERE username='" + input_username + "' AND password='" + input_password + "'". Explain how an attacker could exploit this with SQL injection, and state the correct defence. [4 marks]
5. Explain what a cryptographic hash function's 'collision resistance' property means, and why storing a plain (unhashed) password in a database is a serious security risk even if the database itself is otherwise well protected. [4 marks]
6. Which statements about TCP and UDP are correct? Choose every correct option.
   A. TCP guarantees ordered, reliable delivery of data
   B. UDP guarantees ordered, reliable delivery of data
   C. UDP is commonly preferred for latency-sensitive applications such as live video/voice calls where occasional loss is tolerable
   D. The TCP three-way handshake occurs before any application data is sent over that connection

## Answer key (for the tutor only)
1. [6] M1 /27 leaves 5 host bits, so block size = 2^5 = 32; M1 200 divided by 32 gives 6 remainder 8, so the subnet boundaries near 200 are 192 and 224; A1 200 falls in the 192-223 block, so network address 10.0.5.192; M1 usable hosts = 2^5 - 2; A1 = 30; A1 broadcast address 10.0.5.223 correctly stated as a check on the working (not separately asked, but shows the range 193-222 is the usable host range).
2. [5] B1 client sends SYN with an initial sequence number, proposing a connection; B1 server replies SYN-ACK, acknowledging the client's SYN and proposing its own initial sequence number; B1 client replies ACK, acknowledging the server's SYN, after which data transfer begins; B1 the handshake exists to establish agreed sequence numbers and confirm both sides are ready, part of TCP's reliability/ordering guarantees; B1 UDP is connectionless by design (no ordering/reliability guarantee to establish), so a handshake would only add overhead without UDP delivering on any guarantee that overhead would support.
3. [4] B1 asymmetric encryption solves the key-distribution problem (no need to have shared a secret key in advance), which is essential at connection setup when the two parties have no prior shared secret; B1 but asymmetric encryption is computationally much slower/more expensive than symmetric encryption; B1 so asymmetric encryption is used briefly to securely establish a shared symmetric session key; B1 the much faster symmetric encryption is then used for the bulk of the actual data transfer, giving both security and acceptable performance.
4. [4] B1 an attacker enters something like ' OR '1'='1 as the username (or password), which is concatenated directly into the query, changing its logical structure; B1 the resulting query's WHERE clause becomes always true (or otherwise attacker-controlled), potentially bypassing the login check entirely or extracting/altering data; B1 correct defence: parameterised queries / prepared statements, which pass user input as data bound to placeholders rather than concatenating it into the SQL text, so it can never change the query's structure; B1 (or) input validation alone is an insufficient substitute -- parameterisation is the actually correct fix, credited if explicitly stated why naive input filtering is not enough.
5. [4] B1 collision resistance means it is computationally infeasible to find two different inputs that produce the same hash output; B1 storing a plain password means anyone who gains any kind of read access to that data (a breach, an insider, a backup leak) immediately has the user's actual password, not merely a hash they would then need to separately crack; B1 because many users reuse passwords across sites, a single plaintext password leak can compromise a user's accounts elsewhere too; B1 (or) storing a salted hash instead means an attacker who obtains the database only gets hashes, which (with a strong hash and unique salt) are infeasible to reverse to the original password at any useful scale.
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Computer_Networks_and_Cybersecurity` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 24 marks in all; a pass needs at least 15 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Introduction_to_Machine_Learning_and_AI.
