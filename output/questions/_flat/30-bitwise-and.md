# Day 29: Bitwise AND

---

| Field | Value |
|---|---|
| **Slug** | `30-bitwise-and` |
| **Domain** | tutorials |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-bitwise-and |

---

## Preview

Apply everything we've learned in this bitwise AND challenge.

## Problem Statement

**Objective**		
Welcome to the last day! Today, we're discussing bitwise operations. Check out the [Tutorial](/challenges/30-bitwise-and/tutorial) tab for learning materials and an instructional video!	

**Task**	
Given set $S = \{1, 2, 3,\ldots, N\}$. Find two integers, $A$ and $B$ (where $A \lt B$), from set $S$ such that the value of $A \text{&} B$ is the maximum possible *and also less than a given integer, $K$*. In this case, $\text{&}$ represents the *bitwise AND* operator.

**Function Description** 

Complete the *bitwiseAnd* function in the editor below.  


*bitwiseAnd* has the following paramter(s): 

- *int N:* the maximum integer to consider 

- *int K:* the limit of the result, inclusive 


**Returns** 

- *int:* the maximum value of $A \& B$ within the limit.

## Input Format

The first line contains an integer, $T$, the number of test cases. 		
Each of the $T$ subsequent lines defines a test case as $2$ space-separated integers, $N$ and $K$, respectively.

## Constraints

* $1 \le T \le 10^3$
* $2 \le N \le 10^3$
* $2 \le K \le N$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
3 T = 3
5 2 N = 5, K = 2
8 5 N = 8, K = 5
2 2 N = 2, K = 2
```

### Test 2

```
1
4
0
```
