# Palindromic Subsets

---

| Field | Value |
|---|---|
| **Slug** | `palindromic-subsets` |
| **Domain** | data-structures |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/palindromic-subsets |

---

## Preview

Perform queries of two types on a string.

## Problem Statement

Consider a lowercase English alphabetic letter character denoted by $c$. A *shift* operation on some $c$ turns it into the next letter in the alphabet. For example, and $shift(\texttt{a}) = \texttt{b}$, $shift(\texttt{e}) = \texttt{f}$, $shift(\texttt{z}) = \texttt{a}$ . 

Given a zero-indexed string, $s$, of $n$ lowercase letters, perform $q$ queries on $s$ where each query takes one of the following two forms:

* `1 i j t`: All letters in the inclusive range from $i$ to $j$ are shifted $t$ times.	
* `2 i j`: Consider all indices in the inclusive range from $i$ to $j$. Find the number of non-empty subsets of characters, $c_1, c_2, \ldots, c_k$ where $i \le \text{ index of } c_1 < \text{ index of } c_2 < \ldots < \text{ index of } c_k \le j)$, such that characters $c_1, c_2, c_3, \ldots, c_k$ *can be rearranged* to form a palindrome. Then print this number modulo $10^9 + 7$ on a new line. Two palindromic subsets are considered to be different if their component characters came from different indices in the original string.

**Note**
Two palindromic subsets are considered to be different if their component characters came from different indices in the original string.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $q$.		
The second line contains a string of $n$ lowercase English alphabetic letters (i.e., `a` through `z`) denoting $s$.

Each of the $q$ subsequent lines describes a query in one of the two formats defined above.

## Output Format

For each query of type $2$ (i.e., `2 i j`), print the number of non-empty subsets of characters satisfying the conditions given above, modulo $10^9 + 7$, on a new line.

## Constraints

* $1 \le n \le 10^5$

* $1 \le q \le 10^5$

* $0 \le i \le j < n$ for each query.
* $0 \le t \le 10^9$ for each query of type $1$.

**Subtasks**

For $20\%$ of the maximum score:



- $n \leq 500$
- $q \leq 500$


For another $30\%$ of the maximum score: 


- All queries will be of type $2$.

## Sample Tests

### Test 1

```
3 5
aba
2 0 2
2 0 0
2 1 2
1 0 1 1
2 0 2
```

### Test 2

```
5
1
2
3
```
