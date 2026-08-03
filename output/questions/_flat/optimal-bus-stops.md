# Optimal Bus Stops

---

| Field | Value |
|---|---|
| **Slug** | `optimal-bus-stops` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 65 |
| **Contest** | 101hack53 |
| **URL** | https://www.hackerrank.com/challenges/optimal-bus-stops |

---

## Preview

Find the minimum total unhappiness among all ways to construct bus stops.

## Problem Statement

A village has houses located along a main road, represented by the number line shown below. 
![image](https://s3.amazonaws.com/hr-assets/0/1512113522-403a2cf771-2.png)

Residents prefer a bus stop at their house location, and the farther away the bus stop is, the unhappier they are. The *unhappiness* of a house is defined as the square of the distance between its location and its assigned bus stop. Your task is to construct at most $k$ bus stops along the main road and assign each house to a bus stop in such a way that the sum of the unhappiness across all the houses is minimized.

**Note:** The bus stops can be constructed at any location in the number line, not necessarily where some house is located.

Formally, suppose the $i^\text{th}$ house has been assigned the ${b_i}^\text{th}$ bus stop ($1 \le b_i \le k$) and the location of the $j^\text{th}$ bus stop is $p_{j}$. You need to minimize the following expression:

$$\displaystyle \sum_{i=1}^{n} \left|x_i - p_{b_i}\right|^2$$

Complete the function `minimumTotalUnhappiness` which takes an integer denoting the number of bus stops and an integer array denoting house locations and prints the minimum sum of unhappiness across all houses.

## Input Format

The first line contains two space-separated integers $n$ and $k$, the number of houses and the number of bus stops, respectively.


The next line contains $n$ space-separated integers $x_1, x_2, \ldots, x_n$ denoting the $x$-coordinates of the houses.

## Output Format

Print a single real number denoting the answer.

Your answer is considered correct if its absolute or relative error doesn't exceed $10^{-6}$.

## Constraints

- $1 \le n\le 5 \cdot 10^{4}$
- $1 \le k\le \min(n, 100)$
- $1 \le x_{i}\le 10^{5}$

**Subtasks**

- $1 \le n \le 10^{2}$ for $20\%$ of the maximum score.
- $1 \le n \le 10^{3}$ for $50\%$ of the maximum score.

## Sample Tests

### Test 1

```
3 2
1 2 4
```

### Test 2

```
0.500000000000000
```
