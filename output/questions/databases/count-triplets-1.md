# Count Triplets

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.5648045248718672
- **Total Submissions:** 120578
- **Solved Count:** 68103
- **URL:** https://www.hackerrank.com/challenges/count-triplets-1

## Problem Statement

You are given an array and you need to find number of tripets of indices $(i, j, k)$ such that the elements at those indices are in [geometric progression](https://en.wikipedia.org/wiki/Geometric_progression) for a given common ratio $r$ and $i \lt j \lt k$. 

**Example**    
$arr = [1, 4, 16, 64]$
$r = 4$   

There are $[1, 4, 16]$ and $[4, 16, 64]$ at indices $(0, 1, 2)$ and $(1, 2, 3)$. Return $2$.    

**Function Description**

Complete the *countTriplets* function in the editor below.   

countTriplets has the following parameter(s):

- *int arr[n]:* an array of integers
- *int r*: the common ratio   

**Returns**   

- *int:* the number of triplets   

## Input Format

The first line contains two space-separated integers $n$ and $r$, the size of $arr$ and the common ratio.     
The next line contains $n$ space-seperated integers $arr[i]$.    


## Constraints

- $1 \leq n \leq 10^{5}$  
- $1 \leq r \leq 10^{9}$  
- $1 \leq arr[i] \leq 10^{9}$

## Sample Input

4 2
1 2 2 4

## Sample Output

2

## Explanation

There are  triplets in satisfying our criteria, whose indices are  and
