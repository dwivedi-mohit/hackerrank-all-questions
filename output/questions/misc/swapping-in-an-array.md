# Swapping in an Array

---

| Field | Value |
|---|---|
| **Slug** | `swapping-in-an-array` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack55 |
| **URL** | https://www.hackerrank.com/challenges/swapping-in-an-array |

---

## Preview

Swap two elements to make an array sorted.

## Problem Statement

Safisko has an array $a$ with $n$ positive integer elements. Safisko likes order, so he wants his array to be sorted. (A *sorted* array is an array that contains non-decreasing elements in increasing index order.) He decides to swap two elements in the array to make his array sorted. (A *swap* is defined as switching two elements at distinct locations in the array.) Your task is to determine if this can be done.

- If he can't sort the array with one swap, print $-1$. 
- If the array is already sorted, print $0$. 
- If he can sort the array with one swap, print $1$.

Complete the function `swapToSort` which takes in an integer array $a$ and returns either $-1$, $0$ or $1$.

## Input Format

The first line contains a single integer $n$. The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$, the elements of the array $a$.

## Output Format

Print a single line containing an integer denoting the answer. This should be either $-1$, $0$, or $1$.

## Constraints

- $1 \leq n \leq 10^3$
- $1 \le a_i \le 10^9$

## Sample Tests

### Test 1

```
5
1 10 3 4 3
```

### Test 2

```
1
```

### Test 3

```
5
1 2 2 4 5
```

### Test 4

```
0
```

### Test 5

```
7
6 2 4 3 5 1 7
```

### Test 6

```
-1
```
