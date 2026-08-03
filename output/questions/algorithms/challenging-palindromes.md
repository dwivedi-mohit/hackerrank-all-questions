# Build a Palindrome

---

| Field | Value |
|---|---|
| **Slug** | `challenging-palindromes` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/challenging-palindromes |

---

## Preview

Determine if the substrings of two strings can be concatenated into a palindromic string.

## Problem Statement

You have two strings, $a$ and $b$. Find a string, $s$, such that:

* $s$ can be expressed as $s =s_a + s_b$ where $s_a$ is a non-empty [substring](https://en.wikipedia.org/wiki/Substring) of $a$ and $s_b$ is a non-empty substring of $b$.
* $s$ is a [palindromic](https://en.wikipedia.org/wiki/Palindrome) string.
* The length of $s$ is as long as possible.

For each of the $q$ pairs of strings ($a_i$ and $b_i$) received as input, find and print string $s_i$ on a new line. If you're able to form more than one valid string $s_i$, print whichever one comes first alphabetically. If there is no valid answer, print $-1$ instead.

## Input Format

The first line contains a single integer, $q$, denoting the number of queries. The subsequent lines describe each query over two lines:

1. The first line contains a single string denoting $a$.
2. The second line contains a single string denoting $b$.

## Output Format

For each pair of strings ($a_i$ and $b_i$), find some $s_i$ satisfying the conditions above and print it on a new line. If there is no such string, print $-1$ instead.

## Constraints

* $1 \le q \le 10$

* $1 \le |a|, |b| \le 10^5$

* $a$ and $b$ contain only lowercase English letters.
* Sum of |a| over all queries does not exceed $2 \times 10^5$
* Sum of |b| over all queries does not exceed $2 \times 10^5$

## Sample Tests

### Test 1

```
3
bac
bac
abc
def
jdfh
fds
```

### Test 2

```
aba
-1
dfhfd
```
