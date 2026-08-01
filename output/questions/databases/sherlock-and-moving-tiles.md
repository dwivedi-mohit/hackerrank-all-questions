# Sherlock and Moving Tiles

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.7647813314576524
- **Total Submissions:** 24169
- **Solved Count:** 18484
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-moving-tiles

## Problem Statement

Sherlock is given $2$ square tiles, initially both of whose sides have length $l$ placed in an $x-y$ plane.  Initially, the bottom left corners of each square are at the origin and their sides are parallel to the axes.  

At $t=0$, both squares start moving along line $y=x$ (along the positive $x$ and $y$) with velocities $s1$ and $s2$.     

For each querydetermine the time at which the overlapping area of tiles is equal to the query value, $queries[i]$.  

![img](https://s3.amazonaws.com/hr-challenge-images/5519/1422784979-db005a0a44-drawing-3.svg)

**Note**: Assume all distances are in meters, time in seconds and velocities in meters per second.  

**Function Description**  

Complete the *movingTiles* function in the editor below.  

*movingTiles* has the following parameter(s):  

- *int l:* side length for the two squares  
- *int s1:* velocity of square 1
- *int s2:* velocity of square 2
- *int queries[q]:* the array of queries  

**Returns**  

- *int[n]:* an array of answers to the queries, in order. Each answer will be considered correct if it is at most $0.0001$ away from the true answer.

**Input Format**  
First line contains integers $l, s1, s2$.  
The next line contains $q$, the number of queries.  
Each of the next $q$ lines consists of one integer $queries[i]$ in one line.

**Constraints**   
$1 \le l, s1, s2 \le 10^9$   
$1 \le q \le 10^5$   
$1 \le queries[i] \le L^2$   
$s1 \ne s2$  


**Sample Input**  

	10 1 2
    2
    50
    100
    
**Sample Output**  

	4.1421
    0.0000
    
**Explanation**  

For the first case, note that the answer is around `4.1421356237...`, so any of the following will be accepted:  

    4.1421356237
    4.14214
    4.14215000
    4.1421
    4.1422


## Input Format

First line contains integers .

The next line contains , the number of queries.

Each of the next  lines consists of one integer  in one line.

## Sample Input

10 1 2
2
50
100

## Sample Output

4.1421
0.0000

## Explanation

For the first case, note that the answer is around 4.1421356237..., so any of the following will be accepted:

4.1421356237
4.14214
4.14215000
4.1421
4.1422
