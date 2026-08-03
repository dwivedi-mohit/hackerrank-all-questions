# Roads and Libraries

---

| Field | Value |
|---|---|
| **Slug** | `torque-and-development` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/torque-and-development |

---

## Preview

Help the ruler of HackerLand determine the cheapest way to give his citizens access to libraries.

## Problem Statement

Determine the minimum cost to provide library access to all citizens of HackerLand.  There are $n$ cities numbered from $1$ to $n$. Currently there are no libraries and the cities are not connected.  Bidirectional roads may be built between any city pair listed in $cities$. A citizen has access to a library if:

* Their city contains a library.
* They can travel by road from their city to a city containing a library.

__Example__


The following figure is a sample map of HackerLand where the dotted lines denote possible roads:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481983010-b779ad2b2b-torque1.png)

$c\_road = 2$

$c\_lib = 3$

$cities = [[1, 7], [1, 3], [1,2], [2, 3], [5, 6], [6, 8]]$


The cost of building any road is $c\_road = 2$, and the cost to build a library in any city is $c\_lib = 3$.  Build $5$ roads at a cost of $5 \times 2 = 10$ and $2$ libraries for a cost of $6$.  One of the available roads in the cycle $1 \rightarrow 2 \rightarrow 3 \rightarrow 1$ is not necessary. 


There are $q$ queries, where each query consists of a map of HackerLand and value of $c\_lib$ and $c\_road$. For each query, find the minimum cost to make libraries accessible to all the citizens.

**Function Description**

Complete the function *roadsAndLibraries* in the editor below.

roadsAndLibraries has the following parameters:

- *int n*: integer, the number of cities

- *int c_lib*: integer, the cost to build a library

- *int c_road*: integer, the cost to repair a road

- *int cities[m][2]*: each $cities[i]$ contains two integers that represent cities that can be connected by a new road


**Returns** 

- *int*:  the minimal cost

## Input Format

The first line contains a single integer $q$, that denotes the number of queries. 

The subsequent lines describe each query in the following format:

- The first line contains four space-separated integers that describe the respective values of $n$, $m$, $c\_lib$ and $c\_road$, the number of cities, number of roads, cost of a library and cost of a road.  

- Each of the next $m$ lines contains two space-separated integers, $u[i]$ and $v[i]$, that describe a bidirectional road that can be built to connect cities $u[i]$ and $v[i]$.

## Constraints

* $1 \le q \le 10$
* $1 \le n \le 10^5$ 
* $0 \le m \le min(10^5, \large \frac{n \cdot (n-1)}{2})$
* $1 \le c\_road,c\_lib \le 10^5$
* $1 \le u[i], v[i] \le n$
* Each road connects two distinct cities.

## Sample Tests

### Test 1

```
STDIN Function
----- --------
2 q = 2
3 3 2 1 n = 3, cities[] size m = 3, c_lib = 2, c_road = 1
1 2 cities = [[1, 2], [3, 1], [2, 3]]
3 1
2 3
6 6 2 5 n = 6, cities[] size m = 6, c_lib = 2, c_road = 5
1 3 cities = [[1, 3], [3, 4],...]
3 4
2 4
1 2
2 3
5 6
```

### Test 2

```
4
12
```
