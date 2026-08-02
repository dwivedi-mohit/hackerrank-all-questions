# Security Key Spaces

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9765571526351814
- **Total Submissions:** 5844
- **Solved Count:** 5707
- **URL:** https://www.hackerrank.com/challenges/security-key-spaces

## Problem Statement

$K$ denotes a set called the *key space*. Any element of $K$ is called a *key*.

Each element $e \in K$ uniquely determines a bijection from $M$ to $C$, denoted by $E_e$. The $E_e$ is called an encryption function. Similarly for each $d \in K$, we have a bijection from $C$ to $M$, denoted by $D_d$, and it is called a decryption function.

For example, consider the same shifting function that we dealt with in the previous challenge. Now, suppose the amount of shifting we do is some $e$. In the last challenge, $e = 1$. Then $e$ is a valid key representing the bijective function $f(x, e)= shift\_x\_by\_e$.

For this task, consider a message that consists of decimal digits and a key, $e$, which operates by shifting each digit by $e$ places. Find the corresponding ciphertext.

**Constraints** 

$1\le Length\ of\ the\ string\le 10$  
$0\le e\le 9$

## Input Format

The input consists of $2$ lines.  
The first line contains the message string.  
The second line contains the key $e$.

## Output Format

Output a single line that contains the cipher obtained by shifting each digit $e$ places.

## Sample Input

2

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
