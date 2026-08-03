# Wet Shark and Two Subsequences

---

| Field | Value |
|---|---|
| **Slug** | `wet-shark-and-two-subsequences` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/wet-shark-and-two-subsequences |

---

## Preview

Given a sequence, count number of pairs of subsequences.

## Problem Statement

One day, Wet Shark was given an array $X = \{x_1, x_2, \ldots, x_m\}$. As always, he started playing with its [subsequences](http://en.wikipedia.org/wiki/Subsequence).

<br>
When you came to know about this habit, you presented him a task of finding all pairs of subsequences, $(A, B)$, which satisfies all of the following constraints. We will represent a pair of subsequence as $A = \{x_{a_1}, x_{a_2}, \ldots, x_{a_n}\}$ and $B = \{x_{b_1}, x_{b_2}, \ldots, x_{b_n}\}$ 

- $A$ and $B$ must be of same length, i.e., $|A| = |B|$.
- $\sum\limits_{i=1}^n (x_{a_i}+ x_{b_i}) = r$
- $\sum\limits_{i=1}^n (x_{a_i} - x_{b_i}) = s$

Please help Wet Shark determine how many possible subsequences $A$ and $B$ can exist. Because the number of choices may be big, output your answer modulo $10^{9} + 7 = 1000000007$. 

*Note:* 

- Two segments are different if there's exists at least one index $i$ such that element $x_i$ is present in exactly one of them.
- Both subsequences can overlap each other.
- Subsequences do not necessarily have to be distinct

## Input Format

The first line consists of 3 space-separated integers $m$, $r$, $s$, where $m$ denotes the length of the original array, $X$, and $r$ and $s$ are as defined above.

The next line contains $m$ space-separated integers, $x_1, x_2, \ldots, x_m$ , representing the elements of $X$.

## Output Format

Output total number of pairs of subsequences, $(A, B)$, satisfying the above conditions. As the number can be large, output it's modulo $10^9 + 7 = 1000000007$

## Constraints

+ $1 \le m \le 100$

+ $0 \le r, s \le 2000$

+ $1 \le x_i \le 2000$

## Sample Tests

### Test 1

```
4 5 3
1 1 1 4
```

### Test 2

```
3
```
