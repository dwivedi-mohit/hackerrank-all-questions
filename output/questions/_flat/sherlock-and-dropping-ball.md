# Sherlock and the Dropping Ball

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-dropping-ball` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **Contest** | 101hack40 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-dropping-ball |

---

## Preview

Determine the eventual x-coordinate of the dropped ball.

## Problem Statement

Watson has a new challenge for Sherlock! He defines $n$ line segments on a *2-D* Cartesian plane by their two respective endpoints: $(x_1, y_1)$ and $(x_2, y_2)$. No two line segments intersect or touch each other, and no line segment is horizontal or vertical.

Watson defines gravity in the direction of the negative $y$-axis. If he drops a ball having an infinitesimally small radius from point $(x, y)$, the ball will fall in the direction of the negative $y$-axis. If it touches a line segment in its path, it will *slide* down the surface of this line segment toward negative $y$ and exit from the lower end where it continues to fall in the direction of negative $y$. Note that the ball *does not* gain horizontal velocity while falling or sliding.

For example, the image below has two line segments defined by their respective endpoints as $(4,5), (-5,0)$ and $(3,2), (7,-2)$. The respective trajectories of two balls dropped from points $(4,8)$ and $(6,5)$ are shown in red and blue.
  

![image](https://s3.amazonaws.com/hr-challenge-images/8532/1471882551-2e6ce04e24-blank.jpg)
  

Watson gives Sherlock the coordinates for $n$ line segments and asks him to perform $q$ queries, where each query consists of a point, $(x_i, y_i)$, where a ball is dropped. For each query, Sherlock has to report the $x$-coordinate of the ball at infinite time.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of line segments) and $q$ (the number of queries).		
Each of the $n$ subsequent lines describes a line segment in the form of four space-separated integers; the first two integers describe the respective values of  $x_1$ and $y_1$, and the second two integers describe the respective values of $x_2$ and $y_2$.		
Each of the $q$ subsequent lines contain a pair of space-separated integers denoting the respective $x$ and $y$ values for a query point (i.e., the location where a ball is being dropped from). It's guaranteed that this query point doesn't lie on any line segment.

## Output Format

For each query, print an integer denoting the final $x$-coordinate of the ball at infinite time (i.e., after sliding down any line segments in its path) on a new line.

## Constraints

- $1 \le n, q \le 10^5$  

- $-10^{6} \le \text{all coordinates} \le 10^{6}$  

- $x_1 \ne x_2$ and $y_1 \ne y_2$ for all line segments.

**Subtasks** 


- For $\text{15%}$ of the maximum score, $1 \le n \le 10^3$ and $1 \le q \le 10^3$.

- For an additional $\text{20%}$ of the maximum score, $1 \le n \le 10^3$ and $1 \le q \le 10^5$.

## Sample Tests

### Test 1

```
2 2
4 5 -5 0
3 2 7 -2
4 8
6 5
```

### Test 2

```
-5
7
```
