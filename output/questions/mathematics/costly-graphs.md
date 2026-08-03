# Costly Graphs

---

| Field | Value |
|---|---|
| **Slug** | `costly-graphs` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/costly-graphs |

---

## Preview

Find the total cost of all possible graphs, where the cost of a graph depends on the degrees of its nodes.

## Problem Statement

Let's define the _cost of a simple undirected graph_ as the sum of the costs of its nodes. The _cost of a node_ is defined as _D_<sup>_K_</sup>, where _D_ is its degree.

You are given _N_ and _K_. You need to find the sum of the costs of all possible simple undirected graphs with _N_ nodes. As this number may be very large, output the sum modulo _1005060097_.

**Definitions**

Here are a few definitions from graph theory in case you're not familiar with them.

An _undirected graph_ is an ordered pair (_V_, _E_) consisting of a set _V_ of _nodes_, and a set _E_ of _edges_ which consists of unordered pairs of nodes from _V_.

The _degree_ of a node is the number of edges incident to it.

A _simple undirected graph_ is an undirected graph with no loops and multiple edges. A _loop_ is an edge connecting a node to itself. _Multiple edges_ are two or more edges connecting the same pair of nodes.


**Input Format**

The first line contains the number of test cases _T_. 

Each of the next _T_ lines contains two integers _N_ and _K_ separated by a space.

**Output Format**

For each test case, output one line containing the sum of the costs of all possible simple undirected graphs with _N_ nodes, modulo _1005060097_.


**Constraints**

1 &le; _T_ &le; 2&middot;10<sup>5</sup>

1 &le; _N_ &le; 10<sup>9</sup>

1 &le; _K_ &le; 2&middot;10<sup>5</sup>

The sum of the _K_'s in a single test file is at most 2&middot;10<sup>5</sup>.

**Sample input**


    5
    1 1
    2 3
    3 2
    6 5
    20 20


**Sample Output**


    0
    2
    36
    67584000
    956922563

**Explanation** 

In the first case, there is only one simple graph with 1 node, and the cost of that graph is 0<sup>1</sup> = 0.

In the second case, there are two simple graphs with 2 nodes, one with a single edge and one with no edges.

The cost of the graph with a single edge is 1<sup>3</sup>+1<sup>3</sup> = 2.

The cost of the graph with no edges is 0<sup>3</sup>+0<sup>3</sup> = 0.

Thus, the total is 2+0 = 2.

In the third case, there are eight simple graphs with 3 nodes.

There is one graph with three edges, and its cost is 2<sup>2</sup>+2<sup>2</sup>+2<sup>2</sup> = 12.

There are three graphs with two edges, and the cost of each is 1<sup>2</sup>+1<sup>2</sup>+2<sup>2</sup> = 6.

There are three graphs with one edge, and the cost of each is 0<sup>2</sup>+1<sup>2</sup>+1<sup>2</sup> = 2.

There is one graph with no edges, and its cost is 0<sup>2</sup>+0<sup>2</sup>+0<sup>2</sup> = 0.

Thus, the total is 12&middot;1 + 6&middot;3 + 2&middot;3 + 0&middot;1 = 36.

## Sample Tests

### Test 1

```
5
1 1
2 3
3 2
6 5
20 20
```

### Test 2

```
0
2
36
67584000
956922563
```
