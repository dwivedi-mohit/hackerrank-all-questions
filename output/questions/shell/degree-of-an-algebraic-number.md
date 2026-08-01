# Degree of an algebraic number

- **Domain:** shell
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.8363095238095238
- **Total Submissions:** 336
- **Solved Count:** 281
- **URL:** https://www.hackerrank.com/challenges/degree-of-an-algebraic-number

## Problem Statement

A number is *algebraic* if it is a root of some nonzero polynomial with integer coefficients. A number is *transcendental* if it is not algebraic.

For example, $11$, $i$, $\sqrt[3]{2}$ and $\phi$ ([golden ratio](http://en.wikipedia.org/wiki/Golden_ratio)) are algebraic, because they are roots of $x-11$, $x^2+1$, $x^3-2$ and $x^2-x-1$, respectively. Also, it can be shown that the sum and product of two algebraic numbers is also algebraic, so for example $24+i$, $\sqrt{2}+\sqrt{3}$ and $\sqrt[3]{11}\phi$ are also algebraic. However, it has been shown by Lindemann that [$\pi$ is transcendental](http://en.wikipedia.org/wiki/Lindemann%E2%80%93Weierstrass_theorem).

The *degree* of an algebraic number is the minimal degree of a polynomial with integer coefficients in which it is a root. For example, the degrees of $5$, $i$, $\sqrt[3]{2}$ and $\phi$ are $1$, $2$, $3$ and $2$, respectively.

Given $N$ positive integers $A_1$, $A_2$, ..., $A_N$, calculate the degree of the following algebraic number:
$$\sqrt{A_1} + \sqrt{A_2} + \sqrt{A_3} + \cdots + \sqrt{A_N}$$  

**Input Format**  
The first line of input contains $T$, the number of test cases. The descriptions of the test cases follow.

Each test case has two lines of input. The first line contains a single integer, $N$. The second line contains $N$ integers $A_1$, ..., $A_N$ separated by single spaces.

**Output Format**  
For each test case, output one line containing exactly one integer, which is the answer for that test case.

**Constraints**  
$1 \le T \le 10^5$  
$1 \le N \le 50$  
$1 \le A_i \le 10^7$  
The sum of the $N$'s in a single test file is at most $10^5$  

**Sample Input**  

    3
    1
    4
    3
    2 4 4
    4
    1 2 3 5

**Sample Output** 

    1
    2
    8

**Explanation**  
*Case 1*: A minimal polynomial of $\sqrt{4}$ is $2x-4$.  

*Case 2*: A minimal polynomial of $\sqrt{2}+\sqrt{4}+\sqrt{4}$ is $x^2-8x+14$.  

*Case 3*: A minimal polynomial of $\sqrt{1}+\sqrt{2}+\sqrt{3}+\sqrt{5}$ is:
$$x^8-8x^7-12x^6+184x^5-178x^4-664x^3+580x^2+744x-71$$

## Input Format

The first line of input contains , the number of test cases. The descriptions of the test cases follow.

Each test case has two lines of input. The first line contains a single integer, . The second line contains  integers , ...,  separated by single spaces.

## Output Format

For each test case, output one line containing exactly one integer, which is the answer for that test case.

## Constraints

The sum of the 's in a single test file is at most

## Sample Input

1
4
3
2 4 4
4
1 2 3 5

## Sample Output

2
8

## Explanation

Case 1: A minimal polynomial of  is .

Case 2: A minimal polynomial of  is .

Case 3: A minimal polynomial of  is:
