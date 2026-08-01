# Russian Peasant Exponentiation

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.7608328643781654
- **Total Submissions:** 3554
- **Solved Count:** 2704
- **URL:** https://www.hackerrank.com/challenges/russian-peasant-exponentiation

## Problem Statement

We all know how to calculate $a^b$ using $b$ operations by multiplying $1$ by $a$ a total of $b$ times. The drawback to this method is that $b$ can be large, which makes exponentiation very slow.

There is a well known method called *Russian Peasant Multiplication* that you can read about [here](http://lafstern.org/matt/col3.pdf). Now let's use this to raise some complex numbers to powers!

You're given $q$ queries where each query consists of four integers: $a$, $b$, $k$, and $m$. For each query, calculate $(a + b \cdot i)^k = c + d \cdot i$ (where $i$ is an imaginary unit) and then print the respective values of $c \text{ mod } m$ and $d \text{ mod } m$ as two space-separated integers on a new line. 

## Input Format

The first line contains a single integer, $q$, denoting the number of queries.		
Each of the $q$ subsequent lines describes a query in the form of four space-separated integers: $a$, $b$, $k$, and $m$ (respectively). 

## Output Format

For each query, print the two space-separated integers denoting the respective values of $c \bmod m$ and $d \bmod m$ on a new line.

## Constraints

+ $1 \leq q \leq 10^5$  
+ $0 \leq k \leq 10^{18}$  
+ $2 \leq m \leq 10^9$  
+ $0 \leq a,b \leq m$  

## Sample Input

2 0 9 1000
0 1 5 10
8 2 10 1000000000

## Sample Output

512 0
0 1
880332800 927506432

## Explanation

In the first query, we have , , , . We calculate the following:

-

-
