# Count the Faces

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.38341968911917096
- **Total Submissions:** 193
- **Solved Count:** 74
- **URL:** https://www.hackerrank.com/challenges/count-the-faces

## Problem Statement

You are provided with images of people at meetings, gatherings, group photos etc.
Count the number of faces you can spot in each image. 
There will be no more than $15$ faces in each of the images. Assume that half or more of each face will be visible. 

Here are the first three images corresponding to the 3 sample test cases which are executed on hitting "run".  

<img src="https://s3.amazonaws.com/hr-challenge-images/15190/1450077998-f1789e4822-input00_2.jpg" title="input00_2.jpg" />  
<img src="https://s3.amazonaws.com/hr-challenge-images/15190/1450077990-5cffc22107-input01_3.jpg" title="input01_3.jpg" />  
<img src="https://s3.amazonaws.com/hr-challenge-images/15190/1450078013-2b033f57ed-input02_5.jpg" title="input02_5.jpg" />  


## Input Format

The first line of input will contain two integers, $R$ and $C$, representing the number of rows and columns of image pixels, respectively. 

A 2D grid of pixel values will be provided (in regular text format through STDIN) that represent the pixel-wise values from the images. The images were originally in JPG or PNG formats. 

Each pixel will be represented by three comma separated values denoting the *Blue, Green* and *Red* components, respectively. The pixel values will be in the range $0$ to $255$. There will be a space between consecutive pixels in the same row.  

No input test case exceeds 15MB in size, most are within 5MB and many are less than 1MB. So you may gradually iterate on your solution to handle larger and more complex cases. Take care to account for very different kinds of faces!  

## Output Format

Output a single integer, the number of faces spotted in the provided image.

## Sample Input

This example is for explanation only. The real inputs will be larger than this and will contain  rows and  columns.

3 3
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

The first line indicates the number of rows and columns x.
The above is an image represented by x pixels. For each pixel, the Blue, Green and Red values are provided, separated by commas.

The top left pixel has Blue , Green , Red .

The top right pixel has Blue , Green , Red .

The bottom right pixel has Blue , Green , Red .

The bottom left pixel has Blue , Green , Red .
