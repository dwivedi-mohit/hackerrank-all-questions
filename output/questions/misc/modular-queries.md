# Modular Queries

---

| Field | Value |
|---|---|
| **Slug** | `modular-queries` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | adobe-hackathon |
| **URL** | https://www.hackerrank.com/challenges/modular-queries |

---

## Preview

Mara has learned some new tricks while doing modular operations. After gaining enough expertise, she was playing with a very long number having millions of digits in it.

## Problem Statement

Mara broke a number into $N$ smaller parts. Joining these $N$ parts together in the same order would create the whole, original number again.

**Example:** A number like 12345678 can be broken into ($N=4$) smaller parts: 123 45 6 78.

You are given $N$ parts of the number in the same order in which they would create the original number upon joining. Let's index these parts from $1$ to $N$. Also, there will be $Q$ queries of the following two types:

 - $1$ $i$ $P$ - Replace the part at the $i$<sup>$th$</sup> position with the new part $P$. <br>
 - $0$ $i$ $j$ - Output the number modulo $10$<sup>$9$</sup> $+$ $7$ formed by joining the parts from index $i$ to $j$  without _rearranging_ them in any way. 
 
The first integer in each query is the query type: $1$ or $0$.

 
 
**Constraints:**<br>

$1$ &le; $N$,$Q$ &le; $10$<sup>$5$</sup><br>
$1$ &le; $i$ &le; $j$ &le; $N$<br>
$0$ &le; $P$ &lt; $10$<sup>$18$</sup>

## Input Format

- The first line of input contains an integer $N$, defined above.
 - The next line contains $N$ space-separated parts.
 - The next line contains an integer $Q$, denoting the total number of queries.
 - The following $Q$ lines will have three space-separated integers corresponding to the above 2 types of queries: $1$ $i$ $P$ and $0$ $i$ $j$.
 - Each original/updated part will not have a length of more than $18$ and may have **leading zeros**.

## Output Format

For each query of the form $0$ $i$ $j$, print the required answer on a separate line.

## Sample Tests

### Test 1

```
5
1 2 3 4 5
3
0 1 5
1 2 1
0 1 5
```

### Test 2

```
12345
11345
```
