# Charging the Batteries

---

| Field | Value |
|---|---|
| **Slug** | `charging-the-batteries` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack51 |
| **URL** | https://www.hackerrank.com/challenges/charging-the-batteries |

---

## Preview

Find the minimum time to plug all controllers into sockets in a square-shaped room.

## Problem Statement

Leha loves video games and he is hosting a game night with his friends. But there's a problem: all of his $k$ controllers are out of power. Leha needs to start charging them as soon as possible.

Leha's room is a square on a plane with the lower left corner at coordinates $(0, 0)$ and the top right corner at $(n, n)$. Leha uses electric sockets on the walls of his room to charge his devices. There are $m$ sockets on the *edges* of the square that represent the walls of the room. Note that two or more electric sockets can be at the exact same coordinates on the edges.


Since his friends are coming, Leha doesn't want to make his floor dirty, so he is moving only **along the edges of the square**. Leha can start at any point on the edges. He has a constant speed of $1$ unit per second and plugging a controller to a socket takes $0$ time. 

Your task is to find the minimum possible time for Leha to plug all of his $k$ controllers to different sockets.

## Input Format

The first line contains three space-separated integers denoting the respective values of $n$, $m$, and $k$.

Each line of the following $m$ subsequent lines contains two space-separated integers $x_i, y_i$ denoting the coordinates of the $i$th socket.

## Output Format

Print a single integer denoting the minimum time that Leha needs to plug all controllers to different sockets.

## Constraints

- $1 \leq n, m \leq 10^5$
- $1 \le k \le m$

- $0 \le x_i, y_i \le n$

- $(x_i, y_i)$ is on the outline of the square

**Subtasks**

- For ~37% of the total score, $n, m \le 1000$

## Sample Tests

### Test 1

```
5 5 3
5 3
0 0
0 4
3 0
1 5
```

### Test 2

```
6
```
