# Favorite sequence

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 95
- **Success Ratio:** 0.6652892561983471
- **Total Submissions:** 3630
- **Solved Count:** 2415
- **URL:** https://www.hackerrank.com/challenges/favourite-sequence

## Problem Statement

Johnny, like every mathematician, has his favorite sequence of __distinct__ natural numbers.  Let’s call this sequence $M$. Johnny was very bored, so he wrote down $N$ copies of the sequence $M$ in his big notebook. One day, when Johnny was out, his little sister Mary erased some numbers(possibly zero) from every copy of $M$ and then threw the notebook out onto the street. You just found it. Can you reconstruct the sequence?  
<br>
In the input there are $N$ sequences of natural numbers representing the $N$ copies of the sequence $M$ after Mary’s prank. In each of them all numbers are __distinct__. Your task is to construct the shortest sequence $S$ that might have been the original $M$. If there are many such sequences, return the [lexicographically](http://en.wikipedia.org/wiki/Lexicographical_order) smallest one. It is guaranteed that such a sequence exists.

**Note**  
Sequence $A[1\ldots n]$ is lexicographically less than sequence $B[1\ldots n]$ if and only if there exists $1 \le i \le n$ such that for all $1 \le j < i, A[j] = B[j] \ \ and\ \  A[i] < B[i]$.


## Input Format

In the first line, there is one number $N$ denoting the number of copies of $M$.  
This is followed by $K$   
and in next line a sequence of length $K$ representing one of sequences after Mary's prank. All numbers are separated by a single space.  

**Constraints**  
$1 \le N \le 10^3$  
$2 \le K \le 10^3$  
All values in one sequence are __distinct__ numbers in range $[1, 10^6]$.


## Output Format

In one line, write the space-separated sequence $S$ - the shortest sequence that might have been the original $M$. If there are many such sequences, return the lexicographically smallest one.


## Constraints

All values in one sequence are distinct numbers in range .

## Sample Input

2
1 3
3
2 3 4

## Sample Output

1 2 3 4

## Explanation

You have 2 copies of the sequence with some missing numbers:  and . There are two candidates for the original sequence , where the first one is lexicographically least.
