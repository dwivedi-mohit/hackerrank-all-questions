# Project Euler #14: Longest Collatz sequence

---

| Field | Value |
|---|---|
| **Slug** | `euler014` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler014 |

---

## Preview

Playing with an odd sequence.

## Problem Statement

<sub>This problem is a programming version of [Problem 14](https://projecteuler.net/problem=14) from [projecteuler.net](https://projecteuler.net/)</sub>


The following iterative sequence is defined for the set of positive integers:

$$\begin{align*}
    n &\rightarrow \frac{n}{2} & \text{ n is even }\\\
    n &\rightarrow 3n+1 & \text{ n is odd }
\end{align*}$$



Using the rule above and starting with 13, we generate the following sequence:

 $$13 \rightarrow 40 \rightarrow 20 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$

 
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.


Which starting number, $\le N$ produces the longest chain? If many possible such numbers are there print the maximum one.
 
**Note:** Once the chain starts the terms are allowed to go above $N$.

## Input Format

The first line contains an integer $T$ , i.e., number of test cases.

Next $T$ lines will contain an integers $N$.

## Output Format

Print the values corresponding to each test case.

## Constraints

+ $1 \leqslant T \leqslant 10^4$

+ $1 \leqslant N \leqslant 5 \times 10^6$

## Sample Tests

### Test 1

```
3
10 
15
20
```

### Test 2

```
9
9
19
```
