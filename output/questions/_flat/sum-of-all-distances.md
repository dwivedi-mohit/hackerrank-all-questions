# Sum of all Distances

---

| Field | Value |
|---|---|
| **Slug** | `sum-of-all-distances` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack22 |
| **URL** | https://www.hackerrank.com/challenges/sum-of-all-distances |

---

## Problem Statement

You are given a weighted [tree](http://en.wikipedia.org/wiki/Tree_(graph_theory)) with $N$ nodes. Nodes are numbered from $1$ to $N$. 


or each node, you need to print the sum of the distance of the nodes to all other nodes. Mathematically, for each node $n$, print the value of the expression

$\sum_{i=1}^N$ $Distance from node n to i^{th} node$.

## Input Format

The first line contains $T$, the number of test cases.

For each test case, there are multiple lines. The first line contains $N$, the number of nodes in the tree. The next $N-1$ lines describe the tree; each line contains $3$ integers $X$, $Y$, and $Z$, which denote that there is an edge from $X$ to $Y$ with weight $Z$. 


**Constraints**

Sum of $N$ over all test cases $<= 200000$

$1 <= N <= 100000$ 

$1 <= X,Y <= N$ 

$1 <= Z <= 1000000$

## Output Format

For each test case, output exactly $N$ lines. 

The $i^{th}$ line should contain the answer for the $i^{th}$ node.

## Sample Tests

### Test 1

```
3
4
1 4 7
2 3 5
4 2 6
4
1 2 2
3 1 4
4 3 5
4
1 2 5
2 3 1
3 4 3
```

### Test 2

```
38
24
34
24
15
19
15
25
20
10
10
16
```
