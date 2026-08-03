# Sherlock and Unique Substrings

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-unique-substrings` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | 101hack26 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-unique-substrings |

---

## Problem Statement

_How often have I said to you that when you have eliminated the impossible, whatever remains, however improbable, must be the truth?_

Watson gives Sherlock a string $S$ of $N$ characters, say, $S_1, S_2, ..., S_N$. Now, he defines a substring as a string of characters $S_i, S_{i+1}, ... S_j$ where $1 \le i \le j \le N$. He denotes such a substring as $S[i, j]$. 


Also, he defines a unique substring a substring which occurs only once in the whole string. For example, in string $S$ =`aab`, substrings $S[1,2]$ _i.e._ `aa`, $S[2,3]$ _i.e._ `ab`, $S[3,3]$ _i.e._ `b` and $S[1,3]$ _i.e._ `aab` are unique whereas substrings $S[1,1]$ and $S[2,2]$ are not unique because both are equal to `a`.

Now, he gives Sherlock $Q$ queries of form $(L, R)$. For each such query Sherlock has to report how many substrings of $S[L, R]$ are one of the unique substrings of $S$.

## Input Format

The first line contains the string $S$ of $N$ characters, all of which are lowercase letters.

The next line contains $Q$.

Each of the next $Q$ lines contain a pair of integers denoting the queries.

## Output Format

For each query, output in one line the required answer.

**Constraints** 


$1 \le N, Q\le 10^5$

$1 \le L \le R \le 10^5$

## Sample Tests

### Test 1

```
aabbab
2
1 3
4 5
```

### Test 2

```
2
1
```
