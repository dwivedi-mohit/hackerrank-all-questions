# Falling Rocks 2

---

| Field | Value |
|---|---|
| **Slug** | `falling-rocks-2` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **Contest** | 101hack32 |
| **URL** | https://www.hackerrank.com/challenges/falling-rocks-2 |

---

## Preview

How many initial graph configurations can you survive?

## Problem Statement

You suddenly fall into a magical, 2D world laid out on a $W \times H$ grid. Looking around, you realize you are somewhere in the bottom row at a general coordinate of $(*, 1)$. There are several rocks in other cells.

You notice the rocks are falling down at a constant rate of *one unit of distance per increment* of time. The rock at each $(x, y)$ at time $t$ will be at $(x, y-1)$ at time $t+1$. A rock will disappear from the world once $y$ becomes $0$. 

You must choose to remain in place, move left, or move right to avoid being squashed by the falling rocks. Unlike the rocks, you can move *arbitrary units of distance per increment* of time&mdash;as long as you don't hit any rocks while moving. If your location at time $t$ is $(x, 1)$ and the nearest rocks to your respective left and right are at $(l, 1)$ and $(r, 1)$, then you may move to any position $(x', 1)$ where $l < x' < r$. If there are no rocks to your left, then $l = 0$; if there are no rocks to your right, then $r = W + 1$. The destination cell must exist within the range of $W$ and must *not* contain a rock during both times $t$ and $t+1$.

Given some $W$, $H$, and a starting location of $(1, 1)$, determine how many possible layouts you can survive. Output the answer modulo $M$. 

**Note:** This is a magical world where time is _discrete_. Location $(1, 1)$ is reserved for you and will always initially  be empty when you fall into the world.

## Input Format

A single line of space-separated integers: $W$ (world width), $H$ (world height), and $M$ (for output), respectively.

**Constraints**		
For 25% test cases: $1 \le W, H \le 7$.

For 50% test cases: $1 \le W \le 7; 1 \le H \le 100$.

For 100% test cases: $1 \le W \le 7; 1 \le H \le 10^5; 10^6 \le M \le 10^9 + 9$; $M$ is a prime.

## Output Format

Determine the number of good rock layouts, $g$; as the answer may be very large, print $g \ \% \ M$.

## Sample Tests

### Test 1

```
2 2 1000000007
```

### Test 2

```
2 3 1000000007
```

### Test 3

```
3 2 1000000007
```

### Test 4

```
5
```

### Test 5

```
12
```

### Test 6

```
21
```

### Test 7

```
W = 2, H = 2
```

### Test 8

```
E?
Y?
```

### Test 9

```
RE
YE
```

### Test 10

```
W = 2, H = 3
```

### Test 11

```
E?
E?
Y?
```

### Test 12

```
RE
EE
Y?
```

### Test 13

```
?E
RE
YE
```
