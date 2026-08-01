# Tile Painting: Revisited!

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.6820276497695853
- **Total Submissions:** 217
- **Solved Count:** 148
- **URL:** https://www.hackerrank.com/challenges/tile-painting-revisited

## Problem Statement

Nikita has a row of $N$ white tiles indexed from $1$ to $N$. This time, she's painting them green! 

Find the number of ways Nikita can paint certain tiles in green so that the indices of the green tiles form an [Arithmetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression). As this value can be quite large, your answer must be modulo $(10^9 + 7)$.

**Note:** Nikita must paint *at least* $1$ tile.

## Input Format

The first line contains a single integer, $T$, denoting the number of test cases.	
Each test case consists of a single line containing an integer, $N$, denoting the length of row of tiles.

## Output Format

On a new line for each test case, print the number of ways Nikita can paint her white tiles green so that the indices of the green tiles form an [Arithmetic Progression](https://en.wikipedia.org/wiki/Arithmetic_progression). Because this number can be quite large, your answer must be modulo $(10^9+7)$.

## Constraints

* $1 \le T \le 10$
* $1 \le N \le 10^{10}$

**Scoring**

* $1 \le N \le 2000$ for $20\%$ of test data.
* $1 \le N \le 10^5$ for $50\%$ of test data.
* $1 \le N \le 10^{10}$ for $100\%$ of test data.

## Sample Input

3
4
5

## Sample Output

13
22

## Explanation

Test Case 0:

There are  valid ways to paint the tiles:

Thus, we print the result of  on a new line, which is .

Test Case 1:

There are  valid ways to paint the tiles:

Thus, we print the result of  on a new line, which is .
