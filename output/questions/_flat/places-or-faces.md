# Places or Faces?

---

| Field | Value |
|---|---|
| **Slug** | `places-or-faces` |
| **Domain** | ai |
| **Difficulty** | Advanced |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/places-or-faces |

---

## Preview

Given the data from a set of images, can you identify which ones are portraits or faces of people, and which ones are pictures of places or monuments? - 100 points

## Problem Statement

You are provided the pixel values from a set of images. These images may belong to either of these classes:

(1) **Portraits or faces of people**. The object in focus is a person and there is just one clear face visible in each of these images.   

(2) **Images of landscapes, city skylines, etc.** - places, building or monuments.


Identify the two classes of images as 'face' or 'place' respectively.


![Alt text](https://s3.amazonaws.com/hr-testcases/1635/hackerrank_dip1.png)


**Input Format**

A 2D Grid of pixel values will be provided (in regular text format through STDIN), which represent the pixel wise values from the images (which were originally in JPG or PNG formats).

Each pixel will be represented by three comma separated values in the range 0 to 255 representing the **Blue, Green and Red** components respectively. The will be a space between successive pixels in the same row.


**Input Constraints**

None of the original JPG or PNG images exceeded 150kB in size.
The 2D grids of pixels representing these images will not exceed 5MB.


**Sample Input**


This is for the purpose of explanation only. The real inputs will be much larger than this.


    0,0,200 0,0,10 10,0,0
    90,90,50 90,90,10 255,255,255
    100,100,88 80,80,80 15,75,255

  

 The above is an image represented by 3x3 pixels. For each pixel the Blue, Green and Red values are provided, separated by commas.
 The top left pixel has (Blue=0,Green=0,Red=200). The top-right pixel has (Blue=10,Green=0,Red=0). The bottom-right pixel has (Blue=15,Green=75,Red=255). The bottom-left pixel has (Blue=100,Green=100, Red=88). 
 
 **Output Format**

 Just one word: 'face' or 'place'. Do NOT include the single quote marks.

 
 **Sample Output**  (Please note that the sample input shown above does not actually contain a face!)

 
     face
 
 
 **A Note on the Test Cases and Sample Tests**


The test cases have been generated from the 22 images shown in the picture at the top. The two test cases which run as sample test cases when you compile and test, are the pictures of Abraham Lincoln and that of a lake in Bangalore, i.e. 'face' and 'place' respectively. These have been generated from the first 2 thumbnails in the collection of thumbnails shown at the top of this problem statement.

**Libraries**


Libraries available in our Machine Learning/Real Data challenges will be enabled for this contest and are listed [here](http://www.hackerrank.com/environment). Please note, that occasionally, a few functions or modules might not work in the constraints of our infrastructure. For instance, some modules try to run multiple threads (and fail). So please try importing the library and functions and cross checking if they work in our online editor in case you plan to develop a solution locally, and then upload to our site.

## Sample Tests

### Test 1

```
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255
```

### Test 2

```
face
```
