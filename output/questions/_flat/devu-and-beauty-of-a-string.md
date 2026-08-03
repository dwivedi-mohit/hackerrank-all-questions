# Devu and Beauty of a String

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-beauty-of-a-string` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **Contest** | 101hack25 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-beauty-of-a-string |

---

## Preview

Help Devu find beauty of a string.

## Problem Statement

Devu likes to play with strings a lot. He calls a string $good$ if there is no two or more consecutive equal characters in it. He also defines $beauty$ of a string as the number of $good$ substrings of it. Recently, he obtained a binary string $s$ consisting of either '0' or '1's.

As you know that Devu likes updates and query a lot, he wants to apply $Q$ operations as follows. Each operation is defined by three parameters, $type, l, r$. $l$ and $r$ are having $1$-based indices.

-	$type = 0$ means the operation is a query operation. For this query, you have to answer $beauty$ of substring $s[l, r]$.
-	$type = 1$ means the operation is an update operation. You have to flip all the characters of the substring $s[l, r]$

## Input Format

-	There is a single test case.
-	The first line will contain the string $s$.
-	The second line will contain an integer $Q$.
-	Then for the next $Q$ lines, each line will contain three space-separated integers $type, l, r$ according to operation as defined in the problem statement.

## Output Format

For each query operation, print a single line accordingly.

**Constraints**

-	$ 1\leq$ size of string s $\leq 10^5$
-	$ 1 \leq l \leq r \leq \text{size of string } s$

## Sample Tests

### Test 1

```
0110
5
0 1 4
0 1 2
1 1 2
0 1 4
0 1 2
```

### Test 2

```
6
3
10
3
```
