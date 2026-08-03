# Super Kth LIS

---

| Field | Value |
|---|---|
| **Slug** | `super-kth-lis` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/super-kth-lis |

---

## Preview

Find the lexicographically kth longest increasing subsequence

## Problem Statement

Given an array of $N$ integers ($a_0, a_1, \ldots, a_{N-1}$), find all possible increasing subsequences of maximum length, $L$. Then print the lexicographically $K^{th}$ longest increasing subsequence as a single line of space-separated integers; if there are less than $K$ subsequences of length $L$, print $\texttt{-1}$.

Two subsequences $[a_{p_0}, a_{p_1}, \ldots, a_{p_{L-2}}, a_{p_{L-1}}]$ and $[a_{q_0}, a_{q_1}, a_{q_2}, \ldots, a_{q_{L-2}}, a_{q_{L-1}}]$ are considered to be *different* if there exists at least one $i$ such that $p_i \ne q_i$.

## Input Format

The first line contains $2$ space-separated integers, $N$ and $K$, respectively.	
The second line consists of $N$ space-separated integers denoting $a_0, a_1, \ldots, a_{N-1}$ respectively.

## Output Format

Print a single line of $L$ space-separated integers denoting the lexicographically $K^{th}$ longest increasing subsequence; if there are less than $K$ subsequences of length $L$, print $\texttt{-1}$.

**Note:** $L$ is the length of longest increasing subsequence in the array.

**Sample Input 0**

    5 3
    1 3 1 2 5
  

**Sample Output 0**

    1 3 5
  

**Sample Input 1**

    5 2
    1 3 2 4 5
  

**Sample Output 1**

    1 3 4 5

## Constraints

- $1 \le N \le 10^{5}$ 

- $1 \le K \le 10^{18}$

- $1 \le a_i \le N$

**Scoring**

* $1 \le N \le 10^3$ for $30\%$ of the test data.

* $1 \le N \le 10^5$ for $100\%$ of the test data.

## Sample Tests

### Test 1

```
5 3
1 3 1 2 5
```

### Test 2

```
1 3 5
```

### Test 3

```
5 2
1 3 2 4 5
```

### Test 4

```
1 3 4 5
```
