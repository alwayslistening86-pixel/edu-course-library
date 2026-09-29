# S16_Representing_Images - Lesson: Representing images

## Goal
The learner describes what a pixel is, how a bitmap represents an image using pixels and colour depth, and calculates bitmap image file sizes from pixel count and colour depth.

## Syllabus items taught here
- 3.3.6 - Representing images

## How to teach this
Ask the learner to imagine a photo as a huge grid of tiny coloured squares -- each square is a pixel. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.3.6 Representing images
A **pixel** ('picture element') is the smallest single point of colour in a digital image; a bitmap image is stored as a grid of pixels, so many pixels together (its **resolution**, e.g. width x height) build up the whole picture. **Colour depth** is the number of bits used to represent the colour of each pixel; with n bits per pixel, 2^n different colours can be represented (e.g. 8-bit colour depth gives 2^8 = 256 possible colours; 24-bit "true colour" gives 2^24 = 16,777,216 colours). A bitmap file's size in bits is: **image size (bits) = width (pixels) x height (pixels) x colour depth (bits per pixel)**; dividing by 8 converts to bytes, and by 1,000 (repeatedly) converts to KB/MB. *Worked example:* an image 200 pixels wide by 100 pixels high, with a colour depth of 24 bits per pixel: pixel count = 200 x 100 = 20,000; file size = 20,000 x 24 = 480,000 bits = 60,000 bytes = 60 KB. Both a higher resolution (more pixels) and a greater colour depth (more bits per pixel) increase file size; conversely, binary data can also be read back and rebuilt into the corresponding grid of coloured pixels.

## Explicitly not here
Representing sound (rather than images) is S17.
