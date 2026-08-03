# Calculate Array Size

---

| Field | Value |
|---|---|
| **Slug** | `calculate-array-size` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 15 |
| **Contest** | 101hack49 |
| **URL** | https://www.hackerrank.com/challenges/calculate-array-size |

---

## Preview

Given the dimensions of a multidimensional array, calculate the array's storage size in kilobytes.

## Problem Statement

We define a *multidimensional array of integers* to be an array containing one or more arrays of integers. Here are some examples of multidimensional arrays declared in *C++*:

```c++
int a[93401];      // 1-dimensional array
int b[10][1000];   // 2-dimensional array
int c[25][30][70]; // 3-dimensional array
int d[15][48];     // 2-dimensional array
```

We want to find the amount of storage space required by the array in *kilobytes*, assuming that a single integer is $4$ bytes and there are $1024$ bytes in $1$ kilobyte. 

For example, let's consider array $b[10][1000]$, which is a $2$-dimensional integer array with space for $10\times 1000 = 10000$ integers, which requires $10000 \times 4 = 40000$ bytes of space. When we convert our bytes to kilobytes, we get $\frac{40000}{1024} = 39.0625$ kilobytes.


Given the respective sizes for each dimension of an $n$-dimensional array, print the array's storage space in kilobytes as a single [floor-rounded](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) *integer*.

## Input Format

The first line contains an integer denoting $n$ (the number of dimensions in the multidimensional array).  	
The second line contains $n$ space-separated integers describing the respective values of $d_1, d_2, \ldots, d_n$ for a multidimensional array with the dimensions $[d_1][d_2]\ldots[d_n]$.

## Output Format

Print a floor-rounded integer denoting the multidimensional array's storage space in kilobytes.

## Constraints

- $1 \le n \le 10$

- $1 \le d_i \le 10^8$

- The multidimensional array can hold up to a maximum of $10^8$ total integers.

## Sample Tests

### Test 1

```
int
a
[
93401
];
// 1-dimensional array
int
b
[
10
][
1000
];
// 2-dimensional array
int
c
[
25
][
30
][
70
];
// 3-dimensional array
int
d
[
15
][
48
];
// 2-dimensional array
```

### Test 2

```
1
93401
```

### Test 3

```
364
```

### Test 4

```
2
10 1000
```

### Test 5

```
39
```

### Test 6

```
3
25 30 70
```

### Test 7

```
205
```

### Test 8

```
2
15 48
```

### Test 9

```
2
```
