# Minimum Sum 10

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.77875
- **Total Submissions:** 800
- **Solved Count:** 623
- **URL:** https://www.hackerrank.com/challenges/minimum-sum-11

## Problem Statement



Given an array of integers, perform some number _k_ of operations. Each operation consists of removing an element from the array, dividing it by 2 and inserting the ceiling of that result back into the array. Minimize the sum of the elements in the final array.

 

**Example:**

_nums = __[10, 20, 7]_ 

_k = 4_ 

                           

Pick    Pick/2    Ceiling         Result

 Initial array                            _[10, 20, 7]_

_7           3.5             4             [ 10, 20, 4]_

_10        5                 5               [5, 20, 4]_

_20        10            10               [5, 10, 4]_

_10        5                5                [5, 5, 4]_

 

The sum of the final array is _5 + 5 + 4 = 14,_ and that sum is minimal.

 

Function Description

Complete the function _minSum_ in the editor below.

 

minSum has the following parameters:

    _int nums[n]:_  an array of integers, indexed _0_ to _n-1_

    _int k:_  an integer

**Returns**

    _int:_  the minimum sum of the array after _k_ steps

 

Constraints

- _1 ≤ n ≤ 105_
- _1 ≤ num[i] ≤ 104 (_where_ 0 ≤ i < n)_
- _1 ≤ k ≤ 2\*106_

 

  Input Format For Custom Testing

The first line contains an integer, _n_, denoting the number of elements in _nums_.  
Each line _i_ of the _n_ subsequent lines (where _0 ≤ i < n_) contains an integer describing _nums[i]_.  
The last line contains an integer, _k_, denoting the number of moves.

  Sample Case 0

Sample Input For Custom Testing

STDIN    Function -----    -------- 1    →   nums[] size n = 1 2    →   nums = [2] 1    →   k = 1

Sample Output

1

Explanation

 

In the first operation, the number _2_ is reduced to _1._

Sample Case 1

Sample Input For Custom Testing

STDIN    Function -----    -------- 2    →   nums[] size n = 2 2    →   nums = [2, 3] 3 1    →   k = 1

Sample Output

4

Explanation

 

In the first operation, either of the numbers may be reduced.

- If the number _2_ gets reduced to _1_, the sum of the array is _4_.
- If the number 3 gets reduced to _2_ (_3_ divided by _2_ equals _1.5,_ _ceil(1.5) = 2_), the sum of the array is _4_.

 

The minimum sum of the array after one operation is _4_.



## Constraints

- 1 ≤ n ≤ 105

- _1 ≤ num[i] ≤ 104 (where 0 ≤ i < n)_

- 1 ≤ k ≤ 2*106

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in nums.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing nums[i].

The last line contains an integer, k, denoting the number of moves.

Sample Case 0

Sample Input For Custom Testing

STDIN    Function -----    -------- 1    →   nums[] size n = 1 2    →   nums = [2] 1    →   k = 1

## Explanation

In the first operation, the number 2 is reduced to 1.

Sample Case 1

Sample Input For Custom Testing

STDIN    Function -----    -------- 2    →   nums[] size n = 2 2    →   nums = [2, 3] 3 1    →   k = 1
