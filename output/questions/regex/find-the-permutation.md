# Find the permutation

- **Domain:** regex
- **Difficulty:** Expert
- **Max Score:** 150
- **Success Ratio:** 0.8259911894273128
- **Total Submissions:** 2270
- **Solved Count:** 1875
- **URL:** https://www.hackerrank.com/challenges/find-the-permutation

## Problem Statement

Consider a [permutation](https://en.wikipedia.org/wiki/Permutation), $p_i$, of integers from $1$ to $n$. Let's determine the $distance$ of $p_i$ to be the *minimum absolute difference* between any $2$ consecutive integers in $p_i$: 
$$distance(p_i)= \min \limits_{0 \le j \lt n - 1} \lvert \ p_i[j] - p_i[j+1] \ \rvert \text{ if } n > 1 \text{, or } 0 \text{ if } n = 1$$

Generate a [lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) sorted list of all permutations of length $n$ having a *maximal distance* between all permutations of the same length. Print the lexicographically $k^{th}$ permutation.

## Input Format

The first line contains an integer, $t$ (the number of test cases).

The $t$ subsequent lines each contain two space-separated integers, $n_i$ (the permutation length) and $k_i$ (the 1-based index in the list of permutations having a maximal distance), respectively. The $i^{th}$ line corresponds to the $i^{th}$ test case. 

**Note:** It is guaranteed that the sum of all $n_i$ does not exceed $10^6$.

**Constraints**

- $1 \le t \le 10$
- $1 \le n_i \le 10^6$
- $1 \le k_i \le 10^{18}$

## Output Format

For each test case: if the list of permutations having maximal distance has *at least* $k$ elements, print the $k^{th}$ permutation as sequential (i.e.: from $1$ to $n$) space-separated integers on a new line; otherwise, print $-1$.

## Constraints

-

-

-

## Sample Input

3 5
4 2
4 3

## Sample Output

3 1 2
3 1 4 2
-1

## Explanation

For  and :

Each of the  permutations has distance . We choose the fifth one (because ), and print 3 1 2 on a new line.

For  and :

The maximal distance in the list of permutations of integers from  to  is , and the only permutations having that distance are  and . We choose the second one (because ), and print 3 1 4 2 on a new line.
