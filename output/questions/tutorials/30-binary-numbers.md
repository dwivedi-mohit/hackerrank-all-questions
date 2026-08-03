# Day 10: Binary Numbers

---

| Field | Value |
|---|---|
| **Slug** | `30-binary-numbers` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-binary-numbers |

---

## Preview

Find the maximum number of consecutive 1's in the base-2 representation of a base-10 number.

## Problem Statement

**Objective**	 
Today, we're working with binary numbers. Check out the [Tutorial](/challenges/30-binary-numbers/tutorial) tab for learning materials and an instructional video!	

**Task**	
Given a base-$10$ integer, $n$, convert it to binary (base-$2$). Then find and print the base-$10$ integer denoting the maximum number of consecutive $1$'s in $n$'s binary representation. When working with different bases, it is common to show the base as a subscript. 


**Example**

$n = 125$


The binary representation of $125_{10}$ is $1111101_2$.  In base $10$, there are $5$ and $1$ consecutive ones in two groups.  Print the maximum, $5$.

## Input Format

A single integer, $n$.

## Output Format

Print a single base-$10$ integer that denotes the maximum number of consecutive $1$'s in the binary representation of $n$.

**Sample Input 1**

	5
  

**Sample Output 1**

	1
  

**Sample Input 2**

	13
  

**Sample Output 2**

	2

## Constraints

- $1 \le n \le 10^{6}$

## Sample Tests

### Test 1

```
5
```

### Test 2

```
1
```

### Test 3

```
13
```

### Test 4

```
2
```
