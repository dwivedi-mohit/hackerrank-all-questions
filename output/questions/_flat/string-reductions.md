# String Reductions

---

| Field | Value |
|---|---|
| **Slug** | `string-reductions` |
| **Domain** | fp |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/string-reductions |

---

## Preview

Remove subsequent occurrences.

## Problem Statement

Given a string, $str =  s_1, s_2\ldots s_n$, consisting of $n$ lowercase English characters ($a-z$), remove all of the characters that occurred previously in the string. Formally, remove all characters, $s_i$, for:
<br>

$\exists j, s_j = s_i$ and $ j < i$

## Input Format

A single line of input containing a string $str$ of length $n$.

## Output Format

Print the string after removing all the characters that occurred previously. 


**Sample Input #00**


	accabb

**Sample Output #00**


	acb

**Sample Input #01**


	abc

**Sample Output #01**


	abc

**Sample Input #02**

	pprrqq

**Sample Output #02**


	prq

## Constraints

- $1 \le n \le 10^5$

- $s_i \in \{a,\ b, \ldots,\ z\}, where\ 1 \le i \le n$

## Sample Tests

### Test 1

```
accabb
```

### Test 2

```
acb
```

### Test 3

```
abc
```

### Test 4

```
abc
```

### Test 5

```
pprrqq
```

### Test 6

```
prq
```
