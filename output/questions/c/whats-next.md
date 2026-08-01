# What's Next?

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.537320690493557
- **Total Submissions:** 4113
- **Solved Count:** 2210
- **URL:** https://www.hackerrank.com/challenges/whats-next

## Problem Statement

Johnny is playing with a large binary number, $B$. The number is so large that it needs to be compressed into an array of integers, $A$, where the values in *even indices* ($0, 2, 4, \ldots$) represent some number of consecutive $1$ bits and the values in *odd indices* ($1, 3, 5, \ldots$) represent some number of consecutive $0$ bits in alternating substrings of $B$. 		

For example, suppose we have array $A=\{4,1,3,2,4\}$. $A_0$ represents $\text{"1111"}$, $A_1$ represents $\text{"0"}$, $A_2$ represents $\text{"111"}$, $A_3$ represents $\text{"00"}$, and $A_4$ represents $\text{"1111"}$. The number of consecutive binary characters in the $i^{th}$ substring of $B$ corresponds to integer $A_i$, as shown in this diagram:

<img src="https://s3.amazonaws.com/hr-challenge-images/13530/1460021216-fd1bfc1a08-whats.png" title="whats.png" />

When we assemble the sequential alternating sequences of $1$'s and $0$'s, we get $B = \text{"11110111001111"}$.

We define *setCount($B$)* to be the number of $1$'s in a binary number, $B$. Johnny wants to find a binary number, $D$, that is the smallest binary number $\gt B$ where *setCount($B$)* = *setCount($D$)*. He then wants to compress $D$ into an array of integers, $C$ (in the same way that integer array $A$ contains the compressed form of binary string $B$).

Johnny isn't sure how to solve the problem. Given array $A$, find integer array $C$ and print its length on a new line. Then print the elements of array $C$ as a single line of space-separated integers.

## Input Format

The first line contains a single positive integer, $T$, denoting the number of test cases. Each of the $2T$ subsequent lines describes a test case over $2$ lines:

1. The first line contains a single positive integer, $n$, denoting the length of array $A$. 
2. The second line contains $n$ positive space-separated integers describing the respective elements in integer array $A$ (i.e., $A_{0}, A_{1}, \ldots, A_{n-1}$).




## Output Format

For each test case, print the following $2$ lines:	

1. Print the length of integer array $C$ (the array representing the compressed form of binary integer $D$) on a new line. 
2. Print each element of $C$ as a single line of space-separated integers.

It is *guaranteed* that a solution exists.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq n \leq 10$

**Subtasks**

- For a $50\%$ score, $1 \leq A_i \leq 10^4$.
- For a $100\%$ score, $1 \leq A_i \leq 10^{18}$.

## Sample Input

1
5
4 1 3 2 4

## Sample Output

7
4 1 3 1 1 1 3

## Explanation

, which expands to . We then find setCount() . The smallest binary number  which also has eleven 's is . This can be reduced to the integer array . This is demonstrated by the following figure:

Having found , we print its length () as our first line of output, followed by the space-separated elements in  as our second line of output.
