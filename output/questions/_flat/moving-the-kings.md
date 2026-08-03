# Moving the Kings

---

| Field | Value |
|---|---|
| **Slug** | `moving-the-kings` |
| **Contest** | hourrank-27 |
| **Difficulty** | Hard |
| **Score** | 65 |
| **URL** | https://www.hackerrank.com/challenges/moving-the-kings |

---

## Problem Statement

In the game Chess World, there are multiple kings and the location of each king on the board is known to you. In a single step, a king can move in one of $8$ directions: 

![image](https://s3.amazonaws.com/hr-assets/0/1522407577-86157a05fd-movingkings2.png)

For every query you need to solve, you are given a meeting point for the kings to meet and your task is to calculate the sum of the minimum number of steps for each king to reach the meeting point.

## Input Format

The first line contains two space-separated integers, $n$, denoting the number of kings and $q$, denoting the number of queries.  

The next $n$ lines describe the locations of the kings. In particular, the $i^\text{th}$ line two space-separated integers $x_i^{(L)}$ and $y_i^{(L)}$ denoting the coordinates of the location of the $i^\text{th}$ king.

The next $q$ lines describe the queries. In particular, the $i^\text{th}$ line  contains two space-separated integers $x_i^{(Q)}$ and $y_i^{(Q)}$ denoting the coordinates of the meeting point in the $i^\text{th}$ query.

## Output Format

For each query, print the sum of the minimum number of steps for each king to reach the meeting point.

## Constraints

* $1 \le n \le 10^5$
* $1 \le q \le 10^5$
* $1 \le x_i, y_i \le 10^9$
