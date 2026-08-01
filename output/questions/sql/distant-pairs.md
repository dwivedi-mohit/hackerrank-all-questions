# Distant Pairs

- **Domain:** sql
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.7183662573411639
- **Total Submissions:** 3746
- **Solved Count:** 2691
- **URL:** https://www.hackerrank.com/challenges/distant-pairs

## Problem Statement

We take a line segment of length $c$ on a one-dimensional plane and bend it to create a circle with circumference $c$ that's indexed from $0$ to $c - 1$. For example, if $c = 4$:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1484170037-5740fad055-101hack45-distant-pairs-ps.png)

We denote a *pair* of points, $a$ and $b$, as $\rho(a, b)$. We then plot $n$ pairs of points (meaning a total of $2 \cdot n$ individual points) at various indices along the circle's circumference. We define the distance $d(a, b)$ between points $a$ and $b$ in pair $\rho(a, b)$ as $min(|a-b|, c-|a-b|)$.

Next, let's consider two pairs: $\rho(a_i, b_i)$ and $\rho(a_j, b_j)$. We define distance $d(\rho(a_i, b_i), \rho(a_j, b_j))$ as the *minimum* of the six distances between any two points among points $a_i$, $b_i$, $a_j$, and $b_j$. In other words: 
$$d(\rho_i, \rho_j) = min(d(a_i, a_j), d(a_i, b_i), d(a_i, b_j), d(b_i, b_j), d(a_j, b_i), d(a_j, b_j))$$

For example, consider the following diagram in which the relationship between points in pairs at non-overlapping indices is shown by a connecting line:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1484174919-076032d241-101hack45-distant-pairs-ps-2.png)

Given $n$ pairs of points and the value of $c$, find and print the *maximum* value of $d(\rho_i, \rho_j)$, where $i \ne j$, among all pairs of points.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of pairs of points) and $c$ (the circumference of the circle).		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the values of $a_i$ and $b_i$ (i.e., the locations of the points in pair $i$).

## Output Format

Print a single integer denoting the maximum $d(\rho_i$, $\rho_j)$, where $i \ne j$.

## Constraints

- $1 \le c \le 10^6$
- $2 \le n \le 10^5$
- $0 \le a, b \lt c$

## Sample Input

5 8
0 4
2 6
1 5
3 7
4 4

## Sample Output

2

## Explanation

In the diagram below, the relationship between points in pairs at non-overlapping indices is shown by a connecting line:

As you can see, the maximum distance between any two pairs of points is , so we print  as our answer.
