# Arrange Students

---

| Field | Value |
|---|---|
| **Slug** | `arrange-students` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 20 |
| **Contest** | hack-the-interview-iv |
| **URL** | https://www.hackerrank.com/challenges/arrange-students |

---

## Preview

Determine if an array can be ordered in a way to satisfy certain conditions.

## Problem Statement

A classroom has several students, half of whom are boys and half of whom are girls. You need to arrange all of them in a line for the morning assembly such that the following conditions are satisfied:

- The students must be in order of non-decreasing height.
- Two boys or two girls must not be adjacent to each other.

You have been given the heights of the boys in the array $b$ and the heights of the girls in the array $g$. Find out whether you can arrange them in an order which satisfies the given conditions. Print `"YES"` if it is possible, or `"NO"` if it is not.

For example, let's say there are $n = 3$ boys and $n = 3$ girls, where the boys' heights are $b = [5, 3, 8]$ and the girls' heights are $g = [2, 4, 6]$. These students can be arranged in the order $[g_0, b_1, g_1, b_0, g_2, b_2]$, which is [2, 3, 4, 5, 6, 8]. Because this is in order of non-decreasing height, and no two boys or two girls are adjacent to each other, this satisfies the conditions. Therefore, the answer is `"YES"`.

## Input Format

The first line contains an integer, $t$, denoting the number of test cases.

The first line of each test case contains an integer, $n$, denoting the number of boys and girls in the classroom.

The second line of each test case contains $n$ space separated integers, $b_1, b_2, \cdots b_n$, denoting the heights of the boys.

The third line of each test case contains $n$ space separated integers, $g_1, g_2, \cdots g_n$, denoting the heights of the girls.

## Output Format

Print exactly $t$ lines. In the $i^{th}$ of them, print a single line containing `"YES"` if it is possible to arrange the students in the $i^{th}$ test case, or `"NO"` if it is not.

## Constraints

- $1 \le t \le 10$
- $1 \le n \le 100$
- $1 \le b_i, g_i, \le 100$

## Sample Tests

### Test 1

```
1
2
1 3
2 4
```

### Test 2

```
YES
```

### Test 3

```
2
2
1 2
3 4
3
2 3 5
1 3 4
```

### Test 4

```
NO
YES
```
