# Count Triplets

---

| Field | Value |
|---|---|
| **Slug** | `count-triplets-1` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 35 |
| **URL** | https://www.hackerrank.com/challenges/count-triplets-1 |

---

## Preview

Return the count of triplets that form a geometric progression.

## Problem Statement

You are given an array and you need to find number of tripets of indices $(i, j, k)$ such that the elements at those indices are in [geometric progression](https://en.wikipedia.org/wiki/Geometric_progression) for a given common ratio $r$ and $i \lt j \lt k$. 

**Example**  

$arr = [1, 4, 16, 64]$
$r = 4$ 


There are $[1, 4, 16]$ and $[4, 16, 64]$ at indices $(0, 1, 2)$ and $(1, 2, 3)$. Return $2$.  


**Function Description**

Complete the *countTriplets* function in the editor below. 


countTriplets has the following parameter(s):

- *int arr[n]:* an array of integers
- *int r*: the common ratio 


**Returns** 


- *int:* the number of triplets

## Input Format

The first line contains two space-separated integers $n$ and $r$, the size of $arr$ and the common ratio.   

The next line contains $n$ space-seperated integers $arr[i]$.

## Constraints

- $1 \leq n \leq 10^{5}$

- $1 \leq r \leq 10^{9}$

- $1 \leq arr[i] \leq 10^{9}$

## Sample Tests

### Test 1

```
4 2
1 2 2 4
```

### Test 2

```
2
```

### Test 3

```
6 3
1 3 9 9 27 81
```

### Test 4

```
6
```

### Test 5

```
5 5
1 5 5 25 125
```

### Test 6

```
4
```
