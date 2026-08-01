# Array Construction

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.6795415959252971
- **Total Submissions:** 2356
- **Solved Count:** 1601
- **URL:** https://www.hackerrank.com/challenges/array-construction

## Problem Statement

Professor GukiZ has hobby &mdash; constructing different arrays. His best student, Nenad, gave him the following task that he just can't manage to solve:

Construct an $n$-element array, $A$, where the sum of all elements is equal to $s$ and the sum of absolute differences between each pair of elements is equal to $k$. All elements in $A$ must be non-negative integers.

$$A_0 + A_1 + \ldots + A_{n-1} = s$$

$$\sum_{i=0}^{n-1} \sum_{j=i}^{n-1} \mid A_i-A_j \mid = k$$

If there is more then one such array, you need to find the lexicographically smallest one. In the case no such array $A$ exists, print $-1$.

**Note:** An array, $A$, is considered to be lexicographically smaller than another array, $B$, if there is an index $i$ such that  $A_i \lt B_i$ and, for any index $j \lt i$, $A_j=B_j$.


## Input Format

The first line contains an integer, $q$, denoting the number of queries. 	
Each of the $q$ subsequent lines contains three space-separated integers describing the respective values of $n$ (the number of elements in array $A$), $s$ (the sum of elements in $A$), and $k$ (the sum of absolute differences between each pair of elements).

## Output Format

For each query, print $n$ space-separated integers describing the respective elements of the lexicographically smallest array $A$ satisfying the conditions given above. If no such array exists, print $-1$ instead.

## Constraints

* $1\leq q \leq 100$
* $1 \leq n \leq 50$
* $0 \leq s \leq 200$
* $0 \leq k \leq 2000$

**Subtasks**

For $\text{10%}$ of the maximum score:
 
* $1\leq q \leq 10$
* $1 \leq n \leq 5 $
* $0 \leq s \leq 10 $
* $0 \leq k \leq 20 $

For $\text{50%}$ of the maximum score:

* $1\leq q \leq 10$
* $1 \leq n \leq 50 $
* $0  \leq s \leq 100 $
* $0 \leq k \leq 500 $


## Sample Input

3 3 4

## Sample Output

0 1 2

## Explanation

We have  query in which , , and . The lexicographically smallest array is .

- The sum of array 's elements is

- The absolute differences between each pair of elements are:

The sum of these absolute differences is

As array  is both lexicographically smallest and satisfies the given conditions, we print its contents on a new line as 0 1 2.
