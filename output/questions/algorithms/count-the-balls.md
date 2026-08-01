# Sportsware: Ball Spotting

- **Domain:** algorithms
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.2681564245810056
- **Total Submissions:** 179
- **Solved Count:** 48
- **URL:** https://www.hackerrank.com/challenges/count-the-balls

## Problem Statement

  
![](https://s3.amazonaws.com/hr-testcases/1681/assets/img12.jpg)  
 
You are given an image which contains N balls in it. These could be any popular kind of balls such as tennis, cricket, football, billiards or snooker balls, etc. The pictures have been clicked from a variety of different angles, and the balls might be of different colors. It is also possible that some balls are eclipsed by others, but none of the images contain a ball which has more than half its face eclipsed.  

Count the number of balls you can spot in the image, i.e. find the value of N. Every image has a ball and N will not exceed 20.  

![](https://s3.amazonaws.com/hr-testcases/1681/assets/balls.png)

**Input Format**  
A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).  
Each pixel will be represented by three comma separated values in the range 0 to 255 representing the **Blue, Green and Red** components respectively. The will be a space between successive pixels in the same row.  

**Input Constraints**  
None of the original JPG or PNG images exceeded 50kB in size.
The 2D grids of pixels representing these images will not exceed 5MB.

**Sample Input**  

This is for the purpose of explanation only. The real inputs will be much larger than this.  

    0,0,200 0,0,10 10,0,0
    90,90,50 90,90,10 255,255,255
    100,100,88 80,80,80 15,75,255  
    
 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88). 
 
 **Output Format**  
 Just one integer in the range 1-20.
 
 **Sample Output**  (Please note that the sample input shown above does not actually contain a single ball!)  
 
     3  
 
 
 **A Note on the Test Cases and Sample Tests**  

The test cases have been generated from a set of twenty images, out of which ten images have been shown in the picture at the top. The rest of the test cases are also designed to be at a comparable level of difficulty, perhaps a notch harder.  The four test cases which run as sample test cases when you compile and test, are based on images 01, 02, 08 and 10 respectively.  

**Libraries**  

Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed [here](http://www.hackerrank.com/environment). Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site. 


## Input Format

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).

Each pixel will be represented by three comma separated values in the range 0 to 255 representing the Blue, Green and Red components respectively. The will be a space between successive pixels in the same row.

Input Constraints

None of the original JPG or PNG images exceeded 50kB in size.
The 2D grids of pixels representing these images will not exceed 5MB.

## Output Format

Just one integer in the range 1-20.

Sample Output  (Please note that the sample input shown above does not actually contain a single ball!)

 3

A Note on the Test Cases and Sample Tests

The test cases have been generated from a set of twenty images, out of which ten images have been shown in the picture at the top. The rest of the test cases are also designed to be at a comparable level of difficulty, perhaps a notch harder.  The four test cases which run as sample test cases when you compile and test, are based on images 01, 02, 08 and 10 respectively.

Libraries

Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed here. Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site.

## Sample Input

This is for the purpose of explanation only. The real inputs will be much larger than this.

0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).
