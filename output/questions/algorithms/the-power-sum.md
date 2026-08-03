# The Power Sum

---

| Field | Value |
|---|---|
| **Slug** | `the-power-sum` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/the-power-sum |

---

## Preview

Split up a number in a specified manner.

## Problem Statement

Find the number of ways that a given integer, $X$, can be expressed as the sum of the $N^{th}$ powers of unique, natural numbers. 

For example, if $X=13$ and $N=2$, we have to find all combinations of unique squares adding up to $13$.  The only solution is  $2^2+3^2$.


**Function Description**

Complete the *powerSum* function in the editor below.  It should return an integer that represents the number of possible combinations.


powerSum has the following parameter(s):


- *X*: the integer to sum to

- *N*: the integer power to raise numbers to

## Input Format

The first line contains an integer $X$.

The second line contains an integer $N$.

## Output Format

Output a single integer, the number of possible combinations caclulated.

## Constraints

- $1 \le X \le 1000$ 

- $2 \le N \le 10$

## Sample Tests

### Test 1

```
10
2
```

### Test 2

```
1
```

### Test 3

```
100
2
```

### Test 4

```
3
```

### Test 5

```
100
3
```

### Test 6

```
1
```
