# Inner and Outer

---

| Field | Value |
|---|---|
| **Slug** | `np-inner-and-outer` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/np-inner-and-outer |

---

## Preview

Use NumPy to find the inner and outer product of arrays.

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

## Sample Tests

### Test 1

```
import numpy
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print numpy.inner(A, B) #Output : 4
```

### Test 2

```
import numpy
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print numpy.outer(A, B) #Output : [[0 0]
 # [3 4]]
```

### Test 3

```
0 1
2 3
```

### Test 4

```
3
[[0 0]
 [2 3]]
```
