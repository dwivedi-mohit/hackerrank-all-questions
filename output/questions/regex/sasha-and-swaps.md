# Sasha and Swaps

- **Domain:** regex
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.8367346938775511
- **Total Submissions:** 98
- **Solved Count:** 82
- **URL:** https://www.hackerrank.com/challenges/sasha-and-swaps

## Problem Statement

Little Sasha likes to swap elements in his array. Initially, he has an array of $N$ numbers $1, 2, ..., N$ in ascending order. Then, he swaps some elements in it $K$ times. He really likes this sequence of $K$ swaps and repeats it $T$ times. However, Sasha forgot his favorite swap sequence the next day. 

Given the resulting permutation, find the swap sequence used by Sasha or say that there is no such sequence.

<!-- To reviewer: in Russian language Sasha is a shortened version of my name (Alexander), so he definitely considered to be a boy :) --> 

## Input Format

The first line of input contains three integers $N$, $K$, and $T$, respectively. <br>
The second line contains a permutation of numbers $1, 2, ..., N$.

**Constraints**  
$2 \leqslant N \leqslant 10^5$  
$1 \leqslant K \leqslant 10^5$  
$1 \leqslant T \leqslant 2 \times 10^9$

## Output Format


Print $K$ lines. The $i^{th}$ line contains two distinct integers $a_i$, $b_i$ which means that the $i^{th}$ swap will be of $a_i^{th}$ and $b_i^{th}$ numbers.  If there are multiple possible answers, print any of them.<br>
Otherwise, if there is no such sequence of swaps, print "*no solution*" without quotes.

## Sample Input

5 3 2
4 3 2 1 5

## Sample Output

1 2
2 4
3 4

## Explanation

Let's look at the sequence after each swap:

The first series of swaps:

-

-

-

The second series of swaps:

-

-

-
