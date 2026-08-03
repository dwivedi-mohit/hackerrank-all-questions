# Kth Minimum

---

| Field | Value |
|---|---|
| **Slug** | `kth-minimum` |
| **Contest** | hourrank-24 |
| **Difficulty** | Hard |
| **Score** | 65 |
| **URL** | https://www.hackerrank.com/challenges/kth-minimum |

---

## Problem Statement

Jen likes playing with lists of nonzero integers. She has many such lists in her almirah. To kill her boredom, she would take some list and look for the $k^\text{th}$ smallest number in it. 

However, she soon lost interest in doing so because it was too easy, so she decided to create a new list $L$ using this procedure:

```sql

-- lists are 1-indexed --

procedure generate_list(A, B, x):

    let n = length of A
    let m = length of B
    let L = an empty list

    for i from 1 to min(n, m - x), inclusive:
        for j from (i + x) to m, inclusive:
            Append (A[i]*B[j]) to the end of L

    return L
```

To create $L$, she takes two lists $A$ and $B$ and an integer $x$ and calls `generate_list(A, B, x)`. She was surprised to see such a big list and got stuck on finding the $k^\text{th}$ smallest number in it. Can you help her?

*Note:* The $k^\text{th}$ smallest number in a list $L$ is the $k^\text{th}$ element of $L$ when it is sorted. For example, the $4^\text{th}$ smallest number in $[7, 2, 7, 2, 11]$ is $7$.

## Input Format

The first line contains four space-separated integers $n$, $m$, $x$ and $k$. $n$ and $m$ are the respective sizes of $A$ and $B$.  

The second line contains $n$ space-separated integers $A_1, A_2, \ldots, A_n$.  

The third line contains $m$ space separated integers $B_1, B_2, \ldots, B_m$.

## Output Format

Print a single line containing a single integer denoting the answer: the $k^\text{th}$ smallest number in the list $L$.

## Constraints

- $2 \le n, m\le 2 \times 10^5$
- $1 \le x < m$  
- $1 \le |A_i| \le 2 \times 10^{5}$
- $1 \le |B_i| \le 2 \times 10^{5}$
- $1 \le k \le \mathrm{length}(L)$

**Subtasks**

- $1 \le n, m \le 2 \times 10^3$ for ${\sim}20\%$ of the maximum score.
