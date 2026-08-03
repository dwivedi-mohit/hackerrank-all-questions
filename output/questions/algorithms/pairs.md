# Pairs

---

| Field | Value |
|---|---|
| **Slug** | `pairs` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/pairs |

---

## Preview

Given N numbers, count the total pairs of numbers that have a  difference of K.

## Problem Statement

Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.


**Example** 

$k = 1$

$arr = [1, 2, 3, 4]$ 


There are three values that differ by $k = 1$: $2-1 = 1$, $3-2 = 1$, and $4-3 = 1$.  Return $3$.


**Function Description**

Complete the *pairs* function below. 


pairs has the following parameter(s):

- *int k:* an integer, the target difference
- *int arr[n]:* an array of integers 


**Returns** 


- *int:* the number of pairs that satisfy the criterion

## Input Format

The first line contains two space-separated integers $n$ and $k$, the size of $arr$ and the target value.   

The second line contains $n$ space-separated integers of the array $arr$.

## Constraints

- $2 \le n \le 10^5$

- $0 \lt k \lt 10^9$

- $0 \lt arr[i] \lt 2^{31} - 1$  

- each integer $arr[i]$ will be unique

## Sample Tests

### Test 1

```
STDIN Function
----- --------
5 2 arr[] size n = 5, k =2
1 5 3 4 2 arr = [1, 5, 3, 4, 2]
```

### Test 2

```
3
```
