# Count the Circles (Bonus Challenge)

- **Domain:** fp
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.42021276595744683
- **Total Submissions:** 188
- **Solved Count:** 79
- **URL:** https://www.hackerrank.com/challenges/count-the-circles

## Problem Statement

You are provided images which contain circles drawn on a homogeneous background.
Your task is to count the number of circles in each image.

**WARNING**
Submissions attempting to arrive at answers without actually using algorithms or image processing, will be disqualified. This refers to cases of hard-coding, generating random numbers, visible hit and trial methods.  

<img src="https://s3.amazonaws.com/hr-challenge-images/7028/1426246157-753a89f4fb-circle10_12.png" title="circle10_12.png" /><img src="https://s3.amazonaws.com/hr-challenge-images/7028/1426246168-eaf83fedd4-circle2_7.png" title="circle2_7.png" /><img src="https://s3.amazonaws.com/hr-challenge-images/7028/1426246172-a47e326338-circle3_9.png" title="circle3_9.png" />

**Input Format**

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represents the pixel-wise values from the images (which were originally in JPG or PNG formats).
The first line will contain the number of rows and columns ($R$ and $C$, respectively), separated by a single space.
Each pixel will be represented by three comma-separated values in the range $0$ to $255$ representing the _Blue_, _Green_, and _Red_ components, respectively. There will be a space between successive pixels in the same row.  

**Constraints**

None of the original JPG or PNG images exceeded 10kB in size.
The 2D grids of pixels representing these images will not exceed 4MB.
No image may contain more than 20 circles. 
The background of each image is reasonably flat and homogeneous, in line with the images displayed in this problem statement. Similarly, the circles are also colored with a fairly uniform shade. Some of the circles, may have an outline. However, different circles, might have different colors. For example - one circle might be red, another blue, another green and so on. It might be the case, that some of the circles, are *slightly* elliptical (i.e, eccentricity differs marginally from 1). None of the circles will overlap, though they might touch at the edges.   



**Sample Input**  
_Note_: This is for the purposes of explanation only. The real inputs will be much larger than this.

	3 3
    0,0,200 0,0,10 10,0,0
    90,90,50 90,90,10 255,255,255
    100,100,88 80,80,80 15,75,255  
    
This is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).
 
**Output Format**

Just one integer - the number of circles in the image.
 
**Sample Output**
(Please note that the sample input shown above does not actually contain any circle!)  
 
     3
 
**The first three sample tests**  

The images shown at the top of this problem statement correspond to the first three sample test cases. The respective outputs for them will be: 12, 7, and 9.
 
**Libraries**  
ML Libraries have been enabled for this challenge. The libraries are listed [here](http://www.hackerrank.com/environment).


## Input Format

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represents the pixel-wise values from the images (which were originally in JPG or PNG formats).
The first line will contain the number of rows and columns ( and , respectively), separated by a single space.
Each pixel will be represented by three comma-separated values in the range  to  representing the Blue, Green, and Red components, respectively. There will be a space between successive pixels in the same row.

## Output Format

Just one integer - the number of circles in the image.

## Constraints

None of the original JPG or PNG images exceeded 10kB in size.
The 2D grids of pixels representing these images will not exceed 4MB.
No image may contain more than 20 circles.
The background of each image is reasonably flat and homogeneous, in line with the images displayed in this problem statement. Similarly, the circles are also colored with a fairly uniform shade. Some of the circles, may have an outline. However, different circles, might have different colors. For example - one circle might be red, another blue, another green and so on. It might be the case, that some of the circles, are slightly elliptical (i.e, eccentricity differs marginally from 1). None of the circles will overlap, though they might touch at the edges.

## Sample Input

Note: This is for the purposes of explanation only. The real inputs will be much larger than this.

3 3
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

This is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88).

## Sample Output

(Please note that the sample input shown above does not actually contain any circle!)

 3

The first three sample tests

The images shown at the top of this problem statement correspond to the first three sample test cases. The respective outputs for them will be: 12, 7, and 9.

Libraries

ML Libraries have been enabled for this challenge. The libraries are listed here.
