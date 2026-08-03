# Randomness

---

| Field | Value |
|---|---|
| **Slug** | `randomness` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **URL** | https://www.hackerrank.com/challenges/randomness |

---

## Preview

Answer the queries about the number of distinct substrings of a string.

## Problem Statement

You're given a string $S$ of $N$ characters. It's known that the string consists of lowercase Latin letters. The string is generated randomly. That means that every symbol is chosen randomly and independently from others from the set {'a', 'b', ..., 'z'}. All the letters have equal probability to appear.

You're given $Q$ queries on this string. Each query is of the form `P C`, where $P$ is an integer between $1$ and $N$ (both inclusive) and $C$ is a character from the set {'a', 'b', ..., 'z'}. Both $P$ and $C$ were chosen at random and independently from other queries. 

When you have a query of the form `P C` you have to change the $P$<sup>$th$</sup> symbol of $S$ to $C$. After every change we ask you to output the number of distinct nonempty sub-strings of $S$.

## Input Format

The first line of input consists of two single space-separated integers $N$ and $Q$, the length of the string $S$ and the number of queries, respectively.

The second line contains string $S$.

The following $Q$ lines describe the queries in the form `P C`, where $P$ and $C$ are also separated with a single space.

**Constraints**

$4 \le N \le 75000$

$4 \le Q \le 75000$

## Output Format

Output $Q$ lines. Output the number of distinct substrings of $S$ after the $i$<sup>$th$</sup> query on the $i$<sup>$th$</sup> line of the output.

## Sample Tests

### Test 1

```
4 4 
aaab
1 a
2 b
3 c
4 d
```

### Test 2

```
7
7
9
10
```

### Test 3

```
a b aa ab aaa aab aaab
```

### Test 4

```
a b ab ba aba bab abab
```

### Test 5

```
a b c ab bc cb abc bcb abcb
```

### Test 6

```
a b c d ab bc cd abc bcd abcd
```
