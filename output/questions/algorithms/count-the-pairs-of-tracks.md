# Count the Pairs of Tracks

- **Domain:** algorithms
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.33771929824561403
- **Total Submissions:** 228
- **Solved Count:** 77
- **URL:** https://www.hackerrank.com/challenges/count-the-pairs-of-tracks

## Problem Statement

![](http://s28.postimg.org/7vl79t759/track9_2.jpg)    



You are provided pictures of railway tracks. Your task is to count how many pairs of tracks you can identify in each of the images.

A few notes:    
- All the tracks in the images will be **straight**, i.e. no curves, bends etc.    
- There will be no junctions or merges in the tracks either.  
- There may be pictures in which a train is running on the track - however, in such cases a section of the track will be clearly visible in the image (i.e, not blocked or hidden by the train).    



**Input Format**  

The first line of the input will contain two integers **R** and **C** which represent the number of rows and columns of pixels in the image which will be provided.  
A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).  
Each pixel will be represented by three comma separated values in the range 0 to 255 representing the **Blue, Green and Red** components respectively. The will be a space between successive pixels in the same row.  
  
  
**Input Constraints**    
  
1 <= **R** <= 1000    
1 <= **C** <= 1500  
The input files containing the 2D grids of pixels representing these images will not exceed 10MB.    
  
  
**Sample Input**      

This is for the purpose of explanation only. The real inputs will be much larger than this.  

    3 3  
    0,0,200 0,0,10 10,0,0
    90,90,50 90,90,10 255,255,255
    100,100,88 80,80,80 15,75,255  
    
 The first line indicates the number of rows and columns (3x3).  
 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).  
   
   
 **Output Format**      
 
 Just one integer in the range 1 - 10.
 
 **Sample Output**  
 
 (Please note that the sample input shown above does not actually contain any railway tracks!)  
 
     3  
 
 
 **Images used in Sample Inputs**  
 
 These are the images from which the five sample tests have been created. These tests are visible when you hit the "Compile and Test" button.
 
 The images given below, after conversion to the input format provided by us, can be downloaded [from here](http://hr-testcases.s3.amazonaws.com/2554/assets/samples.zip).    
 
 The expected answers to each these are: 1, 1, 2, 5, 2 respectively (i.e., the count of railway tracks).  
 
 **Sample Test Image 1**
 
 <img src="http://s28.postimg.org/rkp8xntyl/track1_1.jpg" width="175" height="100"/> 
 
 **Sample Test Image 2**  
 
 <img src="http://s28.postimg.org/gjz5pr819/track2_1.jpg" width="175" height="100"/>
 
 **Sample Test Image 3**
 
 <img src="http://s28.postimg.org/5jd7c7ujx/track3_2.jpg" width="175" height="100"/> 
 
 **Sample Test Image 4**
 
 <img src="http://s28.postimg.org/84irzqjxp/track6_5.jpg" width="175" height="100" />
 
 **Sample Test Image 5**  
 
 <img src="http://s28.postimg.org/7vl79t759/track9_2.jpg" width="175" height="100"/>
 
 **A Note on the Test Cases and Sample Tests**  

The test cases have been generated from the fifteen images out of which the first 5 have been shown in the pictures at the top. These five test cases, are also available as visible, sample test cases when you "Compile and Test" your solution. The hidden test cases are largely of similar complexity, or just a notch harder.   

**Libraries**  

Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed [here](http://www.hackerrank.com/environment). Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site.  




## Input Format

The first line of the input will contain two integers R and C which represent the number of rows and columns of pixels in the image which will be provided.

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).

Each pixel will be represented by three comma separated values in the range 0 to 255 representing the Blue, Green and Red components respectively. The will be a space between successive pixels in the same row.

Input Constraints

1 <= R <= 1000

1 <= C <= 1500

The input files containing the 2D grids of pixels representing these images will not exceed 10MB.

## Output Format

Just one integer in the range 1 - 10.

## Sample Input

This is for the purpose of explanation only. The real inputs will be much larger than this.

3 3
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The first line indicates the number of rows and columns (3x3).

 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).

## Sample Output

(Please note that the sample input shown above does not actually contain any railway tracks!)

 3

Images used in Sample Inputs

These are the images from which the five sample tests have been created. These tests are visible when you hit the "Compile and Test" button.

The images given below, after conversion to the input format provided by us, can be downloaded from here.

The expected answers to each these are: 1, 1, 2, 5, 2 respectively (i.e., the count of railway tracks).

Sample Test Image 1

Sample Test Image 2

Sample Test Image 3

Sample Test Image 4

Sample Test Image 5

A Note on the Test Cases and Sample Tests

The test cases have been generated from the fifteen images out of which the first 5 have been shown in the pictures at the top. These five test cases, are also available as visible, sample test cases when you "Compile and Test" your solution. The hidden test cases are largely of similar complexity, or just a notch harder.

Libraries

Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed here. Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site.
