# Divisor Exploration 3

---

| Field | Value |
|---|---|
| **Slug** | `divisor-exploration-3` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 55 |
| **URL** | https://www.hackerrank.com/challenges/divisor-exploration-3 |

---

## Preview

Find the value given at the root of a tree constructing by the given rules.

## Problem Statement

You are given $q$ queries where each query is in the form of three integers, $m$, $a$ and $d$, such that:
$$n = \prod\limits_{i = 1}^{m} p_i^{a+i} \text{, where } p_i \text{ is the } i^{th} \text{ prime.}$$


Using this value of $n$ along with the given $d$, create a tree $T$ as follows :-


+ The value $n$ is the root of the tree.

+ A node is expanded such that all it's divisors are it's children.

+ Continue expanding till the tree has depth $d$.


For example, if $n = 6$ and $d = 2$, then the tree will look like the following:

![image](https://s3.amazonaws.com/hr-assets/0/1495184919-545b96c7df-1443016945-9de543f952-DivisorTree.jpg)

Once the tree is built, we create another tree $U$ as follows :- 

+ Every leaf node $x \in T$, is transformed to $\phi(x)$. Here $\phi()$ is the totient function. 

+ Every non-leaf node is equal to the sum of the values of it's children.


From our previous example tree, after constructing a new tree, we get the following tree.


![image](https://s3.amazonaws.com/hr-assets/0/1495184934-4e72171d3d-1443017061-c3e2051775-DivisorTreewithSpecialValue.jpg)

Print the value at the root of tree $U$ after taking modulo with $(10^9+7)$.

## Input Format

The first line of the input contains a single integer $q$ ( $q \leq 50$ ).

Following $q$ lines contain three integers given by $m$, $a$ and $d$.

## Output Format

For each case, print the value at the root of tree $U$ modulo $(10^9+7)$.

## Constraints

**For $30\%$ points:** 


+ $1 \leq m \leq 100$
+ $0 \leq a \leq 100$
+ $1 \leq d \leq 100$


**For Full Points:**


+ $1 \leq m \leq 1000$
+ $0 \leq a \leq 1000$
+ $1 \leq d \leq 1000$

## Sample Tests

### Test 1

```
3
2 0 1
2 0 2
1 0 3
```

### Test 2

```
18
39
4
```
