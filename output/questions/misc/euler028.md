# Project Euler #28: Number spiral diagonals

---

| Field | Value |
|---|---|
| **Slug** | `euler028` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler028 |

---

## Preview

Running around a matrix.

## Problem Statement

<sub>This problem is a programming version of [Problem 28](https://projecteuler.net/problem=28) from [projecteuler.net](https://projecteuler.net/)</sub>


Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

$$\begin{array}{ccccc}
   \textbf{21} & 22 & 23 & 24 & \textbf{25}\\\
   20 & \textbf{7} & 8 & \textbf{9} & 10\\\

   19 & 6 & \textbf{1} & 2 & 11 \\\
   18 & \textbf{5} & 4 & \textbf{3} & 12 \\\
   \textbf{17} & 16 & 15 & 14 & \textbf{13}
\end{array}$$


It can be verified that the sum of the numbers on the diagonals is $101$.

What is the sum of the numbers on the diagonals in a $N \times N$, (N is odd) spiral formed in the same way?

As the sum will be huge you have to print the result mod $(10^9 + 7)$

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain an integer $N$.

## Output Format

Print the values corresponding to each test case.

## Constraints

$1 \le T \le 10^5$

$1 \le N < 10^{18}, \text{N is odd}$

## Sample Tests

### Test 1

```
2
3
5
```

### Test 2

```
25
101
```
