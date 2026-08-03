# Lexicographically Greater String

---

| Field | Value |
|---|---|
| **Slug** | `linkedin-practice-bigger-is-greater` |
| **Domain** | tutorials |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/linkedin-practice-bigger-is-greater |

---

## Preview

Rearrange the letters of a string to construct another string such that the new string is lexicographically greater than the original.

## Problem Statement

Given a word $w$, rearrange the letters of $w$ to construct another word $s$ in such a way that $s$ is lexicographically greater than $w$. In case of multiple possible answers, find the lexicographically smallest one among them.

## Input Format

The first line of input contains $t$, the number of test cases. Each of the next $t$ lines contains $w$.

## Output Format

For each testcase, output a string lexicographically bigger than $w$ in a separate line. In case  of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print `no answer`.

## Constraints

* $1 \le t \le 10^5$

* $1 \le |w| \le 100$

* $w$ will contain only lower-case English letters and its length will not exceed $100$.

## Sample Tests

### Test 1

```
5
ab
bb
hefg
dhck
dkhc
```

### Test 2

```
ba
no answer
hegf
dhkc
hcdk
```
