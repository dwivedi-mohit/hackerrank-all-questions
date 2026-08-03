# Dot and Cross

---

| Field | Value |
|---|---|
| **Slug** | `np-dot-and-cross` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/np-dot-and-cross |

---

## Preview

Use NumPy to find the dot and cross products of arrays.

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

## Sample Tests

### Test 1

```
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print numpy.dot(A, B) #Output : 11
```

### Test 2

```
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print numpy.cross(A, B) #Output : -2
```

### Test 3

```
2
1 2
3 4
1 2
3 4
```

### Test 4

```
[[ 7 10]
 [15 22]]
```
