# String Similarity

---

| Field | Value |
|---|---|
| **Slug** | `string-similarity` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/string-similarity |

---

## Preview

Calculate the sum of similarities of a string S with each of it's suffixes.

## Problem Statement

For two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings. For example, the similarity of strings "abc" and "abd" is 2, while the similarity of strings "aaa" and "aaab" is 3.

Calculate the sum of similarities of a string S with each of it's suffixes.

## Input Format

The first line contains the number of test cases *t*.

Each of the next *t* lines contains a string to process, $s$.

## Output Format

Output *t* lines, each containing the answer for the corresponding test case.

## Constraints

- $1 \le t \le 10$  

- $1 \le |s| \le 100000$

- $s$ is composed of characters in the range ascii[a-z]

## Sample Tests

### Test 1

```
2
ababaa 
aa
```

### Test 2

```
11 
3
```
