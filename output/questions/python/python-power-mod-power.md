# Power - Mod Power

---

| Field | Value |
|---|---|
| **Slug** | `python-power-mod-power` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/python-power-mod-power |

---

## Preview

Perform modular exponentiation in Python.

## Problem Statement

So far, we have only heard of Python's powers. Now, we will witness them!


Powers or exponents in Python can be calculated using the built-in power function. Call the power function $a^b$ as shown below:


	>>> pow(a,b) 
  

or 

	>>> a**b

It's also possible to calculate $a^b \mod m$.


	>>> pow(a,b,m)

  

This is very helpful in computations where you have to print the resultant % mod.


**Note**: Here, $a$ and $b$ can be floats or negatives, but, if a third argument is present, $b$ cannot be negative.


**Note**: Python has a math module that has its own *pow()*. It takes two arguments and returns a float. It is uncommon to use *math.pow()*.


**Task**

You are given three integers: $a$, $b$, and $m$. Print two lines.

On the first line, print the result of *pow(a,b)*. On the second line, print the result of *pow(a,b,m)*.


**Input Format**

The first line contains $a$, the second line contains $b$, and the third line contains $m$.


**Constraints**

$1 \le a \le 10$ 

$1 \le b \le 10$

$2 \le m \le 1000$


**Sample Input**


    3
    4
    5
  

**Sample Output**


    81
    1

## Sample Tests

### Test 1

```
>>> pow(a,b)
```

### Test 2

```
>>> a**b
```

### Test 3

```
>>> pow(a,b,m)
```

### Test 4

```
3
4
5
```

### Test 5

```
81
1
```
