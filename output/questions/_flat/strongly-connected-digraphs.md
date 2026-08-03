# Strongly Connected Digraphs

---

| Field | Value |
|---|---|
| **Slug** | `strongly-connected-digraphs` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/strongly-connected-digraphs |

---

## Preview

Count the number of labeled strongly connected digraphs with the given number of vertices.

## Problem Statement

Count the number of [labeled strongly connected digraphs](http://en.wikipedia.org/wiki/Directed_graph) with the given number of vertices.


**Input Format**

The first line contains $T$, the number of queries.

Following are $T$ lines. Each line contains one integer $N$, denoting the number of vertices.


**Output Format**

Output $T$ lines. Each line is the number of labeled strongly connected digraphs with $N$ vertices, modulo $(10^9 + 7)$. 

**Constraints**

$1 \le T \le 1000$

$1 \le N \le 1000$


**Sample Input**

	5
	1
	2
	3
	4
	1000

**Sample Output**

	1
	1
    18
    1606
    871606913

**Explanation**

You can refer to [oeis](http://oeis.org/A003030).

## Sample Tests

### Test 1

```
5
1
2
3
4
1000
```

### Test 2

```
1
1
18
1606
871606913
```
