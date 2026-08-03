# Sherlock and Array

---

| Field | Value |
|---|---|
| **Slug** | `one-month-preparation-kit-sherlock-and-array` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array |

---

## Preview

Check whether there exists an element in the array such that sum of elements on its left is equal to the sum of elements on its right.

## Problem Statement

Watson gives Sherlock an array of integers.  His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.


**Example**


$arr = [5, 6, 8, 11]$


$8$ is between two subarrays that sum to $11$.


$arr = [1]$


The answer is $[1]$ since left and right sum to $0$.

You will be given arrays of integers and must determine whether there is an element that meets the criterion.  If there is, return `YES`.  Otherwise, return `NO`.

**Function Description**


Complete the *balancedSums* function in the editor below.


balancedSums has the following parameter(s):


- *int arr[n]:* an array of integers


**Returns**


- *string:*  either `YES` or `NO`

## Input Format

The first line contains $T$, the number of test cases.


The next $T$ pairs of lines each represent a test case.

- The first line contains $n$, the number of elements in the array $arr$.

- The second line contains $n$ space-separated integers $arr[i]$ where $0 \le i < n$.

## Constraints

$1 \le T \le 10$  

$1 \le n \le 10^5$ 

$1 \le arr[i] \le 2 \times 10^4$

$0 \le i < n$

## Sample Tests

### Test 1

```
2
3
1 2 3
4
1 2 3 3
```

### Test 2

```
NO
YES
```
