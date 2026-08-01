# The Captcha Cracker

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.6455186304128903
- **Total Submissions:** 993
- **Solved Count:** 641
- **URL:** https://www.hackerrank.com/challenges/the-captcha-cracker

## Problem Statement

*Note: No advanced computer vision background is required to solve this challenge. A simple understanding of the 256 x 256 x 256 RGB color space is sufficient.*    
    

A website uses Captchas on a form in order to keep the web-bots away. However, the captchas it generates, are quite similar each time:  

	- the number of characters remains the same each time  
    - the font and spacing is the same each time  
    - the background and foreground colors and texture, remain largely the same
    - there is no skew in the structure of the characters.  
    - the captcha generator, creates strictly 5-character captchas, and each of the characters is either an upper-case character (A-Z) or a numeral (0-9)/.  
    
    
Here, take a look at some of the captcha images on the form. As you can see, they resemble each other very much - just that the characters on each of them are different.       

![image](https://s3.amazonaws.com/hr-assets/0/1540818800-f4fcfa304d-input00.jpg)

![image](https://s3.amazonaws.com/hr-assets/0/1540818825-7e1b5572a6-input02.jpg)

![image](https://s3.amazonaws.com/hr-assets/0/1540818837-d2e6daa345-input01.jpg)

![image](https://s3.amazonaws.com/hr-assets/0/1540818850-4e736e6a24-input04.jpg)

You are provided a set of twenty-five captchas, such that, each of the characters A-Z and 0-9 occur at least once in one of the Captchas' text. From these captchas, you can identify texture, nature of the font, spacing of the font, morphological characteristics of the letters and numerals, etc. Download this sample set [from here](http://hr-testcases.s3.amazonaws.com/2587/assets/sampleCaptchas.zip) for the purpose of creating an offline model for this task. 
  


**Given a set of unseen captchas on the same web form, your task is to identify the text on each of the captchas.**  

  

  
  

   

















## Input Format

The first line of the input will contain two integers, **R** and **C**, which represent the number of rows and the number of columns of image pixels respectively.  
A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel-wise values from the images (which were originally in JPG or PNG formats).  
Each pixel will be represented by three comma separated values in the range 0 to 255 representing the **Blue, Green and Red** components respectively. There will be a space between successive pixels in the same row. 

## Output Format

For each input file, the output should contain exactly one line containing a 5-character token, which represents the text of the captcha. 

## Constraints

All images are of similar sizes.  

**R** =  30     
**C** =  60   
The input files containing the 2D grids of pixels representing these images will not exceed 10MB. 
All the captchas will be visually similar to the captcha images displayed above.  

## Sample Input

This is for the purpose of explanation only. The real inputs will be larger than this (and will all contain 30 rows and 60 columns).

3 3
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The first line indicates the number of rows and columns (3x3).

 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).

## Sample Output

This corresponds to the first of the sample images displayed in the problem statement.

SZ1KI

Sample Output (2)

This corresponds to the second of the sample images displayed in the problem statement.

ZR8UG

Sample Output (3)

This corresponds to the third of the sample images displayed in the problem statement.

J3GM4

## Explanation

Sample Images and TestCases

You are provided a set of twenty-five captchas, such that each of the characters A-Z and 0-9 occur at least once in one of the Captchas' text. From these captchas, you can identify texture, nature of the font, spacing of the font, morphological characteristics of the letters and numerals, etc.

Download this sample set from here for the purpose of creating an offline model for this task.

Contents of the sample file above

(a) 25 captcha images (input00.jpg to input24.jpg)

(b) The captcha images converted to our input format specified below (input00.txt to input24.txt)

(c) The expected output text for each of these images (output00.txt to output24.txt)

(d) These correspond to the 25 sample test cases which are run on hitting the Compile & Test button.

These files will not be available while the program is being executed on our platform. Your task is to extract relevant information from the sample images, and transform them into a model or a data-structure embedded within your program, which can then help identify the characters on similar captcha images.

Libraries

No special libraries are really needed to solve this challenge. However, for the convenience of those who might be interested in using extra tools, libraries available in our Machine Learning/Real Data challenges will be enabled and are listed here. Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site.
