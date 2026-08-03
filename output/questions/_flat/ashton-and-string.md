# Ashton and String

---

| Field | Value |
|---|---|
| **Slug** | `ashton-and-string` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/ashton-and-string |

---

## Preview

What is the Kth character in a string formed by concatenating lexicographically arranged substrings of a given string?

## Problem Statement

Ashton appeared for a job interview and is asked the following question. Arrange all the distinct [substrings](https://en.wikipedia.org/wiki/Substring)  of a given string in lexicographical order and concatenate them. Print the $k^{th}$ character of the concatenated string. It is assured that given value of $k$ will be valid i.e. there will be a $k^{th}$ character. Can you help Ashton out with this?


For example, given the string $s = \texttt{abc}$, its distinct substrings are $\texttt{[a, ab, abc, abcd, b, bc, bcd, c, cd, d]}$.  Sorted and concatenated, they make the string $\texttt{aababcabcdbbcbcdccdd}$.  If $K = 5$ then, the answer is $b$, the $5^{th}$ character of the 1-indexed concatenated string.


**Note** We have distinct substrings here, i.e. if string is `aa`, it's distinct substrings are `a` and `aa`.


**Function Description**


Complete the *ashtonString* function in the editor below.  It should return the $k^{th}$ character from the concatenated string, 1-based indexing.


ashtonString has the following parameters:

- *s*: a string

- *k*: an integer

## Input Format

The first line will contain an integer $t$, the number of test cases.



Each of the subsequent $t$ pairs of lines is as follows:

- The first line of each test case contains a string, $s$.  

- The second line contains an integer, $k$.

## Output Format

Print the $k^{th}$ character (1-based index) of the concatenation of the ordered distinct substrings of $s$.

## Constraints

$1 \le t \le 5$

$1 \le |s| \le 10^5$

Each character of string $s \in ascii[a-z]$ 

$k$ will be an appropriate integer.

## Sample Tests

### Test 1

```
1
dbac
3
```

### Test 2

```
c
```

### Test 3

```
a, ac, b, ba, bac, c, d, db, dba, dbac
```

### Test 4

```
aacbbabaccddbdbadbac
```
