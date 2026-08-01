# Maximum Subarray Sum

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 65
- **Success Ratio:** 0.40913695630861735
- **Total Submissions:** 61202
- **Solved Count:** 25040
- **URL:** https://www.hackerrank.com/challenges/maximum-subarray-sum

## Problem Statement

We define the following:

- A *subarray* of array $a$ of length $n$ is a contiguous segment from $a[i]$ through $a[j]$ where $0 \le i \le j \lt n$.
- The *sum* of an array is the sum of its elements.

Given an $n$ element array of integers, $a$, and an integer, $m$, determine the maximum value of the sum of any of its subarrays modulo $m$. 

**Example**    
$a=[1,2,3]$    
$m=2$     

The following table lists all subarrays and their moduli:

```
		sum	%2
[1]		1	1
[2]		2	0
[3]		3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0
```
The maximum modulus is $1$.

**Function Description**

Complete the *maximumSum* function in the editor below.  

maximumSum has the following parameter(s):

- *long a[n]:* the array to analyze   
- *long m:* the modulo divisor   

**Returns**   
- *long:* the maximum (subarray sum modulo $m$)   

## Input Format

The first line contains an integer $q$, the number of queries to perform.

The next $q$ pairs of lines are as follows:

- The first line contains two space-separated integers $n$ and (long)$m$, the length of $a$ and the modulo divisor.  
- The second line contains $n$ space-separated long integers $a[i]$.

## Constraints

- $2 \le n \le 10^{5}$  
- $1 \le m \le 10^{14}$  
- $1 \le a[i] \le 10^{18}$  
- $2 \le $ the sum of $n$ over all test cases $ \le 5 \times 10^5$   

## Sample Input

STDIN       Function
-----       --------
1           q = 1
5 7         a[] size n = 5, m = 7
3 3 9 9 5

## Explanation

The subarrays of array  and their respective sums modulo  are ranked in order of length and sum in the following list:

-  and

 and

-

-

-

-

The maximum value for  for any subarray is .
