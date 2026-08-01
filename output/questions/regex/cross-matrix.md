# Cross Matrix

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 120
- **Success Ratio:** 0.5531914893617021
- **Total Submissions:** 141
- **Solved Count:** 78
- **URL:** https://www.hackerrank.com/challenges/cross-matrix

## Problem Statement

You are given a *N* * *N* matrix, *U*. You have to choose 2 sub-matrices A and B made of only 1s of *U*, such that, they have at least 1 cell in common, and each matrix is not completely engulfed by the other, i.e., 

If *U* is of the form 

![image-U](https://s3.amazonaws.com/hr-assets/0/1526566968-bc96620304-image-u.png)

and *A* is of the form

![image-A](https://s3.amazonaws.com/hr-assets/0/1526566750-388f1c7813-image-A.png)

and *B* is of the form

![image-B](https://s3.amazonaws.com/hr-assets/0/1526566997-2b849f77a5-image-B.png)

then, there exists atleast 1 a<sub>i, j</sub> : a<sub>i, j</sub> &in; *A* and a<sub>i,j</sub> &in; *B*    
then, there exists atleast 1 a<sub>i1, j1</sub> : a<sub>i1, j1</sub> &in; *A* and a<sub>i1,j1</sub> &notin; *B*  
then, there exists atleast 1 a<sub>i2, j2</sub> : a<sub>i2, j2</sub> &in; *B* and a<sub>i2,j2</sub> &notin; *A*  
a<sub>x,y</sub> = 1 &forall; a<sub>x,y</sub> &in; *A*  
a<sub>x,y</sub> = 1 &forall; a<sub>x,y</sub> &in; *B*  

How many such (*A*, *B*) exist?

**Input Format**  
The first line of the input contains a number *N*.  
*N* lines follow, each line containing *N* integers (0/1) **NOT** separated by any space.

**Output Format**  
Output the total number of such (A, B) pairs. If the answer is greater than or equal to 10<sup>9</sup> + 7,
then print answer modulo (%) 10<sup>9</sup> + 7.

**Constraints**  

2 &le; *N* &le; 1500  
a<sub>i,j</sub> &in; [0, 1] : 0 &le; i, j &le; N - 1

**Sample Input**

    4
    0010
    0001
    1010
    1110

**Sample Output**

    10


**Explanation**

X means the common part of A and B. <br>
We can swap A and B to get another answer. 

    0010
    0001
    A010
    XB10
    
    0010
    0001
    A010
    XBB0
    
    0010
    0001
    10A0
    1BX0
    
    0010
    0001
    10A0
    BBX0
    
    0010
    0001
    1010
    AXB0


**TimeLimits**

Time limit for this challenge is mentioned [here](http://hr-testcases.s3.amazonaws.com/2492/timelimit.json)

## Input Format

The first line of the input contains a number N.

N lines follow, each line containing N integers (0/1) NOT separated by any space.

## Output Format

Output the total number of such (A, B) pairs. If the answer is greater than or equal to 109 + 7,
then print answer modulo (%) 109 + 7.

## Constraints

2 ≤ N ≤ 1500

ai,j ∈ [0, 1] : 0 ≤ i, j ≤ N - 1

## Sample Input

0010
0001
1010
1110

## Explanation

X means the common part of A and B.

We can swap A and B to get another answer.

0010
0001
A010
XB10

0010
0001
A010
XBB0

0010
0001
10A0
1BX0

0010
0001
10A0
BBX0

0010
0001
1010
AXB0

TimeLimits

Time limit for this challenge is mentioned here
