# Ugly or Beautiful

---

| Field | Value |
|---|---|
| **Slug** | `ugly-or-beautiful` |
| **Contest** | codeagon-2017 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/ugly-or-beautiful |

---

## Problem Statement

You are given an array, $a$, of $n$ non-zero positive integers. The array is said to be beautiful if all the following constraints are satisfied:

1. The array consists of unique elements.
2. The array elements are not sorted in ascending order.
3. All the array elements should have a value between $1$ to $n$ inclusive, i.e., $1 \le a_{i} \le n$, where, $0 \le i \lt n$.

If the array is beautiful, print `Beautiful`; otherwise print `Ugly`. 

For example, array $A$ = [1, 2, 3, 4] is considered `Ugly` because all elements are sorted in ascending order hence violating the second constraint.

## Input Format

The first line of the input is an integer $q$, the total number of queries. Each query consists of two lines.  
The first line of each query contains an integer $n$ denoting the total number of elements in the array and the second line of each query contains $n$ space separated integers describing the array, $a$.

## Output Format

For each query, print `Beautiful` if the array is beautiful; otherwise print `Ugly` on a new line.

## Constraints

- $1 \le q \le 100$
- $1 \le n \le 10^{4}$
- $1 \le a_{i} \le 10^{9}$, where, $0 \le i \lt n$
