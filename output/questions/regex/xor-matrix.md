# XOR Matrix

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.4376135675348274
- **Total Submissions:** 3302
- **Solved Count:** 1445
- **URL:** https://www.hackerrank.com/challenges/xor-matrix

## Problem Statement

Consider a zero-indexed matrix with $m$ rows and $n$ columns, where each row is filled _gradually_. Given the first row of the matrix, you can generate the elements in the subsequent rows using the following formula:

* $a_{i,j} = a_{i-1,j} \oplus a_{i-1, j+1} \forall j: 0 \le j \le n-2$
* $a_{i, n-1} = a_{i-1, n-1} \oplus a_{i-1,0}$

Each row is generated one by one, from the second row through the last row. Given the first row of the matrix, find and print the elements of the last row as a single line of space-separated integers.

**Note:** The $\oplus$ operator denotes [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of columns in the matrix) and $m$ (the number of rows in the matrix).	
The second line contains $n$ space-separated integers denoting the respective values of the elements in the matrix's first row.

## Output Format

Print $n$ space-separated integers denoting the respective values of the elements in the last row of the matrix.

## Constraints

* $1 \le n \le 10^5$
* $1 \le m \le 10^{18}$
* $0 \le a_{i,j} \le 10^9$

## Sample Input

4 2
6 7 1 3

## Sample Output

1 6 2 5

## Explanation

We use the formula given above to calculate the  values in the last row of the matrix:

-

-

-

-

We then print each value (in order) as a single line of space-separated integers.
