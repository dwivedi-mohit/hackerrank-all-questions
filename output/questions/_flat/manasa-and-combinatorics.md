# Manasa and Combinatorics

---

| Field | Value |
|---|---|
| **Slug** | `manasa-and-combinatorics` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/manasa-and-combinatorics |

---

## Preview

Help Manasa in counting the number of strings.

## Problem Statement

Manasa has a string having **N** number of A's and **2\*N** number of B's. She wants to arrange these characters in such a way that in each prefix and in each suffix of the string the number of **B**'s is greater than or equal to the number of **A**'s. Given the value of N, she wants to find the number of ways to do so.

**Input Format**

The first line contains an integer T i.e. number of test cases.

Next T lines will contain an integer N.


**Output Format**

A single line containing number of ways MOD 99991.

**Constraints**

1 <= T <= 25<br> 
1 <= N <= 10<sup>12</sup>


**Sample Input #00**


	2
    1
    2

  

**Sample Output #00**


    1
    4

**Explanation**


In first case, "BAB" is only valid string.<br>
In second case, "BBAABB", "BABABB" , "BBABAB" and "BABBAB" are valid strings.

## Sample Tests

### Test 1

```
2
1
2
```

### Test 2

```
1
4
```
