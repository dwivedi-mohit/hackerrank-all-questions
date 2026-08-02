# Shape Detection

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 40
- **Success Ratio:** 0.20853080568720378
- **Total Submissions:** 422
- **Solved Count:** 88
- **URL:** https://www.hackerrank.com/challenges/shape-detection

## Problem Statement

You are provided images which contain colored shapes on backgrounds which are quite uniform in color and texture. Your task is to identify whether the shape in the picture is a triangle, box, circle or ellipse. A shape which is identified as either a square or a rectangle is considered as a box.  

![](https://s3.amazonaws.com/hr-testcases/1680/assets/shapes.png)


**Input Format**  
A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).  
Each pixel will be represented by three comma separated values in the range 0 to 255 representing the **Blue, Green and Red** components respectively. The will be a space between successive pixels in the same row.  

**Input Constraints**  
None of the original JPG or PNG images exceeded 10kB in size.
The 2D grids of pixels representing these images will not exceed 1MB.  

**Sample Input**  

This is for the purpose of explanation only. The real inputs will be much larger than this.  

    0,0,200 0,0,10 10,0,0
    90,90,50 90,90,10 255,255,255
    100,100,88 80,80,80 15,75,255  
    
 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88). 
 
 **Output Format**  
 Just one word: 'triangle', 'box', 'circle' or 'ellipse'. Do NOT include the single quote marks.    
 
 **Sample Output**  (Please note that the sample input shown above does not actually contain a box!)  
 
     box  
 
 
 **A Note on the Test Cases and Sample Tests**  

The test cases have been generated from the fifteen images shown in the picture at the top. The two test cases which run as sample test cases when you compile and test, are based on images 01, 07 and 13 respectively.  

Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed [here](http://www.hackerrank.com/environment). Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site. 


## Input Format

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).

Each pixel will be represented by three comma separated values in the range 0 to 255 representing the Blue, Green and Red components respectively. The will be a space between successive pixels in the same row.

Input Constraints

None of the original JPG or PNG images exceeded 10kB in size.
The 2D grids of pixels representing these images will not exceed 1MB.

## Output Format

Just one word: 'triangle', 'box', 'circle' or 'ellipse'. Do NOT include the single quote marks.

Sample Output  (Please note that the sample input shown above does not actually contain a box!)

 box

A Note on the Test Cases and Sample Tests

The test cases have been generated from the fifteen images shown in the picture at the top. The two test cases which run as sample test cases when you compile and test, are based on images 01, 07 and 13 respectively.

Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed here. Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site.

## Sample Input

This is for the purpose of explanation only. The real inputs will be much larger than this.

0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
