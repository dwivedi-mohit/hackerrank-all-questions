# Any or All

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9490966657418439
- **Total Submissions:** 122546
- **Solved Count:** 116308
- **URL:** https://www.hackerrank.com/challenges/any-or-all

## Problem Statement

###<sub>[any()](https://docs.python.org/2/library/functions.html#any)</sub>  
This expression returns `True` if __any__ element of the iterable is true.  
If the iterable is empty, it will return `False`. 

<sub>__Code__</sub>
	
    >>> any([1>0,1==0,1<0])
    True
    >>> any([1<0,2<1,3<2])
    False

---
###<sub>[all()](https://docs.python.org/2/library/functions.html#all)</sub>    
This expression returns `True` if __all__ of the elements of the iterable are true. If the iterable is empty, it will return `True`. 

<sub>__Code__</sub>  

	>>> all(['a'<'b','b'<'c'])
    True
    >>> all(['a'<'b','c'<'b'])
    False
    
--- 
__Task__

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a [palindromic integer](https://en.wikipedia.org/wiki/Palindromic_number).

## Input Format

The first line contains an integer $N$. $N$ is the total number of integers in the list.  
The second line contains the space separated list of $N$ integers.

__Constraints__

$ 0 < N < 100$


## Output Format

Print `True` if all the conditions of the problem statement are satisfied. Otherwise, print `False`.

## Sample Input

12 9 61 5 14

## Sample Output

True

## Explanation

Condition 1: All the integers in the list are positive.

Condition 2: 5 is a palindromic integer.

Hence, the output is True.

Can you solve this challenge in 3 lines of code or less?

There is no penalty for solutions that are correct but have more than 3 lines.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
