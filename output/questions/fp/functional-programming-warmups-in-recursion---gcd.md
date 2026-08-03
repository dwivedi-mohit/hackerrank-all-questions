# Computing the GCD

---

| Field | Value |
|---|---|
| **Slug** | `functional-programming-warmups-in-recursion---gcd` |
| **Domain** | fp |
| **Difficulty** | Easy |
| **Score** | 2 |
| **URL** | https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd |

---

## Preview

Recursively compute the GCD of two integers using the Euclidean Method.

## Problem Statement

**Objective** <Br>
In this challenge, we learn how to compute GCD using the Euclidean algorithm.

**Resources** <br>
Here's a helpful video on the topic: 

[(iframe youtube JUzYl1TYMcU 600 350)] 
 

Given two integers, $x$ and $y$, a recursive technique to find their GCD is the [Euclidean Algorithm](http://people.cis.ksu.edu/~schmidt/301s12/Exercises/euclid_alg.html). 

The algorithm states that, for computing the GCD of two positive integers $x$ and $y$, if $x$ and $y$ are equal, $GCD(x,y) = x$. Otherwise $GCD(x,y) = GCD(x-y,y)$ if $x > y$. There are a few optimizations that can be made to the above logic to arrive at a more efficient implementation.

**Task** <br>
Given the starter code, you need to complete a function body that returns the GCD of two given integers $x$ and $y$. <br>
The task of reading in input and printing the output will be handled by us.

 
**Programming Language Support**

At this point of time, we have a template for Scala. This means that we provide the code required to accept the input and display the output.

## Input Format

One line of input containing $2$ space separated integers.

## Output Format

Output one integer, the GCD of the two given numbers.

## Constraints

$1 \le a,b \le 10^6$

## Sample Tests

### Test 1

```
1 5
```

### Test 2

```
1
```

### Test 3

```
GCD(1,5) = 1 
GCD(10,100) = 10 
GCD(22,131) = 1
```
