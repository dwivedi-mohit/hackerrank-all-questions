# Alien Flowers

- **Domain:** fp
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.8513513513513513
- **Total Submissions:** 148
- **Solved Count:** 126
- **URL:** https://www.hackerrank.com/challenges/alien-flowers

## Problem Statement

Meera bought a house on Mars, and plans to decorate it with chains of alien flowers. Each flower is either red ($R$) or blue ($B$), and Meera knows how many occurrences of `RR`, `RB`, `BB`, and `BR` she wants to see in a chain. 	

The diagram below shows a flower chain of length $10$:

<img src="https://s3.amazonaws.com/hr-challenge-images/14591/1453204624-d20e72c6a1-ornament.jpg" title="ornament.jpg" />

In this example, `RR` occurs $2$ times (at positions $0$ and $4$), `RB` occurs $3$ times (at positions $1$, $5$, and $7$), `BB` occurs $1$ time (at position $2$), and `BR` occurs $3$ times (at positions $3$, $6$, and $8$).

Meera wants your help determining how many different chains with *positive length* can be made. Given $A, B, C$, and $D$, find the number of different chains having occurrences of `RR`, `RB`, `BB` and `BR` equal to inputs $A, B, C$, and $D$, respectively. As the answer can be very large, your printed output should be $answer \ \% \ (10^9+7)$.



## Input Format

One line of space-separated, non-negative integers: $A$ (occurrences of `RR`), $B$ (occurrences of `RB`), $C$ (occurrences of `BB`), and $D$ (occurrences of `BR`), respectively.



## Output Format

Find the number of chains having $A, B, C$, and $D$ occurrences of `RR`, `RB`, `BB`, and `BR`, respectively, and print the $answer \ \% \ (10^9+7)$.

## Constraints

* For $20\%$ Points: $0 \leq A,B,C,D \leq 4$

* For $50\%$ Points: $0 \leq A,B,C,D \leq 10^2$

* For $100\%$ Points: $0 \leq A,B,C,D \leq 10^5$

## Sample Input

1 1 2 1

## Explanation

The  flower chains having exactly , and  occurrences of RR, RB, BB and BR are:
