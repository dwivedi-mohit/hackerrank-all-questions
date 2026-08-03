# Sorting Under Square Distance

---

| Field | Value |
|---|---|
| **Slug** | `sorting-under-square-distance` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack32 |
| **URL** | https://www.hackerrank.com/challenges/sorting-under-square-distance |

---

## Preview

Find the minimum cost to order an array where the cost to swap A[i] and A[j] is (i - j) ^ 2.

## Problem Statement

You have $n$ books randomly arranged on a shelf, $d[n]$, where each book has an ID number, $d_k$. You want to reorganize the shelf so the ID numbers are in ascending order, but the *time cost* associated with swapping any two books between location $d_i$ and $d_j$ is $(i-j)^2$ minutes.

For example, a bookshelf where $n=5$ and $d = [11, 7, 22, 5, 2]$ would be reorganized as $d' = [2, 5, 7, 11, 22]$.

Given an unordered bookshelf, determine the minimum number of minutes it will take to reorganize it so the ID numbers are in ascending order.

## Input Format

The first line is an integer, $n$, denoting the number of books.

The second line contains $n$ space-separated integers, where the $i^{th}$ integer is the ID number of the book initially located at location $d[i]$.

**Constraints**		
For 20% test cases, $1 \le n \le 10$.

For 50% test cases, $1 \le n \le 10^3$.

For 100% test cases, $1 \le n \le 10^5$, and $0 \le d_k \le 10^9$.

## Output Format

Print an integer denoting the minimum time cost (in minutes).

## Sample Tests

### Test 1

```
5
1 2 6 5 7
```

### Test 2

```
1
```
