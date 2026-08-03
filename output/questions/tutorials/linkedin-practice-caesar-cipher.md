# Caesar Cipher: Encryption

---

| Field | Value |
|---|---|
| **Slug** | `linkedin-practice-caesar-cipher` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/linkedin-practice-caesar-cipher |

---

## Preview

Encrypt a string by rotating the alphabets by a fixed value in the string.

## Problem Statement

Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, $K$, making it unreadable by his enemies. Given a string, $S$, and a number, $K$, encrypt $S$ and print the resulting string. 


**Note:** The cipher *only* encrypts letters; symbols, such as `-`, remain unencrypted.

## Input Format

The first line contains an integer, $N$, which is the length of the unencrypted string.		
The second line contains the unencrypted string, $S$.	
The third line contains the integer encryption key, $K$, which is the number of letters to rotate.

**Constraints** 

$1 \le N \le 100$

$0 \le K \le 100$

$S$ is a valid ASCII string and doesn't contain any spaces.

## Output Format

For each test case, print the encoded string.

## Sample Tests

### Test 1

```
11
middle-Outz
2
```

### Test 2

```
okffng-Qwvb
```
