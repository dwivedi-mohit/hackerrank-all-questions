# Sam and substrings

---

| Field | Value |
|---|---|
| **Slug** | `sam-and-substrings` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/sam-and-substrings |

---

## Preview

Samantha and Sam are playing a game. At the end of the 
game, Sam has to find out the total number of candies in the 
box, T.

## Problem Statement

Samantha and Sam are playing a numbers game.  Given a number as a string, no leading zeros, determine the sum of all integer values of substrings of the string. 


Given an integer as a string, sum all of its substrings cast as integers.  As the number may become large, return the value modulo $10^9+7$.


**Example** 

$n = \text{'42'}$


Here $n$ is a string that has $3$ integer substrings: $4$, $2$, and $42$.  Their sum is $48$, and $48 \text{ modulo } (10^9+7) = 48$.

**Function Description**

Complete the *substrings* function in the editor below. 


substrings has the following parameter(s):


- *string n:* the string representation of an integer 


**Returns** 


- *int:* the sum of the integer values of all substrings in $n$, modulo $10^9+7$

## Input Format

A single line containing an integer as a string, without leading zeros.

## Constraints

+ $1 \le n cast as an integer \le 2 \times 10^5$

## Sample Tests

### Test 1

```
16
```

### Test 2

```
23
```

### Test 3

```
123
```

### Test 4

```
164
```
