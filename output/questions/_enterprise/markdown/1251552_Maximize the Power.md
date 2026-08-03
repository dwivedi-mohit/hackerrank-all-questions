# Maximize the Power

## Metadata

- **ID:** 1251552
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Greedy Algorithms, Prefix Sum, Sorting
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates greedy algorithms, prefix sums, and sorting concepts, ideal for mid-level roles. The problem requires maximizing power through strategic subarray selections from given arrays while adhering to specific constraints.

## Problem Statement

Given an array arr of n non-negative integers and an array power of k integers where k is an even number, perform the following operations:

	
- Select two integers i and j such that 0 ≤ i < j < length of power. In each operation, i and j are selected independently.
	
- If power[i] ≤ power[j], add the sum of the subarray arr[power[i]...power[j]] to the power.
	
- If power[i] > power[j], add the sum of the subarray arr[power[j]...power[i]] to the power.
	
- Delete the ith and jth elements from power, reducing its length by 2.

Starting with 0 initial power, maximize the final power after exactly k/2 operations. Return the maximum power modulo (109+7).

 

Note: Subarray arr[l...r] denotes the elements arr[l], arr[l+1], ..., arr[r-1], arr[r].

 

Example

arr = [3, 5, 6, 0, 7] and power = [3, 1, 0, 2].  

k = 4, the size of power, so perform k/2 = 2 operations.

 

One optimal approach is shown.

	
- Select i=0, j=2. Here, power[0] = 3 and power[2] = 0. Add the sum of subarray arr[0...3],  (3 + 5 + 6 + 0) = 14 to the power, 0 + 14 = 14. Remove the two elements from power, and power is [1, 2]. 
	
- Select i=0, j=1. Here, power[0] = 1 and power[1] = 2. Add the sum of subarray arr[1..2], 5 + 6 = 11, so power is 14 + 11 = 25.

 

Return the maximum power possible, 25. (25 modulo (109+7) = 25)

 

Function Description 

Complete the function getMaximumPower in the editor with the following parameter(s):

    int arr[n]:  An array of integers

    int power[k]: An array of integers

 

Returns

    int:  the maximum power modulo (109+7)

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 2 ≤ k ≤ 105, k is even.
	
- 0 ≤ arr[i] ≤ 107, 0 ≤ i < n

	
- 0 ≤ power[i] < n

 

Input Format for Custom Testing

The first line contains an integer, n, number of elements in arr.

Each of the next n lines contains an integer arr[i].

The next line contains an integer, k, number of elements in power.

Each of the next k lines contains an integer power[i].

Sample Case 0

Sample Input 0

STDIN	    FUNCTION
-----	    --------
5      →    n = 5
2      →    arr = [2, 4, 2, 1, 6]
4
2
1
6
4      →    k = 4
4      →    power = [4, 1, 1, 3]
1
1
3

```

Sample Output 0

20

```

Explanation

 

Optimal operations

                                                subarray    resultant
i   j   power[i]    power[j]    subarray        sum         power
--  --  --------    --------    --------        ---------   ---------
0   1   4           1           [4, 2, 1, 6]        13      [1, 3]
0   1   1           3           [1, 6]               7      []  

Total power = 13 + 7 = 20

```

 

arr = [2, 4, 2, 1, 6] and power = [4, 1, 1, 3].
Consider the following two ways to perform the operations:

1st way -

	
- In first operation, select i=0, j=1. Here, power[0] = 4 and power[1] = 1. We add the sum of subarray arr[1...4] which is 13 (4 + 2 + 1 + 6) to the power making it 13. Array power changes to [1, 3]. 
	
- In second operation, select i=0, j=1. Here, power[0] = 1 and power[1] = 3. We add the sum of subarray arr[1..2] which is 7 (4 + 2 + 1) to the power making it 20.

Here we get power = 20 at the end.
2nd way -

	
- In first operation, select i=1, j=2. Here, power[1] = 1 and power[2] = 1. We add the sum of subarray arr[1...1], which is 4, to the power making it 4. Array power changes to [4, 3]. 
	
- In second operation, select i=0, j=1. Here, power[0] = 4 and power[1] = 3. We add the sum of subarray arr[3..4] which is 7 (1 + 6) to the power making it 11.

Here we get power = 11 at the end.
The maximum value of power we get is 20. It can be shown that answer can&#39;t be more than 20.

-->

Sample Case 1

Sample Input 1

STDIN	    FUNCTION
-----	    --------
4      →    n = 4
1      →    arr = [1, 2, 3, 4]
2
3
4
2      →    k = 2
0      →    power = [0, 0]
0

```

Sample Output 1

1

```

Explanation

There is only one way to perform the operation. Select i = 0, j = 1. Here, power[0] = 0 and power[1] = 0. We add the sum of subarray arr[0...0] which is 1 to the power making it 1.

## Sample Input/Output

## Preview

Given an array arr of n non-negative integers and an array power of k integers
