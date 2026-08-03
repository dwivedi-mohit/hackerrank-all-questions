# Contest Performance

---

| Field | Value |
|---|---|
| **Slug** | `contest-performance` |
| **Contest** | hourrank-3 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/contest-performance |

---

## Problem Statement

Alex is participating in 'Simplified Week of Code', a contest that releases one problem per day for $5$ days. Each problem is numbered to match its day of release, so problem $1$ is released on day $1$, problem $2$ is released on day $2$, and so on.

If a problem is solved on the same day it's released, it scores full marks ($100$ points). For each day after its release, a problem's worth decreases at a rate of $10$ points per day until it reaches zero. 

For example, on day $3$, problem $2$ is worth $90$ points; on day $4$, problem $2$ is worth $80$ points; on day $12$ and beyond, problem $2$ is worth $0$ points.

Alex solves all the problems and writes down the day number as she finishes each solution. Given Alex's completion date for each problem, calculate her final score.

## Input Format

Five integers, $[A_1,A_2,...A_5]$, on $5$ separate lines, where $A_i$ is the day number when Alex solved problem $i$.

**Constraints**

$1 \leq A_i \leq 20$

## Output Format

Print the sum of Alex's five scores for the contest problems.
