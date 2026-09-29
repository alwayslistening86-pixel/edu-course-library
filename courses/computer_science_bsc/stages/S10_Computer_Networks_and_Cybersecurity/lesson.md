# S10_Computer_Networks_and_Cybersecurity - Lesson: Computer networks and cybersecurity

## Goal
The learner maps the OSI and TCP/IP models' layers to their responsibilities, performs subnetting calculations from a CIDR prefix, distinguishes TCP and UDP and explains the three-way handshake, and explains the roles of symmetric/asymmetric encryption, hashing and digital signatures alongside common web application attacks.

## Syllabus items taught here
- 10a - The OSI and TCP/IP reference models: layers and their responsibilities
- 10b - IP addressing and subnetting: CIDR notation, subnet masks, calculating network/broadcast addresses and usable hosts
- 10c - Transport and routing: TCP versus UDP, the TCP three-way handshake, routing fundamentals
- 10d - Network and application security: symmetric/asymmetric encryption, hashing, digital signatures, common web attacks

## How to teach this
Ask the learner what actually happens, layer by layer, between clicking a link and a webpage appearing -- before naming any layer. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 10a The OSI and TCP/IP reference models: layers and their responsibilities
**The OSI model** (7 layers, conceptual reference model): Physical (raw bits over a medium), Data Link (framing, MAC addressing, error detection on a local link, e.g. Ethernet), Network (logical addressing and routing between networks, e.g. IP), Transport (end-to-end delivery, e.g. TCP/UDP), Session (managing a communication session), Presentation (data formatting/encryption/compression), Application (the protocol the user-facing software actually speaks, e.g. HTTP). **The TCP/IP model** (the model the real internet is actually built on) collapses this into 4 layers: Network Access/Link (roughly OSI Physical+Data Link), Internet (roughly OSI Network -- IP), Transport (TCP/UDP), Application (roughly OSI Session+Presentation+Application -- HTTP, DNS, SMTP). Each layer only needs to know how to talk to the layer immediately above and below it (encapsulation): an HTTP request is wrapped in a TCP segment, wrapped in an IP packet, wrapped in a link-layer frame, for transmission.

#### 10b IP addressing and subnetting: CIDR notation, subnet masks, calculating network/broadcast addresses and usable hosts
**IP addressing and subnetting.** An IPv4 address is 32 bits, written as four dotted decimal octets (e.g. 192.168.1.10). **CIDR notation** /n means the first n bits are the network portion (fixed for that subnet) and the remaining 32-n bits are the host portion (available to address individual devices). A **subnet mask** expresses the same split in dotted-decimal form (e.g. /24 = 255.255.255.0). The number of usable host addresses on a subnet is 2^(32-n) - 2 (subtracting the network address, all-zero host bits, and the broadcast address, all-one host bits). The **block size** (how far apart subnet boundaries fall) at prefix /n is 2^(32-n); an address's subnet is found by rounding its last relevant octet down to the nearest multiple of the block size.
```python
def subnet_info(ip, prefix):
    octets = [int(o) for o in ip.split('.')]
    host_bits = 32 - prefix
    block_size = 2 ** (host_bits % 8) if host_bits < 8 else None
    usable_hosts = 2 ** host_bits - 2
    return usable_hosts, block_size

usable, block = subnet_info("192.168.1.77", 27)
print("usable hosts on a /27:", usable)
print("block size in the last octet for /27:", block)
# /27 has 5 host bits -> block size 2^5 = 32; 77 falls in the 64-95 block, so network address 192.168.1.64
```
Output:
```
usable hosts on a /27: 30
block size in the last octet for /27: 32
```

#### 10c Transport and routing: TCP versus UDP, the TCP three-way handshake, routing fundamentals
**Transport layer: TCP vs UDP.** **TCP** (Transmission Control Protocol) is connection-oriented and reliable: it guarantees ordered, error-checked, retransmitted-if-lost delivery, using sequence numbers and acknowledgements, at the cost of overhead and latency -- used where correctness matters more than raw speed (e.g. web pages, file transfer, email). **UDP** (User Datagram Protocol) is connectionless and unreliable: it sends packets ('datagrams') with no guarantee of delivery, order, or duplicate-detection, but with much lower overhead -- used where speed/low latency matters more than occasional loss (e.g. video calls, live streaming, DNS queries, online gaming). The **TCP three-way handshake** establishes a connection before data flows: the client sends **SYN** (synchronise, proposing an initial sequence number); the server replies **SYN-ACK** (acknowledging the client's SYN and proposing its own initial sequence number); the client replies **ACK** (acknowledging the server's SYN) -- only then does actual data transfer begin. **Routing** forwards packets between networks hop by hop, each router consulting a routing table to decide the next hop toward the destination IP's network.

#### 10d Network and application security: symmetric/asymmetric encryption, hashing, digital signatures, common web attacks
**Network and application security.** **Symmetric encryption** (e.g. AES) uses the same secret key to encrypt and decrypt -- fast, but the key must somehow be shared securely between parties in advance. **Asymmetric (public-key) encryption** (e.g. RSA) uses a mathematically linked key pair: data encrypted with the public key can only be decrypted with the private key (kept secret by its owner) -- solves the key-distribution problem but is computationally slower, so in practice (e.g. TLS/HTTPS) asymmetric encryption is used briefly to securely exchange a symmetric session key, which then encrypts the actual traffic. **Hashing** (e.g. SHA-256) produces a fixed-length digest from arbitrary input; a good cryptographic hash is one-way (infeasible to reverse) and collision-resistant (infeasible to find two different inputs with the same hash) -- used for verifying integrity (has this file been altered?) and for storing passwords (store a salted hash, never the plaintext password). A **digital signature** uses the signer's private key to sign (a hash of) a message; anyone can verify it with the signer's public key, proving both authenticity (it came from the claimed signer) and integrity (it has not been altered). **Common web attacks**: **SQL injection** (untrusted input concatenated directly into a SQL query lets an attacker inject their own SQL, e.g. bypassing a login check or exfiltrating data -- prevented by parameterised queries/prepared statements, never string concatenation); **Cross-Site Scripting (XSS)** (untrusted input rendered into a page as HTML/JavaScript without escaping lets an attacker run script in another user's browser -- prevented by output encoding/escaping and a Content Security Policy).
```python
import hashlib
password = "correct horse battery staple"
salt = "a1b2c3"
digest = hashlib.sha256((salt + password).encode()).hexdigest()
print(digest[:16], "...")
print(hashlib.sha256((salt + password).encode()).hexdigest() == digest)
print(hashlib.sha256((salt + "wrong password").encode()).hexdigest() == digest)
```
Output:
```
110c31c29ea11773 ...
True
False
```

## Explicitly not here
Cybersecurity threat *types* (malware, phishing, DoS) and the CIA triad are S02; here the focus is the mechanisms (encryption, hashing) and network-layer attacks.
