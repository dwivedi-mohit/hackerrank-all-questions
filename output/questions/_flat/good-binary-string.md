# Valid Binary String

---

| Field | Value |
|---|---|
| **Slug** | `good-binary-string` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 10 |
| **Contest** | hack-the-interview-iv |
| **URL** | https://www.hackerrank.com/challenges/good-binary-string |

---

## Preview

Find the maximum changes needed to make a binary string "valid" according to certain conditions.

## Problem Statement

You have been given a binary string containing only the characters "$\text{0}$" and "$\text{1}$". A binary string is considered valid if each of its substrings of at least a certain length contains at least one "$\text{1}$" character. Given the binary string, and the minimum length of substring, determine how many characters of the string need to be changed in order to make the binary string valid.

Note that string $v$ is a substring of string $w$ if it has a non-zero length and can be read starting from some position in string $w$. For example, string "$\text{010}$" has six substrings: "$\text{0}$", "$\text{1}$", "$\text{0}$", "$\text{01}$", "$\text{10}$", "$\text{010}$".

For example, let's say the binary string $s$ = "$\text{0001}$" of length $n = 4$, and the minimum substring length is $d = 2$. This is currently not valid because one of its substrings, "$\text{000}$", of length 3 has no "$\text{1}$"s in it. By changing the second character to a "$1$", the string becomes "$\text{0101}$". In this case, all of its substrings of length 2 or more has at least one "$\text{1}$" character: "$\text{01}$", "$\text{10}$", and "$\text{01}$". Because this required 1 change, the answer is 1.

## Input Format

The first line contains the binary string, $s$.

The second line contains the integer $d$.

## Output Format

Print a single integer denoting the minimum number of changes required to make the binary string valid.

## Constraints

- $1 \le n \le 10^6$
- $1 \le d \le n$

## Sample Tests

### Test 1

```
00100
2
```

### Test 2

```
2
```

### Test 3

```
101
2
```

### Test 4

```
0
```
