# Binomial Coefficients Revenge

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.6797752808988764
- **Total Submissions:** 178
- **Solved Count:** 121
- **URL:** https://www.hackerrank.com/challenges/bincoefrevenge

## Problem Statement



The binomial coefficient _C(N, K)_ is defined as
_N! / K! / (N − K)!_ for _0 &le; K &le; N_.  
Here _N! = 1 \* 2 \* ... \* N_ for _N &ge; 1_, and _0! = 1_.

You are given a prime number _P_ and a positive integer _N_. 

_A<sub>L</sub>_ is defined as the number of elements in the sequence _C(N, K)_, such that, _P<sup>L</sup>_ divides _C(N, K)_,
but _P<sup>L+1</sup>_ does not divide _C(N, K)_. Here, _0 &le; K &le; N_.


Let _M_ be an integer, such that, _A<sub>M</sub> > 0_,
but _A<sub>L</sub> = 0_ for all _L > M_.
Your task is to find numbers _A<sub>0</sub>, A<sub>1</sub>, ..., A<sub>M</sub>_.

**Input Format**  
The first line of the input contains an integer _T_, denoting the number of test cases.
The description of _T_ test cases follows.
The only line of each test case contains two space-separated integers _N_ and _P_.

**Output Format**  
For each test case, display _M + 1_ space separated integers
_A<sub>0</sub>, A<sub>1</sub>, ..., A<sub>M</sub>_
on the separate line.

**Constraints**

1 &le; T &le; 100  
1 &le; N &le; 10<sup>18</sup>  
2 &le; P &lt; 10<sup>18</sup>  
P is prime  


**Sample Input**

    3
    4 5
    6 3
    10 2

**Sample Output**

    5
    3 4
    4 4 1 2


**Explanation**  

**Example case 1.** Values _C(4, K)_ are _{1, 4, 6, 4, 1}_.
Each of them is not divisible by 5.
Therefore, _A<sub>0</sub> = 5_, _A<sub>1</sub> = 0_, _A<sub>2</sub> = 0_, ..., hence the answer.


**Example case 2.** Values _C(6, K)_ are _{1, 6, 15, 20, 15, 6, 1}_.
Among them _1, 20, 1_ are not divisible by _3_,
while remaining values _6, 15, 15, 6_ are divisible by _3_, but not divisible by _9_.
Therefore, _A<sub>0</sub> = 3_, _A<sub>1</sub> = 4_,
_A<sub>2</sub> = 0_, _A<sub>3</sub> = 0_, ..., hence the answer.


**Example case 3.** Values _C(10, K)_ are _{1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1}_.
Among them _1, 45, 45, 1_ are not divisible by _2_,
values _10, 210, 210, 10_ are divisible by _2_, but not divisible by _4_,
value _252_ is divisible by _4_, but not divisible by _8_,
finally, values _120, 120_ are divisible by _8_, but not divisible by _16_.
Therefore, _A<sub>0</sub> = 4_, _A<sub>1</sub> = 4_,
_A<sub>2</sub> = 1_, _A<sub>3</sub> = 2_,
_A<sub>4</sub> = 0_, _A<sub>5</sub> = 0_, ..., hence the answer.

## Input Format

The first line of the input contains an integer T, denoting the number of test cases.
The description of T test cases follows.
The only line of each test case contains two space-separated integers N and P.

## Output Format

For each test case, display M + 1 space separated integers
A0, A1, ..., AM
on the separate line.

## Constraints

1 ≤ T ≤ 100

1 ≤ N ≤ 1018

2 ≤ P < 1018

P is prime

## Sample Input

4 5
6 3
10 2

## Sample Output

3 4
4 4 1 2

## Explanation

Example case 1. Values C(4, K) are {1, 4, 6, 4, 1}.
Each of them is not divisible by 5.
Therefore, A0 = 5, A1 = 0, A2 = 0, ..., hence the answer.

Example case 2. Values C(6, K) are {1, 6, 15, 20, 15, 6, 1}.
Among them 1, 20, 1 are not divisible by 3,
while remaining values 6, 15, 15, 6 are divisible by 3, but not divisible by 9.
Therefore, A0 = 3, A1 = 4,
A2 = 0, A3 = 0, ..., hence the answer.

Example case 3. Values C(10, K) are {1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1}.
Among them 1, 45, 45, 1 are not divisible by 2,
values 10, 210, 210, 10 are divisible by 2, but not divisible by 4,
value 252 is divisible by 4, but not divisible by 8,
finally, values 120, 120 are divisible by 8, but not divisible by 16.
Therefore, A0 = 4, A1 = 4,
A2 = 1, A3 = 2,
A4 = 0, A5 = 0, ..., hence the answer.
