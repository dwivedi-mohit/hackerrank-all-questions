# Counting Good Partitions of a String

---

| Field | Value |
|---|---|
| **Slug** | `counting-good-partitions-of-a-string` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack25 |
| **URL** | https://www.hackerrank.com/challenges/counting-good-partitions-of-a-string |

---

## Preview

Count the number of good partitions of a string.

## Problem Statement

You are given a string $s$ consisting of lower-case English letters. You have to partition $s$ into $k$ non-empty strings $s_1, s_2, \dots, s_k$ so that the concatenation of all of them is equal to $s$ (i.e. $s = s_1 + s_2 + \dots + s_k$). A partition is called $good$ if the starting characters of $s_i \forall i \in [1,k]$ in the partition are distinct.

You have to find the number of $good$ partitions of a string $s$ where $k$ has the maximum possible value. As the answer could be large, please print the answer modulo $1000$ (i.e. print the last three digits of the answer without extra leading zeros).

## Input Format

-	A single line of input containing the string $s$.

## Output Format

Print a single line containing the answer to the problem.

**Constraints** 

-	$1 \leq \text{size of } s \leq 10^5$

-	$s$ will consist of lower-case English letters (i.e. from 'a' to 'z')

## Sample Tests

### Test 1

```
ab
```

### Test 2

```
1
```

### Test 3

```
a
```

### Test 4

```
1
```

### Test 5

```
abb
```

### Test 6

```
2
```
