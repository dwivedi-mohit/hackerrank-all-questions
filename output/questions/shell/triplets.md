# Triplets

- **Domain:** shell
- **Difficulty:** Advanced
- **Max Score:** 90
- **Success Ratio:** 0.41414141414141414
- **Total Submissions:** 5346
- **Solved Count:** 2214
- **URL:** https://www.hackerrank.com/challenges/triplets

## Problem Statement

There is an integer array $d$ which does not contain more than two elements of the same value. How many distinct ascending triples ($d[i] \lt d[j] \lt d[k], i \lt j \lt k$) are present? 

**Input format**  
The first line contains an integer, $N$, denoting the number of elements in the array. This is followed by a single line, containing $N$ space-separated integers. Please note that there are no leading spaces before the first number, and there are no trailing spaces after the last number.

**Output format:**  
A single integer that denotes the number of distinct ascending triplets present in the array.

**Constraints:**  
$N \le 10$<sup>$5$</sup>  
Every element of the array is present at most twice.  
Every element of the array is a 32-bit non-negative integer.

**Sample input:**  

    6  
    1 1 2 2 3 4  
    
**Sample output:**  

    4

**Explanation**  
The distinct triplets are  
(1,2,3)  
(1,2,4)  
(1,3,4)  
(2,3,4)

The elements of the array might not be sorted. Make no assumptions of the same.

## Constraints

Every element of the array is present at most twice.

Every element of the array is a 32-bit non-negative integer.

Sample input:

6
1 1 2 2 3 4

Sample output:

4

## Explanation

The distinct triplets are

(1,2,3)

(1,2,4)

(1,3,4)

(2,3,4)

The elements of the array might not be sorted. Make no assumptions of the same.
