# Wire Removal

---

| Field | Value |
|---|---|
| **Slug** | `wire-removal` |
| **Contest** | hourrank-24 |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/wire-removal |

---

## Problem Statement

<!--
[Diwali](https://en.wikipedia.org/wiki/Diwali) is the most popular festival in India. It is also known as "The festival of lights" because it spiritually signifies the victory of light over darkness and good over evil. Before Diwali night, people decorate their homes with millions of lights shining on housetops. 

-->

While decorating her house for [Diwali](https://en.wikipedia.org/wiki/Diwali), Anne noticed a *rice light* shaped like a [rooted tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)). We represent the lighting elements as the vertices of the tree and the wires that connect them as the edges. It was hanging from a firm support on the ceiling which we call the *root* of the rice light. The vertices are numbered $1$ to $n$ with $1$ as the root.

<!--
Before:

We can assume the probability of any wire breaking to be directly proportional to its distance from the support. We define the distance of a wire joining lighting elements $u$ and $v$ as the maximum of the [distance](https://en.wikipedia.org/wiki/Distance_(graph_theory)) of $u$ or $v$ from the support (root). 

After:

The probability of any wire breaking depends on the total weight of the lighting elements exerted by the particular branch.

If a wire breaks, the portion of the rice light that got disconnected from the support shatters on the floor, while the other portion remains intact and still hanging from the ceiling.

![image](https://s3.amazonaws.com/hr-assets/0/1504972450-b293ba838a-edge-removal1.png)

One of the wires randomly breaks. Find the [expected](http://en.wikipedia.org/wiki/Expected_value) number of vertices still connected to the ceiling.
-->

The probability of any wire breaking is directly proportional to its distance from the support. The distance of a wire joining lighting elements $u$ and $v$ is considered as the maximum of the [distance](https://en.wikipedia.org/wiki/Distance_(graph_theory)) of $u$ or $v$ from the support (root). 

If a wire breaks, the portion of the rice light that got disconnected from the support shatters on the floor, while the other portion remains intact and still hanging from the ceiling.

This image illustrates the case where the wire joining lighting elements $1$ and $3$ breaks. In this case, three elements ($3$, $6$, $7$) shatters and four elements ($1$, $2$, $4$, $5$) remain connected to the ceiling.

![image](https://s3.amazonaws.com/hr-assets/0/1504972450-b293ba838a-edge-removal1.png)

Given that exactly one of the wires randomly breaks, find the [expected](http://en.wikipedia.org/wiki/Expected_value) number of vertices still connected to the ceiling.

## Input Format

The first line contains a single integer $n$ denoting the number of vertices in the tree. The vertices are numbered $1$ to $n$, with $1$ as the root.  

The next $n - 1$ lines each contains two space-separated integers $x$ and $y$ denoting that there is an edge between vertex $x$ and $y$.

## Output Format

Print a single line containing a single real number denoting the answer. Your answer is considered correct if its absolute error doesn't exceed $10^{-5}$.

## Constraints

- $2 \le n \le 10^{5}$  
- $1 \le x, y \le n$  
- It is guaranteed that the graph is a tree.
