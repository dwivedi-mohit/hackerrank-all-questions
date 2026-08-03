# Optimal Network Routing

---

| Field | Value |
|---|---|
| **Slug** | `optimal-path-1` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | hack-the-interview-iv |
| **URL** | https://www.hackerrank.com/challenges/optimal-path-1 |

---

## Preview

binary search with dfs

## Problem Statement

A network system is defined as a two-dimensional grid. Each cell of the grid has a routing coefficient associated with it. You need to send a packet from the top-left corner to the bottom right corner. 

A packet can travel in four directions only - up, down, left and right and only if the cell does not go beyond bounds. A packet needs an energy of |C[x, y] - C[x', y']| to travel from the cell (x,y) to the cell (x', y'), where |x| denotes the absolute value of x.

The effort required by a packet in any path is defined as the maximum energy needed by the packet along that path. Your task is to find the minimum effort required by the packet to traverse the network from top-left corner to the bottom-right corner. 

Consider, for example, the packet travels in the given grid with number of rows, N = 3 and number of columns, M = 4. as described below - 

![image](https://s3.amazonaws.com/hr-assets/0/1580987902-9f225577ca-Screenshotfrom2020-02-0616-48-06.png)

Suppose the packet travels from 5 → 1 → 4 → 7 → 6 → 7 → 5 → 9. Here the corresponding energies required for each of the transations are 4, 3, 3, 1, 1, 2, 4 respectively. Hence the effort required in the path is 4.

## Input Format

The first line contains two space-separated integers, N and M denoting the number of rows and number of columns respectively. 
N lines follow. Each line contains M integers denoting the $i^{th}$ row of the grid.

## Output Format

In a single line of output, print the minimum possible effort.

## Constraints

- $1 \le N, M \le 300$
- $1 \le C_{i, j} \le 10^{6}$

## Sample Tests

### Test 1

```
3 4
12 6 5 3 
6 13 3 15 
8 2 6 9
```

### Test 2

```
6
```

### Test 3

```
4 4
13 14 13 1 
8 12 12 9 
15 15 14 14 
15 10 10 5
```

### Test 4

```
5
```
