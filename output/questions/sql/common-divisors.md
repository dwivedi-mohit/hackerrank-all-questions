# Common Divisors

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.8693317422434368
- **Total Submissions:** 1676
- **Solved Count:** 1457
- **URL:** https://www.hackerrank.com/challenges/common-divisors

## Problem Statement

Mario and Luigi earn points in their steps to save the Princess Peach from a dragon. Let's denote Mario's points by `M` and Luigi's by `L`. Princess Peach is wondering how many postive integers are there that are divisors to both numbers, `M` and `L`. Help her find the answer.

**Input**  
First line of input contains an integer, `T`, which represent the number of test cases. Then follows `T` lines. Each line contains two space separated integers, `M L`, representing the points earned by Mario and Luigi, respectively.

**Output**  
For each test case, print the solution in different lines.

**Constraints**  
_1 <= T <= 10_  
_1 <= L, M <= 10^8_  
_L, M_ are integers  

**Sample Input**  

    3
    10 4
    1 100
    288 240

**Sample Output**  

    2
    1
    10

**Explanation**  
*Test Case #00:* Divisors of _M = 10_ are _{1,2,5,10}_, while for _L = 4_ they are _{1, 2, 4}_. So _M_ and _L_ shares _{1, 2}_ as their common divisors.  

*Test Case #01:* Here as _M = 1_, both players only share this number as their divisor.  

*Test Case #02:* Here _M_ and _L_ shares _10_ integers, _{1,2,3,4,6,8,12,16,24,48}_, as their divisors.  


## Constraints

1 <= T <= 10

1 <= L, M <= 10^8

L, M are integers

## Sample Input

10 4
1 100
288 240

## Sample Output

1
10

## Explanation

Test Case #00: Divisors of M = 10 are {1,2,5,10}, while for L = 4 they are {1, 2, 4}. So M and L shares {1, 2} as their common divisors.

Test Case #01: Here as M = 1, both players only share this number as their divisor.

Test Case #02: Here M and L shares 10 integers, {1,2,3,4,6,8,12,16,24,48}, as their divisors.
