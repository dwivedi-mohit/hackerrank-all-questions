# Beautiful Triplets

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9109373890821325
- **Total Submissions:** 112696
- **Solved Count:** 102659
- **URL:** https://www.hackerrank.com/challenges/beautiful-triplets

## Problem Statement

Given a sequence of integers $a$, a triplet $(a[i],a[j],a[k])$ is beautiful if:

* $i<j<k$
* $a[j]-a[i] = a[k]-a[j] = d$

Given an increasing sequenc of integers and the value of $d$, count the number of beautiful triplets in the sequence.

**Example**   
$arr = [2, 2, 3, 4, 5]$   
$d = 1$    

There are three beautiful triplets, by index: $[i,j,k] = [0,2,3],[1,2,3],[2,3,4]$.  To test the first triplet, $arr[j] - arr[i] = 3 - 2 = 1$ and $arr[k] - arr[j] = 4 - 3 = 1$.  

**Function Description**  

Complete the *beautifulTriplets* function in the editor below.     

beautifulTriplets has the following parameters:  

- *int d:* the value to match   
- *int arr[n]:*  the sequence, sorted ascending   

**Returns**   

- *int:* the number of beautiful triplets   

## Input Format

The first line contains $2$ space-separated integers, $n$ and $d$, the length of the sequence and the beautiful difference.		
The second line contains $n$ space-separated integers $arr[i]$.

## Constraints

* $1 \le n \le 10^4$
* $1 \le d \le 20$
* $0 \le arr[i] \le 2 \times 10^4$
* $arr[i]>arr[i-1]$

## Sample Input

STDIN           Function
-----           --------
7 3             arr[] size n = 7, d = 3
1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]

## Explanation

There are many possible triplets , but our only beautiful triplets are  ,  and  by value, not index. Please see the equations below:

Recall that a beautiful triplet satisfies the following equivalence relation:  where .
