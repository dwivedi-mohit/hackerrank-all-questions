# Falling Rocks

---

| Field | Value |
|---|---|
| **Slug** | `falling-rocks` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack31 |
| **URL** | https://www.hackerrank.com/challenges/falling-rocks |

---

## Problem Statement

You suddenly fall into a magical, 2D world laid out on a $W$ $*$ $H$ grid. Looking around, you realize you are somewhere in the bottom row at a general coordinate of $(*, 1)$. There are several rocks in other cells.

You notice the rocks are falling down at a constant rate of one unit of distance per increment of time. The rock at each $(x, y)$ at time $t$ will be at $(x, y-1)$ at time $t+1$. A rock will disappear from the world once $y$ becomes $0$. 

You must choose to remain in place, move left, or move right to avoid being squashed by the falling rocks. Like the rocks, you can only move one unit of distance per increment of time. If your location at time $t$ is $(x, 1)$, then you may stay at $(x, 1)$, move to $(x-1, 1)$, or move to $(x+1, 1)$. The destination cell must exist within the range of $W$ and must not be occupied by a rock at both times, $t$ and $t+1$.

**Note:** This is a magical world where time is _discrete_.

## Input Format

The first line is contains two space-separated integers, $W$ and $H$.

The following $H$ lines of input each contain $W$ characters that describe a row in the grid. The $j$<sup>th</sup> character of the $i$<sup>th</sup> line defines the status of the cell at coordinates $(i, j)$. The descriptive characters are as follows:

- **R** indicates that location contains a rock.
- **Y** indicates you are occupying that location.
- **E** indicates an empty cell.

**Constraints**

In $20\%$ test cases: $1$ &le; $W, H$ &le; $10$

In $60\%$ test cases: $1$ &le; $W, H$ &le; $100$

In $100\%$ test cases: $1$ &le; $W, H$ &le; $1000$

## Output Format

Print YES if you can avoid hitting any rocks. Otherwise, print NO.

## Sample Tests

### Test 1

```
5 5
REYEE
EEREE
EREEE
EEERR
REREE
```

### Test 2

```
YES
```

### Test 3

```
EERYE
EREEE
EEERR
REREE
EEEEE
```

### Test 4

```
EREYE
EEERR
REREE
EEEEE
EEEEE
```

### Test 5

```
EEYRR
REREE
EEEEE
EEEEE
EEEEE
```

### Test 6

```
RYREE
EEEEE
EEEEE
EEEEE
EEEEE
```
