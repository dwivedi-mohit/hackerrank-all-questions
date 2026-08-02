# Dot and Cross

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9866893097036166
- **Total Submissions:** 105404
- **Solved Count:** 104001
- **URL:** https://www.hackerrank.com/challenges/np-dot-and-cross

## Problem Statement

[__dot__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)

The *dot* tool returns the dot product of two arrays.

    import numpy

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.dot(A, B)		#Output : 11
    
[__cross__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.cross.html)

The *cross* tool returns the cross product of two arrays.

	import numpy

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.cross(A, B)		#Output : -2
    
---
__Task__

You are given two arrays $A$ and $B$. Both have dimensions of $N $X$ N$.  
Your task is to compute their [matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication#Matrix_product_.28two_matrices.29).

## Input Format

The first line contains the integer $N$.  
The next $N$ lines contains $N$ space separated integers of array $A$.  
The following $N$ lines contains $N$ space separated integers of array $B$.

## Output Format

Print the matrix multiplication of $A$ and $B$.

## Sample Input

1 2
3 4
1 2
3 4

## Sample Output

[[ 7 10]
 [15 22]]

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
