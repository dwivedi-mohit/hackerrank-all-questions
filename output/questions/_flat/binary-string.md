# Binary String

---

| Field | Value |
|---|---|
| **Slug** | `binary-string` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack28 |
| **URL** | https://www.hackerrank.com/challenges/binary-string |

---

## Preview

Given a binary string (only of characters 0 and 1), find the lexicographically largest string that can be obtained from the given string by at T swap operations. You can only swap two characters at distance equal to K.

## Problem Statement

Our two friends Zloba and Mika know a lot about binary strings (strings which only contain characters $0$ and $1$). A public secret is that Zloba knows more than Mika about these strange strings. But nobody knows about Zloba's secret: he has a special program working with these strings. This time Mika invented a really hard problem that Zloba's program can't solve. The problem is:

You are given a binary string $s$ of length $n$, and two numbers $k$ and $t$. You are allowed to perform at most $t$ swap operations. In one swap operation, you can choose two indexes in string $s$, $i$ and $j$ such that $j - i = k$, and then swap values of $s_i$ and $s_j$ in string $s$. Find the lexicographically largest string that can be obtained.

We love Zloba a lot and he is our good friend, so let us help and solve this hard problem for him!

Binary string $s$ is lexicographically larger than binary string $a$ of same length $n$ if there exists position $i$ ($1\leq i \leq n$) such that $s_i = 1$ and $a_i = 0$, and for each position $j$ ($1\leq j < i$) $s_j = a_j$ is fulfilled.

**Input Format**<br>

The first line contains three numbers $n$, $k$, and $t$ ($1 \leq n \leq 10^5$, $1 \leq k \leq n$, $1 \leq t \leq 10^9$), the length of the given binary string, the distance between swapped bits in one operation, and the maximum number of swap operations.

The second line contains binary string $s$ of length $n$.


**Output Format**<br>

Print the lexicographically largest string which can be obtained as described in the statement.

**Sample Input 1:**<br>

    5 1 10
    01010

**Sample Output 1:**<br>

	11000

**Sample Input 2:**<br>

    6 2 3
    000111

**Sample Output 2:**<br>

	110001

## Sample Tests

### Test 1

```
5 1 10
01010
```

### Test 2

```
11000
```

### Test 3

```
6 2 3
000111
```

### Test 4

```
110001
```
