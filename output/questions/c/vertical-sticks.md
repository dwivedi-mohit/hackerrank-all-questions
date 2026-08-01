# Vertical Sticks

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7529289247591773
- **Total Submissions:** 3841
- **Solved Count:** 2892
- **URL:** https://www.hackerrank.com/challenges/vertical-sticks

## Problem Statement

Given an array of integers $Y=[y_1, y_2, \ldots, y_n]$, we have $n$ line segments, such that, the endpoints of $i^{th}$ segment  are $(i, 0)$ and $(i, y_i)$. Imagine that from the top of each segment a horizontal ray is shot to the left, and this ray stops when it touches another segment or it hits the y-axis. We construct an array of $n$ integers, $[v_1, v_2, \ldots, v_n]$, where $v_i$ is equal to length of ray shot from the top of segment $i$. We define $V(y_1, y_2, \ldots, y_n) = v_1 + v_2 + \ldots + v_n$.  
<br>
For example, if we have $Y=[3,2,5,3,3,4,1,2]$, then $v_1, v_2, \ldots, v_8 = [1,1,3,1,1,3,1,2]$, as shown in the picture below:

<img src="https://s3.amazonaws.com/hr-challenge-images/65/1466136228-1e0f816996-vertical.png" title="vertical.png" />

For each permutation $p$ of $[1, 2, \ldots, n]$, we can calculate $V(y_{p_1}, y_{p_2}, \ldots, y_{p_n})$. If we choose a uniformly random permutation $p$ of $[1, 2, \ldots, n]$, what is the expected value of $V(y_{p_1}, y_{p_2}, \ldots, y_{p_n})$?


## Input Format

The first line contains a single integer _T_ (1 <=_T_<= 100). _T_ test cases follow.  
The first line of each test-case is a single integer _N_ (1 <= _n_ <= 50), and the next line contains positive integer numbers $y_1, y_2 ..., y_n$ separated by a single space ($0 < y_i <= 1000$).


## Output Format

For each test-case output expected value of $V(y_{p_1}, y_{p_2}, \ldots, y_{p_n})$, rounded to two digits after the decimal point.


## Sample Input

3
1 2 3
3
3 3 3
3
2 2 3
4
10 2 4 4
5
10 10 10 5 10
6
1 2 3 4 5 6

## Sample Output

4.33
3.00
4.00
6.00
5.80
11.15

## Explanation

Case 1: We have ,

.

Average of these values is 4.33.

Case 2: No matter what the permutation is, , so the answer is 3.00.

Case 3: ,

,

,

and average of these values is 4.00.
