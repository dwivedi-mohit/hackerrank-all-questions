# Beautiful Segments

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 120
- **Success Ratio:** 0.7600827300930714
- **Total Submissions:** 1934
- **Solved Count:** 1470
- **URL:** https://www.hackerrank.com/challenges/beautiful-segments

## Problem Statement

You are given an array, $A$, consisting of $N$ integers.

A segment, $[l, r]$, is *beautiful* if and only if the [*bitwise AND*](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of all numbers in $A$ with indices in the inclusive range of $[l, r]$ is not greater than $X$. In other words, segment $[l, r]$ is *beautiful* if $(A_{l} \land A_{l + 1} \land \ldots \land A_{r}) \leq X$.

You must answer $Q$ queries. Each query, $Q_j$, consists of $3$ integers: $L_j$, $R_j$, and $X_j$. The answer for each $Q_j$ is the number of *beautiful* segments $[l, r]$ such that $L_j ≤ l ≤ r ≤ R_j$ and $X = X_j$.

## Input Format

The first line contains two space-separated integers, $N$ (the number of integers in $A$) and $Q$ (the number of queries).

The second line contains $N$ space-separated integers, where the $i^{th}$ integer denotes the $i^{th}$ element of array $A$.

Each line $j$ of the $Q$ subsequent lines contains $3$ space-separated integers, $L_j$, $R_j$, and $X_j$, respectively, describing query $Q_j$.

**Constraints**

* $1 \leq N \leq 4 \times 10^4$
* $1 \leq Q \leq 10^5$
* $1 \leq L_j \leq R_j \leq N$
* $0 \leq X_j \leq 2^{17}$
* $0 \leq A_{i} \lt 2^{17}$
* $1 \leq N, Q \leq 2000$ holds for test cases worth at least $10\%$ of the problem's score.
* $0 \leq A_{i} \lt 2^{11}$ holds for test cases worth at least $40\%$ of the problem's score. 

## Output Format

Print $Q$ lines, where the $j^{th}$ line contains the number of beautiful segments for query $Q_j$.

## Constraints

-

-

-

-

-

-  holds for test cases worth at least  of the problem's score.

-  holds for test cases worth at least  of the problem's score.

## Sample Input

5 3
1 2 7 3 4
1 5 3
2 4 6
3 5 2

## Sample Output

5
2

## Explanation

The beautiful segments for all queries are listed below.

Query 0: The beautiful segments are .

Query 1: The beautiful segments are .

Query 2: The beautiful segments are .
