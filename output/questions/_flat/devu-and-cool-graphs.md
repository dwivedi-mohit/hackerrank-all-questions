# Devu and Cool Graphs

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-cool-graphs` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 75 |
| **Contest** | 101hack23 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-cool-graphs |

---

## Preview

Help Devu count the number of cool graphs.

## Problem Statement

Devu loves playing with different kinds of graphs a lot. One day he thought about an interesting category of graphs called "cool" graphs which are generated the following way.

Let the set of vertices be $\{1, 2, 3, ..., n\}$. You have to start from left to right (i.e. from vertex $1$ to $n$). At vertex $i$, you can make one of the following two decisions.

-	Add edges between this vertex and all the previous vertices (i.e. from vertex $1$ to $i - 1$). 
-	Don't add any edges between this vertex and any of the previous vertices.

Now Devu is interested in finding the number of "cool" graphs of $n$ vertices having a [perfect matching][111]. Print the answer modulo $(10^9 + 7)$. 

[111]: http://mathworld.wolfram.com/PerfectMatching.html

## Input Format

-	The first line of the input contains a single integer, $T$, denoting the number of test cases.
-	For each test case, there is a single line containing an integer, $n$, denoting the number of vertices of the graph.

## Output Format

For each test case, print a single line containing a single integer denoting the answer to the problem.

**Constraints**

-	$1 \leq T \leq 100$
-	$1 \leq n \leq 10^5$

## Sample Tests

### Test 1

```
2
1
2
```

### Test 2

```
0
1
```
