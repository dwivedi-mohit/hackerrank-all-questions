# Rational Sums

- **Domain:** sql
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.8252427184466019
- **Total Submissions:** 103
- **Solved Count:** 85
- **URL:** https://www.hackerrank.com/challenges/rational-sums

## Problem Statement

Today Konstantin learned about convergence of series. For instance, series  
$$ \sum\limits_{n = 1}^{\infty}\frac1{n(n+1)} = \frac12 + \frac16 + \frac1{12} + \dots = 1, $$ 
$$ \sum\limits_{n = 1}^{\infty}\frac1{n^2} = 1 + \frac14 + \frac19 + \frac1{16} + \dots = \frac{\pi^2}{6}, $$ converge, while 
$$ \sum\limits_{n = 1}^{\infty}\frac1n = 1 + \frac12 + \frac13 + \frac14 + \dots = +\infty $$ diverges. See more at https://en.wikipedia.org/wiki/Convergent_series .

As you may note, some simple looking series can converge to quite complicated numbers, like $\frac{\pi^2}6$, $e$, etc. Konstantin noted this and decided to study only special case of rational functions sums, that is  

$$ \sum\limits_{n = 1}^{\infty}\frac{P(n)}{Q(n)}, $$ where $P$ and $Q$ are polynomials and $Q(n)\not=0$ for positive integer $n$. It can be proven that if $\deg P \leq \deg Q - 2$ the series converges. But, as example $\sum\limits_{n = 1}^{\infty}\frac1{n^2} $ shows, sum of rational functions can be irrational. 

After some time, Konstantin decided to consider some very special case of rational functions when $$ Q(x) = (x + a_1)(x + a_2)\dots(x + a_m) $$ and $$P(x) = b_0 + b_{1}x + \dots + b_{n-2}x^{m - 2}, $$ with constraint that $a_1, a_2, \dots, a_m$ are _distinct_ non-negative integers. Fortunately, it can be proven that in this case sum of the series above is rational number. Now Konstantin want you to calculate it.

## Input Format

The first line of input contains single integer, $m$. The next line contains $m$ integers $a_1, a_2, \dots, a_m$, separated by space. The next line contains $m - 1$ integers $b_0, b_1, \dots, b_{m-2}$.



## Output Format

If answer is irreducible fraction $\frac{a}{b}$, print $ab^{-1} \bmod (10^9 + 7)$, where $b^{-1}$ is multiplicative inverse of $b$ modulo $10^9 + 7$. It is guaranteed that $b \mod 10^9 + 7 \not=0$.   

## Constraints

+ $2 \leq m \leq 5000,$  
+ $0\leq a_i \leq 5000,$  
+ $0 \leq b_i \leq 10^9$.  
+ $a_1, \dots, a_m$ are distinct. 

**Subtasks**  

Solutions that works correctly for $m\leq 100$ will score at least $50\%$ of points.  



## Sample Input

2
0 1
1

## Sample Output

1

## Explanation

the sum is
