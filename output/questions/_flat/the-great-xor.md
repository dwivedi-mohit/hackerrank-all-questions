# The Great XOR

---

| Field | Value |
|---|---|
| **Slug** | `the-great-xor` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/the-great-xor |

---

## Preview

Count the number of non-negative integer a's that are less than some x where the bitwise XOR of a and x is greater than x.

## Problem Statement

Given a long integer $x$, count the number of values of $a$ satisfying the following conditions:


* $a \oplus x > x$
* $0 < a < x$

where $a$ and $x$ are long integers and $\oplus$ is the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator.


You are given $q$ queries, and each query is in the form of a long integer denoting $x$. For each query, print the total number of values of $a$ satisfying the conditions above on a new line.

For example, you are given the value $x=5$.  Condition $2$ requires that $a < x$.  The following tests are run:


$1 \oplus 5 = 4$

$2 \oplus 5 = 7$

$3 \oplus 5 = 6$

$4 \oplus 5 = 1$ 



We find that there are $2$ values meeting the first condition: $2$ and $3$.


**Function Description**


Complete the *theGreatXor* function in the editor below.  It should return an integer that represents the number of values satisfying the constraints.


theGreatXor has the following parameter(s):

- *x*: an integer

## Input Format

The first line contains an integer $q$, the number of queries. 	
Each of the next $q$ lines contains a long integer describing the value of $x$ for a query.

## Output Format

For each query, print the number of values of $a$ satisfying the given conditions on a new line.

## Constraints

* $1 \le q \le 10^{5}$
* $1 \le x \le 10^{10}$

**Subtasks**

For $50\%$ of the maximum score:

* $1 \le q \le 10^{3}$
* $1 \le x \le 10^{4}$

## Sample Tests

### Test 1

```
2
2
10
```

### Test 2

```
1
5
```

### Test 3

```
2
5
100
```

### Test 4

```
2
27
```
