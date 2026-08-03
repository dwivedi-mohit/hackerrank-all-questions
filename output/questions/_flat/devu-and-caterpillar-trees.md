# Devu and Caterpillar Trees

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-caterpillar-trees` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 150 |
| **Contest** | 101hack23 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-caterpillar-trees |

---

## Preview

Help Devu count dominating sets in caterpillar trees.

## Problem Statement

Devu likes to play with caterpillar trees. A tree is called a _caterpillar tree_ if there exists a central path whose removal splits the tree into a collection of [path graphs][222]. 

Devu wants to calculate the number of [dominating sets][111] in the caterpillar tree $G$. Print the answer modulo $(10^9 + 7)$.

Let $G'$ be a caterpillar tree with $n$ vertices. You are provided an array $extra$ of size $n$. $extra_i$ denotes that an extra path of $extra_i$ nodes will be attached to the $i^{th}$ vertex. It is guaranteed that for a non-leaf node, the value of $extra$ will be zero.

The modified tree, after adding the extra path as specifed above to tree $G'$, will be tree $G$. So the total number of vertices in the tree $G$ will be $n + \sum_{i = 1}^{n} extra_i$.

[111]: http://en.wikipedia.org/wiki/Dominating_set
[222]: http://mathworld.wolfram.com/PathGraph.html

## Input Format

-	There is a single test case in the problem.
-	There are $n + 1$ lines of the input. 
	-	The first line will contain a single integer $n$.
    -	The next $n - 1$ lines each contain two space-separated integers, $u, v $ ($1$ based indexing) denoting that there is an edge between $u$ and $v$ in $G'$. It is guaranteed that there won't be multi-edges or loops in $G'$.
    -	The next line contains $n$ space-separated integers denoting the array $extra$.

## Output Format

Print a single integer corresponding to the answer to the problem.

**Constraints**


-	$1 \leq n \leq 10^5$
-	$0 \leq extra[i] \leq 10^9$

**Sample Input 01**

	3
    1 2
    2 3
    0 0 0

**Sample Output 01**


	5
 

**Sample Input 02**
  

    4
    1 2
    2 3
    2 4
    0 0 2 0
  

**Sample Output 02**


    29

## Sample Tests

### Test 1

```
3
1 2
2 3
0 0 0
```

### Test 2

```
5
```

### Test 3

```
4
1 2
2 3
2 4
0 0 2 0
```

### Test 4

```
29
```
