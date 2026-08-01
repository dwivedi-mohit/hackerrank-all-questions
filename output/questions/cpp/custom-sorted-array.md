# Custom-Sorted Array

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.8888888888888888
- **Total Submissions:** 54
- **Solved Count:** 48
- **URL:** https://www.hackerrank.com/challenges/custom-sorted-array

## Problem Statement



Find the minimum number of moves necessary to reorder the array so that even numbers are at the front and odd numbers are at the back

In an array, elements at any two indices can be swapped in a single operation called a _move_. For example, if the array is _arr = [17, 4, 8]_, swap _arr[0] = 17_ and _arr[2] = 8_ to get _arr' = [8, 4, 17]_ in a single move. Determine the minimum number of moves required to sort an array such that all of the _even_ elements are at the beginning of the array and all of the _odd_ elements are at the end of the array.

 

**Example**

_arr = __[6, 3, 4, 5]_

 

The following four arrays are valid custom-sorted arrays:

- _a = [6, 4, 3, 5]_
- _a = [4, 6, 3, 5]_
- _a = [6, 4, 5, 3]_
- _a = [4, 6, 5, 3]_

 

The most efficient sorting requires _1_ move: swap the _4_ and the _3._

    

 

**Function Description **

Complete the function _moves_ in the editor below.

 

moves has the following parameter(s):

    _int arr[n]:_  an array of positive integers

**Returns**

    _int: _the minimum number of moves it takes to sort an array of integers with all even elements at earlier indices than any odd element

 

**Note**: The order of the elements within even or odd does not matter.

 

Constraints

- _2 ≤ n ≤ 105_
- _1 ≤ arr[i] ≤ 109_, where _0 ≤ i < n_.
- It is guaranteed that array _a_ contains at least one _even_ and one _odd_ element.

 

  Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function_._

 

The first line contains an integer _n_, the number of elements in array _a_rr.

The next _n_ lines each contain an integer describing _arr[i ]_where _0 ≤ i < n._

Sample Case 0

Sample Input 0

STDIN    Function -----    ------- 4    →   arr[] size n = 4 13   →   arr = [13, 10, 21, 20] 10 21 20

 

Sample Output 0

1

 

Explanation 0

Swap _arr[0]_ and _arr[3]_ to get the custom-sorted array _arr' = [20, 10, 21, 13]_ in 1 move.

 

Sample Case 1

Sample Input 1

STDIN    Function -----    -------- 5    →   arr[] size n = 5 8    →   arr = [8, 5, 11, 4, 6] 5 11 4 6

 

Sample Output 1

2

 

Explanation 1

Perform the following moves on the array:

1. Swap _arr[1]_ and _arr[3]_ to get the array _arr' = [8, 4, 11, 5, 6]_.
2. Swap _arr[2]_ and _arr[4]_ to get the array _arr'' = [8, 4, 6, 5, 11]_.

 

It took two moves to get a valid custom-sorted array. This is minimal.



## Constraints

- 2 ≤ n ≤ 105

- 1 ≤ arr[i] ≤ 109, where 0 ≤ i < n.

- It is guaranteed that array a contains at least one even and one odd element.

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function_._

The first line contains an integer n, the number of elements in array _a_rr.

The next n lines each contain an integer describing _arr[i ]_where 0 ≤ i < n.

Sample Case 0

## Sample Input

STDIN    Function -----    ------- 4    →   arr[] size n = 4 13   →   arr = [13, 10, 21, 20] 10 21 20

## Sample Output

1

## Explanation

Swap arr[0] and arr[3] to get the custom-sorted array arr' = [20, 10, 21, 13] in 1 move.

Sample Case 1
