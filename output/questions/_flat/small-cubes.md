# Small Cubes

---

| Field | Value |
|---|---|
| **Slug** | `small-cubes` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 60 |
| **Contest** | 101hack51 |
| **URL** | https://www.hackerrank.com/challenges/small-cubes |

---

## Preview

Maximize the value of a given function by placing some cubes in a large cuboid.

## Problem Statement

Consider a large *cuboid* of dimensions $n\times m \times k$ composed of unit cubes. The cuboid is placed on the 3D Cartesian space such that the sides are aligned with the axes and two of its corners are at $(0, 0, 0)$ and $(n, m, k)$.


![image](https://s3.amazonaws.com/hr-assets/0/1502098621-16eca974de-SmallCubes.png)

Each unit cube can be identified by three integers $(x, y, z)$ where $0 \le x < n$, $0 \le y < m$, $0 \le z < k$ describing its corner with the smallest coordinates.


You are going to place *cubes* inside it. You want each cube to be placed in such a way that its sides are aligned with the axes and its corners are at integer coordinates. To be more specific, if you place a cube with side equal to $d$ at point $(x, y, z)$, every unit cube $(X, Y, Z)$ such that $x \le X < x + d$, $y \le Y < y + d$, $z \le Z < z + d$ will be inside it.

In addition, a cube can only be placed if every unit cube inside it is *free*.  We call unit cube $(x, y, z)$ **free** if the following conditions hold:


1. $a_x \le y \le A_x$.
2. $b_x \le z \le B_x$.
3. It is outside any of the previously placed cubes.


Here, $a_x, b_x, A_x, B_x$ are numbers that will be given as input.

Let $\mathrm{num}$ be the number of placed cubes and $\mathrm{max}$ be the longest side length among all placed cubes. Given two constants $p, q$, let's define the function $f$:


$f(\mathrm{num}, \mathrm{max}) = \mathrm{max} \cdot p + \mathrm{num} \cdot q$.


Find and print the **maximum** attainable value of $f(\mathrm{num}, \mathrm{max})$ by placing some cubes.

**Note:** You can use any number of cubes of any side length.

## Input Format

The first line contains three space-separated integers denoting the respective values of $n$, $m$, $k$.


The second line contains two space-separated integers denoting the respective values of $p, q$.

The $i$th of the $n$ subsequent lines contains four space-separated integers, $a_i, b_i, A_i, B_i$ respectively.

## Output Format

Print a single integer denoting the maximum attainable value of $f$ by placing some cubes.

## Constraints

- $1 \le n, m, k \le 10^5$

- $0 \le q \le 10 ^ 3$

- $0 \le p \le 10 ^ 9$

- $0 \le a_i \le A_i < m$

- $0 \le b_i \le B_i < k$


**Subtasks**

- For ~5% of the total score, $n, m, k \le 20$

- For ~15% of the total score, $n, m, k \le 200$

- For ~50% of the total score, $n, m, k \le 5000$

## Sample Tests

### Test 1

```
2 3 4
1 10
0 1 2 2
0 0 1 2
```

### Test 2

```
121
```

### Test 3

```
10 10 10
500 20
0 2 9 8
2 2 8 8
1 1 8 9
3 3 9 9
0 1 9 9
2 2 8 9
1 3 8 9
0 0 7 8
3 1 9 7
2 1 9 7
```

### Test 4

```
13360
```
