# S24_Transmission_Topology_and_Network_Models - Lesson: Data transmission, network topologies and peer-to-peer/client-server networking

## Goal
The learner explains data-transmission methods and basics, network topologies (star, bus), and peer-to-peer vs client-server networking.

## Syllabus items taught here
- 4.9.1.1 - Communication methods and data-transmission basics
- 4.9.2.1 - Network topologies: star and bus
- 4.9.2.2 - Peer-to-peer and client-server networking

## How to teach this
Ask the learner why sending several bits down several wires at once (in parallel) sounds faster than sending them one at a time down one wire (serially) -- yet serial transmission actually wins over long distances. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.9.1.1 Communication methods and data-transmission basics
**Serial transmission** sends bits one at a time, one after another, down a single wire/channel; **parallel transmission** sends multiple bits simultaneously down multiple wires. Serial is preferred over long distances/high speeds because parallel wires suffer **skew** (signals on different wires arriving at very slightly different times, which gets worse over distance/speed) and crosstalk between adjacent wires. **Synchronous** transmission uses a shared clock signal to keep sender and receiver in step, sending data in a continuous, precisely-timed stream; **asynchronous** transmission has no shared clock -- each unit of data (e.g. a byte) is individually framed with a **start bit** (signals the beginning of new data, letting the receiver synchronise for just that unit) and one or more **stop bits** (signal the end), at the cost of some overhead. Key terms: **baud rate** (signal changes per second) is not always the same as **bit rate** (bits transferred per second) -- they only coincide when each signal change encodes exactly one bit; **bandwidth** is the maximum rate a channel can carry (its theoretical capacity); **latency** is the delay before data starts arriving; a **protocol** is an agreed set of rules governing how communication takes place.

#### 4.9.2.1 Network topologies: star and bus
A **network topology** describes how devices are physically/logically connected. A **star topology**: every device connects individually to a central device (e.g. a switch); if one connection cable fails, only that device is affected, but the central device is a single point of failure for the whole network. A **bus topology** (logical, common in older/wireless-style shared-medium networks): all devices share one common communication line (the "bus"); simple and cheap, but the shared line is itself a single point of failure, and only one device can transmit at a time without collisions.

#### 4.9.2.2 Peer-to-peer and client-server networking
In **peer-to-peer (P2P)** networking, connected devices act as equals, each able to act as both client and server, sharing resources (files, processing) directly with each other with no central server required -- suited to smaller networks or decentralised file-sharing, but harder to secure/manage centrally and less reliable if key peers go offline. In **client-server** networking, dedicated, typically more powerful **servers** provide resources/services (files, web pages, authentication) which **client** devices request and use; this centralises management, security and backup, and scales better to larger networks, but the server is a more significant single point of failure and needs greater investment to provision.

## Explicitly not here
Wireless networking, and how the Internet itself works, are S25.
