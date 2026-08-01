# Security Function Inverses

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.8690306848201585
- **Total Submissions:** 9842
- **Solved Count:** 8553
- **URL:** https://www.hackerrank.com/challenges/security-inverse-of-a-function

## Problem Statement

Consider a *bijective* function $f: X\rightarrow Y$.

Define another function $g: Y\rightarrow X$ so that for $x \in X$ and $y \in Y$ if $f(x) = y$ then $g(y) = x$.  <br>

Now, the function $g$ is said to be the inverse function of $f$ and is denoted as $g = f^{-1}$.

In this task, you'll be given an integer $n$ and a bijective function $f: X\rightarrow X$ where $X = \{1, 2, 3, ..., n\}$. <br>

Output the inverse of $f$.




## Input Format

There are $2$ lines in the input. <br>
The first line contains a single positive integer $n$. <br>
The second line contains $n$ space separated integers, the values of $f(1),\ f(2),\ f(3),\ ...,\ f(n)\ $, respectively.

## Output Format

Output $n$ lines. The $i^{th}$ line should contain the value of $f^{-1}(i)$.  

**Sample Input#00**  

	3
    1 2 3
    
**Sample Output#00**  

    1
    2
    3
    
**Sample Input#01**  

    3
    2 3 1
    
**Sample Output#01**  

    3
    1
    2
    


## Constraints

$1 \le n \le 20$

## Explanation

First sample :-

Basically, this is the function . Hence, it's the inverse of itself.

Second Sample :-

Here you can see that

hence  is

 is

 is

One way to confirm is .
