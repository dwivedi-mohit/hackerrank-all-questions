# Minimum Start Value

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.8857142857142857
- **Total Submissions:** 35
- **Solved Count:** 31
- **URL:** https://www.hackerrank.com/challenges/minimum-start-value-1

## Problem Statement



Determine a minimum start value such as the running sum with an array never drops below 1.
    

Start with a given array of integers and an arbitrary initial value _x_. Calculate the running sum of _x_ plus each array element, from left to right. The running sum must never get below _1._  Determine the minimum value of _x._ 

 

Example

_arr = [-2, 3, 1, -5]._ 

 

If _x = 4, _the following results are obtained:

Running sum arr[i] ----- ----- 4 -2 2 3 5 1 6 -5 1

 

The final value is _1,_ and the running sum has never dropped below _1._  The minimum starting value for _x_ is 4.

 

Function Description

Complete the function _minX_ in the editor below.

 

minX has the following parameter(s):

    _int arr[n]:_  an array of integers

 

Returns

    int: the minimum integer value for _x_

 

Constraints

- _1 ≤ n ≤ 105_
- _−100 ≤ arr[i] ≤ 100_

 

  Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer _n_, the size of the array _arr_.

Each of the next _n_ lines contains an integer _arr[i]_.

Sample Case 0

Sample Input

STDIN Function ----- ----- 10 → arr[i] size n = 10 -5 → arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5] 4 -2 3 1 -1 -6 -1 0 5

 

Sample Output

8

 

Explanation

Running sum arr[i] ----- ----- 8 -5 3 4 7 -2 5 3 8 1 9 -1 8 -6 2 -1 1 0 1 5 6

The minimum starting value for _x_ is _8_.

Sample Case 1

Sample Input

STDIN Function ----- ----- 5 → arr[i] size n = 5 -5 → arr = [-5, 4, -2, 3, 1] 4 -2 3 1

 

Sample Output

6

 

Explanation

Running sum arr[i] ----- ----- 6 -5 1 4 5 -2 3 3 6 1 7

The minimum starting value for _x _is _6._

Sample Case 2

Sample Input

STDIN Function ----- ----- 10 → arr[i] size n = 10 -5 → arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, -5] 4 -2 3 1 -1 -6 -1 0 -5

 

Sample Output

13

 

Explanation

Running sum arr[i] ----- ----- 13 -5 8 4 12 -2 10 3 13 1 14 -1 13 -6 7 -1 6 0 6 -5 1

The minimum starting value for _x _is _13. _



## Constraints

- 1 ≤ n ≤ 105

- −100 ≤ arr[i] ≤ 100

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

The first line contains an integer n, the size of the array arr.

Each of the next n lines contains an integer arr[i].

Sample Case 0

## Sample Input

STDIN Function ----- ----- 10 → arr[i] size n = 10 -5 → arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5] 4 -2 3 1 -1 -6 -1 0 5

## Explanation

Running sum arr[i] ----- ----- 8 -5 3 4 7 -2 5 3 8 1 9 -1 8 -6 2 -1 1 0 1 5 6

The minimum starting value for x is 8.

Sample Case 1
