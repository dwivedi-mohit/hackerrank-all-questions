# Max Array Sum 

---

| Field | Value |
|---|---|
| **Slug** | `max-array-sum` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/max-array-sum |

---

## Preview

Find the maximum sum of elements in an array.

## Problem Statement

Given an array of integers, find the subset of non-adjacent elements with the maximum sum.  Calculate the sum of that subset.  It is possible that the maximum sum is $0$, the case when all elements are negative.


**Example** 

$arr = [-2, 1, 3, -4, 5]$ 


The following subsets with more than $1$ element exist.  These exclude the empty subset and single element subsets which are also valid.


	Subset		Sum
	[-2, 3, 5]	 6
    [-2, 3]		 1
    [-2, -4]	-6
    [-2, 5]		 3
    [1, -4]		-3
    [1, 5]		 6
    [3, 5]		 8
 
The maximum subset sum is $8$.  Note that any individual element is a subset as well.


$arr = [-2, -3, -1]$  


In this case, it is best to choose no element: return $0$.

**Function Description**

Complete the $maxSubsetSum$ function in the editor below. 


maxSubsetSum has the following parameter(s):

- *int arr[n]:* an array of integers 


**Returns** 

- *int:* the maximum subset sum

## Input Format

The first line contains an integer, $n$.

The second line contains $n$ space-separated integers $arr[i]$.

## Constraints

+ $1 \le n \le 10^5$
+ $-10^4 \le arr[i] \le 10^4$

## Sample Tests

### Test 1

```
Subset Sum
[-2, 3, 5] 6
[-2, 3] 1
[-2, -4] -6
[-2, 5] 3
[1, -4] -3
[1, 5] 6
[3, 5] 8
```

### Test 2

```
5
3 7 4 6 5
```

### Test 3

```
13
```

### Test 4

```
5
2 1 5 8 4
```

### Test 5

```
11
```

### Test 6

```
5
3 5 -7 8 10
```

### Test 7

```
15
```
