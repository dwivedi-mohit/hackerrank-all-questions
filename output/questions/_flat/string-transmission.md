# String Transmission

---

| Field | Value |
|---|---|
| **Slug** | `string-transmission` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/string-transmission |

---

## Preview

Bob has received a binary string of length N transmitted by
 Alice. He knows that due to errors in transmission, some bits
 might have been corrupted. Find how many possible strings
 could Alice have transmitted.

## Problem Statement

Bob has received a binary string of length N transmitted by Alice. He knows that due to errors in transmission, up to K bits might have been corrupted (and hence flipped). However, he also knows that the string Alice had intended to transmit was not periodic. A string is not periodic if it cannot be represented as a smaller string concatenated some number of times. For example, "0001", "0110" are not periodic while "00000", "010101" are periodic strings.

Now he wonders how many possible strings could Alice have transmitted.

## Input Format

The first line contains the number of test cases T. T test cases follow. Each case contains two integers N and K on the first line, and a binary string of length N on the next line.

## Output Format

Output T lines, one for each test case. Since the answers can be really big, output the numbers modulo 1000000007.

## Constraints

$1 \le T \le 20$

$1 \le N \le 1000$

$0 \le K \le N$

## Sample Tests

### Test 1

```
3 
5 0 
00000 
3 1 
001 
3 3 
101
```

### Test 2

```
0
3
6
```
