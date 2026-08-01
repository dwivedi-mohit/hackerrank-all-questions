# Introduction to Algebra 2

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.1092436974789916
- **Total Submissions:** 119
- **Solved Count:** 13
- **URL:** https://www.hackerrank.com/challenges/introduction-to-algebra-2

## Problem Statement

*Important note: [Introduction to Algebra](https://www.hackerrank.com/contests/zenhacks/challenges/introduction-to-algebra) is a prerequisite for this challenge.*  

Welcome back to Sevenkplus' perfect math class! 
You are now familiar with the following types of magmas: **quasigroup**, **loop**, **semigroup**, **monoid**, **group**, **abelian group**, **rack**, and **quandle**.
Furthermore, you are familiar with the **magic number** of a magma.

Or are you?

The following problem is an exercise to check whether you *really* are familiar with these definitions.

Find as many magmas as you can, such that no two of them have the same magic number.

## Input Format

There is no input for this challenge, your code should print the output in the below mentioned format.  

## Output Format

The first line, $T$, the number of magmas of different magic numbers you can find.
Following are $T$ magmas.

For each magma, the first line is a integer $n$, the size of the set $M$. (Yes, you only need to consider finite algebraic structures here, which greatly simplies the problem.)
Without loss of generality, we assume that $M=\{0,1,\ldots,n-1\}$.

Following are $n$ lines. Each line contains $n$ integers. The $j$-th number on the $i$-th line is $(i-1)\bigodot (j-1)$ where $\bigodot$ is the binary operation of the magma.

You know, judging homework is not fun. So you should make sure that $1\le n\le 100$.
Also, Sevenkplus is generous enough to give you a small hint: $T\le 256$.

Your answer is considered correct only if $T$ is the largest possible, and the $T$ magmas are valid and have different magic numbers.

## Sample Input

NO INPUT

## Sample Output

1
0
2
1 1
1 0

## Explanation

The sample output is not a correct output.
It is there to show the output format.
