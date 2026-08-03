# Factorial Length Sum

---

| Field | Value |
|---|---|
| **Slug** | `private-factorial-set` |
| **Contest** | codeagon-2016 |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/private-factorial-set |

---

## Problem Statement

The *factorial length* of a number is defined here as the sum of [prime powers](https://en.wikipedia.org/wiki/Prime_power) in the number's factorization; for example:		
$factorialLength(6) = 2$. $3 = 2^1 \times 3^1$. Summing the powers, we get $1 + 1 = 2$.      
$factorialLength(12) = 3$. $4 = 2^2 \times 3^1$. Summing the powers, we get $2 + 1 = 3$.

Given an array, $A$, of $N$ integers (where $A = \{a_0, a_1, \ldots, a_{n-2}, a_{N-1}\}$), we define a *super-subsequence* ($S$) of a [subsequence](https://en.wikipedia.org/wiki/Subsequence) ($A'$) to be the sequence of factorials of each number in $A'$. For instance, if $A' = \{a_{j+0}, a_{j+1}, \ldots, a_{j+k-1}\}$ denotes a subsequence of length $k$ (where $j$ is the $j^{th}$ index of $A$ and $0 \leq j+k \leq N-1$), then the corresponding super-subsequence would be $S = \{(a_{j+0})!, (a_{j+1})!, \ldots, (a_{j+k-1})!\}$. Recall that **!** denotes [Factorial](https://en.wikipedia.org/wiki/Factorial). 

The *pleasing value* of a super-subsequence ($S$) is defined here as the sum of the factorial lengths of all the numbers in $S$. 

Find and print the sum of factorial lengths for all super-subsequences with an *even* pleasing value.

## Input Format

The first line contains an integer, $N$, denoting the size of array $A$. 	
The second line contains $N$ space-separated integers describing the ordered elements in $A$. 

**Constraints** 	
$1 \leq N \leq 16$		
$1 \leq a_i \leq 10^6$

## Output Format

Print the sum of factorial lengths for all super-subsequences having an *even* pleasing value.
