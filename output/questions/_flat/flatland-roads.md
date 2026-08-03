# Flatland Roads

---

| Field | Value |
|---|---|
| **Slug** | `flatland-roads` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 75 |
| **Contest** | indeed-prime-codesprint |
| **URL** | https://www.hackerrank.com/challenges/flatland-roads |

---

## Preview

Find number of cities you can visit without using more than p critical roads.

## Problem Statement

[FlatLand](https://en.wikipedia.org/wiki/Flatland) is a country with  $n$ cities, numbered from $1$ to $n$, and $e$ undirected roads. Every city is accessible from other cities. Some roads are ordinary, and some are *critical*. A *critical* road is defined as a road that, if blocked, will cut off access to one or more cities.

The King has given you a task: for each city $n_i$, how many cities can you travel to without using more than $p$ critical roads?

## Input Format

The first line has three space-separated integers, $n$, $e$, and $p$, respectively. Recall that $n$ is the number of cities, $e$ is the number of undirected roads, and $p$ is the threshold number of critical roads to not go over. 	
The $e$ subsequent lines each have two space-separated integers, $n_u$ and $n_v$, respectively, describing a road between city $n_u$ and city $n_v$.

**Constraints**		
$1 \leq n \leq 100000$		
$n-1 \leq e \leq min(250000, \dfrac{n*(n-1)}2)$		
$1 \leq p \leq15$		
$n_u \neq n_v$

There are *at least* one path between any two cities. The given graph is connected.  

There is *at most* one road between any two cities.

## Output Format

For each $n_i$ of $n$ cities, print a new line with the number of cities you can travel to from $n_i$ *without* using more than $p$ critical roads. The $i^{th}$ printed line should be the answer for city $n_i$.

## Sample Tests

### Test 1

```
6 6 1
1 2
2 3
3 1
3 4
4 5
3 6
```

### Test 2

```
4
4
4
4
1
3
```
