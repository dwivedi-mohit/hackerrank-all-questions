# Heavy Light White Falcon

---

| Field | Value |
|---|---|
| **Slug** | `heavy-light-white-falcon` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/heavy-light-white-falcon |

---

## Preview

-

## Problem Statement

Our lazy white falcon finally decided to learn heavy-light decomposition. Her teacher gave an assignment for her to practice this new technique. Please help her by solving this problem. 

You are given a tree with $N$ nodes and each node's value is initially $0$. The problem asks you to operate the following two types of queries:

-	"1 u x" assign $x$ to the value of the node $u$.
-	"2 u v" print the maximum value of the nodes on the unique path between $u$ and $v$.

## Input Format

First line consists of two integers seperated by a space: $N$ and $Q$.<br></br>
Following $N - 1$ lines consisting of two integers denotes the undirectional edges of the tree. <br></br>
Following $Q$ lines consist of the queries you are asked to operate. 

**Constraints**

$1 \leq N,Q,x \leq 50000$<br></br>

It is guaranteed that input denotes a connected tree with $N$ nodes. Nodes are enumerated with 0-based indexing.

## Output Format

For each second type of query print single integer in a single line, denoting the asked maximum value.

## Sample Tests

### Test 1

```
3 3
0 1
1 2
1 0 1
1 1 2
2 0 2
```

### Test 2

```
2
```
