# Road Repairing

---

| Field | Value |
|---|---|
| **Slug** | `road-repairing` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/road-repairing |

---

## Preview

Find the minimum number of reconstructed roads to make a connected graph

## Problem Statement

Some of the roads in a state have been damaged due to recent flood. Your task is to repair just enough roads such that each city
in the state is connected to every other city. You are given the list of functional roads and damaged roads. Each input line will
contain the id of the road and two city which it connects. The roads are bidirectional.

## Input Format

The first line contains an integer $T$, denoting the number of cities.

The second line contains an integer $m$, denoting the number of functional roads.

The next $m$ lines contains two integers describing the endpoints (`u`, `v`) of each road.
The m + 2 line contains an integer $n$, denoting the number of damaged roads.
The next $n$ lines contains two integers describing the endpoints (`u`, `v`) of each road.

## Output Format

If answer doesn't exist, print `-1`.

Otherwise, print the minimum numbers of reconstructed roads such that every two cities connect to each other.

## Constraints

+ $1 \le T \le 10^5$

+ $0 \le n, m \le 10^5$

+ $1 \le u, v \le T$

It is guaranteed that roads are different in the input.

## Sample Tests

### Test 1

```
4
2
1 2
2 3
2
3 4
1 4
```

### Test 2

```
1
```

### Test 3

```
5
0
5
3 5
3 4
1 2
1 3
1 1
```

### Test 4

```
4
```
