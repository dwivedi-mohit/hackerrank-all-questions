# Tandem Repeats

---

| Field | Value |
|---|---|
| **Slug** | `tandem-repeats` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | 101hack31 |
| **URL** | https://www.hackerrank.com/challenges/tandem-repeats |

---

## Problem Statement

_Tandem Repeats_ are consecutive occurrences of a substring $S'$ within a given string $S$. <br>
$S'$ is defined as $[i, i + L - 1]$.<br>
The _Tandem Number_ of some substring $S'$ is the maximum number of **tandem repeats** of $S'$ in the original string $S$.
<br> Basically, there is a maximum, $k$, such that: $[i, i + L - 1], [i + L, i + 2L - 1], [i + 2L, i + 3L-1], ... , [i + (k-1)L, i + kL - 1]$ are all the same.

You are given a string, $S$ of length $N$. $S$ is comprised of lowercase English letters. You are also given $M$ lines of substring ranges $[i, j]$ where $1$ &le; $i$ &le; $j$ &le; $N$.<br><br>
Find and print the _Tandem Number_ for each substring range.

## Input Format

The first line of input contains two integers, $N$ and $M$.

The second line contains a string, $S$.

There are $M$ subsequent lines, each containing two space-separated integers, $i$ and $j$.

**Constraints**

In $20\%$ test cases, $1$ &le; $N$, $M$ &le; $100$ 

In $50\%$ test cases, $1$ &le; $N$, $M$ &le; $3,000$ 

In $100\%$ test cases, $1$ &le; $N$, $M$ &le; $10^5$, $1$ &le; $i$ &le; $j$ &le; $N$

## Output Format

Output $M$ lines of _Tandem Numbers_ according to the queries.

## Sample Tests

### Test 1

```
10 5
ababcabccc
1 2
1 3
2 3
3 5
8 8
```

### Test 2

```
2
1
1
2
3
```
