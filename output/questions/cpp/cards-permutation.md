# Cards Permutation

- **Domain:** cpp
- **Difficulty:** Expert
- **Max Score:** 85
- **Success Ratio:** 0.7412523020257827
- **Total Submissions:** 9774
- **Solved Count:** 7245
- **URL:** https://www.hackerrank.com/challenges/cards-permutation

## Problem Statement

Alice was given the $n$ integers from $1$ to $n$. She wrote all possible permutations in increasing lexicographical order, and wrote each permutation in a new line. For example, for $n = 3$, there are $6$ possible permutations:

1. $[1, 2, 3]$
2. $[1, 3, 2]$
3. $[2, 1, 3]$
4. $[2, 3, 1]$
5. $[3, 1, 2]$
6. $[3, 2, 1]$

She then chose one permutation among them as her *favorite permutation*.

After some time, she forgot some elements of her favorite permutation. Nevertheless, she still tried to write down its elements. She wrote a $0$ in every position where she forgot the true value.

She wants to know the sum of the line numbers of the permutations which could possibly be her favorite permutation, i.e., permutations which can be obtained by replacing the $0$s. Can you help her out? 

Since the sum can be large, find it modulo $10^9 + 7$.

## Input Format

The first line contains a single integer $n$.

The next line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$ denoting Alice's favorite permutation with some positions replaced by $0$.  

## Output Format

Print a single line containing a single integer denoting the sum of the line numbers of the permutations which could possibly be Alice's favorite permutation.


## Constraints

- $1 \le n \le 3\cdot 10^{5}$
- $0 \le a_i \le n$
- The positive values appearing in $[a_1, \ldots, a_n]$ are distinct.

**Subtask**  

- For ~33% of the total points, $n \le 5000$  

## Sample Input

4
0 2 3 0

## Sample Output

23

## Explanation

The possible permutations are  and . The permutation  occurs on line  and the permutation  occurs on line . Therefore the sum is .
