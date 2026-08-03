# Almost Integer Rock Garden

---

| Field | Value |
|---|---|
| **Slug** | `almost-integer-rock-garden` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/almost-integer-rock-garden |

---

## Preview

Finish building a rock garden so that the sum of distances from each stone to the origin is an almost integer.

## Problem Statement

Victor is building a [Japanese rock garden](https://en.wikipedia.org/wiki/Japanese_rock_garden) in his $24 \times 24$ square courtyard. He overlaid the courtyard with a [Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) so that any point $(x, y)$ in the courtyard has coordinates $x \in [-12, 12]$ and $y \in [-12, 12]$. Victor wants to place $12$ stones in the garden according to the following rules:

- The center of each stone is located at some point $(x, y)$, where $x$ and $y$ are integers $ \in [-12, 12]$. 
- The coordinates of all twelve stones are pairwise distinct. 
- The [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions) from the center of any stone to the [origin](https://en.wikipedia.org/wiki/Origin_(mathematics)#Cartesian_coordinates) is *not an integer*. 
- The sum of Euclidean distances between all twelve points and the origin is an [almost integer](https://en.wikipedia.org/wiki/Almost_integer), meaning the absolute difference between this sum and an integer must be $\le 10^{-12}$.

Given the values of $x$ and $y$ for the first stone Victor placed in the garden, place the remaining $11$ stones according to the requirements above. For each stone you place, print two space-separated integers on a new line describing the respective $x$ and $y$ coordinates of the stone's location.

## Input Format

Two space-separated integers describing the respective values of $x$ and $y$ for the first stone's location.

## Output Format

Print $11$ lines, where each line contains two space-separated integers describing the respective values of $x$ and $y$ for a stone's location.

## Constraints

- $-12 \le x, y \le 12$

## Sample Tests

### Test 1

```
7 11
```

### Test 2

```
11 1
-2 12
5 4
12 -3
10 3
9 6
-12 -7
1 11
-6 -6
12 -4
4 12
```
