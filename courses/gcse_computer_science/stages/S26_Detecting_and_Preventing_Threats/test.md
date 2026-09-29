# S26_Detecting_and_Preventing_Threats - Test: Detecting and preventing cyber security threats

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain how CAPTCHA helps protect a website against automated attacks. [2 marks]
2. Explain how automatic software updates help reduce the risk of a successful cyber attack. [2 marks]
3. A bank wants to add a second layer of protection to online logins on top of a password. Suggest and justify one suitable method from this stage. [3 marks]
4. Which method is specifically designed to distinguish a human user from an automated bot? Choose every correct option.
   A. `CAPTCHA`
   B. a firewall
   C. MAC address filtering
   D. `encryption`

## Answer key (for the tutor only)
1. [2] B1 presents a test designed to be easy for a human but hard for an automated program/bot to pass; B1 this stops bots automatically, repeatedly attempting logins/creating accounts at scale.
2. [2] B1 they apply fixes for known security vulnerabilities as soon as they are released; B1 reducing the time available for an attacker to exploit a known, unpatched weakness.
3. [3] B1 e.g. email confirmation / two-step verification, or a biometric check; B1 justification: confirms the real account owner is carrying out the login/action, not just anyone who has obtained the password; B1 (or biometric: much harder for an attacker to fake/steal than a second password).
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S26_Detecting_and_Preventing_Threats` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 8 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S27_Relational_Databases.
