# Two Characters

---

| Field | Value |
|---|---|
| **Slug** | `three-month-preparation-kit-two-characters` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/three-month-preparation-kit-two-characters |

---

## Preview

Print the length of the longest possible string $t$ you can form.

## Problem Statement

Given a string, remove characters until the string is made up of any two alternating characters.  When you choose a character to remove, all instances of that character must be removed.  Determine the longest string possible that contains just two alternating letters.

**Example**  


$s = \text{'abaacdabd'}$ 


Delete `a`, to leave `bcdbd`.  Now, remove the character `c` to leave the valid string `bdbd` with a length of 4. Removing either `b` or `d` at any point would not result in a valid string.  Return $4$. 


Given a string $s$, convert it to the longest possible string $t$ made up only of alternating characters.  Return the length of string $t$.  If no string $t$ can be formed, return $0$.

**Function Description**

Complete the *alternate* function in the editor below.


alternate has the following parameter(s):


- *string s:* a string 


**Returns**. 

- *int:* the length of the longest valid string, or $0$ if there are none

## Input Format

The first line contains a single integer that denotes the length of $s$. 	
The second line contains string $s$.

## Constraints

* $ 1 \le \text{ length of s }\le 1000 $
* $s[i] \in \text{ascii[a-z]}$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
10 length of s = 10
beabeefeab s = 'beabeefeab'
```

### Test 2

```
5
```
