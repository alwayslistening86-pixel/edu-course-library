# S16_Representing_Images - Test: Representing images

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Define the term pixel. [1 mark]
2. An image is 120 pixels wide by 80 pixels high, using a colour depth of 8 bits per pixel. Calculate the file size of this image in bytes. [3 marks]
3. Explain how increasing an image's colour depth from 8 bits to 16 bits per pixel affects both the number of colours available and the file size. [3 marks]
4. An image with a colour depth of 24 bits has a file size of 90000 bytes. Calculate how many pixels it contains. [3 marks]
5. Which change to a bitmap image would increase its file size? Choose every correct option.
   A. increasing the colour depth
   B. reducing the resolution
   C. reducing the colour depth
   D. compressing it using RLE

## Answer key (for the tutor only)
1. [1] B1 the smallest single point of colour in a digital image.
2. [3] M1 pixel count = 120 x 80 = 9,600; M1 bits = 9,600 x 8 = 76,800; A1 bytes = 9,600.
3. [3] B1 number of colours rises from 2^8 = 256 to 2^16 = 65,536 (far more colours can be shown); B1 file size doubles, because each pixel now needs twice as many bits to store its colour; B1 (both) at the same resolution, so every pixel's storage requirement individually doubles.
4. [3] M1 bits = 90000 x 8 = 720,000; M1 pixels = 720,000 / 24; A1 = 30,000 pixels.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S16_Representing_Images` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S17_Representing_Sound.
