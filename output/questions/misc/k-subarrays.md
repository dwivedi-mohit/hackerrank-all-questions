# K-Subarrays

---

| Field | Value |
|---|---|
| **Slug** | `k-subarrays` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/k-subarrays |

---

## Preview

Given a large list of positive integers, count the number of k-subsequences.

## Problem Statement

Given a large list of positive integers, count the number of k-subsequences.

A _k-subarray_ of an array is defined as follows:

- It is a subarray, i.e. made of contiguous elements in the array
- The _sum_ of the subarray elements, _s_, is evenly divisible by _k, _i.e.: _sum mod k = 0_.

 

Given an array of integers, determine the number of _k-subarrays_ it contains.  For example, _k = 5_ and the array _nums = [5, 10, 11, 9, 5]._  The  _10 k-subarrays_ are: _{5}, {5, 10}, {5, 10, 11, 9}, {5, 10, 11, 9, 5}, {10}, {10, 11, 9}, {10, 11, 9, 5}, {11, 9}, {11, 9, 5}, {5}._

 

**Function Description **

Complete the function _kSub_ in the editor below. The function must return a long integer that represents the number of _k-subarrays_ in the array.

 

_kSub_ has the following parameter(s):

    _k:_  the integer divisor of a k-subarray

    _nums[nums[0],...nums[n-1]]:_  an array of integers

 

Constraints

- _1 ≤ n ≤ 3 × 105_
- _1 ≤ k ≤ 100_
- _1 ≤ nums[i] ≤ 104_

 

Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer, _k, _the number the sum of the subarray must be divisible by.

The next line contains an integer, _n_, that denotes the number of elements in _nums_.

Each line _i_ of the _n_ subsequent lines (where _0 ≤ i < n_) contains an integer that describes _nums[i]_.

  Sample Case 0

Sample Input For Custom Testing

**Sample Input 0**

    3 
    5 
    1
    2
    3
    4
    1

 

**Sample Output 0**

    4

 

**Explanation 0**

The _4_ subarrays of _nums_ having sums that are evenly divisible by _k = 3_ are _{3}_, _{1, 2}_, _{1, 2, 3}_, _{2, 3, 4}_.

## Sample Tests

### Test 1

```
3 
5 
1
2
3
4
1
```

### Test 2

```
4
```
