# Black and White Tree

---

| Field | Value |
|---|---|
| **Slug** | `black-n-white-tree-1` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/black-n-white-tree-1 |

---

## Problem Statement

Nikita is making a graph as a birthday gift for her boyfriend, a fellow programmer! She drew an undirected connected graph with $N$ nodes numbered from $1$ to $N$ in her notebook.

Each node is shaded in either *white* or *black*. We define $n_W$ to be the number of white nodes, and $n_B$ to be the number of black nodes. The graph is drawn in such a way that:

* No $2$ adjacent nodes have same coloring.
* The value of $|n_W - n_B|$, which we'll call $D$, is minimal.

Nikita's mischievous little brother erased some of the edges and all of the coloring from her graph! As a result, the graph is now decomposed into one or more components. Because you're her best friend, you've decided to help her reconstruct the graph by adding $K$ edges such that the aforementioned graph properties hold true.

Given the decomposed graph, construct and shade a valid connected graph such that the difference $|n_W - n_B|$ between its shaded nodes is minimal.

## Input Format

The first line contains $2$ space-separated integers, $N$ (the number of nodes in the original graph) and $M$ (the number of edges in the decomposed graph), respectively. 	
The $M$ subsequent lines each contain $2$ space-separated integers, $u$ and $v$, describing a bidirectional edge between nodes $u$ and $v$ in the decomposed graph.

## Output Format

You must have $K+1$ lines of output. 
The first line contains $2$ space-separated integers: $D$ (the minimum possible value of $|n_B-n_W|$) and $K$ (the number of edges you've added to the graph), respectively. 	
Each of the $K$ subsequent lines contains $2$ space-separated integers, $u$ and $v$, describing a newly-added bidirectional edge in your final graph (i.e.: new edge $u \leftrightarrow v$). 

You may print *any* $1$ of the possible reconstructions of Nikita's graph such that the value of $D$ in the reconstructed shaded graph is minimal.

**Sample Input 0**
   

     8 8
     1 2
     2 3
     3 4
     4 1
     1 5
     2 6
     3 7
     4 8
 
 **Sample output 0**

	0 0
 
 **Sample Input 1**
 
     8 6
     1 2
     3 4
     3 5
     3 6
     3 7
     3 8
 
 **Sample Output 1**
 	
    4 1
    1 5
 
 **Sample Input 2**
   

     5 4
     1 2
     2 3
     3 4
     4 1
 
 **Sample Output 2**


      1 2
      2 5
      4 5

## Constraints

* $1 \le N \le 2 \times 10^5$
* $0 \le M \le min(5 \times 10^5, \frac{N \times (N-1)}{2})$
* It is guaranteed that every edge will be between $2$ distinct nodes, and there will never be more than $1$ edge between any $2$ nodes.
* Your answer *must* meet the following criteria:
	* The graph is connected and no $2$ adjacent nodes have the same coloring.
	* The value of $|n_B-n_W|$ is minimal.
	* $K \le 2 \times 10^5$

## Sample Tests

### Test 1

```
8 8
 1 2
 2 3
 3 4
 4 1
 1 5
 2 6
 3 7
 4 8
```

### Test 2

```
0 0
```

### Test 3

```
8 6
 1 2
 3 4
 3 5
 3 6
 3 7
 3 8
```

### Test 4

```
4 1
1 5
```

### Test 5

```
5 4
 1 2
 2 3
 3 4
 4 1
```

### Test 6

```
1 2
 2 5
 4 5
```
