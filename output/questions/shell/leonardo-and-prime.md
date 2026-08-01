# Leonardo's Prime Factors

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.7748971320731368
- **Total Submissions:** 32323
- **Solved Count:** 25047
- **URL:** https://www.hackerrank.com/challenges/leonardo-and-prime

## Problem Statement

Leonardo loves primes and created $q$ queries where each query takes the form of an integer, $n$. For each $n$, count the maximum number of distinct prime factors of any number in the inclusive range $[1, n]$.

**Note:** Recall that a prime number is only divisible by $1$ and itself, and $1$ is *not* a prime number.  

**Example**  
$n = 100$  

The maximum number of distinct prime factors for values less than or equal to $100$ is $3$.  One value with $3$ distinct prime factors is $30$. Another is $42$.    

**Function Description**  

Complete the *primeCount* function in the editor below.  

*primeCount* has the following parameters:  

- *int n:* the inclusive limit of the range to check  

**Returns**  

- *int:* the maximum number of distinct prime factors of any number in the inclusive range $[0 - n]$.  

## Input Format

The first line contains an integer, $q$, the number of queries. 	
Each of the next $q$ lines contains a single integer, $n$.

## Constraints

+ $1 \le q \le 10^{5}$  
+ $1 \le n \le 10^{18}$  

## Sample Input

1
2
3
500
5000
10000000000

## Sample Output

1
1
4
5
10

## Explanation

-  is not prime and its only factor is itself.

-  has  prime factor, .

- The number  has  prime factor, ,  has  and  has  prime factors.

- The product of the first four primes is .  While higher value primes may be a factor of some numbers, there will never be more than  distinct prime factors for a number in this range.
