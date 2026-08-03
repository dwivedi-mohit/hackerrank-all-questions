# Sorting Lists

---

| Field | Value |
|---|---|
| **Slug** | `sorting-lists` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 85 |
| **Contest** | 101hack49 |
| **URL** | https://www.hackerrank.com/challenges/sorting-lists |

---

## Preview

Given some intervals, for each half-integer point list all the intervals covering it. What is k'th lexicographically smallest such list?

## Problem Statement

We have a list of $n$ intervals $(a_1, b_1), (a_2, b_2), \ldots, (a_n, b_n)$ on the real number line. The *interval* $(a, b)$ is defined as the set of all real numbers strictly between $a$ and $b$.


Given an integer $m$, we define $C(m)$ as the sorted list of *all* indices $i$ such that $(a_i, b_i)$ contains $m + {1 \over 2}$. For example, if there are $n = 3$ intervals $(1, 5), (2, 3), (1, 2)$, then $C(1)$ is the list $[1, 3]$, since $1 + {1 \over 2} = 1.5$ is contained in the first and third intervals but not the second.


The following image illustrates this example:

![image](https://s3.amazonaws.com/hr-assets/0/1495001873-e869d447ed-SortingLists1.png)

You can also verify that $C(2) = [1, 2]$ and $C(3) = [1]$.


Let's call a list $S$ *beautiful* if there exists an integer $m$ such that $C(m) = S$. For example, the list $[1, 3]$ is beautiful since $C(1) = [1, 3]$. But $[2, 3]$ is not beautiful since you can't find an $m$ such that $C(m) = [2, 3]$.


We wrote all distinct non-empty beautiful lists in *lexicographical order* and obtained the sequence $\alpha_1, \ldots, \alpha_r$. Given $k$, find $\alpha_k$.


**Note**: Lexicographical ordering is defined as follows. Let $x = (x_1, \ldots, x_p)$ and $y = (y_1, \ldots, y_q)$ be lists. Then $x$ is *lexicographically smaller* than $y$ if one of the following conditions holds:


- $x$ is a *proper* prefix of $y$.

- $x$ and $y$ differ in some position, and if $i$ is the *first* position where they differ, then $x_i < y_i$.

## Input Format

The first line of input contains two space-separated integers $n$ and $k$.

The next $n$ lines contain the intervals. The $i^\text{th}$ line contains two space-separated integers $a_i, b_i$ denoting the endpoints of the $i^\text{th}$ interval.

## Output Format

Print two lines. In the first line, print the number of elements in the list $\alpha_k$. In the second line, print the elements of $\alpha_k$ in increasing order, separated by single spaces.

## Constraints

- $1 \le n \le 2\cdot 10^5$

- $0 \le a_i < b_i \le 10^9$

- There are at least $k$ non-empty beautiful lists.


**Subtasks**


- For $40\%$ of the testcases, $n \le 1500$

## Sample Tests

### Test 1

```
3 2
0 100
50 150
100 200
```

### Test 2

```
2
1 2
```

### Test 3

```
3 2
1 5
2 3
1 2
```

### Test 4

```
2
1 2
```
