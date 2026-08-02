# Minimum Height Triangle

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9249211506082667
- **Total Submissions:** 84338
- **Solved Count:** 78006
- **URL:** https://www.hackerrank.com/challenges/lowest-triangle

## Problem Statement

Given integers $b$ and $a$, find the smallest integer $h$, such that there exists a triangle of height $h$, base $b$, having an area of at least $a$.


![image](https://s3.amazonaws.com/hr-assets/0/1496306792-f2c37eea44-triangle.jpg)  

**Example**  
$b = 4$  
$a = 6$  

The minimum height $h$ is $3$.  One example is a triangle formed at points (0, 0), (4, 0), (2, 3).  

**Function Description**  

Complete the *lowestTriangle* function in the editor below.  

*lowestTriangle* has the following parameters:  

- *int b:* the base of the triangle  
- *int a:* the minimum area of the triangle  

**Returns**  

- *int:*  the minimum integer height to form a triangle with an area of at least $a$ 

## Input Format

There are two space-separated integers $b$ and $a$, on a single line.

## Constraints

+ $1 \le b \leq 10^6$
+ $1 \le a \le 10^6$

## Sample Input

2 2

## Sample Output

2

## Explanation

The task is to find the smallest integer height of the triangle with base  and area at least . It turns out, that there are triangles with height , base  and area , for example a triangle with corners in the following points: :

It can be proved that there is no triangle with integer height smaller than , base  and area at least .

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
