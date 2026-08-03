# Mystery Number

---

| Field | Value |
|---|---|
| **Slug** | `naughty-number` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 30 |
| **Contest** | 101hack31 |
| **URL** | https://www.hackerrank.com/challenges/naughty-number |

---

## Problem Statement

You are given two collections of unordered integers, $A$ and $B$. $B$ has all of the same elements as $A$, as well as one additional mystery element. 

Find and print the mystery element in $B$ that is not present in $A$.

**Note:** The two collections are not sets, and thus _may have multiple elements with the same integer value_.

## Input Format

The first line contains an integer, $N$, indicating the length of $A$.

The second line contains the $N$ space-separated integer elements in collection $A$.

The third line contains the $N+1$ space-separated integer elements in collection $B$.

**Constraints**

$1$ &le; $N$ &le; $100$

Elements in $A$ and $B$ are integer values between $0$ and $100$.

## Output Format

Print the mystery integer found in collection $B$.

## Sample Tests

### Test 1

```
5
1 1 2 3 4
2 3 4 7 1 1
```

### Test 2

```
7
```
