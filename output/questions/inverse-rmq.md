# Inverse RMQ

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.7487573429733394
- **Total Submissions:** 2213
- **Solved Count:** 1657
- **URL:** https://www.hackerrank.com/challenges/inverse-rmq

## Problem Statement

[Range Minimum Query](https://en.wikipedia.org/wiki/Range_minimum_query) is a well-known problem: given an array of distinct integers with size $n = 2 ^ k$ and $m$ queries, find the minimum element on subsegment $[L_i, R_i]$.

One of the most efficient and famous solutions to this problem is a *segment tree*. A segment tree is a full binary tree with $2 \cdot n - 1$ nodes where the leaves contain the values of the original array and each non-leaf node contains the minimum value of its entire subtree.

Usually, a segment tree is represented as an array of integers with $2 \cdot n - 1$ elements. The left child of the $i^{th}$ node is in the $(2 \cdot i + 1)^{th}$ cell, and the right child is in the $(2 \cdot i + 2)^{th}$ cell. For example, $A = [1, 1, 3, 1, 2, 3, 4]$ represents the following segment tree where the first number in a node describes the array index, $i$, in $A$ and the second number denotes the value stored at index $i$ (which corresponds to the minimum value in that node's subtree):

![example1_graph.png](https://s3.amazonaws.com/hr-challenge-images/0/1452359774-5e3ec6eea8-example1_graph.png)

You've just used $n$ *distinct* integers to construct your first segment tree and saved it as an array, $A$, of $2 \cdot n - 1$ values. Unfortunately, some evil guy came and either shuffled or altered the elements in your array. Can you use the altered data to restore the original array? If no, print `NO` on a new line; otherwise, print two lines where the first line contains the word `YES` and the second line contains $2 \cdot n - 1$ space-separated integers denoting the array's original values. If there are several possible original arrays, print the [lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) smallest one.

## Input Format

The first line contains a single integer, $n$, denoting the size of the array.		
The second line contains $2 \cdot n - 1$ space-separated integers denoting the shuffled values of the segment tree.

## Output Format

Print `NO` if this array could not be constructed by shuffling some segment tree. Otherwise, print `YES` on the first line, and $2 \cdot n - 1$ space-separated integers describing the respective values of the original array on the second line. If there are several possible answers, print the lexicographically smallest one.

**Sample Input 0**

    4
    3 1 3 1 2 4 1

**Sample Output 0**

    YES
    1 1 3 1 2 3 4 

**Explanation 0**		
This is the same segment tree shown in the *Problem Statement* above.

**Sample Input 1**

    2
    1 1 1

**Sample Output 1**

	NO 

**Explanation 1**		
A segment tree with three nodes would consist of a root, a left child, and a right child. Because all three numbers in this array are the same and the leaves of the segment tree must be $n$ distinct integers, it's not possible to reconstruct the original array.

## Constraints

- $1 \le n \le 2^{18}$
- $n$ is a power of two.
- Each value in the segment tree is between $-10^9$ and $10^9$.

## Sample Input

4
3 1 3 1 2 4 1

## Sample Output

YES
1 1 3 1 2 3 4

## Explanation

This is the same segment tree shown in the Problem Statement above.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
