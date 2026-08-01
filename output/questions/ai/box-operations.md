# Box Operations

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.7262521588946459
- **Total Submissions:** 2316
- **Solved Count:** 1682
- **URL:** https://www.hackerrank.com/challenges/box-operations

## Problem Statement

Alice purchased an array of $n$ wooden boxes that she indexed from $0$ to $n-1$. On each box $i$, she writes an integer that we'll refer to as $box_i$.

Alice wants you to perform $q$ *operations* on the array of boxes. Each operation is in one of the following forms:

(Note: For each type of operations, $l \le i \le r$)

* ``1 l r c``: Add $c$ to each $box_i$. Note that $c$ can be negative.
* ``2 l r d``: Replace each $box_i$ with $\left\lfloor\frac{box_i}{d}\right\rfloor$. 
* ``3 l r``: Print the minimum value of any $box_i$.
* ``4 l r``: Print the sum of all $box_i$.

Recall that $\left\lfloor x \right\rfloor$ is the maximum integer $y$ such that $y \le x$ (e.g., $\left\lfloor -2.5 \right\rfloor = -3$ and $\left\lfloor -7 \right\rfloor = -7$).

Given $n$, the value of each $box_i$, and $q$ operations, can you perform all the operations efficiently? 



## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of boxes) and $q$ (the number of operations). 		
The second line contains $n$ space-separated integers describing the respective values of $box_0, box_1, \ldots, box_{n-1}$ (i.e., the integers written on each box).			
Each of the $q$ subsequent lines describes an *operation* in one of the four formats defined above.

## Output Format

For each operation of type $3$ or type $4$, print the answer on a new line.

## Constraints

* $1 \le n, q \le 10^5$
* $-10^9 \le box_i \le 10^9$
* $0 \le l \le r \le n-1$
* $-10^4 \le c \le 10^4$
* $2 \le d \le 10^9$

## Sample Input

10 10
-5 -4 -3 -2 -1 0 1 2 3 4
1 0 4 1
1 5 9 1
2 0 9 3
3 0 9
4 0 9
3 0 1
4 2 3
3 4 5
4 6 7
3 8 9

## Sample Output

-2
-2
-2
-2
0
1
1

## Explanation

Initially, the array of boxes looks like this:

We perform the following sequence of operations on the array of boxes:

- The first operation is 1 0 4 1, so we add  to each  where :

- The second operation is 1 5 9 1, so we add  to each  where :

- The third operation is 2 0 9 3, so we divide each  where  by  and take the floor:

- The fourth operation is 3 0 9, so we print the minimum value of  for , which is the result of .

- The fifth operation is 4 0 9, so we print the sum of  for , which is the result of .

... and so on.
