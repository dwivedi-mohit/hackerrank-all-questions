# Prime XOR

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6378361858190709
- **Total Submissions:** 6544
- **Solved Count:** 4174
- **URL:** https://www.hackerrank.com/challenges/prime-xor

## Problem Statement

Penny has an array of $n$ integers, $[ a_0, a_1, \ldots, a_{n-1} ]$. She wants to find the number of unique [multisets](https://en.wikipedia.org/wiki/Multiset) she can form using elements from the array such that the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of all the elements of the multiset is a [prime number](https://en.wikipedia.org/wiki/Prime_number). Recall that a *multiset* is a set which can contain duplicate elements.

Given $q$ queries where each query consists of an array of integers, can you help Penny find and print the number of valid multisets for each array? As these values can be quite large, modulo each answer by $10^9+7$ before printing it on a new line.

## Input Format

The first line contains a single integer, $q$, denoting the number of queries. The $2 \cdot q$ subsequent lines describe each query in the following format:

1. The first line contains a single integer, $n$, denoting the number of integers in the array.
2. The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

On a new line for each query, print a single integer denoting the number of unique multisets Penny can construct using numbers from the array such that the bitwise XOR of all the multiset's elements is prime. As this value is quite large, your answer must be modulo $10^9+7$.

## Constraints

* $1 \le q \le 10$  
* $1 \le n \le 100000$
* $3500 \le a_i \le 4500$

## Sample Input

3
3511 3671 4153

## Explanation

The valid multisets are:

-  is prime.

-  is prime.

-  is prime.

- , which is prime.

Because there are four valid multisets, we print the value of  on a new line.
