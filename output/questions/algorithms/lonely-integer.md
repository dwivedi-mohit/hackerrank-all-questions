# Lonely Integer

---

| Field | Value |
|---|---|
| **Slug** | `lonely-integer` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/lonely-integer |

---

## Preview

Find the unique element in an array of integer pairs.

## Problem Statement

Given an array of integers, where all elements but one occur twice, find the unique element.


**Example**

$a = [1, 2, 3, 4, 3, 2, 1]$


The unique element is $4$.


**Function Description**


Complete the *lonelyinteger* function in the editor below. 


lonelyinteger has the following parameter(s):


- *int a[n]*: an array of integers 


**Returns**


- *int:* the element that occurs only once

## Input Format

The first line contains a single integer, $n$, the number of integers in the array.		
The second line contains $n$ space-separated integers that describe the values in $a$.

## Constraints

- $1 \le n \lt 100$

- It is guaranteed that $n$ is an odd number and that there is one unique element.

- $0 \le a[i] \le 100$, where $0 \le i \lt n$.

## Sample Tests

### Test 1

```
1
1
```

### Test 2

```
1
```

### Test 3

```
3
1 1 2
```

### Test 4

```
2
```

### Test 5

```
5
0 0 1 2 1
```

### Test 6

```
2
```
