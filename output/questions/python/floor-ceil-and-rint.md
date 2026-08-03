# Floor, Ceil and Rint

---

| Field | Value |
|---|---|
| **Slug** | `floor-ceil-and-rint` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/floor-ceil-and-rint |

---

## Preview

Use the floor, ceil and rint tools of NumPy on the given array.

## Problem Statement

[__floor__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.floor.html#numpy-floor)

The tool *floor* returns the floor of the input element-wise.

The floor of $x$ is the largest integer $i$ where $i \le x$. 

    import numpy

    my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print numpy.floor(my_array)			#[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

[__ceil__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ceil.html#numpy-ceil)

The tool *ceil* returns the ceiling of the input element-wise.

The ceiling of $x$ is the smallest integer $i$ where $i \ge x$. 

    import numpy

    my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print numpy.ceil(my_array)			#[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

[__rint__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.rint.html)

The *rint* tool rounds to the nearest integer of input element-wise.

    import numpy

    my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    print numpy.rint(my_array)			#[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
  

--- 
__Task__

You are given a 1-D array, $A$. Your task is to print the $floor$, $ceil$ and $rint$ of all the elements of $A$. 

__Note__

In order to get the correct output format, add the line $\text{numpy.set_printoptions(legacy='1.13')}$ below the numpy import.

## Input Format

A single line of input containing the space separated elements of array $A$.

## Output Format

On the first line, print the $floor$ of A.

On the second line, print the $ceil$ of A.

On the third line, print the $rint$ of A.

## Sample Tests

### Test 1

```
import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array) #[ 1. 2. 3. 4. 5. 6. 7. 8. 9.]
```

### Test 2

```
import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array) #[ 2. 3. 4. 5. 6. 7. 8. 9. 10.]
```

### Test 3

```
import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array) #[ 1. 2. 3. 4. 6. 7. 8. 9. 10.]
```

### Test 4

```
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```

### Test 5

```
[ 1. 2. 3. 4. 5. 6. 7. 8. 9.]
[ 2. 3. 4. 5. 6. 7. 8. 9. 10.]
[ 1. 2. 3. 4. 6. 7. 8. 9. 10.]
```
