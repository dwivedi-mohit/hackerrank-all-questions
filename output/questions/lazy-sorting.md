# Lazy Sorting

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7617717478052674
- **Total Submissions:** 2506
- **Solved Count:** 1909
- **URL:** https://www.hackerrank.com/challenges/lazy-sorting

## Problem Statement

Logan is cleaning his apartment. In particular, he must sort his old favorite sequence, $P$, of $N$ positive integers in nondecreasing order. He's tired from a long day, so he invented an easy way (in his opinion) to do this job. His algorithm can be described by the following pseudocode:

    while isNotSorted(P) do {	
        WaitOneMinute();
        RandomShuffle(P)
    }

Can you determine the expected number of minutes that Logan will spend waiting for $P$ to be sorted?

## Input Format

The first line contains a single integer, $N$, denoting the size of permutation $P$.		
The second line contains $N$ space-separated integers describing the respective elements in the sequence's current order, $P_0, P_1, \ldots, P_{N-1}$.



## Output Format

Print the expected number of minutes Logan must wait for $P$ to be sorted, correct to  $6$ decimal places.

## Constraints

- $2 \le N \le 18$
- $1 \le P_i \le 100$

## Sample Input

5 2

## Sample Output

2.000000

## Explanation

There are two permutations possible after a random shuffle, and each of them has probability . The probability to get the sequence sorted after the first minute is . The probability that  will be sorted after the second minute is , the probability  will be sorted after the third minute is , and so on. So, the answer is equal to the following sum:

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
