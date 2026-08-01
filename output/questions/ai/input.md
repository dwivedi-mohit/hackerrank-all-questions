# Input()

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9401352838887737
- **Total Submissions:** 125366
- **Solved Count:** 117861
- **URL:** https://www.hackerrank.com/challenges/input

## Problem Statement

<sub> `This challenge is only for`__`Python 2`__`.` </sub>

###<sub>[input()](https://docs.python.org/2/library/functions.html#input)</sub>

In __Python 2__, the expression *input()* is equivalent to _eval(raw_ __input(prompt))_.

<sub>__Code__</sub>

	>>> input()  
    1+2
    3
    >>> company = 'HackerRank'
    >>> website = 'www.hackerrank.com'
    >>> input()
    'The company name: '+company+' and website: '+website
    'The company name: HackerRank and website: www.hackerrank.com'
    
---
__Task__  

You are given a [polynomial](https://en.wikipedia.org/wiki/Polynomial) $P$ of a single indeterminate (or variable), $x$.  
You are also given the values of $x$ and $k$. Your task is to verify if $P(x) = k$.

__Constraints__  
All coefficients of polynomial $P$ are integers.  
$x$ and $y$ are also integers.

## Input Format

The first line contains the space separated values of $x$ and $k$.  
The second line contains the polynomial $P$. 

## Output Format

Print `True` if $P(x) = k$. Otherwise, print `False`.

## Constraints

All coefficients of polynomial  are integers.

 and  are also integers.

## Sample Input

1 4
x**3 + x**2 + x + 1

## Sample Output

True

## Explanation

Hence, the output is True.
