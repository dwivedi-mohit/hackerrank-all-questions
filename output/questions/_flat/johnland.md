# Roads in HackerLand

---

| Field | Value |
|---|---|
| **Slug** | `johnland` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/johnland |

---

## Preview

Help John to calculate sum of minimum distances of each pair of cities.

## Problem Statement

John lives in HackerLand, a country with $N$ cities and $M$ bidirectional roads. Each of the roads has a distinct length, and each length is a *power of two* (i.e., $2$ raised to some exponent). It's possible for John to reach any city from any other city.

Given a map of HackerLand, can you help John determine the sum of the minimum distances between each pair of cities? Print your answer in [binary representation](https://en.wikipedia.org/wiki/Binary_number#Representation).

## Input Format

The first line contains two space-seperated integers denoting $N$ (the number of cities) and $M$ (the number of roads), respectively.		
Each line $i$ of the $M$ subsequent lines contains the respective values of $A_i$, $B_i$, and $C_i$ as three space-separated integers. These values define a bidirectional road between cities $A_i$ and $B_i$ having length $2^{C_i}$.

## Output Format

Find the sum of minimum distances of each pair of cities and print the answer in [binary representation](https://en.wikipedia.org/wiki/Binary_number#Representation).

## Constraints

* $1 \le N \le 10^5$
* $1 \le M \le 2 \times 10^5$
* $1 \le A_i,B_i \le N$, $A_i \ne B_i$
* $0 \le C_i < M$
* If $i \ne j$, then $C_i \ne C_j$.

## Sample Tests

### Test 1

```
5 6
1 3 5
4 5 0
2 1 3
3 2 1
4 3 4
4 2 2
```

### Test 2

```
1000100
```
