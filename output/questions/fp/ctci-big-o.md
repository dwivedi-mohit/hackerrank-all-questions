# Time Complexity: Primality

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.8593927615415643
- **Total Submissions:** 54542
- **Solved Count:** 46873
- **URL:** https://www.hackerrank.com/challenges/ctci-big-o

## Problem Statement

A *prime* is a natural number *greater than* $1$ that has no positive divisors other than $1$ and itself. Given $p$ integers, determine the primality of each integer and return `Prime` or `Not prime` on a new line. 

**Note:** If possible, try to come up with an $\mathcal{O}(\sqrt{n})$ primality algorithm, or see what sort of optimizations you can come up with for an $\mathcal{O}(n)$ algorithm. Be sure to check out the *Editorial* after submitting your code.

**Function Description**

Complete the *primality* function in the editor below.  

primality has the following parameter(s):

-  *int n:* an integer to test for primality  

**Returns**  

- *string:* `Prime` if $n$ is prime, or `Not prime`

## Input Format

The first line contains an integer, $p$, the number of integers to check for primality. 	
Each of the $p$ subsequent lines contains an integer, $n$, the number to test.

## Constraints

* $1 \le p \le 30$
* $1 \le n \le 2 \times 10^{9}$

## Sample Input

STDIN   Function
-----   --------
3       p = 3 (number of values to follow)
12      n = 12 (first number to check)
5       n = 5
7       n = 7

## Sample Output

Not prime
Prime
Prime

## Explanation

We check the following  integers for primality:

-  is divisible by numbers other than  and itself (i.e.: , , , ).

-  is only divisible  and itself.

-  is only divisible  and itself.
