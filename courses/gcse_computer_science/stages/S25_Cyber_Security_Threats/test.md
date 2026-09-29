# S25_Cyber_Security_Threats - Test: Cyber security threats: social engineering and malware

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what is meant by pharming, and how it differs from phishing. [3 marks]
2. Explain why leaving software unpatched (not updated) is a cyber security risk. [2 marks]
3. Explain the difference between a computer virus and a trojan. [3 marks]
4. Explain the difference between internal and external penetration testing. [2 marks]
5. Which threat is a form of malware that secretly monitors and reports back a user's activity, such as keystrokes? Choose every correct option.
   A. `spyware`
   B. `phishing`
   C. `blagging`
   D. `shouldering`

## Answer key (for the tutor only)
1. [3] B1 pharming redirects a user from a legitimate website to a fraudulent one, often by corrupting how the site's address is looked up; B1 this happens without the user clicking anything; B1 phishing, by contrast, relies on tricking the user into clicking a link or attachment in a fraudulent message.
2. [2] B1 updates often fix known security vulnerabilities that the supplier has already published/identified; B1 unpatched software remains open to attackers exploiting that already-known weakness.
3. [3] B1 a virus attaches to a legitimate file/program and can replicate itself, spreading to other files/systems; B1 a trojan disguises itself as legitimate/desirable software to trick the user into installing it; B1 a trojan does not replicate itself, unlike a virus.
4. [2] B1 internal: simulates an attack from within the organisation's own network / by someone with existing access; B1 external: simulates an attack from outside the organisation, e.g. over the internet, with no prior access.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S25_Cyber_Security_Threats` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S26_Detecting_and_Preventing_Threats.
