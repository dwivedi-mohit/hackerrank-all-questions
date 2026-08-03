# Day 1: Quartiles

---

| Field | Value |
|---|---|
| **Slug** | `s10-quartiles` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/s10-quartiles |

---

## Preview

Calculate quartiles for an array of integers

## Problem Statement

**Objective** <br>
In this challenge, we practice calculating *quartiles*. Check out the [Tutorial](/challenges/s10-quartiles/tutorial) tab for learning materials and an instructional video!

**Task** <br>
Given an array, $arr$, of $n$ integers, calculate the respective first quartile ($Q_1$), second quartile ($Q_2$), and third quartile ($Q_3$). It is guaranteed that $Q_1$, $Q_2$, and $Q_3$ are integers.


**Example** 

$arr = [9, 5, 7, 1, 3]$ 


The sorted array is $[1, 3, 5, 7, 9]$ which has an odd number of elements.  The lower half consists of $[1, 3]$, and its median is $\frac{1+3}{2} = 2$.  The middle element is $5$ and represents the second quartile.  The upper half is $[7, 9]$ and its median is $\frac{7 + 9}{2} = 8$.  Return $[2, 5, 8]$. 


----------------

$arr = [1, 3, 5, 7]$


The array is already sorted.  The lower half is $[1,3]$ with a median = $\frac{1 + 3}{2} = 2$.  The median of the entire array is $\frac{3 + 5}{2} = 4$, and of the upper half is $\frac{5 + 7}{2} = 6$.  Return $[2, 4,6]$.


**Function Description** 


Complete the *quartiles* function in the editor below.


*quartiles* has the following parameters:


- *int arr[n]:* the values to segregate 


**Returns**


- *int[3]:* the medians of the left half of $arr$, $arr$ in total, and the right half of $arr$.

## Input Format

The first line contains an integer, $n$, the number of elements in $arr$. 	
The second line contains $n$ space-separated integers, each an $arr[i]$.

## Constraints

- $5 \le n \le 50$

- $0 \lt arr[i]  \le 100$, where $arr[i]$ is the $i^{th}$ element of the array.

## Sample Tests

### Test 1

```
STDIN Function
----- -------- 
9 arr[] size n = 9 
3 7 8 5 12 14 21 13 18 arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
```

### Test 2

```
6
12
16
```
