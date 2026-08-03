# Play with words

---

| Field | Value |
|---|---|
| **Slug** | `strplay` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 65 |
| **URL** | https://www.hackerrank.com/challenges/strplay |

---

## Preview

Given string S, find two palindromic subsequences such that product of length of these is maximal and these don't overlap

## Problem Statement

Shaka and his brother have created a boring game which is played like this:


They take a word composed of lowercase English letters and try to get the maximum possible score by building exactly 2 **palindromic subsequences**. The score obtained is the product of the length of these 2 [subsequences](https://en.wikipedia.org/wiki/Subsequence).

Let's say $A$ and $B$ are two subsequences from the initial string. If $A_i$ & $A_j$ are the smallest and the largest positions (from the initial word) respectively in $A$ ; and $B_i$ & $B_j$ are the smallest and the largest positions (from the initial word) respectively in $B$, then the following statements hold true:

$A_i \le A_j$, 

$B_i \le B_j$, &  

$A_j < B_i$. 

i.e., the positions of the subsequences should not cross over each other. 

Hence the score obtained is the product of lengths of subsequences $A$ & $B$. Such subsequences can be numerous for a larger initial word, and hence it becomes harder to find out the maximum possible score. Can you help Shaka and his brother find this out?

## Input Format

Input contains a word $S$ composed of lowercase English letters in a single line.

## Output Format

Output the maximum score the boys can get from $S$.

## Constraints

$1 < |S| \le 3000$

each character will be a lower case english alphabet.

## Sample Tests

### Test 1

```
eeegeeksforskeeggeeks
```

### Test 2

```
50
```
