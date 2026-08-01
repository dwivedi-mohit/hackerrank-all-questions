# Bitwise AND

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.8521959459459459
- **Total Submissions:** 9472
- **Solved Count:** 8072
- **URL:** https://www.hackerrank.com/challenges/linkedin-practice-bitwise-and

## Problem Statement

Given set $S = \{1, 2, 3,\ldots, N\}$. Find two integers, $A$ and $B$ (where $A \lt B$), from set $S$ such that the value of $A \text{&} B$ is the maximum possible *and also less than a given integer, $K$*. In this case, $\text{&}$ represents the *bitwise AND* operator.

## Input Format

The first line contains an integer, $T$, the number of test cases. 		
Each of the $T$ subsequent lines defines a test case as $2$ space-separated integers, $N$ and $K$, respectively.

## Output Format

For each test case, print the maximum possible value of  $A \text{&} B$ on a new line.

## Constraints

* $1 \le T \le 10^3$
* $2 \le N \le 10^3$
* $2 \le K \le N$

## Sample Input

5 2
8 5
2 2

## Sample Output

4
0

## Explanation

All possible values of  and  are:

-

-

-

-

-

-

-

-

-

-

The maximum possible value of  that is also  is , so we print  on a new line.
