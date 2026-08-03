# Quadrant Queries

---

| Field | Value |
|---|---|
| **Slug** | `quadrant-queries` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/quadrant-queries |

---

## Preview

How many points on a grid lie in each quadrant? What happens after performing various reflection operations?

## Problem Statement

There are $n$ points on a plane.  Each point $p[i]$ is described by $[x[i], y[i]]$, where $1 \le i \le n$. There are three types of queries needed: 
  

1. `X i j` Reflect all points in the inclusive range between points $p[i]$ and $p[j]$ along the $x$-axis.

2. `Y i j` Reflect all points in the inclusive range between points $p[i]$ and $p[j]$ along the $y$-axis. 
3. `C i j` Count the number of points in the inclusive range between points $p[i]$ and $p[j]$ in each of the $4$ quadrants. Then print a single line of four space-separated integers describing the respective numbers of points in the first, second, third, and fourth quadrants in that order. 

As a reminder, the four quadrants of a graph are labeled as follows:		
    ![](https://static.hackerrank.com/hackerrank/quadrant-queries.gif)

Given a set of $n$ points and $q$ queries, perform each query in order. For example, given points $p = [(1,1), (-1, -1)]$ and $queries = [\texttt{'X 1 2', 'C 1 2', 'Y 1 1' 'C 1 2'}]$.  Initially the points are in quadrants $1$ and $3$.  The first query says to reflect points with indices from $1$ to $2$ along the $x$-axis.  After the query, $p = [(1, -1), (-1, 1)]$ and quadrants are $4$ and $2$.  The next query prints the number of points in each quadrant: `0 1 0 1`.  The third query says to reflect the point with index $1$ to $1$ along the $y$-axis, so now $p = [(-1, -1), (-1, 1)]$.  The points now lie in quadrants $3$ and $2$, so the fourth query output is `0 1 1 0`.

**Note:** Points may sometimes share the same coordinates.


**Function Description**


Complete the *quadrants* function in the editor below.  It should print the results of each `C` type query on a new line.


quadrants has the following parameters:

- *p[p[1]...p[n]]*: a 2-dimensional array of integers where each element $p[i]$ contains two integers  $x[i]$ and $y[i]$

- *queries[queries[1]...queries[n]*: an array of strings

## Input Format

The first line contains a single integer, $n$, that denotes the number of points. 	
Each line $i$ of the $n$ subsequent lines contains two space-separated integers that describe the respective $x[i]$ and $y[i]$ values for point $p[i]$ .  	
The next line contains a single integer, $q$, that denotes the number of queries. 	
Each of the $q$ subsequent lines contains three space-separated values that describe a query in one of the three forms defined above.

## Output Format

For each query of type `C i j`, print four space-separated integers that describe the number of points having indices in the inclusive range between $i$ and $j$ in the first, second, third, and fourth graph quadrants in that order.

## Constraints

- $1 \le n \le 10^5 $
- $1 \le q \le 10^6$

- No point lies on the $x$ or $y$ axes.
- $1 \le x[i], y[i] \le 2^{31}-1$
- In all queries, $1 \le i \le j \le n$.

## Sample Tests

### Test 1

```
4
1 1
-1 1
-1 -1
1 -1
5
C 1 4
X 2 4
C 3 4
Y 1 2
C 1 3
```

### Test 2

```
1 1 1 1
1 1 0 0
0 2 0 1
```
