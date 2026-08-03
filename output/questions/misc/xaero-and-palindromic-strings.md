# Xaero And Palindromic Strings

---

| Field | Value |
|---|---|
| **Slug** | `xaero-and-palindromic-strings` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 60 |
| **Contest** | 101hack29 |
| **URL** | https://www.hackerrank.com/challenges/xaero-and-palindromic-strings |

---

## Problem Statement

Xaero likes strings a lot but, moreover, he likes palindromic strings. A string $s$ is called a palindromic string if it can be read the same going forward as well as backwards. For example: strings like **"abbba"**, **"abcba"**, **"a"** etc. are all palindromic strings whereas strings like **"abab"**, **"abcab"**, **"ab"** are not palindromic at all.

Today, Xaero got a hold of a string $S$ consisting of lower case alphabet letters i.e. ( **'a'** to **'z'** ) and challenged his best friend, Smurf, to a mathematical puzzle. What is the probability of choosing a substring of $S$ such that the letters of the chosen substring can be shuffled to make it a palindromic string? Smurf has no idea how to tackle it. Can you help him solve this challenge?

## Input Format

First line of input contains a single integer $T$ denoting the number of test cases. First and only line of each test case contains a string $S$ consisting of lower case alphabet letters.

**Constraints:**

$1 \le T \le 10^{5}$. 

$1 \le |S| \le 10^{6}$.

Sum of $|S|$ over all test cases does not exceed $10^{6}$.

## Output Format

For each test case, print the required probability in the form of an irreducible ratio $P/Q$.

## Sample Tests

### Test 1

```
3
hacker
aaaaa
racer
```

### Test 2

```
2/7
1/1
1/3
```
