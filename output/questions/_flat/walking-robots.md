# Walking Robots

---

| Field | Value |
|---|---|
| **Slug** | `walking-robots` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack48 |
| **URL** | https://www.hackerrank.com/challenges/walking-robots |

---

## Preview

Given the robots' positions and directions, find the number of moving robots that will collide.

## Problem Statement

We define the following conditions for $n$ robots numbered from $0$ to $n-1$: 

- The robots are initially spaced apart on an infinitely long straight line. Some of them begin moving simultaneously at the same constant speed. Two robots moving in the same direction never collide.
- Two robots moving toward each other will crash, break down, and stay at that point forever. This counts as $2$ collisions.
- A robot moving toward a non-moving robot will crash into it, break down, and stay at that point forever. This counts as $1$ collision.

<!-- TODO -->
To clarify, whenever a moving robot crashes onto another robot, it will stay at that point and become a non-moving robot at that location. 
<!-- TODO -->

We describe their movement instructions in a string, $s$, consisting of the letters `l`, `r`, and `d`. The $i^{th}$ character in $s$ denotes the $i^{th}$ robot's instruction according to the following rules:

- `l`: Move *left* indefinitely until a collision occurs.
- `r`: Move *right* indefinitely until a collision occurs.
- `d`: Do not move at all.

Complete the function below so that it returns the total number of collisions that eventually occur.

## Input Format

The first line contains an integer, $q$, denoting the total number of queries (i.e., calls to the function).		
Each of the $q$ subsequent lines describes a query in the form of a string, $s$, consisting of the letters `l`, `r`, and `d`.

## Output Format

Return an integer denoting the total number of collisions that eventually occur after movement begins.

## Constraints

- $1 \le q \le 100$
- $1 \le n \le 10^{5}$, where $n$ is the length of $s$.
- Each $s$ consists of the letters `l`, `r`, and `d` only.

## Sample Tests

### Test 1

```
5
r
lrrl
rrrll
rrdlldrr
rrrdllrllrrl
```

### Test 2

```
0
3
5
4
11
```
