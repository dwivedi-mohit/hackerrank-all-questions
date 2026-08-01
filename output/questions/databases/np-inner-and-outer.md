# Inner and Outer

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9826181901432635
- **Total Submissions:** 113567
- **Solved Count:** 111593
- **URL:** https://www.hackerrank.com/challenges/np-inner-and-outer

## Problem Statement

[__inner__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.inner.html)  

The *inner* tool returns the [inner product](https://en.wikipedia.org/wiki/Inner_product_space) of two arrays.

    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.inner(A, B)		#Output : 4
    
[__outer__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.outer.html)    

The *outer* tool returns the [outer product](https://en.wikipedia.org/wiki/Outer_product) of two arrays.

    import numpy

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.outer(A, B)		#Output : [[0 0]
 								#		   [3 4]]
                                
---
__Task__  

You are given two arrays: $A$ and $B$.  
Your task is to compute their *inner* and *outer* product.

## Input Format

The first line contains the space separated elements of array $A$.  
The second line contains the space separated elements of array $B$.


## Output Format

First, print the inner product.  
Second, print the outer product.

## Sample Input

0 1
2 3

## Sample Output

[[0 0]
 [2 3]]
