# Special Multiple

---

| Field | Value |
|---|---|
| **Slug** | `special-multiple` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/special-multiple |

---

## Preview

Can you find the least positive integer that is made of only 0s and 9s? - 30 Points

## Problem Statement

You are given an integer _N_. Can you find the least positive integer _X_ made up of only 9's and 0's, such that, X is a multiple of _N_?

**Update**


_X_ is made up of one or more occurences of 9 and zero or more occurences of 0. 

**Input Format**

The first line contains an integer T which denotes the number of test cases. T lines follow.

Each line contains the integer _N_ for which the solution has to be found.

**Output Format**

Print the answer _X_ to STDOUT corresponding to each test case. The output should not contain any leading zeroes. 

**Constraints**

1 <= T <= 10<sup>4</sup>

1 <= N <= 500

**Sample Input**


	3
    5
    7
    1

**Sample Output**


	90
    9009
    9

**Explanation**

90 is the smallest number made up of 9's and 0's divisible by 5. 
Similarly, you can derive for other cases. 

**Timelimits**
Timelimits for this challenge is given [here](https://www.hackerrank.com/environment)

## Sample Tests

### Test 1

```
3
5
7
1
```

### Test 2

```
90
9009
9
```
