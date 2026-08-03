# Longest Path

---

| Field | Value |
|---|---|
| **Slug** | `longest-path` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack33 |
| **URL** | https://www.hackerrank.com/challenges/longest-path |

---

## Preview

Find the longest path of black nodes in a tree.

## Problem Statement

You are given a tree with $N$ nodes. Each node can either be black or white. You need to find the longest path in this tree that consists only of black nodes.	
Nodes are numbered from $1$ to $N$.

## Input Format

The first line contains $N$ the number of nodes. 
The second line contains $N$ integers, representing $ c_i $ the colour of node $i$.	
Here, $c_i$ is $0$ for a white node and $1$ for a black node.		
The next line contains $N-1$ integers. The $i^{th}$ integer ($1$-indexed) represents the parent of node $i+1$, which is between $1$ and $i$. 	
$1$ is considered the root of the tree.	
You can assume that the input is a valid tree.

**Constraints** 


$1 \le N \le 10^5$

## Output Format

Output the length of the longest path containing only black nodes.

## Sample Tests

### Test 1

```
5 
1 1 0 1 1 
1 2 3 4
```

### Test 2

```
2
```
