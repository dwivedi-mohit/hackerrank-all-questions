# Zurikela's Graph

---

| Field | Value |
|---|---|
| **Slug** | `zurikela` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/zurikela |

---

## Preview

Build a graph.

## Problem Statement

Zurikela is creating a graph with a special graph maker. At the begining, it is empty and has no nodes or edges. He can perform $3$ types of operations:	

1. $A$ $x$: Create a set of $x$ new nodes and name it $set$-$K$.	
2. $B$ $x$ $y$: Create edges between nodes of $set$-$x$ and $set$-$y$.		
3. $C$ $x$: Create a set composed of nodes from $set$-$x$ and its directly and indirectly connected nodes, called $set$-$K$. Note that each node can only exist in one set, so other sets become empty.		

The first $set$'s name will be $set$-$1$. In first and third operation $K$ is referring to the index of new set:
	
    K = [index of last created set] + 1


Create the graph by completing the $Q$ operations specified during input. Then calculate the [maximum number of independent nodes](https://en.wikipedia.org/wiki/Independent_set_(graph_theory)) (i.e.:how many nodes in the final graph which don't have direct edge between them).

## Input Format

The first line contains $Q$.		
The $Q$ subsequent lines each contain an operation to be performed.

**Constraints** <br>
$ 1 \le Q \le 10^5 $.<br>
For the first operation, $1 \le x \le 10^4$. <br>
For the second operation, $x<y$ and all $y$s are *distinct*.<br>
For the second and third operation, it's guaranteed that $set$-$x$ and $set$-$y$ exist.

## Output Format

Print maximum number of *independent nodes* in the final graph (i.e.: nodes which have no direct connection to one another).

## Sample Tests

### Test 1

```
K = [index of last created set] + 1
```

### Test 2

```
8
A 1
A 2
B 1 2
C 1
A 2
A 3
B 3 4
B 4 5
```

### Test 3

```
5
```
