# The Strange Function

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.7948193592365371
- **Total Submissions:** 2934
- **Solved Count:** 2332
- **URL:** https://www.hackerrank.com/challenges/the-strange-function

## Problem Statement

One of the most important skills a programmer needs to learn early on is the ability to pose a problem in an abstract way. This skill is important not just for researchers but also in applied fields like software engineering and web development.  

You are able to solve most of a problem, except for one last subproblem, which you have posed in an abstract way as follows: Given an array consisting of $n$ integers $[a_1, a_2, \ldots, a_n]$, define $$f(l, r) = \gcd(a_l, a_{l + 1}, ..., a_r) \cdot \left(\left(\sum\limits_{i=l}^{r} a_i\right) - \max(a_l, a_{l + 1}, \ldots, a_r)\right).$$

For example, for an input array [ 10, -5, 5, 20 ], a subsegment $f(1,1)$ would be computed as follows: 

![image](https://s3.amazonaws.com/hr-assets/0/1514443882-d4fd00ae66-strange_function5.png) 

What is $\max\limits_{1 \leq l \leq r \leq n}\ f(l, r)$, i.e., the maximum value of $f(l, r)$ among all subsegments $[l, r]$?  

Complete the function `maximumValue` which takes an integer array as input and returns the maximum value of $f$ among all subsegments $[l, r]$.
    
Note that:

- $\gcd(x, y) = \gcd(|x|, |y|)$
- $\gcd(x, 0) = \gcd(0, x) = |x|$


## Input Format

The first line contains a single integer $n$

The second line contains $n$ space-separated integers $a_1, a_2, \ldots{a_n}$


## Output Format

 Print a single integer denoting the answer

## Constraints

 $1\leq n\leq 50000$  
$-10^6\leq a_i\leq 10^6$  

## Sample Input

4
10 -5 5 20

## Sample Output

50

## Explanation

The maximum value occurs at  as shown below.
