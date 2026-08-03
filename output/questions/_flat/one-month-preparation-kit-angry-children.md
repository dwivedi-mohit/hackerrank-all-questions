# Max Min

---

| Field | Value |
|---|---|
| **Slug** | `one-month-preparation-kit-angry-children` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children |

---

## Preview

Given a list of N integers, your task is to select K integers from
 the list such that its unfairness is minimized.

## Problem Statement

You will be given a list of integers, $arr$, and a single integer $k$.  You must create an array of length $k$ from elements of $arr$ such that its *unfairness* is minimized. Call that array $arr'$.  Unfairness of an array is calculated as

$$max(arr') - min(arr')$$


Where:

- _max_ denotes the largest integer in $arr'.$

- _min_ denotes the smallest integer in $arr'.$

 
**Example**


$arr = [1, 4, 7, 2]$

$k = 2$   


Pick any two elements, say $arr' = [4, 7]$.

$unfairness = max(4,7) - min(4,7) = 7 - 4 = 3$

Testing for all pairs, the solution $[1, 2]$ provides the minimum unfairness.

**Note**: Integers in $arr$ may not be unique. 

**Function Description**

Complete the *maxMin* function in the editor below.

maxMin has the following parameter(s):

- *int k:*  the number of elements to select

- *int arr[n]:*: an array of integers 


**Returns**


- *int:* the minimum possible _unfairness_

## Input Format

The first line contains an integer $n$, the number of elements in array $arr$.

The second line contains an integer $k$.

Each of the next $n$ lines contains an integer $arr[i]$ where $0 \le i < n$.

## Constraints

$2 \le n \le 10^5$

$2 \le k \le n$

$0 \le arr[i] \le 10^9$

## Sample Tests

### Test 1

```
10
4
1
2
3
4
10
20
30
40
100
200
```

### Test 2

```
3
```

### Test 3

```
max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
```
