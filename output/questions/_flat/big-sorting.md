# Big Sorting

---

| Field | Value |
|---|---|
| **Slug** | `big-sorting` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/big-sorting |

---

## Preview

Sort an array of very long numeric strings.

## Problem Statement

Consider an array of numeric strings where each string is a positive number with anywhere from $1$ to $10^6$ digits. Sort the array's elements in *non-decreasing*, or ascending order of their integer values and return the sorted array.

**Example**

$unsorted = \text{['1', '200', '150', '3']}$


Return the array ['1', '3', '150', '200']. 

**Function Description**


Complete the *bigSorting* function in the editor below.


bigSorting has the following parameter(s):


- *string unsorted[n]:* an unsorted array of integers as strings


**Returns**


- *string[n]:*  the array sorted in numerical order

## Input Format

The first line contains an integer, $n$, the number of strings in $unsorted$.		
Each of the $n$ subsequent lines contains an integer string, $unsorted[i]$.

## Constraints

* $1 \le n \le 2 \times 10^5$
* Each string is guaranteed to represent a positive integer.
* There will be no leading zeros.
* The total number of digits across all strings in $unsorted$ is between $1$ and $10^6$ (inclusive).

## Sample Tests

### Test 1

```
6
31415926535897932384626433832795
1
3
10
3
5
```

### Test 2

```
1
3
3
5
10
31415926535897932384626433832795
```

### Test 3

```
8
1
2
100
12303479849857341718340192371
3084193741082937
3084193741082938
111
200
```

### Test 4

```
1
2
100
111
200
3084193741082937
3084193741082938
12303479849857341718340192371
```
