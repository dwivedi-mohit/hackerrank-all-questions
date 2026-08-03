# Min Max Riddle

---

| Field | Value |
|---|---|
| **Slug** | `min-max-riddle` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/min-max-riddle |

---

## Preview

Maximum of minimum for every sized subarray.

## Problem Statement

Given an integer array of size $n$, find the maximum of the minimum(s) of every window size in the array. The window size varies from $1$ to $n$.


For example, given $arr = [6, 3, 5, 1, 12]$, consider window sizes of $1$ through $5$.  Windows of size $1$ are $(6), (3), (5), (1), (12)$.  The maximum value of the minimum values of these windows is $12$.  Windows of size $2$ are $(6,3), (3,5), (5,1), (1,12)$ and their minima are $(3, 3, 1, 1)$.  The maximum of these values is $3$.  Continue this process through window size $5$ to finally consider the entire array.  All of the answers are $12, 3, 3, 1, 1$.

**Function Description**

Complete the *riddle* function in the editor below.  It must return an array of integers representing the maximum minimum value for each window size from $1$ to $n$.


riddle has the following parameter(s):

- *arr*: an array of integers

## Input Format

The first line contains a single integer, $n$, the size of $arr$.

The second line contains $n$ space-separated integers, each an $arr[i]$.

## Output Format

Single line containing $n$ space-separated integers denoting the output for each window size from $1$ to $n$.

## Constraints

$1 \le n \le 10^6$

$0 \le arr[i] \le 10^9$

## Sample Tests

### Test 1

```
4
2 6 1 12
```

### Test 2

```
12 2 1 1
```

### Test 3

```
7
1 2 3 5 1 13 3
```

### Test 4

```
13 3 2 1 1 1 1
```

### Test 5

```
6
3 5 4 7 6 2
```

### Test 6

```
7 6 4 4 3 2
```
