# Even-odd Boxes

---

| Field | Value |
|---|---|
| **Slug** | `even-and-odd-boxes` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack50 |
| **URL** | https://www.hackerrank.com/challenges/even-and-odd-boxes |

---

## Preview

Help Lucy arrange chocolates in boxes to get an even-odd repetitive pattern.

## Problem Statement

Lucy has an array of $n$ boxes. The boxes are arranged in a straight line numbered $0$ to $n-1$ from left to right. Box $i$ contains $x_i$ chocolates.

Lucy thinks the arrangement looks beautiful if the boxes follow an even-odd repetitive pattern. That means the first box contains an even number of chocolates, the second box contains an odd number, the third box contains even, and so on. Here's a beautiful even-odd arrangement:

![image](https://s3.amazonaws.com/hr-assets/0/1497358053-a821000604-ChocolateBoxes.png)

Lucy is asking you to make beautiful even-odd arrangements from her arrays of boxes. You are allowed to move some chocolates from one box to another. But you are not allowed to swap the boxes. In the final arrangement, every box must contain at least one chocolate.

Calculate the minimum number of chocolates you need to move to get an even-odd repetitive pattern. If it's not possible to get the desired pattern, print `-1`.

## Input Format

The first line contains an integer $q$ denoting the number of queries.

The first line of each query contains an integer $n$ denoting the number of boxes.

The second line of each query contains $n$ space-separated integers $x_0, x_1, \ldots x_{n-1}$ describing the number of chocolates in each box.

## Output Format

Print an integer describing the minimum number of chocolates you need to transfer to get the even-odd repetitive pattern. If it's not possible to get the desired pattern, print $-1$.

## Constraints

* $ 1 \le q \le 10 $

* $ 1 \le n, x_i \le 10^5 $


**Subtask**


* $ 1 \le n \le 1000 $ for $50 \%$ of the maximum score

## Sample Tests

### Test 1

```
3
6
6 8 3 1 1 4
5
3 1 1 1 1
3
14 3 10
```

### Test 2

```
2
-1
0
```
