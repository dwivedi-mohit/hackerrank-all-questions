# Manasa loves Maths

---

| Field | Value |
|---|---|
| **Slug** | `manasa-loves-maths` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/manasa-loves-maths |

---

## Preview

Find out if any permutation of the given number is divisible by 8.

## Problem Statement

You are given an integer N. Is there a permutation of digits of integer that's divisible by 8? A permutation of digits of integer N is defined as an integer formed by rearranging the digits of N. For example, if the number N = 123, then {123, 132, 213, 231, 312, 321} are the possible permutations.

**Input Format**

The first line contains an integer _T_ i.e. number of test cases.

_T_ lines follow, each containing the integer _N_. 

**Output Format**

For each test case print `YES` if there exists one such re-arrangement of N such that it is divisible by 8 or `NO` if there isn't. 

**Constraints**

1 <= T <= 45<br>
0 <= N <= 10<sup>110</sup>


**Note**

Re-arrangements of _10_ are _{10, 01}_ which boils down to _{10, 1}_.

**Sample Input**


	2
	61
	75
  

**Sample Output**


    YES
    NO
  

**Explanation**

_Test case #00:_ 16 is permutation of 61 which is divisible by 8.

_Test case #01:_ None of permutation of 75, {57, 75}, are divisible by 8.

## Sample Tests

### Test 1

```
2
61
75
```

### Test 2

```
YES
NO
```
