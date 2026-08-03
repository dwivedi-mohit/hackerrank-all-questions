# Cartesian Country

---

| Field | Value |
|---|---|
| **Slug** | `cartesian-country` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack49 |
| **URL** | https://www.hackerrank.com/challenges/cartesian-country |

---

## Preview

Find the maximum number of roads the Rulers of Cartesian Country can commission.

## Problem Statement

*Cartesian Country* is a rectangular region of the [xy-plane](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) with corners at $(x_1, y_1)$ and $(x_2, y_2)$. Each *lattice point* (i.e., point with *integer* $x$ and $y$ coordinates) in Cartesian Country denotes an island city surrounded by water.

The country's Rulers live in the *capital* at coordinate $(x_c, y_c)$. Traveling between cities and the capital is a treacherous sea journey, so they decide to commission *bridges* satisfying *all* the following conditions:

- A bridge is a straight line with endpoints at two non-capital cities.
- The capital must be at the exact center (or midpoint) of the line.
- Two overlapping bridges are considered to be *different* if they connect different cities.

For example, the diagram on the left depicts Cartesian Country as a rectangle with opposite corners at $(1,1)$ and $(5,4)$ and isolated cities at its lattice points. The diagram on the right depicts the maximum number of bridges we can build when the capital is located at $(2, 3)$ (i.e., the *red* circle):


![image](https://s3.amazonaws.com/hr-assets/0/1495136496-9c31411d40-Cartesian-Country.png)

Note that any two cities connected by a bridge have the same color, and we've constructed a maximal $4$ bridges between cities $(1, 4)$ and $(3,2)$, $(1, 3)$ and $(3,3)$, $(1, 2)$ and $(3, 4)$, and $(2, 2)$ and $(2, 4)$.

Given $(x_1, y_1)$, $(x_2, y_2)$, and $(x_c, y_c)$, find and print the *maximum* number of bridges the Rulers will commission.

## Input Format

The first line contains two space-separated integers describing the respective values of $x_1$ and $y_1$.

The second line contains two space-separated integers describing the respective values of $x_2$ and $y_2$.

The third line contains two space-separated integers describing the respective values of $x_c$ and $y_c$.

## Output Format

Print a long integer denoting the maximum number of bridges the Rulers will commission.

## Constraints

* $ -10^{8} \le x_1 < x_2 \le 10^8 $

* $ -10^{8} \le y_1 < y_2 \le 10^8 $

* $ x_1 \le x_c \le x_2 $
* $ y_1 \le y_c \le y_2 $

## Sample Tests

### Test 1

```
1 1
5 4
2 3
```

### Test 2

```
4
```

### Test 3

```
1 1
5 4
3 2
```

### Test 4

```
7
```
