# Project Euler #19: Counting Sundays

---

| Field | Value |
|---|---|
| **Slug** | `euler019` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 100 |
| **Contest** | projecteuler |
| **URL** | https://www.hackerrank.com/challenges/euler019 |

---

## Preview

Programming with poetry.

## Problem Statement

<sub>This problem is a programming version of [Problem 19](https://projecteuler.net/problem=19) from [projecteuler.net](https://projecteuler.net/)</sub>


You are given the following information, but you may prefer to do some research for yourself.


1 Jan 1900 was a Monday.

Thirty days has September, 

April, June and November.

All the rest have thirty-one,

Saving February alone,

Which has twenty-eight, rain or shine.

And on leap years, twenty-nine.


A leap year occurs on any year evenly divisible by $4$, but not on a century unless it is divisible by $400$.

How many Sundays fell on the first of the month between two dates(both inclusive)?

## Input Format

The first line contains an integer $T$, i.e., number of test cases.

Each testcase will contain two lines

$Y_1 ~ M_1 ~D_1$ on first line denoting starting date.

$Y_2 ~ M_2 ~D_2$ on second line denoting ending date.

## Output Format

Print the values corresponding to each test case.

## Constraints

+ $1 \leqslant T \leqslant 100$

+ $1900 \leqslant Y_1 \leqslant 10^{16}$

+ $Y_1 \leqslant Y_2 \leqslant (Y_1 + 1000)$

+ $1 \leqslant M_1,M_2 \leqslant 12$

+ $1 \leqslant D_1,D_2 \leqslant 31$

## Sample Tests

### Test 1

```
2
1900 1 1
1910 1 1
2000 1 1
2020 1 1
```

### Test 2

```
18
35
```

### Test 3

```
1 April 1900
1 July 1900
1 September 1901
1 December 1901
1 June 1902
1 February 1903
1 March 1903
1 November 1903
1 May 1904
1 January 1905
1 October 1905
1 April 1906
1 July 1906
1 September 1907 
1 December 1907
1 March 1908
1 November 1908
1 August 1909
```
