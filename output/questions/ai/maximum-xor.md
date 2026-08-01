# Maximum Xor

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 55
- **Success Ratio:** 0.4434286607282388
- **Total Submissions:** 12798
- **Solved Count:** 5675
- **URL:** https://www.hackerrank.com/challenges/maximum-xor

## Problem Statement

You are given an array $arr$ of $n$ elements. A list of integers, $queries$ is given as an input, find the maximum value of $queries[j] \oplus \text{ each } arr[i]$ for all $0 \le i < n$ , where $\oplus$ represents  [xor](https://en.wikipedia.org/wiki/Exclusive_or) of two elements.

Note that there are multiple test cases in one input file.

For example:

$arr = [3, 7, 15, 10]$  

$queries[j] = 3$  
$3 \oplus 3 = 0, \text{max} = 0$  
$3 \oplus 7 = 4, \text{max} = 4$  
$3 \oplus 15 = 12, \text{max} = 12$  
$3 \oplus 10 = 9, \text{max} = 12$  

**Function Description**

Complete the *maxXor* function in the editor below.  It must return an array of integers, each representing the maximum xor value for each element $queries[j]$ against all elements of $arr$.  

maxXor has the following parameter(s):

-  *arr*: an array of integers   
-  *queries*: an array of integers to query  

## Input Format

The first line contains an integer $n$, the size of the array $arr$.

The second line contains $n$ space-separated integers, $arr[i]$ from  $0 \le i < n$.

The third line contain $m$, the size of the array $queries$.

Each of the next $m$ lines contains an integer $queries[j]$ where $0 \le j \lt m$.  

## Output Format

The output should contain $m$ lines with each line representing output for the corresponding input of the testcase.

## Constraints

$1 \le n, m \le 10^5$

$0 \le arr[i], queries[j] \le 10^9$


## Sample Input

3
0 1 2
3
3
7
2

## Sample Output

3
7
3
