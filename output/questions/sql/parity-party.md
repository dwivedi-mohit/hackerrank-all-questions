# Parity Party

- **Domain:** sql
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.5915492957746479
- **Total Submissions:** 142
- **Solved Count:** 84
- **URL:** https://www.hackerrank.com/challenges/parity-party

## Problem Statement

We need your help to divide candies at a very unusual party!  
There are $n$ different candies in total. There are three kinds of people at party:   
  
* $a$ of them want to get *odd* number of candies,  
* $b$ of them want to get *even* number of candies,
* $c$ simply don't care about parity of candies they get.   
    
Find out the number of ways to divide all of $n$ candies between everybody ($a + b + c$ people), such that everyone is satisfied.  Some people may not receive a candy.

## Input Format

One line of input contains four space-separated integers $n, a, b, c$.   


## Output Format

Print one line containing answer to the problem modulo $7340033$.

## Constraints

+ $1 \leq n \leq 10^9$,  
+ $0 \leq a, b, c \leq 50000$,  
+ $1 \leq a + b + c$.

## Sample Input

3 1 1 0

## Sample Output

4

## Explanation

Let  be three different candies. One of the visitors wants to get odd number of candies, the other wants to get even number. There are four good splittings:

.
