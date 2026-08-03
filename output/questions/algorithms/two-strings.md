# Two Strings

---

| Field | Value |
|---|---|
| **Slug** | `two-strings` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/two-strings |

---

## Preview

Given two strings, you find a common substring of non-zero length.

## Problem Statement

Given two strings, determine if they share a common substring.  A substring may be as small as one character.


**Example** 

$s1 = \text{'and'}$

$s2 = \text{'art'}$


These share the common substring $a$.


$s1 = \text{'be'}$

$s2 = \text{'cat'}$


These do not share a substring.


**Function Description**

Complete the function *twoStrings* in the editor below.  


twoStrings has the following parameter(s):


- *string s1:*  a string
- *string s2:*  another string  


**Returns**


- *string:* either `YES` or `NO`

## Input Format

The first line contains a single integer $p$, the number of test cases.		

The following $p$ pairs of lines are as follows:

- The first line contains string $s1$.
- The second line contains string $s2$.

## Output Format

For each pair of strings, return `YES` or `NO`.

## Constraints

- $s1$ and $s2$ consist of characters in the range ascii[a-z].
- $1 \le p \le 10$
- $1 \le |s1|, |s2| \le 10^5$

## Sample Tests

### Test 1

```
2
hello
world
hi
world
```

### Test 2

```
YES
NO
```
