# Find the Running Median

---

| Field | Value |
|---|---|
| **Slug** | `three-month-preparation-kit-find-the-running-median` |
| **Domain** |  |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/three-month-preparation-kit-find-the-running-median |

---

## Preview

Find the median of the elements after inputting each element.

## Problem Statement

The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

- If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set $\{1, 2, 3\}$, $2$ is the median.
- If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set $\{1, 2, 3, 4\}$, $\frac{2 + 3}{2} = 2.5$ is the median.

Given an input stream of $n$ integers, perform the following task for each $i^{th}$ integer:

1. Add the $i^{th}$ integer to a running list of integers.
2. Find the median of the updated list (i.e., for the first element through the $i^{th}$ element).
3. Print the updated median on a new line. The printed value must be a double-precision number scaled to $1$ decimal place (i.e., $12.3$ format).


**Example**

$a = [7, 3, 5, 2]$


<pre>
Sorted			Median
[7]				7.0
[3, 7]			5.0
[3, 5, 7]		5.0
[2, 3, 5, 7]	4.0
</pre>


Each of the median values is stored in an array and the array is returned for the main function to print.


**Note:**  Add formatting to the print statement.


**Function Description** 

Complete the *runningMedian* function in the editor below.


*runningMedian* has the following parameters: 

- *int a[n]:* an array of integers


**Returns**

- *float[n]:* the median of the array after each insertion, modify the print statement in main to get proper formatting.

## Input Format

The first line contains a single integer, $n$, the number of integers in the data stream.		
Each line $i$ of the $n$ subsequent lines contains an integer, $a[i]$, to be inserted into the list.

## Constraints

- $1 \le n \le 10^5$

- $0 \le a[i] \le 10^5$

## Sample Tests

### Test 1

```
Sorted Median
[7] 7.0
[3, 7] 5.0
[3, 5, 7] 5.0
[2, 3, 5, 7] 4.0
```

### Test 2

```
STDIN Function
----- --------
6 a[] size n = 6
12 a = [12, 4, 5, 3, 8, 7]
4
5
3
8
7
```

### Test 3

```
12.0
8.0
5.0
4.5
5.0
6.0
```
