# Game of Thrones - I

---

| Field | Value |
|---|---|
| **Slug** | `game-of-thrones` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/game-of-thrones |

---

## Preview

Check whether any anagram of a string can be a palindrome or not.

## Problem Statement

Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

![door](https://s3.amazonaws.com/hr-assets/0/1526565753-0c557c119f-game-of-thrones.png "block")

But, to lock the door he needs a key that is an [anagram](https://en.wikipedia.org/wiki/Anagram) of a [palindrome](http://en.wikipedia.org/wiki/Palindrome).  He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.  Given a string, determine if it can be rearranged into a palindrome.  Return the string `YES` or `NO`.


**Example** 

$s = \text{'aabbccdd'}$


One way this can be arranged into a palindrome is $abcddcba$.  Return `YES`.

**Function Description**

Complete the *gameOfThrones* function below. 

gameOfThrones has the following parameter(s):


- *string s*: a string to analyze 


**Returns**


- *string:*  either `YES` or `NO`

## Input Format

A single line which contains $s$.

## Constraints

+ $1 \le$ |s| $\le 10^5$

+ $s$ contains only lowercase letters in the range $ascii[a\ldots z]$

## Sample Tests

### Test 1

```
aaabbbb
```

### Test 2

```
YES
```

### Test 3

```
cdefghmnopqrstuvw
```

### Test 4

```
NO
```

### Test 5

```
cdcdcdcdeeeef
```

### Test 6

```
YES
```
