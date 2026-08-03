# Range Minimum Query

---

| Field | Value |
|---|---|
| **Slug** | `range-minimum-query` |
| **Domain** | fp |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/range-minimum-query |

---

## Preview

Find the minimum value in a range.

## Problem Statement

Range Minimum Query ([RMQ](http://en.wikipedia.org/wiki/Range_Minimum_Query)) is a set of problems which deals with finding a property (here minimum) of a range. Segment Tree can be very helpful when solving with such problems. A segment tree is a tree like data structure which is used to store the information about intervals. Here's the [([wiki link](http://en.wikipedia.org/wiki/Segment_tree))] of it.

You are given a array of _N_ integers, _arr[0], arr[1], .., arr[(N-1)]_. And you are given a list of ranges. For each range, _(l, r)_ you have to find the minimum value between range _arr[l], arr[l+1], arr[l+2], .., arr[r]_.

**Input**

First line will contain two integers, _N M_, length of array and number of queries. Then in next line, there are N space separated integers which represent the array, _arr[0], arr[1], .., arr[N-1]_. Then _M_ line follows. Each _M_ line will contain two integers, _l r_, representing a range.

**Output**

For each range, _(l, r)_, you have to print the minimum integer in subarray _arr[l], arr[l+1], .., arr[r]_ in separate line.

**Constraints**

_1 <= N, M <= 10<sup>5</sup>_

_-10<sup>5</sup> <= arr[i] <= 10<sup>5</sup>_  , where _0 <= i < N_ 

_0 <= l <= r < N_


**Sample Input**


    10 5
    10 20 30 40 11 22 33 44 15 5
    0 5
    1 2
    8 9
    0 9
    4 6

**Sample Output**


    10
    20
    5
    5
    11

**Explanation**


+ For range (0, 5), subarray will be [10, 20, 30, 40, 11, 22]. So minimum value will be 10.
+ For range (1, 2), subarray will be [20, 30]. Minimum value = 20.
+ For range (8, 9), subarray is [15, 5]. Minimum value = 5.
+ For range (0, 9), Here we have to find the minimum (5) of the whole array.
+ For range (3, 5), subarray is [40, 11, 22]. Minimum value = 11.

## Sample Tests

### Test 1

```
10 5
10 20 30 40 11 22 33 44 15 5
0 5
1 2
8 9
0 9
4 6
```

### Test 2

```
10
20
5
5
11
```
