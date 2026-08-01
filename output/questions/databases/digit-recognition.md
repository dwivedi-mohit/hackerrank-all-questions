# Digit Recognition

- **Domain:** databases
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.15384615384615385
- **Total Submissions:** 78
- **Solved Count:** 12
- **URL:** https://www.hackerrank.com/challenges/digit-recognition

## Problem Statement

Given an image with a digit drawn on it, identify the digit, using geometric properties or otherwise.   

**Input Format**  

The first line of the input will contain two integers, **R** and **C**, which represent the number of rows and the number of columns of image pixels respectively.  
A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel-wise values from the images (which were originally in JPG or PNG formats).  
Each pixel will be represented by three comma separated values in the range 0 to 255 representing the **Blue, Green and Red** components respectively. There will be a space between successive pixels in the same row.  
  
  
**Input Constraints**  

The text representation of the image (i.e, the grid with pixel details) will not exceed a total of 6MB.  

There is no collected training data available - however, you may build  an offline model if required. Regular machine-learning mode libraries will be available.  

**Output Format**  

Exactly one digit (the one in the provided image).  
 
**Four Sample Images (from which the inputs have been generated)**  

The sample input files corresponding to these images may be downloaded [from here](https://dl.dropboxusercontent.com/u/81420380/samples.zip).  
The order in which the files are provided is same as the ordering of the images here. 
  

*Corresponding to the first sample input*  
  
    
      

![](http://s29.postimg.org/4qo9f6e07/img00_5.png)  
  
    
    
*Corresponding to the second sample input*  
  
    
      
![](http://s24.postimg.org/hi08e6jwl/img02_1.jpg)

  
    
*Corresponding to the third sample input*  
  
    
      

![](http://s24.postimg.org/f38ctr3np/img03_7.png)  
  
    
    
*Corresponding to the fourth sample input*  
  
    
          

![](http://s24.postimg.org/wujz87j2d/img11_3.jpg)  

 
 
  
**Sample Input**      

This is for the purpose of explanation only. The real inputs will be larger than this.  

    3 3  
    0,0,200 0,0,10 10,0,0
    90,90,50 90,90,10 255,255,255
    100,100,88 80,80,80 15,75,255  
    
 The first line indicates the number of rows and columns (3x3).  
 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).  

**Output Format**  
For each input file, output one **one digit** (the digit on the provided image).   

**Sample Output (1)**  
*This corresponds to the first of the sample images displayed in the problem statement.*

    5
  

**Sample Output (2)**  
*This corresponds to the second of the sample images displayed in the problem statement.*  

    1

**Sample Output (3)**  
*This corresponds to the third of the sample images displayed in the problem statement.*

    7
    
**Sample Output (4)**  
*This corresponds to the fourth of the sample images displayed in the problem statement.*  

    3
   

## Input Format

The first line of the input will contain two integers, R and C, which represent the number of rows and the number of columns of image pixels respectively.

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel-wise values from the images (which were originally in JPG or PNG formats).

Each pixel will be represented by three comma separated values in the range 0 to 255 representing the Blue, Green and Red components respectively. There will be a space between successive pixels in the same row.

Input Constraints

The text representation of the image (i.e, the grid with pixel details) will not exceed a total of 6MB.

There is no collected training data available - however, you may build  an offline model if required. Regular machine-learning mode libraries will be available.

## Output Format

Exactly one digit (the one in the provided image).

Four Sample Images (from which the inputs have been generated)

The sample input files corresponding to these images may be downloaded from here.

The order in which the files are provided is same as the ordering of the images here.

Corresponding to the first sample input

Corresponding to the second sample input

Corresponding to the third sample input

Corresponding to the fourth sample input

## Sample Input

This is for the purpose of explanation only. The real inputs will be larger than this.

3 3
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The first line indicates the number of rows and columns (3x3).

 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).
