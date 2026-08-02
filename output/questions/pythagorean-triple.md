# Pythagorean Triple

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.6878209831254586
- **Total Submissions:** 2726
- **Solved Count:** 1875
- **URL:** https://www.hackerrank.com/challenges/pythagorean-triple

## Problem Statement

A *Pythagorean triple* consists of three positive integers $a$, $b$, and $c$, such that $a^2 + b^2 = c^2$. Such a triple is commonly written as $(a, b, c)$. This term comes from the [Pythagorean theorem](http://en.wikipedia.org/wiki/Pythagorean_theorem), which says that a Pythagorean Triple will be the lengths of the sides of a [right-angled triangle](http://en.wikipedia.org/wiki/Right_triangle).  

You have been given an integer $a$ which represents the length of one of [cathetus](https://en.wikipedia.org/wiki/Cathetus) of a right-angle triangle.  


![image](https://s3.amazonaws.com/hr-assets/0/1496133929-d6c8a1a890-1428670428-5294116a8c-HRRT.JPG)

You need to find the lengths of the remaining sides. There may be multiple possible answers; any one will be accepted.

*Hints:* 

- Every odd number $2k+1$ can be represented as $(k+1)^2 - k^2$.  
- If $m$ and $n$ are integers and $m > n$, then $(m^2-n^2)^2 + (2mn)^2 = (m^2+n^2)^2$. 


## Input Format

The first line contains an integer $a$ denoting the length of one of cathetus of the right-angled triangle.  

## Output Format

A single line containing the possible values of $a$, $b$ and $c$. You may print them in any order. 


## Constraints

+ $5 \le a < 10^9$


## Sample Input

5

## Sample Output

5 12 13

## Explanation

We can see that the triple  is a pythagorean triple:

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
