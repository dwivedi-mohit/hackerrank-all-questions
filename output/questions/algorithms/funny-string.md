# Funny String

---

| Field | Value |
|---|---|
| **Slug** | `funny-string` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/funny-string |

---

## Preview

Is the absolute difference between consecutive characters the same for a string and the reverse of that string for all indices?

## Problem Statement

In this challenge, you will determine whether a string is *funny* or not.  To determine whether a string is funny, create a copy of the string in reverse e.g. $abc \rightarrow cba$.  Iterating through each string, compare the absolute difference in the [ascii](https://en.wikipedia.org/wiki/ASCII) values of the characters at positions 0 and 1, 1 and 2 and so on to the end.  If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny.  If it is, return `Funny`, otherwise return `Not Funny`.

**Example**

$s = \texttt{'lmnop'}$


The ordinal values of the charcters are $[108, 109, 110, 111, 112]$.  $s_{reverse} = \texttt{'ponml'}$ and the ordinals are $[112, 111, 110, 109, 108]$.  The absolute differences of the adjacent elements for both strings are $[1, 1, 1, 1]$, so the answer is `Funny`.

**Function Description**

Complete the *funnyString* function in the editor below. 


funnyString has the following parameter(s):


- *string s:* a string to test


**Returns**


- *string:* either `Funny` or `Not Funny`

## Input Format

The first line contains an integer $q$, the number of queries. 	
The next $q$ lines each contain a string, $s$.

## Constraints

- $1 \leq q \leq 10$  	
- $2 \leq \text{length of }s  \leq 10000$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
2 q = 2
acxz s = 'acxz'
bcxz s = 'bcxz'
```

### Test 2

```
Funny
Not Funny
```
