# Bus Stops

---

| Field | Value |
|---|---|
| **Slug** | `bus-stops` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 45 |
| **Contest** | 101hack54 |
| **URL** | https://www.hackerrank.com/challenges/bus-stops |

---

## Preview

Answer queries about bus stops.

## Problem Statement

There are $n$ bus stops on the street. You can imagine the street as a line with the coordinate system. The coordinates of the bus stops are $x_1, x_2, \dots, x_n$, where $x_i$ is the distance in meters from the $i^\text{th}$ bus stop to the beginning of the street. The first bus stop is located at the beginning of the street and the last is located at the end of the street. 

![image](https://s3.amazonaws.com/hr-assets/0/1524824595-4cb259f446-bus.png)

There is exactly one bus route. A bus goes from the beginning to the end of the street every $w$ minutes with speed $v$ meters per minute, starting at time $0$. A bus stops at each stop. Stopping takes no time.

There are $q$ people who want to reach the end of the street. The $i^\text{th}$ person starts at point $p_i$ at time $t_i$ and has walking speed $u_i$ meters per minute. For each person, you should find the minimum time when this person can reach the end of the street.

Complete the function `minimumTimeToEnd` that takes in the array $x$ of coordinates of the bus stops and three integers $w$, $v$ and $q$ (the meanings of which are explained in the statement) and prints $q$ real numbers, the $i^\text{th}$ of which denotes the minimum time when the $i^\text{th}$ person can reach the end of the street. The description of the people should be taken from the standard input as described in the input format section.

## Input Format

The first line contains a single integer $n$.

The second line contains $n$ space-separated integers $x_1, x_2, \dots, x_n$.

The third line contains two space-separated integers $w$ and $v$.

The fourth line contains a single integer $q$.

The next $q$ lines contain the description of people. The $i^\text{th}$ of these lines contains three space-separated integers $p_i$, $t_i$, $u_i$.

## Output Format

Print $q$ lines. The $i^\text{th}$ line should contain the minimum time when the $i^\text{th}$ person can reach the end of the street.

The output is considered correct if it has an absolute error of at most $10 ^ {-5}$ from the answer.

## Constraints

- $2 \leq n \leq 150000$
- $0 = x_1 < x_2 < \dots < x_n \leq 10 ^ 9$
- $1 \leq w, v \leq 10 ^ 9$
- $1 \leq q \leq 150000$
- $0 \leq p_i < x_n$
- $0 \leq t_i \leq 10 ^ 9$
- $1 \leq u_i \leq 10 ^ 9$

Additionally, for 1/3 of the total points:

- $n, q \leq 3000$

## Sample Tests

### Test 1

```
4
0 10 40 100
20 10
3
0 0 4
15 10 1
40 2 16
```

### Test 2

```
10.0000000000
30.0000000000
5.7500000000
```
