# Testing the Game

---

| Field | Value |
|---|---|
| **Slug** | `testing-the-game` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 65 |
| **Contest** | 101hack51 |
| **URL** | https://www.hackerrank.com/challenges/testing-the-game |

---

## Preview

Given a special kind of grid with enemies, find the number of enemies that can reach each cell of the grid in a given amount of time.

## Problem Statement

Leha is a huge video game fan so he couldn't refuse when was asked to test a new Vladgaming game.


The action in this game happens on a rectangular matrix of dimensions $n \times (2m - 1)$. The rows are numbered top down from $1$ to $n$ and columns from left to right from $1$ to $2m - 1$. Each cell is a either wall or empty. To be more precise, **every second element in each row, except the first and the last, is a wall. All the other cells are empty.** For example, in the following grid, the red cells are the walls and the white cells are empty:

<img src="https://s3.amazonaws.com/hr-challenge-images/26285/1475780471-d3cad9a852-c03a60c05de7ec3cda1364b6a7e340ea66637fb5.png" title="c03a60c05de7ec3cda1364b6a7e340ea66637fb5.png" />

Also, there are some enemy units in the matrix. They could only be in free cells. There are no enemies in the first and the last row. Each enemy unit can move to a free cell adjacent to it. This takes $1$ second. Enemies can go through each other and each cell can contain more than one unit, but initially there is at most one unit in each cell.


There are given $q$ queries. Each query consists of a single integer $t_k$. For each cell except cells in the first and the last row, you have to find the number of enemies that can reach that cell in at most $t_k$ seconds. Let $\mathrm{num}_{i, j}$ be the answer for cell $(i, j)$. Print the sum $\sum\limits_{i=2}^{n-1} \sum\limits_{j=1}^{2m-1} \left(i\cdot j\cdot \mathrm{num}_{i, j}^2\right)$ modulo $10^9+7$.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$, $m$.


The next $n$ lines contain $2m - 1$ characters each: the description of the map. Each of the characters is either `.` (it means that corresponding cell is free and doesn't contain an enemy unit), `t` (it means that corresponding cell is free and contains exactly one enemy unit) or `#` (it means that corresponding cell is a wall).


The next line contains a single integer $q$ denoting the number of queries.


$q$ lines follow. The $k$th line contains a single integer $t_k$.

## Output Format

Print $q$ lines. The $k$th line should contain a single integer, the answer to the $k$th query.

## Constraints

- $3 \le n \le 1000$

- $1 \le m \le 1000$

- $1 \le t_k \le 5000$

- $1 \le q \le 20$


**Subtasks**


- For ~10% of the total score, $n, m \le 100$

- For ~30% of the total score, $n, m \le 500$

## Sample Tests

### Test 1

```
3 2
...
t#.
...
1
3
```

### Test 2

```
2
```

### Test 3

```
4 3
.....
t#.#t
t#.#.
.....
1
5
```

### Test 4

```
180
```

### Test 5

```
3 4
.......
t#t#t#t
.......
1
8
```

### Test 6

```
512
```

### Test 7

```
8 5
.........
.#.#.#.#.
.#.#.#.#.
.#.#.#.#.
.#.#.#.#.
.#.#.#t#t
.#.#.#.#.
.........
1
10
```

### Test 8

```
2425
```
