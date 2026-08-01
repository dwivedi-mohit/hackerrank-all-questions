# Manipulative Numbers

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 55
- **Success Ratio:** 0.5991098938719617
- **Total Submissions:** 2921
- **Solved Count:** 1750
- **URL:** https://www.hackerrank.com/challenges/manipulative-numbers

## Problem Statement

Suppose that $A$ is a list of $n$ numbers $\{A_1, A_2, A_3, \ldots , A_n\}$ and $B = \{B_1, B_2, B_3, .. ,B_n\}$ is a permutation of these numbers, we say B is *K-Manipulative* if and only if:

$M(B) = minimum(B_1 \oplus B_2, B_2 \oplus B_3, B_3 \oplus B_4, \ldots , B_{n-1} \oplus B_n, B_n \oplus B_1 )$ is not less than $2^K$, where $\oplus$ represents the _XOR_ operator.

You are given $A$. Find the largest $K$ such that there exists a _K-manipulative_ permutation $B$.


**Input:**

The first line is an integer $N$. The second line contains $N$ space separated integers - $A_1\ A_2\ \ldots\ A_n$.  

**Output:**  
The largest possible $K$, or $-1$ if there is no solution.

**Constraints:**  

- $1 < n <= 100$ 
- $0 \le A_i \le 10^9, where\ i \in [1, n]$ 


## Constraints

-

-

## Sample Input

3
13 3 10

## Sample Output

2

## Explanation

Here the list  is . One possible permutation . Here

.

So there exists a permutation  of  such that  is not less than . However there does not exist any permutation  of  such that  is not less than . So the maximum possible value of  is .
