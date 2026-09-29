# S30_Friction - Test: Friction

## How to run this
A real checkpoint in the style of OCR's papers: structured questions with marks shown. Give the whole test at once, with no hints; the learner shows full working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A block of mass 5 kg is on the point of sliding down a rough plane inclined at 20°. Find μ. [3 marks]
2. A sledge of mass 12 kg is pulled across rough horizontal ground by a rope at 30° above the horizontal with tension 50 N. μ = 0.3. Find the acceleration. [5 marks]
3. A particle is projected up a rough slope inclined at 30° with speed 8 m/s; μ = 0.25. Find how far it travels up the slope before coming to rest. [5 marks]
4. Determine whether the particle in the previous question then slides back down the slope, justifying your answer. [2 marks]

## Answer key (for the tutor only)
1. [3] M1 R = 5g cos 20°, F = 5g sin 20°; M1 F = μR; A1 μ = tan 20° = 0.364.
2. [5] M1 R = 12g - 50sin 30° = 92.6 N; M1 F = 0.3R; A1 F = 27.78 N; M1 50cos 30° - F = 12a; A1 a = 1.293 m s^-2.
3. [5] M1 deceleration g(sin 30° + 0.25cos 30°); A1 7.022 m s^-2; M1 v^2 = u^2 + 2as; A1 s = 4.56 m; B1 correct direction of friction (down the slope).
4. [2] M1 compares tan 30° = 0.577 with μ = 0.25 (or mg sin 30° with μmg cos 30°); A1 tan 30° > 0.25, so the component of weight down the slope exceeds the maximum friction: it slides back down.

## Grading
Apply `rubric.json`'s `stage_rubrics.S30_Friction` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S31_Moments.
