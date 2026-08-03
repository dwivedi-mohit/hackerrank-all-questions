# Two Robots

---

| Field | Value |
|---|---|
| **Slug** | `two-robots` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/two-robots |

---

## Preview

Find the minimum distance traveled by two warehouse robots.

## Problem Statement

You have a warehouse with $M$ containers filled with an infinite number of candies. The containers are arranged in a single row, equally spaced to be $1$ meter apart. You also have $2$ robots that can pick up $1$ piece of candy and transport it between any two containers.

The robots take instructions in the form of *queries* consisting of two integers, $M_a$ and $M_b$, respectively. To execute a query, a robot travels to container $M_a$, picks up $1$ candy, transports it to container $M_b$, and then stops at $M_b$ until it receives another query.	

  

Calculate the *minimum total distance* the robots must travel to execute $N$ queries *in order*. 

**Note:** You choose which robot executes each query.

## Input Format

The first line contains a single integer, $T$ (the number of test cases); each of the $T$ test cases is described over $N+1$ lines. 	

The first line of a test case has two space-separated integers, $M$ (the number of containers) and $N$ (the number of queries).  	
The $N$ subsequent lines each contain two space-separated integers, $M_a$ and $M_b$, respectively; each line $N_i$ describes the $i^{th}$ query.

**Constraints**


- $1 \le T \le 50$

- $1 < M \le 1000$

- $1 \le N \le 1000$

- $1 \le a, b \le M$ 

- $M_a \ne M_b$

## Output Format

On a new line for each test case, print an integer denoting the *minimum total distance* that the robots must travel to execute the queries in order.

## Sample Tests

### Test 1

```
3
5 4
1 5
3 2
4 1
2 4
4 2
1 2
4 3
10 3
2 4
5 4
9 8
```

### Test 2

```
11
2
5
```
