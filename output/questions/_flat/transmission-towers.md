# Transmission Towers

---

| Field | Value |
|---|---|
| **Slug** | `transmission-towers` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 85 |
| **Contest** | 101hack55 |
| **URL** | https://www.hackerrank.com/challenges/transmission-towers |

---

## Preview

Find the number of connected city pairs given the capacities of their transmission towers.

## Problem Statement

Country Republicia has $n$ cities (numbered $1$ to $n$) is constructed such that the distance between the $i^\text{th}$ city and the $(i+1)^\text{th}$ city is $1$. Each city in Republicia has exactly one transmission tower. The tower in the $i^\text{th}$ city has receiver capacity $b_i$ and transmitter capacity $a_i$.

The information in $i^\text{th}$ city can be transmitted to the $j^\text{th}$ city *directly* if $|i-j|\le |a_i + b_j|$. Information can also be transmitted *indirectly* by using more than one direct transmissions. Notice that sometimes it is impossible to transmit information from one city to another city, either directly or indirectly.

Two cities $x$ and $y$ said to be *connected* if information in city $x$ can be transmitted to city $y$ and information in city $y$ can be transmitted to city $x$, directly or indirectly. 

President Taang wants your help to find the number connected city pairs $(i, j)$ such that $i \lt j$.


Complete the function `connectedCityPairs` which takes in two integer arrays $a$ and $b$ denoting the transmitter and receiver capacities of the towers and returns the number of connected city pairs.

## Input Format

The first line contains a single integer $n$.


The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$ denoting the tranmitter capacities. 

The third line contains $n$ space-separated integers $b_1, b_2, \ldots, b_n$ denoting the receiver capacities.

## Output Format

Print a single line containing a single integer denoting the number of connected city pairs $(i,j)$ such that $i \lt j$.

## Constraints

- $1 \leq n \leq 2\times10^5$
- $0 \le a_i, b_i \le n$

**Subtask**

- $1 \le n \le 5000$ for $20\%$ of the maximum score

## Sample Tests

### Test 1

```
6
0 0 1 0 0 2
0 0 1 0 0 1
```

### Test 2

```
4
```

### Test 3

```
6
6 6 6 6 6 6
6 6 6 6 6 6
```

### Test 4

```
15
```
