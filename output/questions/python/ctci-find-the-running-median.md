# Heaps: Find the Running Median

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6438098042102164
- **Total Submissions:** 33965
- **Solved Count:** 21867
- **URL:** https://www.hackerrank.com/challenges/ctci-find-the-running-median

## Problem Statement

The median of a dataset of integers is the midpoint value of the dataset for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your dataset of integers in non-decreasing order, then:

- If your dataset contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted dataset $\{1, 2, 3\}$, $2$ is the median.
- If your dataset contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted dataset $\{1, 2, 3, 4\}$, $\frac{2 + 3}{2} = 2.5$ is the median.

Given an input stream of $n$ integers, for each $i^{th}$ integer:

1. Add the $i^{th}$ integer to a running list of integers.
2. Find the median of the updated list (i.e., for the first element through the $i^{th}$ element).
3. Print the list's updated median on a new line. The printed value must be a double-precision number scaled to $1$ decimal place (i.e., $12.3$ format).   

**Note:** The code checker does not test whether you have used heaps.  To get the expected benefit of solving this problem, please try to implement your solution using heaps.  

**Function Description**    

Complete the *runningMedian* function in the editor below.   

*runningMedian* has the following parameters:   
- *int arr[n]:* an array of integers   

**Prints**   

- *float:* After each insertion, print the median of the array to 1 decimal on a new line.  No return value is expected.      

## Input Format

The first line contains a single integer, $n$, the number of integers in the data stream.		
Each line $i$ of the $n$ subsequent lines contains an integer, $a[i]$, to be added to the list.

## Output Format

After each new integer is added to the list, print the list's updated median on a new line as a single double-precision number scaled to $1$ decimal place (i.e., $12.3$ format).

## Constraints

- $1 \le n \le 10^5$  
- $0 \le a[i] \le 10^5$

## Sample Input

STDIN   Function
-----   --------
6       a[] size n = 6
12      a = [12, 4, 5, 3, 8, 7]
4
5
3
8
7

## Sample Output

12.0
8.0
5.0
4.5
5.0
6.0

## Explanation

There are  integers, so we must print the new median on a new line as each integer is added to the list:

-

-

-

-

-

-
