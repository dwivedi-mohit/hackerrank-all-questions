# Repair Roads

---

| Field | Value |
|---|---|
| **Slug** | `repair-roads` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/repair-roads |

---

## Preview

You need to send robots through every road in Byteland without any road being visited twice. How many robots are needed?

## Problem Statement

The country of Byteland contains $N$ cities and $N - 1$ bidirectional roads. There is a path between any two cities. The roads in Byteland were built long ago, and now they are in need of repair. You have been hired to fix all the roads. You intend to do this by dispatching robots on some of the roads. Each robot will repair the road he is currently on and then moves to one of the adjacent unrepaired roads. After repairing that, it will move to another adjacent unrepaired road, repair that and so on.

Two roads are adjacent if they have the same city at one of their endpoints. For the process to be efficient, no two robots will ever repair the same road, and no road can be visited twice. What is the minimum number of robots needed to accomplish the task?

## Input Format

The first line contains the number of test cases $T$. $T$ test cases follow. The first line of each test case contains $N$, the number of cities in Byteland. The cities are numbered $0..N - 1$. The following $N - 1$ lines contain the description of the roads. The $i^{th}$ line contains two integers $a_{i}$ and $b_{i}$, meaning that there is a road connecting cities with numbers $a_{i}$ and $b_{i}$.

## Output Format

Print $T$ lines, one corresponding to each test case containing the required answer for that test case.

## Constraints

- $1 \le T \le 20$

- $1 \le N \le 10000$

- $0 \le a_i, b_i \lt N$

## Sample Tests

### Test 1

```
3 
4 
0 1 
0 2 
0 3 
6 
0 1 
1 2 
2 3 
2 4 
4 5 
7 
0 1 
1 2 
2 3 
2 4 
4 5 
3 6
```

### Test 2

```
1 
1 
2
```
