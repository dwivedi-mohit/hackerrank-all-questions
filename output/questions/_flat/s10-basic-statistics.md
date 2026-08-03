# Day 0: Mean, Median, and Mode

---

| Field | Value |
|---|---|
| **Slug** | `s10-basic-statistics` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/s10-basic-statistics |

---

## Preview

Compute the mean, median, mode, and standard deviation.

## Problem Statement

**Objective**	
In this challenge, we practice calculating the *mean*, *median*, and *mode*. Check out the [Tutorial](/challenges/s10-basic-statistics/tutorial) tab for learning materials and an instructional video!

**Task**	
Given an array, $X$, of $N$ integers, calculate and print the respective *mean*, *median*, and *mode* on separate lines. If your array contains more than one *modal value*, choose the numerically smallest one.

**Note:** Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of $1$ decimal place (i.e., $12.3$, $7.0$ format).


**Example**

$N = 6$

$X = [1, 2, 3, 4, 5, 5]$


The mean is $\frac{20}{6} = 3.3$.

The median is $\frac{3+4}{2} = 3.5$.  

The mode is $5$ because $5$ occurs most frequently.

## Input Format

The first line contains an integer, $N$, the number of elements in the array. 	
The second line contains $N$ space-separated integers that describe the array's elements.

## Output Format

Print $3$ lines of output in the following order:

1. Print the *mean* on the first line to a scale of $1$ decimal place (i.e., $12.3$, $7.0$).
2. Print the *median* on a new line, to a scale of $1$ decimal place (i.e., $12.3$, $7.0$).
3. Print the *mode* on a new line. If more than one such value exists, print the numerically smallest one.

## Constraints

- $10 \le N \le 2500$

- $0 \lt x[i]  \le 10^5$, where $x[i]$ is the $i^{th}$ element of the array.

## Sample Tests

### Test 1

```
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
```

### Test 2

```
43900.6
44627.5
4978
```

### Test 3

```
4978
:
1
11735
:
1
14216
:
1
14470
:
1
38120
:
1
51135
:
1
64630
:
1
67060
:
1
73429
:
1
99233
:
1
```
