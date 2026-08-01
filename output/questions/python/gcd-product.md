# GCD Product

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 150
- **Success Ratio:** 0.6182965299684543
- **Total Submissions:** 1268
- **Solved Count:** 784
- **URL:** https://www.hackerrank.com/challenges/gcd-product

## Problem Statement

This time your assignment is really simple.

Calculate GCD(1, 1) * GCD(1, 2) * ... * GCD(1, M) * GCD(2, 1) * GCD(2, 2) * ... * GCD(2, M) * ... * GCD(N, 1) * GCD(N, 2) * ... * GCD(N, M).

where GCD is defined as the [Greatest Common Divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor). 

**Input Format**

The first and only line contains two space separated integers *N* and *M*.

**Output Format**

Output the required product modulo 10<sup>9</sup>+7.

**Constraints**

1 <= *N*, *M* <= 1.5 * 10<sup>7</sup>

**Sample input:**

<pre>4 4</pre>

**Sample output:**

<pre>96</pre>

**Explanation**

For the above testcase, N = 4, M = 4. So, 

GCD(1, 1) * GCD(1, 2) * ...... * GCD(4, 4) = 1 * 1 * 1 * 1 * 1 * 2 * 1 * 2 * 1 * 1 * 3 * 1 * 1 * 2 * 1 * 4 = 96. 



## Input Format

The first and only line contains two space separated integers N and M.

## Output Format

Output the required product modulo 109+7.

## Constraints

1 <= N, M <= 1.5 * 107

Sample input:

4 4

Sample output:

96

## Explanation

For the above testcase, N = 4, M = 4. So,

GCD(1, 1) * GCD(1, 2) * ...... * GCD(4, 4) = 1 * 1 * 1 * 1 * 1 * 2 * 1 * 2 * 1 * 1 * 3 * 1 * 1 * 2 * 1 * 4 = 96.
