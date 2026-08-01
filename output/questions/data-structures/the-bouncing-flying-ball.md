# The Bouncing Flying Ball

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.8294117647058824
- **Total Submissions:** 340
- **Solved Count:** 282
- **URL:** https://www.hackerrank.com/challenges/the-bouncing-flying-ball

## Problem Statement



Sergey and Chen are locked in a rectangular box of Dimension L\*W\*H. Evil Larry has put a machine which is located at a point inside the box (p,q,r) which starts shooting balls in every direction (dx,dy,dz) where 

-N &le; dx, dy, dz &le; N except (0, 0, 0) 

such that the ball goes through (p, q, r) -> (p + dx, q + dy, r + dz) -> (p + 2dx, q + 2dy, r + 2dz) and so on. 

so, a total of (2N + 1)<sup>3</sup> - 1 balls are fired. Sergey is standing at (a,b,c) and Chen is standing at (d,e,f). Provided all the balls follow reflection property and have constant velocity and gravity is not taken into account, can you tell how many balls are caught by Sergey and Chen? Sergey and Chen can catch the ball if it passes through the point at which they are standing. 

**Input Format**  
The first line contains the number of test cases, T lines follow, each containing a testcase.  
Each testcase contains 13 integers in the following order 

    L W H a b c d e f p q r N

**Output Format**  
For each test case please output two integers indicating the number of balls that are caught by Sergey and C, respectively.

**Constraints**  
T = 1  
1 &le; L, W, H, a, b, c, d, e, f, p, q, r, N &le; 50  

**Sample Input**

    1
    3 3 3 1 1 1 1 1 2 2 2 2 1

**Sample Output**

    8 4

**Explanation**

Here, L, W, H  = (3, 3, 3), Sergey is at (1, 1, 1) and Chen is at (1, 1, 2) and the machine Larry put is at (2, 2, 2).   
Balls are thrown at -1 &le; x, y, z &le; 1 from (2, 2, 2).  

+ (-1, -1, -1): (2, 2, 2)->(1, 1, 1) Sergey
+ (-1, -1, 0): (2, 2, 2)->(1, 1, 2) Chen
+ (-1, -1, 1): (2, 2, 2)->(1, 1, 3)->(0, 0, 2)->(1, 1, 1) Sergey
+ (-1, 0, -1): (2, 2, 2)->(1, 2, 1)->(0, 2, 0)->(1, 2, 1)->(2, 2, 2)->(3, 2, 3)->...
+ (-1, 0, 0): (2, 2, 2)->(1, 2, 2)->(0, 2, 2)->(1, 2, 2)->(2, 2, 2)->(3, 2, 2)->...
+ (-1, 0, 1): (2, 2, 2)->(1, 2, 3)->(0, 2, 2)->(1, 2, 1)->(2, 2, 0)->(3, 2, 1)->...
+ (-1, 1, -1): (2, 2, 2)->(1, 3, 1)->(0, 2, 0)->(1, 1, 1) Sergey
+ (-1, 1, 0): (2, 2, 2)->(1, 3, 2)->(0, 2, 2)->(1, 1, 2) Chen
+ (-1, 1, 1): (2, 2, 2)->(1, 3, 3)->(0, 2, 2)->(1, 1, 1) Sergey
+ (0, *, *): x-coordinate never changed
+ (1, -1, -1): (2, 2, 2)->(3, 1, 1)->(2, 0, 0)->(1, 1, 1) Sergey
+ (1, -1, 0): (2, 2, 2)->(3, 1, 2)->(2, 0, 2)->(1, 1, 2) Chen
+ (1, -1, 1): (2, 2, 2)->(3, 1, 3)->(2, 0, 2)->(1, 1, 1) Sergey
+ (1, 0, -1): (2, 2, 2)->(3, 2, 1)->(2, 2, 0)->(1, 2, 1)->(0, 2, 2)->...
+ (1, 0, 0): (2, 2, 2)->(3, 2, 2)->(2, 2, 2)->(1, 2, 2)->(0, 2, 2)->...
+ (1, 0, 1): (2, 2, 2)->(3, 2, 3)->(2, 2, 2)->(1, 2, 1)->(0, 2, 0)->...
+ (1, 1, -1): (2, 2, 2)->(3, 3, 1)->(2, 2, 0)->(1, 1, 1) Sergey
+ (1, 1, 0): (2, 2, 2)->(3, 3, 2)->(2, 2, 2)->(1, 1, 2) Chen
+ (1, 1, 1): (2, 2, 2)->(3, 3, 3)->(2, 2, 2)->(1, 1, 1) Sergey

## Input Format

The first line contains the number of test cases, T lines follow, each containing a testcase.

Each testcase contains 13 integers in the following order

L W H a b c d e f p q r N

## Output Format

For each test case please output two integers indicating the number of balls that are caught by Sergey and C, respectively.

## Constraints

T = 1

1 ≤ L, W, H, a, b, c, d, e, f, p, q, r, N ≤ 50

## Sample Input

3 3 3 1 1 1 1 1 2 2 2 2 1

## Sample Output

8 4

## Explanation

Here, L, W, H  = (3, 3, 3), Sergey is at (1, 1, 1) and Chen is at (1, 1, 2) and the machine Larry put is at (2, 2, 2).

Balls are thrown at -1 ≤ x, y, z ≤ 1 from (2, 2, 2).

- (-1, -1, -1): (2, 2, 2)->(1, 1, 1) Sergey

- (-1, -1, 0): (2, 2, 2)->(1, 1, 2) Chen

- (-1, -1, 1): (2, 2, 2)->(1, 1, 3)->(0, 0, 2)->(1, 1, 1) Sergey

- (-1, 0, -1): (2, 2, 2)->(1, 2, 1)->(0, 2, 0)->(1, 2, 1)->(2, 2, 2)->(3, 2, 3)->...

- (-1, 0, 0): (2, 2, 2)->(1, 2, 2)->(0, 2, 2)->(1, 2, 2)->(2, 2, 2)->(3, 2, 2)->...

- (-1, 0, 1): (2, 2, 2)->(1, 2, 3)->(0, 2, 2)->(1, 2, 1)->(2, 2, 0)->(3, 2, 1)->...

- (-1, 1, -1): (2, 2, 2)->(1, 3, 1)->(0, 2, 0)->(1, 1, 1) Sergey

- (-1, 1, 0): (2, 2, 2)->(1, 3, 2)->(0, 2, 2)->(1, 1, 2) Chen

- (-1, 1, 1): (2, 2, 2)->(1, 3, 3)->(0, 2, 2)->(1, 1, 1) Sergey

- (0, *, *): x-coordinate never changed

- (1, -1, -1): (2, 2, 2)->(3, 1, 1)->(2, 0, 0)->(1, 1, 1) Sergey

- (1, -1, 0): (2, 2, 2)->(3, 1, 2)->(2, 0, 2)->(1, 1, 2) Chen

- (1, -1, 1): (2, 2, 2)->(3, 1, 3)->(2, 0, 2)->(1, 1, 1) Sergey

- (1, 0, -1): (2, 2, 2)->(3, 2, 1)->(2, 2, 0)->(1, 2, 1)->(0, 2, 2)->...

- (1, 0, 0): (2, 2, 2)->(3, 2, 2)->(2, 2, 2)->(1, 2, 2)->(0, 2, 2)->...

- (1, 0, 1): (2, 2, 2)->(3, 2, 3)->(2, 2, 2)->(1, 2, 1)->(0, 2, 0)->...

- (1, 1, -1): (2, 2, 2)->(3, 3, 1)->(2, 2, 0)->(1, 1, 1) Sergey

- (1, 1, 0): (2, 2, 2)->(3, 3, 2)->(2, 2, 2)->(1, 1, 2) Chen

- (1, 1, 1): (2, 2, 2)->(3, 3, 3)->(2, 2, 2)->(1, 1, 1) Sergey
