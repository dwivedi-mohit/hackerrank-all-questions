# Selective Additions

---

| Field | Value |
|---|---|
| **Slug** | `selective-additions` |
| **Contest** | hourrank-23 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/selective-additions |

---

## Problem Statement

Zane has just received an array $A$ of length $n$. Because of his endless curiosity, he has decided to play with this array by applying some operations to it. Needless to say, your task is to perform these operations for him, as there will be a lot of them.

In one operation, Zane chooses some segment of array $A$ and increases the values of numbers in that segment by some number of his choice. However, he has $k$ favorite numbers, so as an exception, he will not add anything to those numbers, not even if they are in the segment he chooses.

For example, let's assume $A = [5, 3, 2, 4, 1]$ and Zane's favorite numbers are $3$ and $4$. Suppose he wants to add $7$ to the segment $[A_1,\ldots, A_4] = [5, 3, 2, 4]$. Then the array $A$ would become $[12, 3, 9, 4, 1]$. Note that $A_2 = 3$ and $A_4 = 4$ do not change, because they are his favorite numbers.

Given the elements of array $A$, a set $S$ containing Zane's $k$ favorite numbers, and $m$ operations, find the sum of all numbers in array $A$ after each operation.

## Input Format

The first line contains three space-separated integers $n$, $m$, and $k$.

The second line contains $n$ space-separated integers, describing the array $A$.

The third line contains $k$ space-separated distinct integers, describing the set $S$.

The $i$th of the next $m$ lines contains three space-separated integers $l$, $r$, and $x$, respectively, meaning that the $i$th operation is performed on the segment $[A_l, A_{l+1}, \ldots, A_r]$ with $x$ as the value to add.

## Output Format

Print $m$ lines, the $i$th of which contains a single integer that denotes the sum of all elements of $A$ after the $i$th operation.

## Constraints

- $1 \le n, m \le 10^5$  
- $1 \le k \le 5$  
- $1 \le \text{any element of $A$ or $S$} \le 10^9$  
- For all operations, $1 \le l \le r \le n$ and $1 \le x \le 10^4$ hold.  

**Subtasks**

- For $20\%$ of the maximum points, $nmk \le 2\cdot 10^8$
