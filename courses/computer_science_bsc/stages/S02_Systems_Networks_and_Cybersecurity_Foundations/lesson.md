# S02_Systems_Networks_and_Cybersecurity_Foundations - Lesson: Systems, networks and cybersecurity foundations

## Goal
The learner explains IEEE 754 floating-point representation and character encoding, distinguishes cloud service/deployment models and client-server versus peer-to-peer architectures, describes the mobile computing stack, and identifies common cybersecurity threats and the CIA triad.

## Syllabus items taught here
- 2a - Data representation in depth: IEEE 754 floating point, character encoding (ASCII/Unicode/UTF-8)
- 2b - Cloud and distributed computing: IaaS/PaaS/SaaS, virtualisation, client-server vs peer-to-peer models
- 2c - Mobile computing architectures: mobile OS stack, sensors, app sandboxing
- 2d - Cybersecurity fundamentals: threat types, the CIA triad, authentication vs authorisation

## How to teach this
Ask the learner to predict, before running it, what 0.1 + 0.2 prints in Python -- most expect 0.3. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 2a Data representation in depth: IEEE 754 floating point, character encoding (ASCII/Unicode/UTF-8)
**IEEE 754 floating point.** A float is stored as sign, exponent and mantissa (significand) bits (32-bit single precision: 1+8+23; 64-bit double: 1+11+52), representing value = (-1)^sign x 1.mantissa x 2^(exponent-bias). Because most decimal fractions (e.g. 0.1) have no exact finite binary representation, floating-point arithmetic is inherently approximate, which is why equality comparisons on floats are unsafe practice.
```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 10) == round(0.3, 10))
```
Output:
```
0.30000000000000004
False
True
```
**Character encoding.** ASCII uses 7 bits (128 characters, English-only); Unicode assigns every character in every script a unique code point (e.g. U+0041 for 'A'); UTF-8 is a variable-length encoding of Unicode that uses 1 byte for ASCII characters (backward compatible) and up to 4 bytes for others, which is why it is the dominant web/text encoding.
```python
print(ord('A'), ord('€'))
print('A'.encode('utf-8'), '€'.encode('utf-8'))
print(len('€'.encode('utf-8')), 'bytes for the euro sign in UTF-8')
```
Output:
```
65 8364
b'A' b'\xe2\x82\xac'
3 bytes for the euro sign in UTF-8
```

#### 2b Cloud and distributed computing: IaaS/PaaS/SaaS, virtualisation, client-server vs peer-to-peer models
**Cloud service models.** *IaaS* (Infrastructure as a Service, e.g. raw virtual machines/storage) gives the most control and the most management burden; *PaaS* (Platform as a Service) provides a managed runtime so developers deploy code without managing servers/OS; *SaaS* (Software as a Service) delivers a complete application over the internet (e.g. webmail) with no infrastructure management at all -- control decreases and convenience increases from IaaS to SaaS. **Virtualisation** runs multiple isolated virtual machines (each with its own OS) on one physical host via a hypervisor, underpinning most cloud infrastructure; *containers* (e.g. Docker) are a lighter-weight alternative that share the host OS kernel while isolating the application and its dependencies. **Client-server vs peer-to-peer.** In client-server, clients request services from a central server (simpler to secure/manage, a single point of failure/bottleneck); in peer-to-peer, nodes act as both client and server to each other (no single point of failure, harder to secure/coordinate, used by e.g. BitTorrent).

#### 2c Mobile computing architectures: mobile OS stack, sensors, app sandboxing
**Mobile computing architectures.** A modern mobile OS (e.g. Android, iOS) runs each app in its own sandbox: a restricted execution environment that limits what an app can access (files, other apps' data, hardware) without explicit user-granted permission, protecting both the user and the OS from misbehaving or malicious apps. A typical device integrates sensors (accelerometer, GPS, gyroscope, camera, touchscreen digitiser) whose data apps request through the OS's permission model rather than accessing hardware directly. Mobile apps are typically event-driven (responding to touches, sensor changes, network callbacks) and must manage a battery/power budget and intermittent connectivity, constraints a desktop application usually does not face.

#### 2d Cybersecurity fundamentals: threat types, the CIA triad, authentication vs authorisation
**Cybersecurity fundamentals.** Common threat types: *malware* (viruses, worms, trojans, ransomware -- malicious software, differing in how they spread/what they do); *phishing* (fraudulent communication, often email, tricking a user into revealing credentials or installing malware); *social engineering* (manipulating a person, not a system, e.g. pretexting or impersonation, to bypass technical controls); *denial-of-service (DoS)*, and *distributed* DoS (DDoS, from many sources), which overwhelm a system so legitimate users cannot use it. The **CIA triad** frames security goals: *Confidentiality* (only authorised parties can read data), *Integrity* (data is not altered without authorisation), *Availability* (authorised users can access the system/data when needed) -- a DDoS attack targets availability specifically. **Authentication** (proving who you are, e.g. a password or biometric) is distinct from **authorisation** (what an authenticated identity is permitted to do); a system can authenticate a user correctly and still refuse to authorise a particular action.

## Explicitly not here
Deeper network protocol layers, subnetting and encryption mechanisms are S10 (Computer Networks and Cybersecurity).
