# Walking the Approximate Longest Path

---

| Field | Value |
|---|---|
| **Slug** | `walking-the-approximate-longest-path` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/walking-the-approximate-longest-path |

---

## Preview

Find longest path

## Problem Statement

Jenna is playing a computer game involving a large map with $n$ cities numbered sequentially from $1$ to $n$ that are connected by $m$ bidirectional roads. The game's objective is to travel to as many cities as possible without visiting any city more than once. The more cities the player visits, the more points they earn.

As Jenna's fellow student at Hackerland University, she asks you for help choosing an optimal path. Given the map, can you help her find a path that maximizes her score?

**Note:** She can start and end her path at any two distinct cities.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of cities) and $m$ (the number of roads). 		
Each line $i$ of the $m$ subsequent lines contains two space-separated integers, $x_i$ and $y_i$, describing a bidirectional road between cities $x_i$ and $y_i$.

**Map Generation Algorithm** 	

The graph representing the map was generated randomly in the following way:

1. Initially, the graph was empty.
2. Permutations $p_1, \ldots, p_n$ were chosen uniformly at random among all $n!$ permutations.
3. For each $i \in \{1,\ldots, n-1\}$, edge $(p_i, p_{i+1})$ was added to the graph.
4. An additional $m-n+1$ edges were chosen uniformly at random among all possible sets of $m-n+1$ edges which don't intersect with edges added during step $3$.

## Output Format

Print the following two lines of output:

1. The first line must contain a single integer, $d$, denoting the length of the path.
2. The second line must contain $d$ distinct space-separated integers describing Jenna's path in the same order in which she visited each city.

## Constraints

* $1 \le n \le 10^4$
* $1 \le m \le 10^5$
* $1 \le x_i, y_i \le n$
* For $30\%$ of test $n \le 25$ and $m \le 75$.
* For $50\%$ of test $n \le 100$ and $m \le 500$.
* For $70\%$ of test $n \le 500$ and $m \le 2500$.
- It's guaranteed that a valid path of length $n$ always exists. 

**Scoring**

- A valid path of length $d$ earns $(\frac{d}{n})^2 \times \text{100%}$ of a test case's available points. The total score will be rounded to next $5\%$.

## Sample Tests

### Test 1

```
4 5
3 1
3 4
2 4
2 3
4 1
```

### Test 2

```
4
1 4 2 3
```
