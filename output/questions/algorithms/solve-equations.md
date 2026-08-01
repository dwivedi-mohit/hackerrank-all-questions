# Solve Equations

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.3304904051172708
- **Total Submissions:** 469
- **Solved Count:** 155
- **URL:** https://www.hackerrank.com/challenges/solve-equations

## Problem Statement

You are given a straight line, $a \cdot x + b \cdot y = c$. Find the point closest to the origin that also satisfies the following properties:  

1. $x$ and $y$ are *integers*.  
2. $x$ is *greater than* zero.  

If more than one solution exists satisfying $1$ and $2$, then choose the point in which $x$ is minimal.  

Given $q$ queries consisting of $a_i$, $b_i$, and $c_i$, find and print the point satisfying the above conditions for each respective query. Each point must be printed on a new line as two space-separated integers denoting the point's respective $x_i$ and $y_i$ values.

**Note:** It is guaranteed that there will always be integral points on the line.  

## Input Format

The first line contains an integer, $q$, denoting the number of queries.  
Each line $i$ of the $q$ subsequent lines contains three space-separated integers describing the respective values of $a_i$, $b_i$, and $c_i$ for the query.  

## Output Format

For each query, print $2$ space-separated integers on a new line denoting the respective values of $x_i$ and $y_i$ for the point satisfying the $i^{th}$ query.

## Constraints

+ $1 \le q \le 10^5$  
+ $1 \le a \le 10^8$  
+ $1 \le b \le 10^8$  
+ $1 \le c \le 10^8$  

## Sample Input

2 3 1

## Sample Output

2 -1

## Explanation

Given the line , the point  is on the line and satisfies the conditions specified above. Thus, we print the coordinate as two space-separated integers on a new line.
