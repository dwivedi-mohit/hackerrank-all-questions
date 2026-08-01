# Min Max Riddle

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.48804947350827343
- **Total Submissions:** 17949
- **Solved Count:** 8760
- **URL:** https://www.hackerrank.com/challenges/min-max-riddle

## Problem Statement

Given an integer array of size $n$, find the maximum of the minimum(s) of every window size in the array. The window size varies from $1$ to $n$.  

For example, given $arr = [6, 3, 5, 1, 12]$, consider window sizes of $1$ through $5$.  Windows of size $1$ are $(6), (3), (5), (1), (12)$.  The maximum value of the minimum values of these windows is $12$.  Windows of size $2$ are $(6,3), (3,5), (5,1), (1,12)$ and their minima are $(3, 3, 1, 1)$.  The maximum of these values is $3$.  Continue this process through window size $5$ to finally consider the entire array.  All of the answers are $12, 3, 3, 1, 1$.

**Function Description**

Complete the *riddle* function in the editor below.  It must return an array of integers representing the maximum minimum value for each window size from $1$ to $n$.  

riddle has the following parameter(s):

- *arr*: an array of integers  


## Input Format

The first line contains a single integer, $n$, the size of $arr$.  
The second line contains $n$ space-separated integers, each an $arr[i]$.  



## Output Format

Single line containing $n$ space-separated integers denoting the output for each window size from $1$ to $n$.

## Constraints

$1 \le n \le 10^6$

$0 \le arr[i] \le 10^9$


## Sample Input

4
2 6 1 12

## Sample Output

12 2 1 1

## Explanation

Here  and

  window size
  window1
  window2
  window3
  window4
  maximum of all windows

  1
  2
  6
  1
  12
  12

  2
  2
  1
  1

  2

  3
  1
  1

  1

  4
  1

  1
