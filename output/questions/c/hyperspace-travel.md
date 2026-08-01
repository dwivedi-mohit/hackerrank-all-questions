# Hyperspace Travel 

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7574850299401198
- **Total Submissions:** 334
- **Solved Count:** 253
- **URL:** https://www.hackerrank.com/challenges/hyperspace-travel

## Problem Statement

A group of $n$ friends living in an $m$-dimensional hyperspace want to meet up at some central location. The hyperspace is in the form of an $m$-dimensional grid, and each person can only move along grid lines. For example, to go from $(0, 0) \rightarrow (1, 1)$ in a $2$-dimensional space, one possible route is $(0, 0) \rightarrow (0, 1) \rightarrow (1, 1)$ for a total distance traveled of $2$ units.

Given the coordinates, $(X[0, 1, \ldots, m - 1])$, for $n$ friends, find a point at which all $n$ friends can meet such that the total sum of the distances traveled by all $n$ friends is minimal. If there are multiple such points, choose the lexicographically smallest one. The point $P_1[0, 1, \ldots, m - 1]$ is lexicographically smaller than $P_2[0, 1, \ldots, m - 1]$ if there exists such $j \lt m$ that $\forall i \lt j\,P_1[i] = P_2[i]$ and $P_1[j]<P_2[j]$.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $m$.		
Each line $i$ of the $n$ subsequent lines contains $m$ space-separated integers describing the respective coordinates (i.e., $x_0, x_1, \ldots, x_{m - 1}$) for friend $i$.

## Output Format

Print $m$ space-separated integers describing the coordinates of the meeting point.

## Constraints

+ $1 \le n \le 10^4$  
+ $1 \le m \le 10^2$  
+ $-10^9 \le x_i \le 10^9$  

## Sample Input

3 2
1 1
2 2
3 3

## Sample Output

2 2

## Explanation

There are  friends (we'll call them , , and ) located at points , , and . The minimal solution is for friends  and  to meet at friend 's current location; this means  travels  units from  to ,  travels  units from  to , and  stays put at . The total distance traveled by all friends is , which is minimal. Thus, we print  space-separated integers describing the coordinate where the  friends meet: 2 2.
