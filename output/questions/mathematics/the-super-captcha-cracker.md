# The Super Captcha Cracker

- **Domain:** mathematics
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.0
- **Total Submissions:** 117
- **Solved Count:** 0
- **URL:** https://www.hackerrank.com/challenges/the-super-captcha-cracker

## Problem Statement

As a warmup for this challenge, you might find it useful to go through [this captcha reader challenge and its editorial](https://www.hackerrank.com/challenges/the-captcha-cracker). Keep in mind that the requirements for this challenge are more advanced, and it will involve deeper application of principles of image processing, digital geometry, and certain elements of machine learning. 

----

A website uses Captchas in a form in order to keep web-bots away; however, the Captchas it generates do have certain common features:  

- Each Captcha contains exactly $5$ characters.
- Each character is an uppercase letter A-Z  
- These characters are skewed, stretched, and rotated, but are largely based on a very limited set of font types.
- There is a squiggle cutting through one or more of the characters.
- The texture and color of the Captcha's background is always similar.
- The foreground colors used for the characters and the squiggle are always restricted to a small group of colors and shades.
    
Take a look at some of the captcha images in the form and understand how the above mentioned properties hold true. 
    
![](http://s11.postimg.org/i6c38cdv3/test196.jpg)  
![](http://s11.postimg.org/7akpczsxb/test197.jpg)    
![](http://s11.postimg.org/7xjm2iptb/test198.jpg)  
![](http://s22.postimg.org/z4p7kkjwt/test199.jpg)
![](http://s11.postimg.org/f21fbjx2n/test200.jpg)  

You must build a model to read other captchas on the same web form. 
You are provided a set of $150$ Captchas with the image, the input (an $RGB$ matrix corresponding to the image) and the output (the text in the Captcha). From these Captchas, you may build an offline model to read other Captchas in the same form, based on principles of image processing, machine learning, and computer vision algorithms related to image segmentation and digital geometry. Download this sample set [from here](https://www.dropbox.com/s/puj1blk92ecwzic/captchaTrainingSet.zip?dl=0) for the purpose of creating an offline model for this task.  
  
The above set has $150$ captchas. *outputN.txt* corresponds to the expected output value for the input file given by *inputN.txt*, which has been generated from the captcha *testN.gif*.

Given a set of $50$ unseen captchas in the same web form, identify the text in each of the Captchas.  	

As the sample set has been annotated and created manually, it is indeed possible that a few discrepencies may have crept in. If you do spot any such issue where there is a mismatch between the output file, input file and the image - do drop a note in the forum comments and we will make fixes as required. 

----

**Sample Images and Test Cases**  

These files *will not be available* while the program is being executed on our platform. Your task is to extract relevant information from the sample images and transform them into a model or a data-structure embedded within your program, which can then help identify the characters on similar captcha images.  

**Libraries**  

No special libraries are really needed to solve this challenge. However, for the convenience of those who might be interested in using extra tools, libraries available in our Machine Learning/Real Data challenges will be enabled and are listed [here](http://www.hackerrank.com/environment). Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). If you plan on developing your solution locally/offline and then uploading it to our site, please try importing the library and functions and cross-check whether they work in our online editor.

## Input Format

The first line contains $2$ space-separated integers, $R$ and $C$, denoting the respective number of rows and columns of pixels in the image.

The $R$ subsequent lines describe the $2D$ grid representing the pixel-wise values from the images (which were originally in *JPG* or *PNG* formats). 
Each line contains $C$ pixels, and each pixel is represented by three comma-separated values in the range from $0$ to $255$ denoting the respective *Blue*, *Green*, and *Red* components. There is a space between successive pixels in the same row.

## Output Format

For row of input, print a line containing a $5$-character token representing the Captcha's text.

## Constraints

- $\textit{All images are of similar sizes.}$
- $R =  50$
- $C =  170   $
- $\textit{The inputs containing the 2D grids of pixels representing these images will not exceed 100kB.}$

## Sample Input

This is for the purpose of explanation only. The real inputs will be larger than this (and will all contain the specified number of rows and columns,  and  respectively).

3 3
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The first line indicates the number of rows and columns (3x3).

 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).

## Sample Output

Captcha 0

This corresponds to the first sample image in the problem statement:

VSDFD

Captcha 1

This corresponds to the second sample image in the problem statement:

CBAOH

Captcha 2

This corresponds to the third sample image in the problem statement:

TZRGV

You may make no more than 15 submissions for this problem, during the contest.
Also, submissions to this challenge may be rerun with additional tests at the end.
